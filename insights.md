# Insights – Global Superstore

Respuestas a las 18 preguntas de [preguntas.md](preguntas.md), calculadas sobre la **muestra** `data/superstore_muestra.csv` (5,130 filas, 2011–2014). Es la misma data que se usa en Power BI, así que los números coinciden con el dashboard.

Definiciones:
- **Margen %** = `Profit` / `Sales`
- **Pedido con pérdida** = fila con `Profit` < 0
- **Días de envío** = `Ship.Date` − `Order.Date`

---

## Gráfica 1 – Situación actual (KPI)

### 1. ¿Cómo estamos hoy en términos generales de ventas, margen y operación?

| KPI | Valor |
|---|---|
| Ventas totales | $1.26 M |
| Ganancia total | $143 K |
| Margen | 11.4% |
| Pedidos únicos | 4,651 |
| Filas con pérdida | 23.9% |
| Días promedio de envío | 4.0 |

**Insight:** el negocio es rentable, pero **1 de cada 4 ventas pierde dinero**.

### 4. ¿Los pedidos de prioridad Critical/High se envían más rápido que los Low?

| Prioridad | Días promedio de envío |
|---|---|
| Critical | 1.9 |
| High | 3.1 |
| Medium | 4.5 |
| Low | 6.4 |

**Insight:** sí. Un pedido Critical sale 3.5 veces más rápido que uno Low. **La operación está sana.**

### 5. ¿Qué porcentaje de pedidos deja pérdida?

| Año | Filas con pérdida |
|---|---|
| 2011 | 23.8% |
| 2012 | 25.0% |
| 2013 | 24.1% |
| 2014 | 23.1% |

**Insight:** el problema es **estable**: se mantiene alrededor de 24% todos los años. Es estructural, no de un año puntual.

---

## Gráfica 2 – Crecimiento

### 2. ¿Estamos creciendo en ventas o no?

| Año | Ventas | Crecimiento |
|---|---|---|
| 2011 | $215 K | — |
| 2012 | $266 K | +23.6% |
| 2013 | $332 K | +24.9% |
| 2014 | $445 K | +33.8% |

**Insight:** sí, y cada año más rápido. Las ventas se **duplicaron en 4 años** (+107%).

### 3. ¿El margen acompaña el crecimiento de las ventas?

| Año | Margen |
|---|---|
| 2011 | 9.9% |
| 2012 | 10.9% |
| 2013 | **12.8%** |
| 2014 | **11.3%** |

**Insight:** hasta 2013 sí: el margen subió junto con las ventas. **En 2014 las ventas crecieron más que nunca (+33.8%), pero el margen cayó 1.5 puntos.**

### 6. ¿Existen señales tempranas de deterioro?

Margen por trimestre:

| Trimestre | 2011 | 2012 | 2013 | 2014 |
|---|---|---|---|---|
| T1 | 8.1% | 8.0% | 12.4% | **8.3%** |
| T2 | 8.6% | 11.7% | 13.1% | **8.5%** |
| T3 | 13.3% | 10.8% | 12.6% | 16.9% |
| T4 | 8.9% | 11.6% | 12.7% | **9.7%** |

**Insight:** **sí hay una señal.** En 2013 todos los trimestres estuvieron por encima de 12%. En 2014, tres de los cuatro trimestres volvieron a estar por debajo de 10%; solo el T3 (16.9%) sostuvo el año.

---

## Gráfica 3 – Dónde, a quién y cómo vendemos

### 7. ¿Qué tipo de cliente genera más ventas y más margen?

| Segmento | % de ventas | Margen |
|---|---|---|
| Consumer | 51.3% | 12.0% |
| Corporate | 31.3% | **9.7%** |
| Home Office | 17.4% | 12.5% |

**Insight:** **Consumer genera la mitad de las ventas.** Corporate es el segmento menos rentable.

### 8. ¿Qué mercados muestran crecimiento en ventas respecto al año anterior?

| Mercado | Crecimiento 2014 vs 2013 | Margen |
|---|---|---|
| EU | **+124.9%** | 12.3% |
| US | +54.7% | 10.7% |
| EMEA | +18.0% | **7.5%** |
| Canada | +12.8% | **28.0%** |
| Africa | +11.3% | 12.5% |
| LATAM | +5.1% | 11.8% |
| APAC | **+1.3%** | 11.0% |

**Insight:** **EU y US impulsan el crecimiento de 2014.** APAC, que es el mercado más grande, se estancó. EMEA tiene el peor margen.

> Nota: en la muestra, unos pocos pedidos grandes pesan mucho en el total de cada mercado. Estos crecimientos son menos precisos que los porcentajes por fila.

### 9. ¿Qué modo de envío usan más los clientes y cuál deja más margen?

| Modo | % de ventas | Margen |
|---|---|---|
| Standard Class | 62.4% | 11.8% |
| Second Class | 19.1% | 10.6% |
| First Class | 12.6% | 12.6% |
| Same Day | 5.9% | **6.4%** |

**Insight:** **6 de cada 10 ventas van por Standard Class.** Same Day deja la mitad del margen que los demás modos.

### 12. ¿Qué modo de envío tiene mayor costo de envío respecto a la venta?

| Modo | Costo de envío / venta |
|---|---|
| First Class | 16.7% |
| Same Day | 15.7% |
| Second Class | 12.7% |
| Standard Class | 8.3% |

**Insight:** los envíos rápidos cuestan **el doble** en proporción a la venta que Standard Class. Solo representan el 18% de las ventas, así que su impacto en el total es limitado.

### 13. ¿Qué mercado tarda más en enviar los pedidos?

Todos los mercados tardan entre **3.8 y 4.1 días**.

**Insight:** **no hay mercados con retrasos.** La logística es igual de eficiente en todos.

---

## Gráfica 4 – Qué vendemos

### 10. ¿Qué productos bajan el margen?

| Subcategoría | Ventas | Ganancia | Margen |
|---|---|---|---|
| **Tables** | $75 K | **−$7.0 K** | **−9.3%** |
| Machines | $97 K | $6.0 K | 6.2% |
| Binders | $44 K | $3.1 K | 7.0% |
| Phones | $169 K | $16.3 K | 9.6% |
| Supplies | $19 K | $1.9 K | 10.1% |

**Insight:** **Tables es la única subcategoría que pierde dinero.** Machines y Binders están muy por debajo del margen promedio (11.4%).

### 11. ¿Qué categorías venden mucho pero aportan poco margen?

| Categoría | % de ventas | Margen |
|---|---|---|
| Technology | 38.0% | 12.2% |
| **Furniture** | **32.6%** | **7.7%** |
| Office Supplies | 29.4% | 14.3% |

**Insight:** **Furniture vende un tercio del total, pero tiene el peor margen.**

### 16. ¿Qué combinaciones subcategoría × mercado son más críticas?

Combinaciones con más de $5 K en ventas, ordenadas por ganancia:

| Subcategoría | Mercado | Ganancia | Margen |
|---|---|---|---|
| Tables | APAC | −$3.8 K | **−16.4%** |
| Tables | US | −$2.6 K | −16.3% |
| Tables | EU | −$1.6 K | −14.6% |
| Bookcases | Africa | −$0.9 K | −16.2% |
| Machines | US | −$0.8 K | −3.6% |
| Chairs | EMEA | −$0.8 K | −13.8% |
| Tables | LATAM | −$0.6 K | −4.3% |

**Insight:** **Tables pierde dinero en los 4 mercados grandes.** El caso más grave es **Tables en APAC**.

---

## Gráfica 5 – Causa y acción

### 14. ¿El problema está generalizado o concentrado?

**Por nivel de descuento:**

| Descuento | % de filas | Filas con pérdida | Ganancia |
|---|---|---|---|
| 0% | 56.5% | 0.0% | +$173.4 K |
| 1–20% | 21.7% | 21.2% | +$52.5 K |
| 21–40% | 8.3% | **71.6%** | **−$15.5 K** |
| >40% | 13.5% | **98.8%** | **−$67.4 K** |

**Por otras dimensiones:**
- **Segmento:** 23.8%–24.2% de filas con pérdida. No cambia.
- **Mercado:** Canada tiene **0% de pérdidas y 0% de descuento**. EMEA tiene el mayor descuento promedio (19.1%) y el mayor % de pérdidas (31.4%).
- **Categoría:** Furniture tiene 31.6% de filas con pérdida, frente a 21–26% en las otras dos.

**Insight:** el problema **está concentrado en los descuentos mayores al 20%**. No depende del tipo de cliente. **Sin descuento, ningún pedido pierde dinero.**

### 15. ¿Qué problemas tienen mayor impacto en el margen?

Los descuentos mayores al 20% están en **21.8% de las filas** y generan **−$82.8 K** de ganancia. Eso equivale a más de la mitad de la ganancia total ($143 K).

**Insight:** **el descuento excesivo es el principal problema del negocio.** Tables y Furniture son el segundo.

### 17. ¿Dónde deberíamos priorizar acciones?

Pérdidas por pedidos con descuento mayor al 20%:

| Por mercado | Pérdida | Por subcategoría | Pérdida |
|---|---|---|---|
| EU | −$17.3 K | Tables | −$14.7 K |
| APAC | −$16.6 K | Phones | −$11.7 K |
| US | −$16.5 K | Machines | −$7.5 K |
| LATAM | −$13.0 K | Binders | −$7.4 K |
| EMEA | −$11.4 K | Bookcases | −$7.2 K |

**Insight:** hay que priorizar **Tables** en **EU, APAC y US**. EMEA requiere atención especial porque es el mercado que más descuenta y el de peor margen.

### 18. ¿Qué mejora tendría mayor impacto?

**Ponerle un tope de 20% a los descuentos.**

Si los pedidos con más de 20% de descuento hubieran quedado sin ganancia ni pérdida, en lugar de perder dinero:

| | Actual | Con el tope |
|---|---|---|
| Ganancia | $143 K | **$226 K** (+58%) |

**Insight:** es la acción con mayor impacto. **Recupera hasta $82.8 K**, y no hace falta tocar la logística, que ya funciona bien.

*Supuesto: los pedidos con descuento mayor al 20% pasan a ganancia cero. El efecto real depende de cuántos clientes seguirían comprando con menos descuento.*

---

## Historia para la presentación

> **Crecemos rápido y la operación funciona bien**: las ventas se duplicaron en 4 años (+33.8% solo en 2014) y los envíos respetan la prioridad.
>
> **Pero en 2014 el margen cayó de 12.8% a 11.3%, y 1 de cada 4 ventas pierde dinero.** No es por el cliente ni por la logística: es por **descuentos mayores al 20%**, que se comen $82.8 K, sobre todo en **Tables (Furniture)** y en mercados como **EU, APAC y US**.
>
> **Recomendación:** ponerle un tope de 20% a los descuentos y revisar el precio de Tables. Esto podría aumentar la ganancia hasta en 58% sin frenar el crecimiento.
