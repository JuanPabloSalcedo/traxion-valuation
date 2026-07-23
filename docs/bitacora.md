# Bitácora de decisiones metodológicas

Registro de hallazgos, criterios aplicados y decisiones de modelación.

Orden cronológico inverso: la entrada más reciente primero.

Formato: fecha, qué se encontró o decidió, en qué se basa,
qué implica para el resto del modelo.




## 2026-07-22 — Cobertura de intereses del 1T26 y rating sintético

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

El rating sintético se estima con el EBIT normalizado, no con el de un
trimestre aislado. Un único trimestre golpeado por alza de combustible
y caída de volumen en carga no es base válida para asignar calificación.
De igual forma, este rating sintetico esta en dólares. Traxion reporta en pesos, 
aplicar este spread en dólares a una tasa libre de riesgo en pesos mezcla monedas. Esto se resolverá en 
el Modulo 2.

**Decisión**

El número se registra como observación preliminar. El cálculo
definitivo se hace en el Módulo 2, con la corrección de la divisa, el EBIT normalizado 
sobre serie anual, y con el gasto financiero que corresponda a la definición de
deuda ya adoptada (16,518, incluyendo IFRS 16).

**Implicaciones**

- Este es el contraste que motivó elegir Traxión: permite medir cuánto
  se desvía el rating sintético del real cuando ambos existen. En una
  empresa privada solo se dispone del sintético, sin forma de
  verificarlo.
- Pendiente: obtener el reporte de Fitch y verificar qué definición de
  deuda y qué EBIT utiliza. Si Fitch excluye IFRS 16 como lo hace la
  compañía, los ratios no son comparables sin ajuste.

## 2026-07-22 — Reestructuración anunciada en movilidad de carga

Fuente: Reporte Trimestral 1T26, p. 3 (Mensaje del Presidente Ejecutivo).

**Qué se encontro**

La administración anuncia un plan de ajuste.

Objetivo declarado: reducir base de costos y bajar el apalancamiento
hacia el cierre del año.

Contexto: la guía original para 2026 era crecimiento de ~10% en
ingresos y EBITDA con margen cercano a 16%. El 1T26 cerró con margen
de 13.7%.

**Criterio aplicado**

Un anuncio de reestructuración modifica la
trayectoria futura de capex, márgenes y base de activos, que son
insumos directos de la proyección de flujos.

**Decisión**

Se registra como hecho conocido a la fecha de valoración. No se
incorpora a los supuestos: faltaría verificar ejecución en los
trimestres siguientes.


## 2026-07-22 — El 1T26 no es un trimestre representativo

Fuente: Reporte Trimestral 1T26, p. 5 (Análisis de Resultados).

**Qué se encontro** 

La propia administración advierte contra usar este trimestre como base:

- El 1T25 fue "un trimestre particularmente favorable en términos
  financieros y operativos", y los trimestres siguientes se vieron
  afectados por fenómenos geopolíticos.
- El margen EBITDA del 1T26 (13.7%) se ubica "en un nivel atípico
  comparado con las operaciones regulares de la compañía".
- La compañía se describe a sí misma "en una etapa de normalización
  operativa".

Factores no recurrentes identificados en el trimestre:

Conflicto militar en Medio Oriente
Incertidumbre arancelaria
Fortaleza del peso
Integración de Solistica

**Criterio aplicado**

La base de proyección debe reflejar la capacidad normal de generación
del negocio, no un punto atípico del ciclo. Ni el 1T25 (pico) ni el
1T26 (valle) sirven aislados.

**Decisión**

Pendiente. La elección de año base se resuelve con la serie anual
completa, no con este documento.

**Implicaciones**

- El año base no puede ser un trimestre anualizado.
- La advertencia de la empresa sobre el 1T25 obliga a revisar si 2024
  y 2025 tienen distorsiones equivalentes.

## 2026-07-22 — Arrendamientos y definición de deuda

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

**Diferencia: 2,034 (+14.0%)**, correspondiente íntegramente a las
obligaciones por arrendamiento bajo IFRS 16.

**Qué dice la empresa**

Pie de nota 5 de la tabla de PERFIL DE LA DEUDA (p. 8): la
deuda total está calculada "basado en la definición de deuda como lo
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

Se adopta 16,518 como deuda para todos los cálculos del modelo. La
cifra de 14,484 se conserva únicamente como referencia de lo que
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

  ## 2026-07-22 — Módulo 1 iniciado

Estructura del repositorio creada. Primer commit.
Alcance: Valoración FCFF completa y se incluye módulo de estructura óptima
de capital porque Traxión tiene rating real de Fitch contra el cual calibrar un cronograma
de costo de deuda kd.