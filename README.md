# Global Superstore – Análisis de ventas para Power BI

Trabajo de la semana 12. El objetivo es partir de **preguntas de negocio**, responderlas con datos y presentar los hallazgos en un **dashboard de Power BI** de 4 a 5 gráficas.

## Flujo del trabajo

1. **Datos:** se obtuvo el dataset Global Superstore desde Kaggle.
2. **Muestra:** se redujo el dataset con un muestreo aleatorio que conserva todos los meses.
3. **Preguntas:** se adaptaron 18 preguntas de negocio a las columnas disponibles ([preguntas.md](preguntas.md)).
4. **Insights:** se responden las preguntas con números *(pendiente)*.
5. **Maqueta:** se diseñan las gráficas del dashboard *(pendiente)*.
6. **Power BI:** se construye el dashboard final *(pendiente)*.

## El dataset

**Global Superstore** registra las ventas de una tienda minorista internacional ficticia que vende muebles, artículos de oficina y tecnología.

| Característica | Valor |
|---|---|
| Fuente | Kaggle: [fatihilhan/global-superstore-dataset](https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset) |
| Notebook base | Kaggle: [osmanahmedosman/global-superstore](https://www.kaggle.com/code/osmanahmedosman/global-superstore) |
| Periodo | Enero 2011 – diciembre 2014 (48 meses) |
| Filas | 51,290 (cada fila es un producto dentro de un pedido) |
| Columnas | 27 |
| Mercados | 7: APAC, EU, US, LATAM, EMEA, Africa, Canada |
| Regiones | 13 |
| Categorías | 3: Furniture, Office Supplies, Technology (17 subcategorías) |
| Segmentos de cliente | 3: Consumer, Corporate, Home Office |

### Columnas principales

| Tema | Columnas |
|---|---|
| Tiempo | `Order.Date`, `Ship.Date`, `Year`, `weeknum` |
| Ubicación | `Market`, `Market2`, `Region`, `Country`, `State`, `City` |
| Producto | `Category`, `Sub.Category`, `Product.ID`, `Product.Name` |
| Cliente | `Segment`, `Customer.ID`, `Customer.Name` |
| Dinero | `Sales`, `Profit`, `Discount`, `Quantity` |
| Envío | `Ship.Mode`, `Order.Priority`, `Shipping.Cost` |
| Identificadores | `Order.ID`, `Row.ID` |

La columna `记录数` ("cantidad de registros") vale 1 en todas las filas y se puede eliminar.

### Limitaciones

- **No hay devoluciones:** se usan los pedidos con pérdida (`Profit` < 0) como indicador de problema.
- **No hay fecha de entrega comprometida (SLA):** se usan los días de envío (`Ship.Date` − `Order.Date`).
- **No hay canal de venta:** se usa el modo de envío (`Ship.Mode`).

## La muestra

Archivo: [data/superstore_muestra.csv](data/superstore_muestra.csv)

- **Método:** muestreo aleatorio estratificado por año y mes. Se toma el 10% de las filas de cada mes, con semilla fija (`random_state=42`) para que sea reproducible.
- **Resultado:** 5,130 filas que cubren los 48 meses y mantienen la proporción de filas por año.

| Año | Filas |
|---|---|
| 2011 | 900 |
| 2012 | 1,096 |
| 2013 | 1,379 |
| 2014 | 1,755 |

- **Codificación:** UTF-8 con BOM, para que Power BI y Excel lean bien los caracteres especiales.

> **Importante:** la muestra sirve para practicar la maqueta y para porcentajes calculados fila por fila (por ejemplo, % de pedidos con pérdida o pérdida según el nivel de descuento). Los **totales por grupo y año** (crecimiento por mercado, margen anual) deben calcularse con el dataset completo, porque en la muestra unos pocos pedidos grandes los distorsionan. Por ejemplo, el crecimiento de APAC en 2014 es +24% en la data completa y +1% en la muestra.

## Archivos del repositorio

| Archivo | Contenido |
|---|---|
| [global-superstore.ipynb](global-superstore.ipynb) | Notebook de análisis exploratorio (Python: pandas, matplotlib, seaborn) |
| [data/superstore_muestra.csv](data/superstore_muestra.csv) | Muestra de 5,130 filas para Power BI |
| [preguntas.md](preguntas.md) | 18 preguntas de negocio agrupadas en 5 gráficas |

El dataset completo (`superstore.csv`, 15 MB) no está en el repositorio. El notebook lo lee desde `data/superstore.csv`; para ejecutarlo, descárgalo de Kaggle y guárdalo en esa ruta.

## Preguntas y gráficas del dashboard

El detalle está en [preguntas.md](preguntas.md).

| Gráfica | Tema | Preguntas |
|---|---|---|
| 1. Tarjetas KPI | Situación actual: ventas, margen, % de pedidos con pérdida, días de envío | 1, 4, 5 |
| 2. Ventas y margen por trimestre | ¿Crecemos? ¿El margen acompaña? | 2, 3, 6 |
| 3. Mercados, segmentos y modo de envío | Dónde, a quién y cómo vendemos | 7, 8, 9, 12, 13 |
| 4. Margen por subcategoría | Qué productos bajan el margen | 10, 11, 16 |
| 5. Descuento vs pérdida | Causa del problema y acción recomendada | 14, 15, 17, 18 |

## Hallazgos preliminares (data completa)

- Las ventas crecen en promedio más de 20% al año: +18.5% en 2012, +27.2% en 2013 y +26.3% en 2014.
- El margen se mantiene estable entre 11% y 12%.
- El **24.5% de los pedidos deja pérdida**.
- **Tables** es la única subcategoría con margen negativo (−8.5%).
- En la muestra, los pedidos con descuento mayor a 20% pierden dinero en su gran mayoría: 72% entre 21–40% de descuento y 99% sobre 40%.

## Cómo usar en Power BI

1. **Obtener datos → Texto/CSV** → elegir `data/superstore_muestra.csv`.
2. En Power Query, verificar que `Order.Date` y `Ship.Date` sean de tipo **Fecha**.
3. Crear las columnas y medidas que necesitan las preguntas:
   - `Días de envío = Ship.Date − Order.Date`
   - `Margen % = SUM(Profit) / SUM(Sales)`
   - `Pedido con pérdida = Profit < 0`
