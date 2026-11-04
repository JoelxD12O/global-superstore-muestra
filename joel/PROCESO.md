# Proceso en Power BI – Joel

Registro paso a paso de cómo se construye el dashboard de Global Superstore en Power BI: qué se hizo, por qué, qué problemas aparecieron y cómo se resolvieron.

- **Archivo de Power BI:** [supermuestra.pbix](supermuestra.pbix)
- **Data:** [`../data/superstore_muestra.csv`](../data/superstore_muestra.csv) (5,130 filas, 2011–2014)
- **Números de referencia:** [`../insights.md`](../insights.md). Todo lo que muestre Power BI debe coincidir con ese archivo.

## Plan

| Paso | Qué se hace | Estado |
|---|---|---|
| 1 | Cargar y limpiar la data | ✅ Hecho |
| 2 | Crear columnas calculadas y medidas | ✅ Hecho |
| 3 | Gráfica 1 – Tarjetas KPI | ✅ Hecho |
| 4 | Gráfica 2 – Crecimiento | 🔄 En progreso |
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

## Paso 2 – Columnas calculadas y medidas ✅

### 2.1 Columnas calculadas

Se crean en la vista **Tabla**, con la tabla `superstore_muestra` seleccionada: **Herramientas de tablas → Nueva columna**. Una columna calculada se evalúa **fila por fila** y queda guardada en la tabla.

| Columna | Fórmula | Para qué |
|---|---|---|
| `Dias envio` | `DATEDIFF('superstore_muestra'[Order.Date], 'superstore_muestra'[Ship.Date], DAY)` | Días entre el pedido y el envío |
| `Trimestre` | `"T" & QUARTER('superstore_muestra'[Order.Date])` | Margen por trimestre (pregunta 6) |
| `Rango descuento` | `SWITCH(TRUE(), [Discount] = 0, "0%", [Discount] <= 0.2, "1–20%", [Discount] <= 0.4, "21–40%", ">40%")` | Agrupar las filas por nivel de descuento (Gráfica 5) |
| `Orden rango` | `SWITCH(TRUE(), [Discount] = 0, 1, [Discount] <= 0.2, 2, [Discount] <= 0.4, 3, 4)` | Número para ordenar los rangos de menor a mayor |

### 2.2 Medidas

Se crean en una tabla aparte, `_Medidas` (**Herramientas de tablas → Nueva tabla**: `_Medidas = ROW("x", BLANK())`), para tenerlas todas juntas. Una medida **no** se guarda por fila: se calcula en el momento según los filtros de cada gráfica.

| Medida | Fórmula | Formato |
|---|---|---|
| `Ventas` | `SUM('superstore_muestra'[Sales])` | número |
| `Ganancia` | `SUM('superstore_muestra'[Profit])` | número |
| `Margen %` | `DIVIDE([Ganancia], [Ventas])` | % |
| `Pedidos` | `DISTINCTCOUNT('superstore_muestra'[Order.ID])` | entero |
| `% con perdida` | `DIVIDE(CALCULATE(COUNTROWS('superstore_muestra'), 'superstore_muestra'[Profit] < 0), COUNTROWS('superstore_muestra')) + 0` | % |
| `Dias promedio envio` | `AVERAGE('superstore_muestra'[Dias envio])` | número |
| `Costo envio / venta` | `DIVIDE(SUM('superstore_muestra'[Shipping.Cost]), [Ventas])` | % |
| `% de ventas` | `DIVIDE([Ventas], CALCULATE([Ventas], ALLSELECTED('superstore_muestra')))` | % |
| `Ganancia desc >20%` | `CALCULATE([Ganancia], 'superstore_muestra'[Discount] > 0.2)` | número |
| `Ganancia con tope 20%` | `[Ganancia] - [Ganancia desc >20%]` | número |
| `Crecimiento %` | ver abajo | % |

```
Crecimiento % =
VAR anio = MAX('superstore_muestra'[Year])
VAR actual = CALCULATE([Ventas], 'superstore_muestra'[Year] = anio)
VAR anterior = CALCULATE([Ventas], 'superstore_muestra'[Year] = anio - 1)
RETURN DIVIDE(actual - anterior, anterior)
```

Por qué `DIVIDE` y no `/`: si el divisor es 0 o vacío, `DIVIDE` devuelve vacío en lugar de un error.

> **Ojo:** sin filtro de año, `Crecimiento %` muestra el último año (2014 vs 2013 = 33.8%). En una tarjeta hay que titularla "Crecimiento 2014".

### 2.3 Problema: los porcentajes se veían como decimales

**Síntoma:** las medidas de porcentaje tenían formato `0.0`. `Margen %` se iba a ver como **0.1** en vez de **11.4%**.

**Solución:** seleccionar cada medida → **Herramientas de medición → Formato: Porcentaje**, 1 decimal. Se aplicó a `Margen %`, `% con perdida`, `Costo envio / venta`, `% de ventas` y `Crecimiento %`.

### 2.4 Problema: las columnas de montos redondeaban a entero

**Síntoma:** `Discount` tenía formato `0` y mostraba **0** en todas las filas (0.4 → 0).

**Solución:** seleccionar la **columna** (no la tabla: arriba debe decir **Herramientas de columnas**) y cambiar el formato:

| Columna | Formato |
|---|---|
| `Discount` | Porcentaje, 0 decimales |
| `Profit` | Número decimal, 2 decimales |
| `Sales` | Número decimal |
| `Shipping.Cost` | Número decimal, 2 decimales, separador de miles |

> **Error que pasó:** al cambiar `Discount` a Porcentaje, ese formato quedó seleccionado y se aplicó también a `Profit`, `Sales` y `Shipping.Cost` (una venta de 221 salía como **22,100 %**). Hay que revisar el formato de cada columna por separado.

### 2.5 Problema: `% con perdida` salía vacío en el rango 0%

**Síntoma:** en el rango de descuento 0% no hay ninguna fila con pérdida. `CALCULATE(COUNTROWS(...))` devuelve **vacío** (no 0), así que el rango 0% desaparecía de la tabla.

**Solución:** agregar `+ 0` al final de la fórmula. Vacío + 0 = 0, y el rango aparece con **0.0%**.

> Hay que confirmar la fórmula con **Enter** o el botón **✓**. Si se hace clic en otro lado, el cambio se pierde.

### 2.6 Problema: Power BI iba a sumar columnas que no son montos

**Síntoma:** `Year`, `weeknum`, `Row.ID`, `Dias envio` y `Orden rango` tenían **Resumen: Suma** (o Recuento), con el ícono **Σ**. Si se arrastra `Year` a una gráfica, sale la suma de los años (miles) en vez de cada año.

**Solución:** seleccionar cada columna → **Herramientas de columnas → Resumen: No resumir**. El **Σ** desaparece.

### 2.7 Problema: ordenar `Rango descuento` daba dependencia circular

**Objetivo:** que la gráfica de descuentos salga siempre en orden **0% → 1–20% → 21–40% → >40%**. Se hace con **Rango descuento → Herramientas de columnas → Ordenar por columna → Orden rango**.

**Problema:** la primera versión de `Orden rango` se calculaba a partir de `Rango descuento`:

```
SWITCH('superstore_muestra'[Rango descuento], "0%", 1, "1–20%", 2, "21–40%", 3, 4)
```

Power BI no deja ordenar una columna por otra que depende de ella (dependencia circular).

**Solución:** reescribir `Orden rango` para que lea `Discount` directamente (fórmula de la tabla 2.1). Da los mismos valores (1 a 4) y ya no depende de `Rango descuento`.

### 2.8 Verificación

Se conectó a Power BI Desktop con el MCP `powerbi-modeling` y se ejecutaron consultas DAX:

| Verificación | Power BI | `insights.md` |
|---|---|---|
| Ventas / Ganancia | 1,258,116 / 143,046 | ✓ |
| Margen / Pedidos | 11.4% / 4,651 | ✓ |
| % con pérdida / Días envío | 23.9% / 3.99 | ✓ |
| Crecimiento 2012 / 2013 / 2014 | 23.6% / 24.9% / 33.8% | ✓ |
| Margen 2011–2014 | 9.9% / 10.9% / 12.8% / 11.3% | ✓ |
| Margen por trimestre (16 celdas) | todas iguales | ✓ |
| Ganancia por rango de descuento | +173.4K / +52.5K / −15.5K / −67.4K | ✓ |
| % con pérdida por rango | 0.0% / 21.2% / 71.6% / 98.8% | ✓ |
| Ganancia desc >20% / con tope | −82.8K / 225.9K | ✓ |
| Modo de envío (% ventas, margen, costo/venta) | coinciden | ✓ |

### Lecciones del paso 2

- **Columna vs. tabla:** para cambiar formato o resumen hay que seleccionar la **columna**. Si arriba dice *Herramientas de tablas*, está seleccionada la tabla.
- **Columna calculada** = un valor por fila, guardado. **Medida** = se calcula según los filtros de la gráfica. Para totales y porcentajes se usan medidas.
- Revisar el **formato** de cada medida y columna antes de graficar.
- Una columna de orden no puede depender de la columna que ordena.

---

## Paso 3 – Gráfica 1: Tarjetas KPI ✅

Responde la pregunta 1: *¿cómo estamos hoy en ventas, margen y operación?*

### 3.1 Crear una tarjeta

1. Ir a la **Vista de informe** (primer ícono de la barra izquierda).
2. En **Visualizaciones**, elegir **Tarjeta**: el ícono "123", a la derecha del velocímetro. No confundir con **KPI** (triangulitos rojo y verde), que pide más campos.
3. Arrastrar la medida `Ventas` al campo **Valor**.

### 3.2 Las otras 5 tarjetas

Copiar la primera (**Ctrl+C**, **Ctrl+V**), quitar `Ventas` de **Valor** con la **✗** y arrastrar la nueva medida.

| Tarjeta | Medida | Muestra | `insights.md` |
|---|---|---|---|
| Ventas | `Ventas` | 1.26 M | $1.26 M ✓ |
| Ganancia | `Ganancia` | 143.05 K | $143 K ✓ |
| Margen | `Margen %` | 11.4 % | 11.4% ✓ |
| Pedidos | `Pedidos` | 4,651 | 4,651 ✓ |
| Con pérdida | `% con perdida` | 23.9 % | 23.9% ✓ |
| Días de envío | `Dias promedio envio` | 4.0 | 4.0 ✓ |

### 3.3 Problemas y ajustes

- **Tarjetas encimadas y con espacios desiguales.** Seleccionar las 6 (**Ctrl+clic**) → **Formato → Alinear → Distribuir horizontalmente** y luego **Alinear arriba**.
- **`Dias promedio envio` sin formato:** podía mostrar 3.988888. Se le puso **Número decimal, 1 decimal**.

### 3.4 Verificación

Se leyó el `.pbix` guardado (carpeta `Report/definition/pages/.../visuals/`). Hay 6 visuales `cardVisual`, uno por medida, en la misma fila y con 65 px de separación entre cada uno.

---

## Paso 4 – Gráfica 2: Crecimiento 🔄

Responde las preguntas 2 y 3: *¿estamos creciendo?* y *¿el margen acompaña?* Las dos van en una sola gráfica.

### 4.1 Crear la gráfica

1. Hacer clic en un espacio vacío de la hoja, para que ninguna tarjeta quede seleccionada.
2. En **Visualizaciones**, elegir **Gráfico de líneas y columnas agrupadas**: es el **último ícono de la 2.ª fila**. El 5.º ícono es la versión *apilada* y el 1.º de la 3.ª fila es el gráfico de *cinta*.
3. Llenar los campos:

| Campo | Valor |
|---|---|
| Eje X | `Year` |
| Eje Y de columna | `Ventas` |
| Eje Y de línea | `Margen %` |

**Resultado:** columnas de 215K → 266K → 332K → 445K y una línea que sube hasta 12.8% en 2013 y baja a 11.3% en 2014. Coincide con `insights.md`.

### 4.2 Personalización

Con la gráfica seleccionada: **Visualizaciones → Formato visual → Objeto visual**.

| Ajuste | Dónde | Estado |
|---|---|---|
| Línea recta, no curva | **Líneas → Tipo de interpolación: Lineal** (estaba en *Suave*) | ✅ |
| Marcadores en cada año | **Marcadores: Activado** | ✅ |
| Números sobre la gráfica | **Etiquetas de datos: Activado** | ✅ |
| Título con la conclusión | **General → Título**: *Las ventas crecen cada año, pero el margen cayó en 2014* | ⏳ |
| Colores | columnas `#5B7DA8`, línea y marcadores `#F28E2B` | ⏳ |

**Por qué la línea recta:** con interpolación *Suave*, Power BI dibuja una curva que inventa un pico entre 2013 y 2014. Solo hay 4 datos, así que la línea debe unirlos en tramos rectos.

> **Ojo:** al hacer clic en una columna (por ejemplo 2014), **toda la página se filtra a ese año** y las tarjetas muestran solo los números de 2014. No es un error. Para volver al total, hacer clic en un espacio vacío de la gráfica.

> **Pendiente:** la tarjeta de **Pedidos** redondea a "5 mil". Hay que ponerle **Unidades de visualización: Ninguno** para que muestre 4,651.
