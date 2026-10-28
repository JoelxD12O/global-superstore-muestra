# Preguntas de análisis – Global Superstore

Dataset: `data/superstore_muestra.csv` (5,130 pedidos, muestra aleatoria del 10% por mes, 2011–2014).

## 1. Evolución en el tiempo

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 1 | ¿Cómo han evolucionado las ventas y la ganancia de 2011 a 2014? | `Order.Date`, `Sales`, `Profit` | Líneas |
| 2 | ¿Hay meses o temporadas con más ventas? | `Order.Date` (mes), `Sales` | Columnas por mes o mapa de calor año×mes |

## 2. Dónde vendemos

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 3 | ¿Qué mercados y regiones generan más ventas y más ganancia? | `Market`, `Region`, `Sales`, `Profit` | Barras o mapa |
| 4 | ¿Qué países tienen mucha venta pero poca ganancia o pérdida? | `Country`, `Sales`, `Profit` | Dispersión |

## 3. Qué vendemos

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 5 | ¿Qué categoría aporta más ventas y cuál es la más rentable? | `Category`, `Sales`, `Profit` | Barras agrupadas |
| 6 | ¿Qué subcategorías generan pérdidas? | `Sub.Category`, `Profit` | Barras horizontales ordenadas |

## 4. A quién vendemos

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 7 | ¿Qué segmento de cliente (Consumer, Corporate, Home Office) compra más? | `Segment`, `Sales` | Dona |
| 8 | ¿Quiénes son los 10 clientes que más compran? | `Customer.Name`, `Sales` | Tabla o barras top 10 |

## 5. Rentabilidad y descuentos

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 9 | ¿Los descuentos altos hacen perder dinero? | `Discount`, `Profit` | Dispersión |
| 10 | ¿Qué porcentaje de pedidos deja pérdida? | `Profit` < 0 | Tarjeta KPI |

## 6. Logística

| # | Pregunta | Columnas | Gráfico |
|---|---|---|---|
| 11 | ¿Cuánto cuesta el envío según el modo y la prioridad del pedido? | `Ship.Mode`, `Order.Priority`, `Shipping.Cost` | Barras apiladas |
| 12 | ¿Cuántos días tarda en enviarse un pedido según el modo de envío? | `Ship.Date` − `Order.Date`, `Ship.Mode` | Columnas |

## Dato clave

En la muestra, **el 24% de los pedidos deja pérdida**. Las preguntas 6 y 9 ayudan a explicar de dónde viene.

## Selección para el dashboard

Para un dashboard de una página: preguntas **1, 3, 5, 6, 9 y 10**.
