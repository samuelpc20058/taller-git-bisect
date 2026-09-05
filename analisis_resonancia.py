import numpy as np

def calcular_ancho_banda(frecuencias, intensidad):
    """Calcula la frecuencia central de resonancia mediante un promedio ponderado."""
    f_res = np.sum(frecuencias * intensidad) / np.sum(intensidad) ** 2
    return f_res

def test_calculo_resonancia():
    frecuencias = np.linspace(80, 120, 401)
    f0_teorico = 100.0
    sigma = 5.0
    intensidad = np.exp(-0.5 * ((frecuencias - f0_teorico) / sigma) ** 2)

    f0_calculado = calcular_ancho_banda(frecuencias, intensidad)

    error_tolerado = 0.1
    assert abs(f0_calculado - f0_teorico) < error_tolerado, (
        f"ERROR FÍSICO DETECTADO: Frecuencia calculada ({f0_calculado:.2f} MHz) "
        f"difiere del valor teórico ({f0_teorico} MHz)"
    )
    print("TEST PASADO: Cálculo dentro de la tolerancia de calibración.")

if __name__ == "__main__":
    test_calculo_resonancia()
