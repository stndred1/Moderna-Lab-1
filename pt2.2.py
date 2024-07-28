import numpy as np
import matplotlib.pyplot as plt

# Constantes
c = 299792458  # Velocidad de la luz en metros por segundo

def dilatacion_del_tiempo(velocidad, duracion_horas):
    """
    Calcular el efecto de la dilatación del tiempo para una velocidad y duración de vuelo dadas.
    """
    # Convertir velocidad de km/h a m/s
    velocidad_m_por_s = velocidad * 1000 / 3600
    
    # Calcular gamma (factor de Lorentz)
    gamma = 1 / np.sqrt(1 - (velocidad_m_por_s ** 2 / c ** 2))
    
    # Calcular la diferencia de tiempo
    duracion_segundos = duracion_horas * 3600
    tiempo_en_avion = duracion_segundos / gamma
    diferencia_de_tiempo = duracion_segundos - tiempo_en_avion
    
    return tiempo_en_avion, diferencia_de_tiempo

def main():
    # Entrada del usuario
    velocidad = float(input("Ingrese la velocidad del avión en km/h: "))
    direccion = input("¿El avión vuela de este a oeste? (sí/no): ").strip().lower()
    duracion = float(input("Ingrese la duración del vuelo en horas: "))
    
    tiempo_en_avion, diferencia_de_tiempo = dilatacion_del_tiempo(velocidad, duracion)
    
    # Convertir la diferencia de tiempo a nanosegundos
    diferencia_de_tiempo_ns = diferencia_de_tiempo * 1e9
    
    # Mostrar los resultados
    print(f"Tiempo en el avión: {tiempo_en_avion:.6f} segundos")
    print(f"Diferencia de tiempo: {diferencia_de_tiempo_ns:.6f} nanosegundos")
    
    # Generar datos para el gráfico
    velocidades = np.linspace(0, 3000, 100)  # Rango de velocidad de 0 a 3000 km/h
    diferencias_de_tiempo = []
    
    for v in velocidades:
        _, dt = dilatacion_del_tiempo(v, duracion)
        diferencias_de_tiempo.append(dt * 1e9)  # Convertir a nanosegundos
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(velocidades, diferencias_de_tiempo, label='Diferencia de tiempo (ns)')
    plt.xlabel('Velocidad (km/h)')
    plt.ylabel('Diferencia de tiempo (ns)')
    plt.title('Dilatación del Tiempo vs. Velocidad')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

