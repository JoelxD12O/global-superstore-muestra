# Preguntas del negocio – Global Superstore

Dataset: Global Superstore (51,290 filas, pedidos 2011–2014). Tienda minorista internacional que vende muebles, artículos de oficina y tecnología en 7 mercados.

Las preguntas se adaptaron de un modelo de 18 preguntas de negocio a las columnas disponibles en esta data.

## Ajustes por limitaciones de la data

| Concepto original | Qué usamos | Motivo |
|---|---|---|
| Devoluciones | Pedidos con pérdida (`Profit` < 0) | La data no tiene columna de devoluciones |
| SLA | Días de envío (`Ship.Date` − `Order.Date`) según `Order.Priority` | No hay fecha de entrega comprometida |
| Canal | Modo de envío (`Ship.Mode`) | No hay canal de venta |

## Preguntas agrupadas por gráfica

### Gráfica 1 – Tarjetas KPI: situación actual

| # | Pregunta | Columnas |
|---|---|---|
| 1 | ¿Cómo estamos hoy en términos generales de ventas, margen y operación? | `Sales`, `Profit`, días de envío |
| 4 | ¿Los pedidos de prioridad Critical/High se envían más rápido que los Low? | `Order.Priority`, `Ship.Mode`, días de envío |
| 5 | ¿Qué porcentaje de pedidos deja pérdida? | `Profit` < 0 |

### Gráfica 2 – Ventas y margen por trimestre: crecimiento

| # | Pregunta | Columnas |
|---|---|---|
| 2 | ¿Estamos creciendo en ventas o no? | `Order.Date`, `Sales` |
| 3 | ¿El margen acompaña el crecimiento de las ventas? | `Order.Date`, `Sales`, `Profit` |
| 6 | ¿Existen señales tempranas de deterioro (por trimestre)? | `Order.Date`, margen % |

### Gráfica 3 – Mercados, segmentos y modo de envío: dónde y a quién vendemos

| # | Pregunta | Columnas |
|---|---|---|
| 7 | ¿Qué tipo de cliente genera más ventas y más margen? | `Segment`, `Sales`, `Profit` |
| 8 | ¿Qué mercados muestran crecimiento en ventas respecto al año anterior? | `Market`, `Order.Date`, `Sales` |
| 9 | ¿Qué modo de envío usan más los clientes y cuál deja más margen? | `Ship.Mode`, `Sales`, `Profit` |
| 12 | ¿Qué modo de envío tiene mayor costo de envío respecto a la venta? | `Ship.Mode`, `Shipping.Cost`, `Sales` |
| 13 | ¿Qué mercado tarda más en enviar los pedidos? | `Market`, días de envío |

### Gráfica 4 – Margen por subcategoría: qué vendemos

| # | Pregunta | Columnas |
|---|---|---|
| 10 | ¿Qué productos bajan el margen? | `Sub.Category`, `Profit`, `Sales` |
| 11 | ¿Qué categorías venden mucho pero aportan poco margen? | `Category`, `Sub.Category`, `Sales`, `Profit` |
| 16 | ¿Qué combinaciones subcategoría × mercado son más críticas? | `Sub.Category`, `Market`, margen % |

### Gráfica 5 – Descuento vs pérdida: causa y acción

| # | Pregunta | Columnas |
|---|---|---|
| 14 | ¿El problema está generalizado o concentrado en ciertos segmentos? | `Discount`, `Profit`, `Segment` |
| 15 | ¿Qué problemas tienen mayor impacto en el margen? | `Discount`, `Profit` |
| 17 | ¿Dónde deberíamos priorizar acciones para mejorar resultados? | `Sub.Category`, `Market`, `Discount` |
| 18 | ¿Qué mejora tendría mayor impacto? (cuantificada en ganancia) | `Discount`, `Profit` |

## Nota sobre la muestra

Las preguntas se responden con `data/superstore_muestra.csv` (5,130 filas, 10% de cada mes), que es la misma data del dashboard en Power BI. Los totales por grupo y año (crecimiento por mercado) son menos precisos que los porcentajes por fila, porque en la muestra unos pocos pedidos grandes pesan mucho.
