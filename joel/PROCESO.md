# Proceso en Power BI – Joel

Registro paso a paso de cómo se construye el dashboard de Global Superstore en Power BI: qué se hizo, por qué, qué problemas aparecieron y cómo se resolvieron.

- **Archivo de Power BI:** [supermuestra.pbix](supermuestra.pbix)
- **Data:** [`../data/superstore_muestra.csv`](../data/superstore_muestra.csv) (5,130 filas, 2011–2014)
- **Números de referencia:** [`../insights.md`](../insights.md). Todo lo que muestre Power BI debe coincidir con ese archivo.

## Plan

| Paso | Qué se hace | Estado |
|---|---|---|
| 1 | Cargar y limpiar la data | ✅ Hecho |
| 2 | Crear columnas calculadas y medidas | ⏳ Pendiente |
| 3 | Gráfica 1 – Tarjetas KPI | ⏳ Pendiente |
| 4 | Gráfica 2 – Crecimiento | ⏳ Pendiente |
| 5 | Gráfica 3 – Mercados, segmentos y envío | ⏳ Pendiente |
| 6 | Gráfica 4 – Margen por subcategoría | ⏳ Pendiente |
| 7 | Gráfica 5 – Descuento vs pérdida | ⏳ Pendiente |
| 8 | Comparar todos los números con `insights.md` | ⏳ Pendiente |

---

## Paso 1 – Cargar y limpiar la data ✅

### 1.1 Cargar el CSV

1. Abrir **Power BI Desktop**.
2. **Inicio → Obtener datos → Texto/CSV**.
3. Elegir `semana12\data\superstore_muestra.csv`.
4. En la vista previa, revisar:
   - **Origen de archivo:** `65001: Unicode (UTF-8)`. Así se leen bien los caracteres especiales.
   - **Delimitador:** `Coma`.
5. Para entrar a Power Query, abrir la flecha **⌄** junto a **Load** y elegir **Transform data**. Con **Load** directo, la data entra sin limpiar.

> La vista previa es solo para mirar. Ahí no funciona el clic derecho; para editar hay que entrar a **Power Query** (Transformar datos).

### 1.2 Problema: los decimales se leían como enteros

**Síntoma:** en la vista previa, `Discount` mostraba `4`, `2`, `27` en lugar de `0.4`, `0.2`, `0.27`, con el ícono **1²3** (número entero).

**Causa:** Power BI estaba configurado en **Español (Perú)**, donde el punto (`.`) es separador de miles. Leía `0.4` como "cero mil cuatro", o sea `4`. Pasaba lo mismo con `Profit` y `Shipping.Cost`. `Sales` no se afectaba porque en el CSV viene sin decimales.

**Consecuencia si no se corrige:** la ganancia total salía **306,830,315** en vez de **143,046**, y el descuento máximo **602** en vez de **0.85**.

**Intento 1 (no bastó):** cambiar **Archivo → Opciones y configuración → Opciones → ARCHIVO ACTUAL → Configuración regional → Inglés (Estados Unidos)**. No arregló la carga, porque Power BI ya había guardado un paso de conversión con formato `"es"` (español).

**Solución:** reescribir la consulta en el **Editor avanzado** (ver 1.4) con formato `"en-US"` y las columnas de montos como número decimal (`type number`).

### 1.3 Problema: `Ship.Date` daba error en todas las filas

**Síntoma:** al aplicar la consulta corregida apareció el aviso *"Se cargaron 5,130 filas. 5,130 errores"*, y `Ship.Date` mostraba `[Error]` en todas las filas. Al cargar, esos errores quedaron como celdas vacías.

**Causa:** en el CSV las dos fechas vienen en formatos distintos:

| Columna | Formato en el CSV |
|---|---|
| `Order.Date` | `2011-01-03` (solo fecha) |
| `Ship.Date` | `2011-01-09 00:00:00.000` (fecha **con hora**) |

Power Query no puede convertir directamente a **fecha** un texto que trae hora.

**Solución:** convertir `Ship.Date` en dos pasos: primero a **fecha y hora** (`type datetime`) y luego a **solo fecha** (`type date`).

### 1.4 Consulta final de Power Query

Se pega en **Inicio → Transformar datos → Editor avanzado** (Ctrl+A, borrar todo, pegar, **Listo**):

```
let
  Origen = Csv.Document(File.Contents("C:\Users\Joel\Desktop\2026-2\comunicacion\semana12\data\superstore_muestra.csv"), [Delimiter = ",", Columns = 27, Encoding = 65001, QuoteStyle = QuoteStyle.Csv]),
  #"Encabezados promovidos" = Table.PromoteHeaders(Origen, [PromoteAllScalars = true]),
  #"Columnas quitadas" = Table.RemoveColumns(#"Encabezados promovidos", {"记录数"}),
  #"Tipo de columna cambiado" = Table.TransformColumnTypes(#"Columnas quitadas", {{"Category", type text}, {"City", type text}, {"Country", type text}, {"Customer.ID", type text}, {"Customer.Name", type text}, {"Discount", type number}, {"Market", type text}, {"Order.Date", type date}, {"Order.ID", type text}, {"Order.Priority", type text}, {"Product.ID", type text}, {"Product.Name", type text}, {"Profit", type number}, {"Quantity", Int64.Type}, {"Region", type text}, {"Row.ID", Int64.Type}, {"Sales", type number}, {"Segment", type text}, {"Ship.Date", type datetime}, {"Ship.Mode", type text}, {"Shipping.Cost", type number}, {"State", type text}, {"Sub.Category", type text}, {"Year", Int64.Type}, {"Market2", type text}, {"weeknum", Int64.Type}}, "en-US"),
  #"Ship.Date a fecha" = Table.TransformColumnTypes(#"Tipo de columna cambiado", {{"Ship.Date", type date}})
in
  #"Ship.Date a fecha"
```

**Qué hace cada paso:**

| Paso | Qué hace | Por qué |
|---|---|---|
| `Origen` | Lee el CSV en UTF-8, separado por comas | `QuoteStyle.Csv` respeta las comas dentro de comillas. Algunos nombres de producto tienen comas y sin esto se partirían en dos columnas. |
| `Encabezados promovidos` | Usa la primera fila como nombres de columna | El CSV trae los encabezados en la fila 1 |
| `Columnas quitadas` | Elimina `记录数` | Vale 1 en todas las filas y no aporta nada |
| `Tipo de columna cambiado` | Asigna el tipo de cada columna con formato `en-US` | Lee el punto como decimal. `Discount`, `Profit`, `Sales` y `Shipping.Cost` quedan como número decimal. |
| `Ship.Date a fecha` | Pasa `Ship.Date` de fecha y hora a solo fecha | Así queda igual que `Order.Date` y se pueden restar para calcular los días de envío |

Después: **Close & Apply** → esperar a que cargue → **Ctrl+S**.

> **Ojo:** después de cerrar Power Query hay que **guardar** (Ctrl+S). La primera vez la consulta se corrigió, pero no se guardó, y el `.pbix` seguía con los números malos.

### 1.5 Verificación

Se leyó el `.pbix` guardado con la librería de Python `pbixray` y se comparó con la muestra:

| Verificación | Power BI | Esperado |
|---|---|---|
| Filas | 5,130 | 5,130 ✓ |
| Columnas | 26 | 26 ✓ |
| Celdas vacías | 0 | 0 ✓ |
| Ventas totales | 1,258,116 | 1,258,116 ✓ |
| Ganancia total | 143,045.82 | 143,046 ✓ |
| Descuento máximo | 0.85 | 0.85 ✓ |
| Pedidos únicos | 4,651 | 4,651 ✓ |
| Filas con pérdida | 23.9% | 23.9% ✓ |
| Días promedio de envío | 3.99 | 3.99 ✓ |

### Lecciones del paso 1

- Antes de cargar, **revisar siempre que los decimales se vean bien** en la vista previa. El ícono **1²3** en una columna de montos es señal de problema.
- Un error de tipo en Power Query **no detiene la carga**: las celdas con error quedan vacías sin avisar en el reporte. Hay que leer el mensaje de "errores" al cargar.
- Guardar con **Ctrl+S** después de cada cambio.

---

## Paso 2 – Columnas calculadas y medidas ⏳

*Pendiente.*
