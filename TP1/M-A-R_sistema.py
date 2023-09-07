import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definición de la EDO para el sistema masa-resorte-amortiguador
def sistema(x, t, m, b, k, F, t_inicial, t_final):
    v, u = x
    dVdt = u
    # Aplicar la fuerza externa solo durante el período especificado
    if t_inicial <= t <= t_final:
        F_ext = F
    else:
        F_ext = 0.0
    dUdt = (-b/m) * u - (k/m) * v + (1/m) * F_ext
    return [dVdt, dUdt]

# Parámetros del sistema
m = 50.0 # Masa [Kg]
b = 30.0 # Coeficiente de amortiguación [N*s/cm]
k =25.0  # Constante del resorte [N/cm]

# Condiciones iniciales
x0 = [0.0, 0.0]  # Posición inicial y velocidad inicial (x,dx/dt)

# Fuerza externa [N]
F = 1000.0

# Tiempo de simulación [s]
t = np.linspace(0, 50, 10000) 

# Resolución de la EDO
t_inicial = 0
t_final = 15
x = odeint(sistema, x0, t, args=(m, b, k, F, t_inicial, t_final))

# Gráfica de la respuesta del sistema
plt.figure(figsize=(8, 6))
plt.plot(t, x[:, 0], label='Posición')
plt.plot(t, x[:, 1], label='Velocidad')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Respuesta del Sistema Masa-Resorte-Amortiguador')
plt.legend()
plt.grid()
plt.show()
