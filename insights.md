# Insights – Global Superstore

Respuestas a las 18 preguntas de [preguntas.md](preguntas.md), calculadas sobre el **dataset completo** (51,290 filas, 2011–2014).

Definiciones:
- **Margen %** = `Profit` / `Sales`
- **Pedido con pérdida** = fila con `Profit` < 0
- **Días de envío** = `Ship.Date` − `Order.Date`

---

## Gráfica 1 – Situación actual (KPI)

### 1. ¿Cómo estamos hoy en términos generales de ventas, margen y operación?

| KPI | Valor |
|---|---|
| Ventas totales | $12.64 M |
| Ganancia total | $1.47 M |
| Margen | 11.6% |
| Pedidos únicos | 25,035 |
| Filas con pérdida | 24.5% |
| Días promedio de envío | 4.0 |

**Insight:** el negocio es rentable, pero **1 de cada 4 ventas pierde dinero**.

### 4. ¿Los pedidos de prioridad Critical/High se envían más rápido que los Low?

| Prioridad | Días promedio de envío |
|---|---|
| Critical | 1.8 |
| High | 3.1 |
| Medium | 4.5 |
| Low | 6.5 |

**Insight:** sí. La prioridad se respeta: un pedido Critical sale 3.6 veces más rápido que uno Low. **La operación está sana.**

### 5. ¿Qué porcentaje de pedidos deja pérdida?

| Año | Filas con pérdida |
|---|---|
| 2011 | 24.7% |
| 2012 | 24.5% |
| 2013 | 24.1% |
| 2014 | 24.6% |

**Insight:** el problema es **estable**: no empeora, pero tampoco se corrige. Es un problema estructural, no de un año puntual.

---

## Gráfica 2 – Crecimiento

### 2. ¿Estamos creciendo en ventas o no?

| Año | Ventas | Crecimiento |
|---|---|---|
| 2011 | $2.26 M | — |
| 2012 | $2.68 M | +18.5% |
| 2013 | $3.41 M | +27.2% |
| 2014 | $4.30 M | +26.3% |

**Insight:** sí. Las ventas casi se **duplicaron en 4 años** (+90%).

### 3. ¿El margen acompaña el crecimiento de las ventas?

| Año | Margen |
|---|---|
| 2011 | 11.0% |
| 2012 | 11.5% |
| 2013 | 11.9% |
| 2014 | 11.7% |

**Insight:** sí. El margen se mantiene estable entre 11% y 12%, así que **la ganancia crece al mismo ritmo que las ventas** ($249 K → $504 K).

### 6. ¿Existen señales tempranas de deterioro?

Margen por trimestre: entre 10.1% y 13.1%, sin una tendencia a la baja. El 2014 cierra en 11.3% (T4), dentro del rango normal.

**Insight:** **no hay señales de deterioro.** La variación entre trimestres es normal. El riesgo no está en la tendencia, sino en el 24.5% de pedidos con pérdida, que se mantiene fijo.

---

## Gráfica 3 – Dónde, a quién y cómo vendemos

### 7. ¿Qué tipo de cliente genera más ventas y más margen?

| Segmento | % de ventas | Margen |
|---|---|---|
| Consumer | 51.5% | 11.5% |
| Corporate | 30.3% | 11.5% |
| Home Office | 18.3% | 12.0% |

**Insight:** **Consumer genera la mitad de las ventas.** Los márgenes son casi iguales en los tres segmentos, así que el tipo de cliente no explica el problema.

### 8. ¿Qué mercados muestran crecimiento en ventas respecto al año anterior?

| Mercado | Crecimiento 2014 vs 2013 | Margen |
|---|---|---|
| EMEA | **+47.4%** | **5.4%** |
| EU | +36.8% | 12.7% |
| APAC | +24.1% | 12.2% |
| Africa | +23.6% | 11.3% |
| Canada | +20.9% | **26.6%** |
| US | +20.6% | 12.5% |
| LATAM | +16.2% | 10.2% |

**Insight:** todos los mercados crecen. **EMEA es el que más crece, pero tiene el peor margen (5.4%).** Crece "comprando" ventas. APAC y EU son los mercados más grandes y rentables.

### 9. ¿Qué modo de envío usan más los clientes y cuál deja más margen?

| Modo | % de ventas | Margen |
|---|---|---|
| Standard Class | 59.9% | 11.8% |
| Second Class | 20.3% | 11.4% |
| First Class | 14.5% | 11.4% |
| Same Day | 5.3% | 11.4% |

**Insight:** **6 de cada 10 ventas van por Standard Class.** El margen casi no cambia según el modo de envío.

### 12. ¿Qué modo de envío tiene mayor costo de envío respecto a la venta?

| Modo | Costo de envío / venta |
|---|---|
| Same Day | 17.4% |
| First Class | 16.8% |
| Second Class | 12.2% |
| Standard Class | 8.1% |

**Insight:** los envíos rápidos cuestan **el doble** en proporción a la venta que Standard Class. Aun así, el margen se mantiene (pregunta 9), así que **el costo de envío no es el problema.**

### 13. ¿Qué mercado tarda más en enviar los pedidos?

Todos los mercados tardan entre **3.7 y 4.0 días**.

**Insight:** **no hay mercados con retrasos.** La logística es igual de eficiente en todo el mundo.

---

## Gráfica 4 – Qué vendemos

### 10. ¿Qué productos bajan el margen?

| Subcategoría | Ventas | Ganancia | Margen |
|---|---|---|---|
| **Tables** | $757 K | **−$64 K** | **−8.5%** |
| Machines | $779 K | $59 K | 7.6% |
| Supplies | $243 K | $23 K | 9.3% |
| Chairs | $1.50 M | $140 K | 9.3% |
| Storage | $1.13 M | $108 K | 9.6% |

**Insight:** **Tables es la única subcategoría que pierde dinero.** Machines, Chairs y Storage están por debajo del margen promedio (11.6%).

### 11. ¿Qué categorías venden mucho pero aportan poco margen?

| Categoría | % de ventas | Margen |
|---|---|---|
| Technology | 37.5% | 14.0% |
| **Furniture** | **32.5%** | **6.9%** |
| Office Supplies | 30.0% | 13.7% |

**Insight:** **Furniture vende un tercio del total, pero su margen es la mitad del de las otras categorías.** Es la categoría problema, por Tables, Chairs y Bookcases.

### 16. ¿Qué combinaciones subcategoría × mercado son más críticas?

Combinaciones con más de $50 K en ventas, ordenadas por ganancia:

| Subcategoría | Mercado | Ganancia | Margen |
|---|---|---|---|
| Tables | EU | −$21.0 K | **−19.9%** |
| Tables | APAC | −$20.1 K | −8.9% |
| Tables | US | −$17.7 K | −8.6% |
| Tables | LATAM | −$12.3 K | −8.5% |
| Bookcases | US | −$3.5 K | −3.0% |
| Chairs | EMEA | −$0.6 K | −0.9% |

**Insight:** **Tables pierde dinero en los 4 mercados grandes.** El caso más grave es **Tables en EU** (−19.9%).

---

## Gráfica 5 – Causa y acción

### 14. ¿El problema está generalizado o concentrado?

**Por nivel de descuento:**

| Descuento | % de filas | Filas con pérdida | Ganancia |
|---|---|---|---|
| 0% | 56.6% | 0.0% | +$1.77 M |
| 1–20% | 21.4% | 21.6% | +$0.51 M |
| 21–40% | 8.5% | **76.2%** | **−$0.19 M** |
| >40% | 13.6% | **98.4%** | **−$0.63 M** |

**Por otras dimensiones:**
- **Segmento:** 24.1%–24.6% de filas con pérdida. No cambia.
- **Mercado:** Canada tiene **0% de pérdidas y 0% de descuento**. EMEA tiene el mayor descuento promedio (19.6%) y el mayor % de pérdidas (31.9%).
- **Categoría:** Furniture tiene 31.6% de filas con pérdida, frente a 22–24% en las otras dos.

**Insight:** el problema **está concentrado en los descuentos mayores al 20%**. No depende del tipo de cliente. **Sin descuento, ningún pedido pierde dinero.**

### 15. ¿Qué problemas tienen mayor impacto en el margen?

Los descuentos mayores al 20% están en **22% de las filas** y generan **−$815 K** de ganancia. Eso equivale a más de la mitad de la ganancia total ($1.47 M).

**Insight:** **el descuento excesivo es el principal problema del negocio.** Tables y Furniture son el segundo, y se explican en parte por lo mismo.

### 17. ¿Dónde deberíamos priorizar acciones?

Pérdidas por pedidos con descuento mayor al 20%:

| Por mercado | Pérdida | Por subcategoría | Pérdida |
|---|---|---|---|
| EU | −$165 K | Tables | −$133 K |
| APAC | −$157 K | Bookcases | −$90 K |
| LATAM | −$146 K | Phones | −$87 K |
| US | −$135 K | Machines | −$73 K |
| EMEA | −$123 K | Chairs | −$72 K |

**Insight:** hay que priorizar **Tables y Bookcases** (Furniture) en **EU, APAC y LATAM**. EMEA requiere atención especial porque es el mercado de mayor crecimiento y el de peor margen.

### 18. ¿Qué mejora tendría mayor impacto?

**Ponerle un tope de 20% a los descuentos.**

Si los pedidos con más de 20% de descuento hubieran quedado sin ganancia ni pérdida, en lugar de perder dinero:

| | Actual | Con el tope |
|---|---|---|
| Ganancia | $1.47 M | **$2.28 M** (+55%) |

**Insight:** es la acción con mayor impacto. **Recupera hasta $815 K**, y no hace falta tocar la logística, que ya funciona bien.

*Supuesto: los pedidos con descuento mayor al 20% pasan a ganancia cero. El efecto real depende de cuántos clientes seguirían comprando con menos descuento.*

---

## Historia para la presentación

> **Crecemos rápido y la operación funciona bien**: las ventas suben más de 20% al año, el margen se mantiene estable en 11–12% y los envíos respetan la prioridad.
>
> **Pero 1 de cada 4 ventas pierde dinero.** No es por el cliente ni por la logística: es por **descuentos mayores al 20%**, que se comen $815 K, sobre todo en **Tables (Furniture)** y en mercados como **EU, APAC y EMEA**.
>
> **Recomendación:** ponerle un tope de 20% a los descuentos y revisar el precio de Tables. Esto podría aumentar la ganancia hasta en 55% sin frenar el crecimiento.
