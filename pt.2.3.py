import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

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

def mostrar_resultados(tiempo_en_avion_este, diferencia_de_tiempo_este_ns, tiempo_en_avion_oeste, diferencia_de_tiempo_oeste_ns, diferencia_total_ns):
    result_text = (f"Tiempo en el avión que va hacia el este: {tiempo_en_avion_este:.6f} segundos\n"
                   f"Diferencia de tiempo para el avión que va hacia el este: {diferencia_de_tiempo_este_ns:.6f} nanosegundos\n"
                   f"Tiempo en el avión que va hacia el oeste: {tiempo_en_avion_oeste:.6f} segundos\n"
                   f"Diferencia de tiempo para el avión que va hacia el oeste: {diferencia_de_tiempo_oeste_ns:.6f} nanosegundos\n"
                   f"Diferencia total entre los dos aviones: {diferencia_total_ns:.6f} nanosegundos")
    messagebox.showinfo("Resultados", result_text)

def calcular():
    try:
        velocidad_este = float(entry_velocidad_este.get())
        velocidad_oeste = float(entry_velocidad_oeste.get())
        duracion = float(entry_duracion.get())

        tiempo_en_avion_este, diferencia_de_tiempo_este = dilatacion_del_tiempo(velocidad_este, duracion)
        tiempo_en_avion_oeste, diferencia_de_tiempo_oeste = dilatacion_del_tiempo(velocidad_oeste, duracion)

        # Convertir las diferencias de tiempo a nanosegundos
        diferencia_de_tiempo_este_ns = diferencia_de_tiempo_este * 1e9
        diferencia_de_tiempo_oeste_ns = diferencia_de_tiempo_oeste * 1e9

        # Calcular la diferencia entre los dos tiempos
        diferencia_total_ns = abs(diferencia_de_tiempo_este_ns - diferencia_de_tiempo_oeste_ns)

        mostrar_resultados(tiempo_en_avion_este, diferencia_de_tiempo_este_ns, tiempo_en_avion_oeste, diferencia_de_tiempo_oeste_ns, diferencia_total_ns)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Dilatación del Tiempo")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_velocidad_este = tk.Label(frame, text="Velocidad del avión que va hacia el este (km/h):")
label_velocidad_este.grid(row=0, column=0, sticky="e")
entry_velocidad_este = tk.Entry(frame)
entry_velocidad_este.grid(row=0, column=1)

label_velocidad_oeste = tk.Label(frame, text="Velocidad del avión que va hacia el oeste (km/h):")
label_velocidad_oeste.grid(row=1, column=0, sticky="e")
entry_velocidad_oeste = tk.Entry(frame)
entry_velocidad_oeste.grid(row=1, column=1)

label_duracion = tk.Label(frame, text="Duración del vuelo (horas):")
label_duracion.grid(row=2, column=0, sticky="e")
entry_duracion = tk.Entry(frame)
entry_duracion.grid(row=2, column=1)

btn_calcular = tk.Button(frame, text="Calcular", command=calcular)
btn_calcular.grid(row=3, columnspan=2, pady=10)

root.mainloop()
