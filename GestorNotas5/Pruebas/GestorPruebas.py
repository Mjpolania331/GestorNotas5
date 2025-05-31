import pytest
import sys
from importlib import import_module

def ejecutar_con_pytest():
    """
    Ejecuta los archivos de prueba utilizando pytest.

    Archivos ejecutados:
    ---------------------
    - Pruebas_Casos_Normales.py
    - Pruebas_Casos_Extremos.py
    - Pruebas_Error.py

    Muestra en consola la salida detallada (-v) y
    el código de salida de pytest al finalizar.
    """
    print("\n" + "=" * 60)
    print(" EJECUTANDO CON PYTEST ".center(60, "="))
    print("=" * 60)

    exit_code = pytest.main([
        "Pruebas_Casos_Normales.py",
        "Pruebas_Casos_Extremos.py",
        "Pruebas_Error.py",
        "-v"
    ])

    print("\n" + "=" * 60)
    print(f"Pruebas completadas (código: {exit_code})")

if _name_ == "_main_":
    print("SISTEMA DE EJECUCIÓN DE PRUEBAS".center(60, "="))
    print("\n1. Ejecutar con pytest")
    print("2. Salir")

    while True:
        opcion = input("\nSeleccione opción (1-2): ").strip()

        if opcion == "1":
            ejecutar_con_pytest()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")