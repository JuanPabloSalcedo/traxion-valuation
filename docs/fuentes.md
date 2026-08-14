# Fuentes de datos


Los reportes originales están en `data/raw/`. Esta tabla registra su
procedencia y fecha de consulta.

| Archivo | Documento | URL | Fecha descarga o consulta |
|---|---|---|---|
| traxion_1T26_trimestral.pdf | Reporte trimestral 1T26 | https://traxion.global/es/inversionistas/reportes | 2026-07-22 |
| traxion_2025_anual.pdf | Reporte anual 2025 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_2024_anual.pdf | Reporte anual 2024 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_informe_integrado_2024.pdf | Informe integrado anual 2024 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_2023_anual.pdf | Reporte anual 2023 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_informe_integrado_2023.pdf | Informe integrado anual 2023 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_2022_anual.pdf | Reporte anual 2022 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_informe_integrado_2022.pdf | Informe integrado anual 2022 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_2021_anual.pdf | Reporte anual 2021 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_informe_integrado_2021.pdf | Informe integrado anual 2021 | https://traxion.global/es/inversionistas/reportes | 2026-07-25 |
| traxion_2T26_trimestral.pdf | Reporte trimestral 2T26 | https://traxion.global/es/inversionistas/reportes | 2026-07-28 |
| BANXICO_encuesta_expectativas_jul2026.pdf | Encuesta sobre las Expectativas de los Especialistas en Economía del Sector Privado, julio 2026 | https://www.banxico.org.mx | 2026-08-07 |
| damodaran_ctryprem_ene2026.xlsx | Country Default Spreads and Risk Premiums | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html | 2026-08-07 |

## Mapa de documentos

Dónde está cada sección.

### informes integrados

Los informes integrados se conservan localmente como contexto corporativo pero no se versionan por su peso. Las cifras financieras del modelo provienen de los reportes anuales regulatorios.

### traxion_2021_anual.pdf

| Sección | Página |
|---|---|
| Estado de situación financiera (Balance) | 90-92 |
| Estados de resultados | 92,93 |
| Estados de flujos de efectivo | 112,113 |

### traxion_2022_anual.pdf

| Sección | Página |
|---|---|
| Estado de situación financiera (Balance) | 93,94 |
| Estados de resultados | 95,96 |
| Estados de flujos de efectivo | 114,115 |

### traxion_2023_anual.pdf

| Sección | Página |
|---|---|
| Estado de situación financiera (Balance) | 105,106 |
| Estados de resultados | 106,107 |
| Estados de flujos de efectivo | 123,124 |

### traxion_2024_anual.pdf

| Sección | Página |
|---|---|
| Estado de situación financiera (Balance) | 99-101 |
| Estados de resultados | 101,102 |
| Estados de flujos de efectivo | 118,119 |

### traxion_2025_anual.pdf

| Sección | Página |
|---|---|
| Estado de situación financiera (Balance) | 105-107 |
| Estados de resultados | 107,108 |
| Estados de flujos de efectivo | 123,124 |
| Notas a los estados financieros | 261-325 |

### traxion_1T26_trimestral.pdf

| Sección | Página |
|---|---|
| Indicadores financieros y operativos | 4 |
| Análisis por segmento | 5,6,7 |
| Perfil de la deuda | 8 y 9 |
| Balance general | 13 |
| Estado de resultados | 14 |
| Estado de flujos de efectivo | 15 |

### traxion_2T26_trimestral.pdf

| Sección | Página |
|---|---|
| Mensaje del presidente ejecutivo | 3 |
| Indicadores financieros y operativos | 4 |
| Análisis de resultados y segmento logística | 5 |
| Segmentos carga y personas | 6 |
| Costos totales y resultado integral de financiamiento | 7 |
| CapEx y perfil de la deuda | 8 |
| Balance general | 13 |
| Estado de resultados | 14 |
| Estado de flujos de efectivo | 15 |

## Datos de mercado

Parámetros de mercado a la fecha de valoración (2026-08-07). Cada dato con su fuente primaria y la ruta para reconstruirlo.

| Parámetro | Valor | Fuente | Ubicación exacta | Fecha |
|---|---|---|---|---|
| Treasury EE.UU. 10 años | 4.65% | U.S. Department of the Treasury | Daily Treasury Par Yield Curve Rates, columna 10 Yr | 2026-08-07 |
| Bono M 10 años (YTM) | 9.12% | Banco de México | Últimas emisiones subastadas de Bonos con Cupones Fijos. Bono venc. 21/02/36. YTM calculado desde precio sucio 96.308857, cupón 8.00%, 3486 días | 2026-08-06 |
| Bono M 10 años (verificación) | 9.129% | Cbonds | Mexico 10Y YTM | 2026-08-07 |
| Inflación esperada USD (10 años) | 2.25% | FRED, Federal Reserve Bank of St. Louis | Serie T10YIE, 10-Year Breakeven Inflation Rate | 2026-08-07 |
| Inflación esperada MXN (5-8 años) | 3.75% | Banco de México | Encuesta de Expectativas jul-2026, Cuadro 5, p. 6. Mediana, horizonte 2031-2034 | 2026-08-03 |
| Calificación soberana México | Baa2 (Moody's) | Damodaran, ctryprem | Hoja principal, fila México | 2026-01-01 |
| Spread default México (rating) | 1.62% | Damodaran, ctryprem | Columna Rating-based Default Spread | 2026-01-01 |
| Spread default México (CDS) | 1.52% | Damodaran, ctryprem | Columna Sovereign CDS, net of Swiss CDS | 2026-01-01 |
| Prima de riesgo país México (CDS) | 2.32% | Damodaran, ctryprem | Columna Country Risk Premium, vía CDS | 2026-01-01 |
| ERP total México (CDS) | 6.55% | Damodaran, ctryprem | Columna Total Equity Risk Premium, vía CDS | 2026-01-01 |
| ERP de mercado maduro | 4.23% | Damodaran, ctryprem | Encabezado del archivo | 2026-01-01 |
| Multiplicador volatilidad relativa | 1.52 | Damodaran, ctryprem | Encabezado del archivo, hoja "Relative Equity Volatility" | 2026-01-01 |

**Nota sobre el archivo de Damodaran:** la página `datacurrent.html` se sobrescribe en cada actualización (una o dos veces al año). Por eso el archivo se conserva en `data/raw/` con la fecha de corte en el nombre.


### BANXICO_encuesta_expectativas_jul2026.pdf

| Sección | Página |
|---|---|
| Cuadro 1, resumen de expectativas | 1 |
| Cuadro 2, expectativas de inflación anual | 2 |
| Cuadro 5, expectativas de largo plazo (dato utilizado) | 6 |
| Gráficas 4 y 5, expectativas de largo plazo | 7 |
| Cuadro 10, expectativas Bono M a 10 años | 12 |
| Anexo, estadísticas básicas de inflación de largo plazo | 24 |


## Archivos de Damodaran

| Archivo | Contenido | Fecha de corte |
|---|---|---|
| damodaran_ctryprem_ene2026.xls | Country Default Spreads and Risk Premiums | 2026-01-01 |
| damodaran_betas_sector_us_ene2026.xls | Betas by Sector, EE.UU. | 2026-01-01 |
| damodaran_betas_sector_global_ene2026.xls | Betas by Sector, global | 2026-01-01 |
| damodaran_betas_sector_emergentes_ene2026.xls | Betas by Sector, mercados emergentes | 2026-01-01 |
| damodaran_industry_company_listing_ene2026.xls | Industry Name and Global Company Listing | 2026-01-01 |

## Datos derivados

| Archivo | Contenido |
|---|---|
| data/interim/traxion_anual.csv | Serie 2021-2025 más UDM a jun-2026, transcrita de los reportes |
| data/interim/universo_comparables.csv | 153 empresas de Trucking y Transportation, extraídas del listado de Damodaran |
| data/interim/comparables.csv | Selección final de comparables con segmento asignado y verificación de negocio |