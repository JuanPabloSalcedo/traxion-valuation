"""
Lee el CSV de datos anuales transcritos de los reportes de Traxion y deriva
las cantidades que se calculan directamente de esa serie
"""

import pandas as pd


#carga

COLUMNAS_REQUERIDAS = [
    "anio",
    "ingresos_totales",
    "ebit",
    "ebit_normalizado",
    "dep_amort",
    "gasto_intereses",
    "deuda_total",
]


def cargar_serie(ruta):
    """Lee la serie anual desde un CSV y la devuelve ordenada por anio"""
    df = pd.read_csv(ruta)

    faltantes = [c for c in COLUMNAS_REQUERIDAS if c not in df.columns]
    if faltantes:
        raise ValueError(f"El CSV no tiene estas columnas requeridas: {faltantes}")

    df = df.sort_values("anio").reset_index(drop=True)
    return df


#serie sin adquisiciones "organica"

def serie_organica(df, col_total, col_adquirida, nombre_salida):
    """Resta la contribucion de una adquisicion para aislar el negocio base"""
    aporte = df[col_adquirida].fillna(0)
    df[nombre_salida] = df[col_total] - aporte
    return df


#ratios derivados

def margenes(df, col_ingresos_org=None, col_ebit_org=None):
    """Calcula margen operativo, cobertura de intereses y, si se indican las
    columnas organicas, el margen del negocio base"""
    df["margen_ebit"] = df["ebit_normalizado"] / df["ingresos_totales"]
    df["cobertura_intereses"] = df["ebit_normalizado"] / df["gasto_intereses"]

    if col_ingresos_org and col_ebit_org:
        df["margen_ebit_organico"] = df[col_ebit_org] / df[col_ingresos_org]

    return df

#ultimos doce meses

def construir_udm(anual, semestre_anterior, semestre_actual):
    """Construye una ventana de doce meses: ejercicio anual completo, menos el
    primer semestre de ese año, mas el primer semestre del año siguiente"""
    return anual - semestre_anterior + semestre_actual


def anualizar(monto_parcial, meses_reportados):
    """Lleva a base anual un monto reportado por un periodo menor a 12 meses"""
    return monto_parcial * 12 / meses_reportados


#año base

def construir_ano_base(ingresos_base, margen_ebit):
    """Arma las cifras de partida a partir de un nivel de ingresos y un margen
    operativo supuesto"""
    return {
        "ingresos_base": ingresos_base,
        "margen_ebit_supuesto": margen_ebit,
        "ebit_base": ingresos_base * margen_ebit,
    }


#retorno sobre el capital

def capital_invertido(deuda, patrimonio, efectivo):
    """Capital invertido en la operacion: deuda mas patrimonio menos caja"""
    return deuda + patrimonio - efectivo


def roc(ebit, capital, tasa_impuestos):
    """Retorno sobre el capital invertido, despues de impuestos"""
    return ebit * (1 - tasa_impuestos) / capital
