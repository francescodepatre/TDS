import numpy as np
import matplotlib.pyplot as plt

# Definisci la funzione complessa
def complex_function(x):
    return 1 / (1 + 1j*x)

# Crea un array di valori x
x_values = np.linspace(-10, 10, 400)

# Calcola i valori della funzione complessa
y_values = complex_function(x_values)

# Visualizza la parte reale e immaginaria separatamente
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, np.real(y_values))
plt.title('Parte Reale')

plt.subplot(1, 2, 2)
plt.plot(x_values, np.imag(y_values))
plt.title('Parte Immaginaria')

plt.show()
