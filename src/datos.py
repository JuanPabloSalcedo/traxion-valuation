"""
Lee el CSV de datos anuales transcritos de los reportes de Traxion y deriva
las cantidades que se calculan directamente de esa serie
"""

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