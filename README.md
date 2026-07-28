# Valoración intrínseca - Grupo Traxión (BMV: TRAXIONA)

Valoración por flujo de caja libre a la firma (FCFF).

Grupo Traxión es la empresa líder de transporte y logística en México.
Se valora como ensayo metodológico previo a la valoración de una empresa privada de transporte de pasajeros.

## Estado

En construcción. Módulo 1 (datos y normalización) en curso.

- Estructura del repositorio
- Serie histórica 2021-2025 transcrita y verificada
- Criterio de deuda (incluye arrendamientos IFRS 16)
- Partidas no recurrentes identificadas y normalización del EBIT
- Construcción de año base


## Estructura

- `data/` : datos crudos (no versionados), intermedios y procesados
- `supuestos/` : parámetros del modelo con fuente y fecha
- `src/` : lógica de cálculo 
- `notebooks/` : narrativa del análisis
- `docs/` : bitácora de decisiones metodológicas y fuentes

Las decisiones metodológicas están documentadas en
[`docs/bitacora.md`](docs/bitacora.md).

## Decisiones metodológicas destacadas

El detalle completo está en [`docs/bitacora.md`](docs/bitacora.md).

Metodo de Valoración construida sobre la metodologia de Aswath Damodaran: Definición de deuda con arrendamientos, metodo de Betas ascendentes, ERP basada en precios de mercado actuales y no el promedio historico, en Valor Terminal el ROC implicito y, por tanto, el crecimiento terminal, debe ser razonable y menor a la tasa libre de riesgo, etc.

- **Definición de deuda.** La empresa excluye los arrendamientos IFRS 16 de su "deuda total". Se reincorporan siguiendo el criterio económico de Damodaran: +14% de deuda, lo que altera ponderaciones del WACC y cobertura de intereses.

- **Discontinuidad por adquisición.** La compra de Solistica por parte de Traxion (jul-2025) parte la serie en dos. 2025 es un año híbrido (6 meses con Solistica).
Se aísla la contribución de la adquisición para medir el crecimiento real alrededor de3%, frente al consolidado de 16%.

- **Normalización del EBIT.** Se ubica cada partida no recurrente dentro o debajo de la utilidad de operación antes de ajustarla. Al normalizar, la aparente caída de márgenes de 2024 parece ser un efecto contable de gastos de reestructura.

- **Año base construido, no copiado.** Ningún ejercicio anual representa la empresa actual. El tamaño se toma de los últimos doce meses medidos (jul-2025 a jun-2026, primeros doce meses completos con Solistica) y el margen se decide descomponiendo la rentabilidad por segmento.


## Instalación

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt