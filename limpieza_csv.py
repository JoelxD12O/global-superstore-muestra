"""
Limpieza de data/base.csv y armado de un modelo estrella para Power BI.

Salida en data/powerbi/:
    fact_ventas.csv        -> tabla de hechos (una fila por línea de pedido)
    dim_calendario.csv     -> una fila por día (se relaciona con Fecha_Pedido y Fecha_Envio)
    dim_cliente.csv
    dim_producto.csv
    dim_geografia.csv
    dim_modo_envio.csv
    dim_prioridad.csv
"""
from pathlib import Path

import pandas as pd

SALIDA = Path("data/powerbi")
SALIDA.mkdir(parents=True, exist_ok=True)

df_original = pd.read_csv("data/base.csv")

# ---------------------------------------------------------------------------
# 1. Limpieza: columnas que no aportan al análisis
# ---------------------------------------------------------------------------
columnas_a_eliminar = [
    "记录数",   # Contador exportado por la herramienta BI: vale 1 en todas las filas
    "Row.ID",   # Índice técnico de la fila, sin significado de negocio
    "Market2",  # Duplica Market (solo agrupa US + Canada en "North America")
    "City",     # 1,754 valores en 5,130 filas: demasiado disperso para sacar conclusiones
    "weeknum",  # No coincide con la semana real de Order.Date (~20% de filas); va en dim_calendario
    "Year",     # Se deriva de Order.Date; va en dim_calendario
]
df = df_original.drop(columns=columnas_a_eliminar)

df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"]).dt.normalize()  # quita " 00:00:00.000"


def crear_dimension(columnas, nombre_id, orden=None):
    """Devuelve una dimensión con llave sustituta (1..n) a partir de combinaciones únicas."""
    dim = df[columnas].drop_duplicates().sort_values(orden or columnas).reset_index(drop=True)
    dim.insert(0, nombre_id, dim.index + 1)
    return dim


# ---------------------------------------------------------------------------
# 2. Dimensiones
# ---------------------------------------------------------------------------
# Cliente: Customer.ID es único por cliente (nombre y segmento consistentes)
dim_cliente = (
    df[["Customer.ID", "Customer.Name", "Segment"]]
    .drop_duplicates()
    .sort_values("Customer.ID")
    .rename(columns={"Customer.ID": "id_cliente", "Customer.Name": "Cliente", "Segment": "Segmento"})
)

# Producto: Product.ID NO es único (66 IDs tienen varios nombres) -> llave sustituta
dim_producto = crear_dimension(
    ["Category", "Sub.Category", "Product.ID", "Product.Name"], "id_producto"
)

# Geografía: un mismo State puede repetirse entre países -> llave sustituta
dim_geografia = crear_dimension(["Market", "Region", "Country", "State"], "id_geografia")

# Modo de envío, ordenado de más rápido a más lento
orden_envio = ["Same Day", "First Class", "Second Class", "Standard Class"]
dim_modo_envio = pd.DataFrame({
    "id_modo_envio": range(1, len(orden_envio) + 1),
    "Modo_Envio": orden_envio,
    "Orden": range(1, len(orden_envio) + 1),
})

# Prioridad, ordenada de mayor a menor urgencia
orden_prioridad = ["Critical", "High", "Medium", "Low"]
dim_prioridad = pd.DataFrame({
    "id_prioridad": range(1, len(orden_prioridad) + 1),
    "Prioridad": orden_prioridad,
    "Orden": range(1, len(orden_prioridad) + 1),
})

# Calendario: todos los días desde el 1-ene del primer año hasta el 31-dic del último
# (cubre tanto fechas de pedido como de envío, sin huecos, como exige Power BI)
inicio = pd.Timestamp(year=df["Order.Date"].min().year, month=1, day=1)
fin = pd.Timestamp(year=df["Ship.Date"].max().year, month=12, day=31)
fechas = pd.date_range(inicio, fin, freq="D")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
iso = fechas.isocalendar()

dim_calendario = pd.DataFrame({
    "Fecha": fechas,
    "Anio": fechas.year,
    "Trimestre": "T" + fechas.quarter.astype(str),
    "Anio_Trimestre": fechas.year.astype(str) + "-T" + fechas.quarter.astype(str),
    "Mes_Num": fechas.month,
    "Mes": [meses[m - 1] for m in fechas.month],
    "Anio_Mes": fechas.strftime("%Y-%m"),
    "Semana_ISO": iso["week"].to_numpy(),
    "Dia": fechas.day,
    "Dia_Semana_Num": fechas.dayofweek + 1,  # 1 = lunes
    "Dia_Semana": [dias[d] for d in fechas.dayofweek],
    "Es_Fin_De_Semana": fechas.dayofweek >= 5,
})

# ---------------------------------------------------------------------------
# 3. Tabla de hechos
# ---------------------------------------------------------------------------
fact = (
    df.merge(dim_producto, on=["Category", "Sub.Category", "Product.ID", "Product.Name"])
      .merge(dim_geografia, on=["Market", "Region", "Country", "State"])
      .merge(dim_modo_envio[["id_modo_envio", "Modo_Envio"]], left_on="Ship.Mode", right_on="Modo_Envio")
      .merge(dim_prioridad[["id_prioridad", "Prioridad"]], left_on="Order.Priority", right_on="Prioridad")
)

fact_ventas = pd.DataFrame({
    "id_pedido": fact["Order.ID"],
    "Fecha_Pedido": fact["Order.Date"],
    "Fecha_Envio": fact["Ship.Date"],
    "id_cliente": fact["Customer.ID"],
    "id_producto": fact["id_producto"],
    "id_geografia": fact["id_geografia"],
    "id_modo_envio": fact["id_modo_envio"],
    "id_prioridad": fact["id_prioridad"],
    "Ventas": fact["Sales"],
    "Cantidad": fact["Quantity"],
    "Descuento": fact["Discount"],
    "Ganancia": fact["Profit"],
    "Costo_Envio": fact["Shipping.Cost"],
    "Dias_Envio": (fact["Ship.Date"] - fact["Order.Date"]).dt.days,
}).sort_values(["Fecha_Pedido", "id_pedido"])

# Renombrar columnas de dimensiones a español
dim_producto = dim_producto.rename(columns={
    "Category": "Categoria", "Sub.Category": "Subcategoria",
    "Product.ID": "Codigo_Producto", "Product.Name": "Producto",
})
dim_geografia = dim_geografia.rename(columns={
    "Market": "Mercado", "Region": "Region", "Country": "Pais", "State": "Estado",
})

# ---------------------------------------------------------------------------
# 4. Validaciones y exportación
# ---------------------------------------------------------------------------
assert len(fact_ventas) == len(df_original), "Se perdieron filas al construir la tabla de hechos"
assert fact_ventas.isna().sum().sum() == 0, "Hay llaves sin relación en la tabla de hechos"
assert fact_ventas["Fecha_Envio"].max() <= fin and fact_ventas["Fecha_Pedido"].min() >= inicio
assert abs(fact_ventas["Ventas"].sum() - df_original["Sales"].sum()) < 1e-6

tablas = {
    "fact_ventas": fact_ventas,
    "dim_calendario": dim_calendario,
    "dim_cliente": dim_cliente,
    "dim_producto": dim_producto,
    "dim_geografia": dim_geografia,
    "dim_modo_envio": dim_modo_envio,
    "dim_prioridad": dim_prioridad,
}
for nombre, tabla in tablas.items():
    tabla.to_csv(SALIDA / f"{nombre}.csv", index=False, date_format="%Y-%m-%d", encoding="utf-8-sig")
    print(f"{nombre:<16} {tabla.shape[0]:>6} filas x {tabla.shape[1]:>2} columnas")

print(f"\nArchivos guardados en {SALIDA}/")
