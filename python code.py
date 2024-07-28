import numpy as np
import matplotlib.pyplot as plt

# Constantes
c = 299792458  # Velocidad de la luz en metros por segundo

# Generar velocidades desde 0.00001c hasta 0.99999c
fracciones_v = np.linspace(0.00001, 0.99999, 1000)
velocidades = fracciones_v * c

# Cálculos de dilatación temporal y contracción de longitud
gamma = 1 / np.sqrt(1 - fracciones_v**2)  # Factor de Lorentz
dilatacion_temporal = gamma
contraccion_longitud = 1 / gamma

# Graficar los resultados
plt.figure(figsize=(14, 6))

# Gráfico de dilatación temporal
plt.subplot(1, 2, 1)
plt.plot(fracciones_v, dilatacion_temporal, label='Dilatación Temporal')
plt.xlabel('Velocidad (fracción de c)')
plt.ylabel('Factor de Dilatación Temporal (γ)')
plt.title('Dilatación Temporal vs Velocidad')
plt.legend()
plt.grid(True)

# Gráfico de contracción de longitud
plt.subplot(1, 2, 2)
plt.plot(fracciones_v, contraccion_longitud, label='Contracción de Longitud', color='r')
plt.xlabel('Velocidad (fracción de c)')
plt.ylabel('Factor de Contracción de Longitud (1/γ)')
plt.title('Contracción de Longitud vs Velocidad')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
