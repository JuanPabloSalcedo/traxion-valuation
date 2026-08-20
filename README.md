# Valoración intrínseca - Grupo Traxión (BMV: TRAXIONA)

Valoración por flujo de caja libre a la firma (FCFF).

Grupo Traxión es la empresa líder de transporte y logística en México.
Se valora como ensayo metodológico previo a la valoración de una empresa privada de transporte de pasajeros.

## Estado

Módulo 1 (datos y normalización) completado.
Módulo 2 (costo de capital) en curso.

- [x] Estructura del repositorio
- [x] Serie histórica 2021-2025 transcrita y verificada
- [x] Criterio de deuda (incluye arrendamientos IFRS 16)
- [x] Partidas no recurrentes y normalización del EBIT
- [x] UDM a junio 2026 y construcción del año base
- [x] Moneda de trabajo y tasa libre de riesgo
- [x] Prima de riesgo de mercado y riesgo país
- [x] Selección de comparables para el beta ascendente
- [ ] Regresiones, desapalancamiento y ponderación del beta
- [ ] Costo de deuda y rating sintético
- [ ] Ponderaciones y WACC
- [ ] Estructura óptima de capital
- [ ] Flujos, crecimiento y valor terminal
- [ ] Puente al patrimonio y verificación contra mercado
- [ ] Valoración relativa
- [ ] Simulación de Monte Carlo

## Estructura

- `data/` : reportes fuente, datos intermedios y procesados
- `supuestos/` : parámetros del modelo con fuente y fecha
- `src/` : lógica de cálculo 
- `notebooks/` : narrativa del análisis
- `docs/` : bitácora de decisiones metodológicas y fuentes

Las decisiones metodológicas están documentadas en
[`docs/bitacora.md`](docs/bitacora.md).

## Metodología

Construida sobre la metodología de Aswath Damodaran (*Corporate Finance*, Stern NYU):

- Definición de deuda con arrendamientos capitalizados
- Betas ascendentes a partir de comparables cotizadas del sector
- ERP basada en precios de mercado actuales y no en el promedio histórico
- Rating sintético por cobertura de intereses, contrastado contra la calificación real
- En valor terminal, el ROC implícito y por tanto el crecimiento terminal deben ser razonables y menores a la tasa libre de riesgo

Cada supuesto lleva fuente y fecha, o se marca explícitamente como estimación.

## Decisiones metodológicas destacadas

El detalle completo está en [`docs/bitacora.md`](docs/bitacora.md).

- **Definición de deuda.** La empresa excluye los arrendamientos IFRS 16 de su "deuda total". Se reincorporan siguiendo el criterio económico de Damodaran: +14% de deuda, lo que altera ponderaciones del WACC y cobertura de intereses.

- **Discontinuidad por adquisición.** La compra de Solistica por parte de Traxion (jul-2025) parte la serie en dos. 2025 es un año híbrido (6 meses con Solistica).
Se aísla la contribución de la adquisición para medir el crecimiento real alrededor de 3%, frente al consolidado de 16%.

- **Normalización del EBIT.** Se ubica cada partida no recurrente dentro o debajo de la utilidad de operación antes de ajustarla. Al normalizar, la aparente caída de márgenes de 2024 resulta ser un efecto contable de gastos de reestructura.

- **Año base construido, no copiado.** Ningún ejercicio anual representa la empresa actual. El tamaño se toma de los últimos doce meses medidos (jul-2025 a jun-2026, primeros doce meses completos con Solistica) y el margen se decide descomponiendo la rentabilidad por segmento.

- **Construcción en dólares, flujos en pesos.** La tasa de descuento debe estar en la moneda de los flujos, pero se construye en dólares porque los insumos de calidad (ERP implícita, betas sectoriales, spreads por rating) están estimados sobre mercados en dólares. La conversión usa paridad de Fisher. El bono soberano mexicano no se usa como tasa libre de riesgo: no está libre de incumplimiento, y usarlo crudo contaría el riesgo país dos veces. Se emplea como verificación cruzada.

- **El Treasury tampoco es libre de riesgo.** Estados Unidos tiene calificación Aa1, lo que implica un spread de default de 0.22%. Se ajusta la tasa base y se traslada ese spread a la prima, aplicando a Estados Unidos el mismo criterio que con el bono mexicano.

- **Sector de referencia verificado, no supuesto.** Se descargó el listado de compañías por industria para comprobar qué contiene cada sector en vez de inferirlo del nombre. Resultado: Trucking y Transportation son categorías paralelas y cada segmento de Traxión tiene su propia referencia. La muestra de mercados emergentes se descarta pese a que Traxión es mexicana: su R² de 1.5% y un D/E implícito de 170% indican betas sesgados por iliquidez, y el riesgo país ya entró por la prima.

- **Comparables verificadas una por una.** De 153 empresas del universo se evaluaron 91 y se incluyeron 20. Las verificaciones produjeron siete correcciones sobre la clasificación inicial hecha por sector y nombre: Universal Logistics, RXO y Landstar resultaron asset-light y pasaron a logística; Werner, ArcBest y Covenant resultaron híbridas; Ryder resultó conglomerado sin negocio dominante. Cada descarte queda documentado con su razón.

- **Sin beta separado para movilidad de personas.** No existe sector de transporte de pasajeros bajo contrato en la clasificación de Damodaran y las comparables cotizadas del nicho son inviables: Mobico está en reestructuración, Ryder y Zigup arriendan flota sin operarla, y los operadores japoneses son transporte público regulado. Se usa el beta del grupo de carga, que comparte estructura de costos fijos y contratos de largo plazo. Kelsian se conserva como verificación, no como insumo.

## Datos

- `data/interim/traxion_anual.csv` : serie histórica 2021-2025 más UDM a jun-2026
- `data/interim/universo_comparables.csv` : 153 empresas del listado de Damodaran
- `data/interim/comparables.csv` : selección final con verificación de negocio y razón de cada descarte

La procedencia de cada dato está en [`docs/fuentes.md`](docs/fuentes.md).

## Instalación

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt