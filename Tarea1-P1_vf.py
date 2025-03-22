
import matplotlib.pyplot as plt
import numpy as np

def calcular_factor_capitalizacion(tasa_anual, tipo_interes, periodo=1):
    tiempos = np.linspace(0, 10, 100)

    if tipo_interes == 'simple':
        future_value = 1 + tasa_anual * tiempos

    elif tipo_interes == 'compuesto':
        future_value = (1 + tasa_anual / periodo) ** (periodo * tiempos)

    elif tipo_interes == 'continuo':
        # Fórmula para el interés compuesto continuo: e^(tasa_anual * tiempo)
        future_value = np.exp(tasa_anual * tiempos)

    else:
        raise ValueError("Tipo de interés inválido. Debe ser 'simple', 'compuesto' o 'continuo'.")

    return tiempos, future_value

def graficar_capitalizacion(tasa_anual, tipo_interes, periodo=1):

    try:
        tiempos, future_value = calcular_factor_capitalizacion(tasa_anual, tipo_interes, periodo)

        # Labels
        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, future_value)
        plt.xlabel('Tiempo (años)')       
        plt.ylabel('Factor de Capitalización')

        # Titulo:
        if tipo_interes == "compuesto":
          titulo = f'Factor de Capitalización ({tipo_interes.capitalize()} {periodo} veces al año) - Tasa: {tasa_anual*100:.2f}%'
        else:
          titulo = f'Factor de Capitalización ({tipo_interes.capitalize()}) - Tasa: {tasa_anual*100:.2f}%'

        plt.title(titulo)
        plt.grid(True)                
        plt.show()                    


    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"Ocurrió un error inesperado: {ex}")


# Entrada
while True:  # Bucle para permitir multiples pruebas sin reiniciar el script
  try:
    tasa = float(input("Ingrese la tasa de interés anual (ej. 0.05 para 5%): "))
    if not (0 <= tasa <= 1):
        print("La tasa debe estar entre 0 y 1 (o 0% y 100%).")
        continue #Vuelve al inicio del bucle while

    tipo = input("Ingrese el tipo de interés (simple, compuesto, continuo): ").lower()
    if tipo not in ["simple", "compuesto", "continuo"]:
        print("Tipo de interés inválido.  Debe ser 'simple', 'compuesto' o 'continuo'.")
        continue

    periodo = 1  # Valor por defecto.
    if tipo == 'compuesto':
        while True: # Bucle para obtener un periodo valido
            try:
                periodo = int(input("Ingrese el número de periodos de capitalización por año (ej. 1 para anual, 4 para trimestral, 12 para mensual): "))
                if periodo <= 0:
                  print("El periodo debe ser un entero positivo")
                  continue
                break # Sale del bucle while de periodo si todo es correcto
            except ValueError:
              print("Por favor ingrese un número entero.")


    graficar_capitalizacion(tasa, tipo, periodo)
    break

  except ValueError:
    print("Por favor, ingrese un número válido para la tasa.")
  except Exception as e:
    print(f"Ocurrió un error: {e}")
