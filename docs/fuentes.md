# Fuentes de datos

Los reportes originales están en `data/raw/`. Esta tabla registra su
procedencia y fecha de consulta.

## Reportes de Traxión

| Archivo | Documento | Fecha |
|---|---|---|
| traxion_2021_anual.pdf | Reporte anual 2021 | 2026-07-25 |
| traxion_2022_anual.pdf | Reporte anual 2022 | 2026-07-25 |
| traxion_2023_anual.pdf | Reporte anual 2023 | 2026-07-25 |
| traxion_2024_anual.pdf | Reporte anual 2024 | 2026-07-25 |
| traxion_2025_anual.pdf | Reporte anual 2025 | 2026-07-25 |
| traxion_1T26_trimestral.pdf | Reporte trimestral 1T26 | 2026-07-22 |
| traxion_2T26_trimestral.pdf | Reporte trimestral 2T26 | 2026-07-28 |
| traxion_informe_integrado_2021..2024.pdf | Informes integrados | 2026-07-25 |

Todos de https://traxion.global/es/inversionistas/reportes

Los informes integrados se conservan como contexto corporativo. Las cifras
financieras del modelo provienen de los reportes anuales y trimestrales
regulatorios.

## Datos de mercado

Parámetros a la fecha de valoración (2026-08-07). Cada dato con su fuente
primaria y la ruta para reconstruirlo.

| Parámetro | Valor | Fuente | Ubicación exacta | Fecha |
|---|---|---|---|---|
| Treasury EE.UU. 10 años | 4.65% | U.S. Department of the Treasury | Daily Treasury Par Yield Curve Rates, columna 10 Yr | 2026-08-07 |
| Bono M 10 años (YTM) | 9.12% | Banco de México | Últimas emisiones subastadas de Bonos con Cupones Fijos. Bono venc. 21/02/36. YTM calculado desde precio sucio 96.308857, cupón 8.00%, 3486 días | 2026-08-06 |
| Bono M 10 años (verificación) | 9.129% | Cbonds | Mexico 10Y YTM | 2026-08-07 |
| Inflación esperada USD (10 años) | 2.25% | FRED | Serie T10YIE, 10-Year Breakeven Inflation Rate | 2026-08-07 |
| Inflación esperada MXN (5-8 años) | 3.75% | Banco de México | Encuesta de Expectativas jul-2026, Cuadro 5, p. 6. Mediana, horizonte 2031-2034 | 2026-08-03 |
| ERP implícita S&P 500 | 4.28% | Damodaran | Implied ERP, trailing 12m con reparto ajustado | 2026-08-01 |
| Spread de default EE.UU. (Aa1) | 0.22% | Damodaran | Implied ERP, nota al pie | 2026-08-01 |
| Calificación soberana México | Baa2 (Moody's) | Damodaran, ctryprem | Hoja principal, fila México | 2026-01-01 |
| Spread default México (rating) | 1.62% | Damodaran, ctryprem | Columna Rating-based Default Spread | 2026-01-01 |
| Spread default México (CDS) | 1.52% | Damodaran, ctryprem | Columna Sovereign CDS, net of Swiss CDS | 2026-01-01 |
| Prima de riesgo país México (CDS) | 2.32% | Damodaran, ctryprem | Columna Country Risk Premium, vía CDS | 2026-01-01 |
| ERP total México (CDS) | 6.55% | Damodaran, ctryprem | Columna Total Equity Risk Premium, vía CDS | 2026-01-01 |
| ERP de mercado maduro | 4.23% | Damodaran, ctryprem | Encabezado del archivo | 2026-01-01 |
| Multiplicador volatilidad relativa | 1.52 | Damodaran, ctryprem | Encabezado, hoja "Relative Equity Volatility" | 2026-01-01 |

## Betas sectoriales de referencia

| Sector | Muestra | β desapalancado | Correlación | Archivo |
|---|---|---|---|---|
| Trucking | EE.UU. | 0.87 | 36.24% | damodaran_betas_sector_us_ene2026.xls |
| Trucking | Global | 0.68 | 19.56% | damodaran_betas_sector_global_ene2026.xls |
| Trucking | Emergentes | 0.37 | 12.36% | damodaran_betas_sector_emergentes_ene2026.xls |
| Transportation | EE.UU. | 0.71 | 32.27% | damodaran_betas_sector_us_ene2026.xls |
| Transportation | Global | 0.75 | 16.94% | damodaran_betas_sector_global_ene2026.xls |
| Auto & Truck | Global | 1.15 | 20.49% | damodaran_betas_sector_global_ene2026.xls |

## Verificación de comparables

Fuentes consultadas para verificar el desglose por segmento, la liquidez y
la historia de precios de cada candidata.

| Uso | Fuente | Ruta |
|---|---|---|
| Desglose por segmento, empresas de EE.UU. | SEC EDGAR | sec.gov, 10-K más reciente |
| Desglose por segmento, resto | Sitio de relaciones con inversionistas | Annual Report |
| Liquidez, volumen, historia de precios | Yahoo Finance | Pestañas Summary e Historical Data, listado principal |
| Liquidez cuando no está en Yahoo | Investing.com | Ficha del instrumento |


## Enlaces

- US Treasury: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
- Banxico, Bonos M: https://www.banxico.org.mx Sistema de Información Económica : Mercado de Valores : Últimas emisiones subastadas de Bonos con Cupones Fijos
- Banxico, encuesta: https://www.banxico.org.mx/publicaciones-y-prensa/encuestas-sobre-las-expectativas-de-los-especialis/
- Cbonds: https://cbonds.com/indexes/24265/
- FRED: https://fred.stlouisfed.org/series/T10YIE
- Damodaran: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html
- SEC EDGAR: https://www.sec.gov/edgar/searchedgar/companysearch

## Archivos de Damodaran

| Archivo | Contenido | Fecha de corte |
|---|---|---|
| damodaran_ctryprem_ene2026.xls | Country Default Spreads and Risk Premiums | 2026-01-01 |
| damodaran_betas_sector_us_ene2026.xls | Betas by Sector, EE.UU. | 2026-01-01 |
| damodaran_betas_sector_global_ene2026.xls | Betas by Sector, global | 2026-01-01 |
| damodaran_betas_sector_emergentes_ene2026.xls | Betas by Sector, mercados emergentes | 2026-01-01 |
| damodaran_industry_company_listing_ene2026.xls | Industry Name and Global Company Listing | 2026-01-01 |

La página `datacurrent.html` se sobrescribe en cada actualización (una o dos veces al año). Por eso los archivos se conservan en `data/raw/` con la fecha de corte en el nombre. La ERP implícita, en cambio, se actualiza mensualmente en la misma página.

Las capturas de las tablas consultadas están en `docs/img/`.

## Datos derivados

| Archivo | Contenido |
|---|---|
| data/interim/traxion_anual.csv | Serie 2021-2025 más UDM a jun-2026, transcrita de los reportes |
| data/interim/universo_comparables.csv | 153 empresas de Trucking y Transportation del listado de Damodaran, sin OTC, mercados desarrollados más LatAm |
| data/interim/comparables.csv | 91 empresas evaluadas: 20 incluidas (11 carga, 8 logística, 1 personas) y 71 descartadas con razón documentada |

## Mapa de páginas

### Reportes anuales

| Reporte | Balance | Resultados | Flujos |
|---|---|---|---|
| 2021 | 90-92 | 92-93 | 112-113 |
| 2022 | 93-94 | 95-96 | 114-115 |
| 2023 | 105-106 | 106-107 | 123-124 |
| 2024 | 99-101 | 101-102 | 118-119 |
| 2025 | 105-107 | 107-108 | 123-124 |

Notas a los estados financieros del reporte 2025: pp. 261-325.

### Reportes trimestrales

Misma estructura en 1T26 y 2T26.

| Sección | Página |
|---|---|
| Mensaje del presidente ejecutivo | 3 |
| Indicadores financieros y operativos | 4 |
| Análisis por segmento | 5-6 |
| Costos totales y resultado integral de financiamiento | 7 |
| CapEx y perfil de la deuda | 8 |
| Balance general | 13 |
| Estado de resultados | 14 |
| Estado de flujos de efectivo | 15 |

### BANXICO_encuesta_expectativas_jul2026.pdf

| Sección | Página |
|---|---|
| Cuadro 1, resumen de expectativas | 1 |
| Cuadro 2, expectativas de inflación anual | 2 |
| Cuadro 5, expectativas de largo plazo (dato utilizado) | 6 |
| Gráficas 4 y 5, expectativas de largo plazo | 7 |
| Cuadro 10, expectativas Bono M a 10 años | 12 |
| Anexo, estadísticas básicas de inflación de largo plazo | 24 |