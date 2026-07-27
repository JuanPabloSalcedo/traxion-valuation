# Bitácora de decisiones metodológicas

Registro de hallazgos, criterios aplicados y decisiones de modelación.

Orden cronológico inverso: la entrada más reciente primero.

Formato: fecha, qué se encontró o decidió, en qué se basa,
qué implica para el resto del modelo.

## 2026-07-26 - Decisión del año base

**Problema**

La empresa a valorar (2026 en adelante) incluye Solistica el año completo pero ningún año de la serie representa eso:
- 2021-2024: sin Solistica se subestima el tamaño
- 2025: híbrido, solo 6 meses de Solistica, con factores transitorios (combustible, trimestre atípico).
- 2026 completo: aún no existe. El 2T26 no se ha publicado.

**Lo que muestra la serie (EBIT normalizado):**

Con el csv armado se puede observar que:

Margen EBIT normalizado: ebit_normalizado / ingresos_totales
Y Cobertura de interees: ebit_normalizado / gasto_intereses

| Año | Margen EBIT norm. | Cobertura intereses |
|---|---|---|
| 2021 | 11.12% | 3.30x |
| 2022 | 8.29% | 1.88x |
| 2023 | 9.31% | 1.58x |
| 2024 | 9.21% | 1.60x |
| 2025 | 7.37% | 1.40x |

El negocio operó en 8-9% de margen en 2022-2024. La caída a 7.4% en 2025 coincide con Solistica.

**Crecimiento real (sin Solistica):**

Ingresos 2025 = 33,814 − 3,736 = 30,078.
Contra 2024 (29,142): crecimiento cercani a 3.2%. El 16% consolidado es mayormente adquisición, no crecimiento del negocio base.

**Decisión**

Ante la probelamatica se decide que el año base no se va a copiar de ningún año sino que se va a construir.
- Tamaño (ingresos base): Traxión sin solistica + Solistica anualizada, para intentar reflejar la empresa completa de hoy.
- Rentabilidad (margen base): margen EBIT normalizado de mediano plazo (~8-9% histórico)
- Los factores transitorios de 2025 (combustible, trimestre) seexcluyen; el efecto estructural de la mezcla post-Solistica se conserva.


## 2026-07-25 - Verificación de 2021,2022 y 2023 y márgenes normalizados

Cifras convertidas a millones de pesos. 

**2021, 2022 y 2023 son años limpios:** la reconciliación de EBITDA sin reestructura, sin ganancias po adquisición. ebit_normalizado = ebit = 2,310.5.


**Hallazgo - la caída de márgenes era en parte un espejismo:**
con EBIT normalizado, el margen operativo es 9.31% (2023), 9.21% (2024) y 7.37% (2025). El deterioro aparente de 2024 (8.43% con EBIT crudo) se debía a los gastos de reestructura; al normalizar, 2023 y 2024 quedan casi iguales. El desplome real ocurre solo en 2025, coincidiendo con Solistica.
A investigar.

**Discrepancia de efectivo en 2021:** el balance reporta 1,260.7, pero otra sección del reporte muestra 1,335.1 para el mismo año. Se adopta el valor del balance (estado financiero primario). 

## 2026-07-25 - Verificación de 2024 y ubicación de partidas no recurrentes

Cifras convertidas a millones de pesos. 

**Verificación**
Ingresos y EBIT de 2024 son idénticos en el reporte 2024 y en la comparativa del reporte 2025. 
Se usa el reporte 2024 como fuente.

**EBIT normalizado 2024 = 2,685.3**

EBIT reportado: 2,457.1
+ 228.2 gastos por reestructura anotado en el desglose del EBITDA.
el estado de resultados no tiene línea propia de reestructura, por lo que el gasto está dentro de la utilidad de operación. Por eso sí
se ajusta al EBIT, a diferencia de la ganancia por adquisición de 2025, que está debajo del EBIT y no se ajusta.

**Deuda total 2024 = 13,625.9** (suma de 6 líneas, incluye IFRS 16).

## 2026-07-25 - Serie anual:verificación de 2025

Cifras convertidas a millones de pesos. 

**Verificaciones**

- PyG (ingresos, EBIT, DyA, intereses, utilidad neta, impuesto base fiscal, utilidad antes de impuestos)
- capex_flota: La cifra es "Adquisiciones de equipo de transporte y maquinaria" del estado de flujos.
- capex_adquisiciones: "Contraprestación por adquisición de negocios" (Solistica).
- deuda_total: 16,019.4, armada sumando las seis líneas de deuda del balance (incluye obligaciones por arrendamiento IFRS 16, según el
criterio ya adoptado). El balance anual agrupa el arrendamiento capitalizable e IFRS 16 en una sola línea, a diferencia del trimestral que los desglosa.
- efectivo (1,600.2) y capital_contable (14,444.4)

**Contribución de Solistica (6 meses, jul-dic 2025), según nota d combinaciones de negocios:**

- Ingresos: 3,735.9
- Utilidad de operación: 286.6
Permite construir la serie orgánica (sin Solistica) por diferencia.

**EBIT normalizado 2025 = 2,493.2**

- EBIT reportado: 2,482.0
- + 11.2 de costos de adquisición de Solistica (auditoría, legales, notariales), reconocidos en gastos generales no recurrentes.
- La ganancia por adquisición de negocios (42.7) no se ajusta en el EBIT: en el estado de resultados aparece debajo de la utilidad deoperación, en el bloque financiero. Solo afectaría un EBIT/utilidad neta normalizados, no el EBIT operativo.

## 2026-07-25 - Fecha de discontinuidad de la integración de Solistica

En el 1T26 se observó que los ingresos de logística crecian rapidamente por la integración de Solistica.
Dicha adquisición rompe la serie histórica en dos. Pues si la empresa compra otra compañia grande, los años anteriores 
y posteriores no son comparables por composición.

Se revisa el reporte anual de 2025 para poder saber esta fecha de corte.

**Qué se encontro**

"En julio de 2025 adquirimos Solistica, una empresa líder de servicios logísticos propiedad de Grupo FEMSA y con 
operaciones en tres países: México, Brasil y Colombia. De manera simultánea, vendimos las operaciones de Brasil y 
Colombia, por lo que TRAXION únicamente adquirió operaciones y activos de México, por una inversión neta de Ps. 
1,650 millones." 

"el 1 de julio de 2025 Grupo  Traxión adquirió el 100% de las acciones con derecho a voto de Solística. 
Por lo anterior, los ingresos, costos y gastos de Solística no forman parte del estado de resultados consolidado de Grupo Traxión 
por los primeros seis meses del año 2025, ni por los años completos 2024 y 2023. Así mismo, los activos y pasivos de Solística no forman parte del estado de situación financiera consolidado de Grupo Traxión al 31 de diciembre de 2024 y 2023" 

"En julio 2025 realizamos una disposición por 1,600 millones del crédito sindicado para la adquisición de 
Solística." 

"Así mismo el 1º de julio de 2025 simultáneamente se llevó a cabo la venta de las operaciones de Solística 
en Brasil y Colombia, el precio pactado por esta transacción fue de $2,381,631" 

"Por los seis meses terminados desde la fecha de adquisición al 31 de diciembre de 2025 Solística contribuyó 
a los resultados del Grupo con un total de $3,735,889 de ingresos y aportó una utilidad de operación de 
$286,567." 

"En el año terminado el 31 de diciembre de 2025, Grupo Traxión incurrió en costos relacionados con la 
adquisición de Solistica por $11,200 principalmente relacionadas con auditoria de compra, honorarios legales 
y notariales, los cuales fueron reconocidos en gastos generales" 

"El 1º de julio de 2025 se llevó a cabo la adquisición y venta simultanea de las subsidiarias de Solistica 
correspondientes a las operaciones de Brasil y Colombia, mismas que clasificadas cómo disponibles para la 
venta y reconocidas a su valor razonable menos costos estimados de venta por un monto de $2,381,631   El 
precio de la venta fue el mismo que el costo de la compra, por lo que no se generaron pérdidas o ganancias 
en esta transacción. La razón de la venta fue por enfocar los esfuerzos estratégicos del Grupo en México y 
Estados Unidos" 

**Decisión**

La serie deja de ser comparable a partir del 2025. Concretamente a partir de julio. 
Se puede considerar 2025 como un año híbrido: seis meses de la Traxión vieja y seis meses de la Traxión con Solistica. 
No es comparable ni con 2024 ni con 2026.

La empresa manifiesta que "Solística contribuyó con $3,735,889 de ingresos y aportó una utilidad de operación de $286,567" (seis meses).
Esto puede permitir construir una serie orgánica y comparable (Traxion sin solistica, 2021-2025)
Ejemplo: Ingresos 2025 sin Solistica = Ingresos totales 2025 − 3,736

Para efectos de valoración lo relevante es que Traxion se quedo solo con Mexico financiado con 1,600 de disposición del crédito sindicado.
Deuda bancaria.

Los 11,2 de costos de adquisición hacen caer la utilidad de 2025 por el evento mencionado. Es un gasto no recurrente por lo que se tendrá
en cuenta cuando se normalice EBIT.

Otros ajustes para tener en cuenta al normalizar EBIT en 2025:
![Reconciliación de utilidad neta a EBITDA ajustado, reporte anual 2025](img/reconciliacion_ebitda_2025.png)


- Ganancia por adquisicion
- gastos por reestructura

La empresa ofrece su EBITDA ya calculado, es util como referencia pero se usará EBIT para valorar, la depreciación es relevante
en transportadora que consume flota. Tambien, la empresa decide los ajustes que le conviene resaltar. Por eso se contruye Ebit normalizado propio.


## 2026-07-22 - Cobertura de intereses del 1T26 y rating sintético

Fuente: Reporte Trimestral 1T26, p. 14 (Estado de Resultados).
Cifras en miles de pesos.

**Qué se encontro**

Cobertura de intereses = Utilidad de operación / Gasto por intereses

455,825 / 430,990 = 1.06

para el 1T25:

689,545 / 463,036 = 1.49

**Rating sintético implícito**

Aplicando la tabla de calificaciones sintéticas por índice de cobertura para empresas grandes no financieras:

![Tabla de rating sintético por índice de cobertura de intereses](img/damodaran_ratings_cobertura.png)

*Fuente: Damodaran, "Ratings, Interest Coverage Ratios and Default Spread". Consultado 2026-07-22.*

Para 1T2026:
    Rating sintético implícito: Caa/CCC
    Spread por incumplimiento asociado: 8,85%


**Calificación real de Fitch**

Pendiente de obtener.

**Criterio aplicado**

El rating sintético se estima con el EBIT normalizado, no con el de un trimestre aislado. Un único trimestre golpeado por alza de combustible y caída de volumen en carga no es base válida para asignar calificación.
De igual forma, este rating sintetico esta en dólares. Traxion reporta en pesos,  aplicar este spread en dólares a una tasa libre de riesgo en pesos mezcla monedas. Esto se resolverá en  el Modulo 2.

**Decisión**

El número se registra como observación preliminar. El cálculo definitivo se hace en el Módulo 2, con la corrección de la divisa, el EBIT normalizado  sobre serie anual, y con el gasto financiero que corresponda a la definición de deuda ya adoptada (16,518, incluyendo IFRS 16).

**Implicaciones**

- Este es el contraste que motivó elegir Traxión: permite medir cuánto se desvía el rating sintético del real cuando ambos existen. En una
empresa privada solo se dispone del sintético, sin forma de verificarlo.
- Pendiente: obtener el reporte de Fitch y verificar qué definición de deuda y qué EBIT utiliza. Si Fitch excluye IFRS 16 como lo hace la
compañía, los ratios no son comparables sin ajuste.

## 2026-07-22 - Reestructuración anunciada en movilidad de carga

Fuente: Reporte Trimestral 1T26, p. 3 (Mensaje del Presidente Ejecutivo).

**Qué se encontro**

La administración anuncia un plan de ajuste.

Objetivo declarado: reducir base de costos y bajar el apalancamiento hacia el cierre del año.

Contexto: la guía original para 2026 era crecimiento de ~10% en ingresos y EBITDA con margen cercano a 16%. El 1T26 cerró con margen
de 13.7%.

**Criterio aplicado**

Un anuncio de reestructuración modifica la trayectoria futura de capex, márgenes y base de activos, que son insumos directos de la proyección de flujos.

**Decisión**

Se registra como hecho conocido a la fecha de valoración. No se incorpora a los supuestos: faltaría verificar ejecución en los trimestres siguientes.


## 2026-07-22 - El 1T26 no es un trimestre representativo

Fuente: Reporte Trimestral 1T26, p. 5 (Análisis de Resultados).

**Qué se encontro** 

La propia administración advierte contra usar este trimestre como base:

- El 1T25 fue "un trimestre particularmente favorable en términos financieros y operativos", y los trimestres siguientes se vieron afectados por fenómenos geopolíticos.
- El margen EBITDA del 1T26 (13.7%) se ubica "en un nivel atípico comparado con las operaciones regulares de la compañía".
- La compañía se describe a sí misma "en una etapa de normalización operativa".

Factores no recurrentes identificados en el trimestre:

Conflicto militar en Medio Oriente
Incertidumbre arancelaria
Fortaleza del peso
Integración de Solistica

**Criterio aplicado**

La base de proyección debe reflejar la capacidad normal de generación del negocio, no un punto atípico del ciclo. Ni el 1T25 (pico) ni el
1T26 (valle) sirven aislados.

**Decisión**

Pendiente. La elección de año base se resuelve con la serie anual completa, no con este documento.

**Implicaciones**

- El año base no puede ser un trimestre anualizado.
- La advertencia de la empresa sobre el 1T25 obliga a revisar si 2024
y 2025 tienen distorsiones equivalentes.

## 2026-07-22 - Arrendamientos y definición de deuda

Fuente: Reporte Trimestral 1T26, pp. 8 y 13. Cifras en millones MXN.

**Qué se encontro**

La empresa reporta una "Deuda total" de 14,484 (p. 8), compuesta por:
deuda CP 1,290 + arrend. capitalizable CP 2 + deuda LP 13,192
+ arrend. capitalizable LP 0.

Clasificando línea por línea el pasivo del balance (p. 13) según los
criterios de deuda, el total asciende a 16,518:

| Línea | Monto |
|---|---|
| Venc. circulante de deuda a largo plazo | 1,070 |
| Deuda bursátil circulante | 220 |
| Obligaciones por arrendamiento capitalizable CP | 2 |
| Obligaciones por arrendamiento IFRS 16 CP | 884 |
| Deuda bancaria a largo plazo | 8,692 |
| Deuda bursátil a largo plazo | 4,500 |
| Obligaciones por arrendamiento capitalizable LP | 0 |
| Obligaciones por arrendamiento IFRS 16 LP | 1,150 |
| **Total deuda** | **16,518** |

Conciliación: deuda 16,518 + pasivos no financieros 8,978
= 25,496 = total del pasivo. 

**Diferencia: 2,034 (+14.0%)**, correspondiente íntegramente a las obligaciones por arrendamiento bajo IFRS 16.

**Qué dice la empresa**

Pie de nota 5 de la tabla de PERFIL DE LA DEUDA (p. 8): la deuda total está calculada "basado en la definición de deuda como lo
determina el crédito sindicado". Es decir, una definición contractual, no una definición económica.

**Criterio aplicado**

Definición de deuda típica en Finanzas Corpotativas de profesores como
Aswath Damodaran basada en 3 criterios: compromiso contractual de
pago, deducibilidad fiscal del pago, y pérdida de control del activo
ante incumplimiento. Un arrendamiento bajo IFRS 16 cumple las tres: hay
calendario contractual de cuotas, el componente de interés es
deducible, y el incumplimiento faculta al arrendador a recuperar el
activo. El balance lo reconoce como pasivo y registra su
contrapartida en el activo por derecho de uso (2,046).

**Decisión**

Se adopta 16,518 como deuda para todos los cálculos del modelo. La cifra de 14,484 se conserva únicamente como referencia de lo que
reporta la empresa.

**Implicaciones**

- Ponderaciones del costo de capital: la D del WACC sube 14%.
- Beta ascendente: el D/E de reapalancamiento cambia.
- Rating sintético: la cobertura de intereses se calcula con el gasto
financiero que incluye el componente de interés de los arrendamientos.
- Deuda neta: 15,101 en lugar del 13,067 reportado en la pag 8.
- Comparabilidad: al cotejar apalancamiento contra comparables del
sector hay que verificar si ellos también excluyen IFRS 16. Si se
compara la cifra ajustada de Traxión contra la cifra reportada de
otros, Traxión aparece artificialmente más endeudada.

## 2026-07-22 - Módulo 1 iniciado

Estructura del repositorio creada. Primer commit.
Alcance: Valoración FCFF completa y se incluye módulo de estructura óptima
de capital porque Traxión tiene rating real de Fitch contra el cual calibrar un cronograma
de costo de deuda kd.