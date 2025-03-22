import datetime

def tasa_dolares_implicita(fecha_actual, fecha_madurez, puntos_forward, precio_spot, tasa_pesos):

    plazo_dias = (fecha_madurez - fecha_actual).days
    plazo_anios = plazo_dias / 365.0

    precio_forward = precio_spot + puntos_forward

    factor_capitalizacion_pesos = (1 + tasa_pesos) ** plazo_anios

    factor_capitalizacion_dolares = (precio_spot / precio_forward) * factor_capitalizacion_pesos


    tasa_dolares = (factor_capitalizacion_dolares ** (1 / plazo_anios)) - 1

    return tasa_dolares


def obtener_datos_usuario():
    while True:
        try:
            fecha_actual_str = input("Ingrese la fecha actual (YYYY-MM-DD): ")
            fecha_actual = datetime.datetime.strptime(fecha_actual_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Formato de fecha incorrecto. Use YYYY-MM-DD.")

    while True:
        try:
            fecha_madurez_str = input("Ingrese la fecha de madurez (YYYY-MM-DD): ")
            fecha_madurez = datetime.datetime.strptime(fecha_madurez_str, "%Y-%m-%d").date()
            if fecha_madurez <= fecha_actual:
                print("La fecha de madurez debe ser posterior a la fecha actual.")
                continue
            break
        except ValueError:
            print("Formato de fecha incorrecto. Use YYYY-MM-DD.")

    while True:
        try:
            puntos_forward = float(input("Ingrese los puntos forward: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para los puntos forward.")

    while True:
        try:
            precio_spot = float(input("Ingrese el precio spot del dólar: "))
            if precio_spot <= 0:
                print("El precio spot debe ser un valor positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio spot.")

    while True:
        try:
            tasa_pesos = float(input("Ingrese la tasa en pesos (anual compuesta, ej. 0.05 para 5%): "))
            if not 0 <= tasa_pesos <=1:
                print("La tasa en pesos debe estar entre 0 y 1")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la tasa en pesos.")

    return fecha_actual, fecha_madurez, puntos_forward, precio_spot, tasa_pesos


# --- Ejemplo de uso ---
if __name__ == "__main__":
    fecha_actual, fecha_madurez, puntos_forward, precio_spot, tasa_pesos = obtener_datos_usuario()


    tasa_dolar = tasa_dolares_implicita(fecha_actual, fecha_madurez, puntos_forward, precio_spot, tasa_pesos)

    print(f"\nLa tasa en dólares implícita es: {tasa_dolar * 100:.4f}% (anual compuesta)")