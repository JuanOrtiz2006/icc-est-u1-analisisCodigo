import matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

nombre_linea = "Línea de ejemplo"
plt.plot(x, y, label=nombre_linea, color="blue")
plt.title("Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()

