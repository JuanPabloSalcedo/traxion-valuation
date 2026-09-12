"""
Costo de capital: rating sintetico, costo de deuda, reapalancamiento del beta
y cronograma de estructura de capital.

"""


#rating sintetico

TABLA_PEQUENIAS = [
    (-100000,     0.499999, "D2/D",     0.1900),
    (0.5,         0.799999, "C2/C",     0.1600),
    (0.8,         1.249999, "Ca2/CC",   0.1261),
    (1.25,        1.499999, "Caa/CCC",  0.0885),
    (1.5,         1.999999, "B3/B-",    0.0509),
    (2.0,         2.499999, "B2/B",     0.0321),
    (2.5,         2.999999, "B1/B+",    0.0275),
    (3.0,         3.499999, "Ba2/BB",   0.0184),
    (3.5,         3.999999, "Ba1/BB+",  0.0138),
    (4.0,         4.499999, "Baa2/BBB", 0.0111),
    (4.5,         5.999999, "A3/A-",    0.0089),
    (6.0,         7.499999, "A2/A",     0.0078),
    (7.5,         9.499999, "A1/A+",    0.0070),
    (9.5,        12.499999, "Aa2/AA",   0.0055),
    (12.5,   100000,        "Aaa/AAA",  0.0040),
]


def rating_sintetico(cobertura, tabla=TABLA_PEQUENIAS):
    """Traduce un indice de cobertura de intereses a rating y spread de default"""
    for minimo, maximo, rating, spread in tabla:
        if minimo <= cobertura <= maximo:
            return rating, spread
    raise ValueError(f"Cobertura fuera de rango: {cobertura}")


# conversion de monedas

def convertir_tasa(tasa, inflacion_destino, inflacion_origen):
    """Convierte una tasa entre monedas con paridad de Fisher"""
    return (1 + tasa) * (1 + inflacion_destino) / (1 + inflacion_origen) - 1


# apalancamiento del beta

def reapalancar_beta(beta_desapalancado, deuda_sobre_patrimonio, tasa_impuestos):
    """Aplica la estructura de capital al beta del negocio"""
    return beta_desapalancado * (1 + (1 - tasa_impuestos) * deuda_sobre_patrimonio)


#costo de capital

def costo_patrimonio(rf, beta, prima_riesgo):
    """Costo del patrimonio segun el CAPM"""
    return rf + beta * prima_riesgo


def wacc(ke, kd_despues_impuestos, peso_deuda):
    """Costo promedio ponderado de capital"""
    return ke * (1 - peso_deuda) + kd_despues_impuestos * peso_deuda