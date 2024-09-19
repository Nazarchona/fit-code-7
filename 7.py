import numpy as np
import matplotlib.pyplot as plt

# Табличні значення
x_vals = np.array([1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390])
y_vals = np.array([4.2556, 4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706])

# Функція для обчислення кінцевих різниць
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    
    return coef[0, :]  # Повертає лише перший рядок коефіцієнтів

# Функція для обчислення багаточлена Ньютона
def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Обчислення коефіцієнтів для багаточлена Ньютона
coefficients = divided_diff(x_vals, y_vals)

# Побудова інтерполяційного багаточлена для різних значень x
x_new = np.linspace(min(x_vals), max(x_vals), 100)
y_new = [newton_poly(coefficients, x_vals, xi) for xi in x_new]

# Графік
plt.plot(x_vals, y_vals, 'bo', label="Табличні значення")
plt.plot(x_new, y_new, 'r-', label="Інтерполяційний багаточлен Ньютона")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Інтерполяція багаточленом Ньютона")
plt.grid(True)
plt.show()
