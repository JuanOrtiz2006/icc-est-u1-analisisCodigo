from metodos_ordenamiento import MetodosOrdenamiento
from benchmarking import Benchmarking
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona")
    marking=Benchmarking()
    metodos = MetodosOrdenamiento()
    tamanio=[500, 1000, 2000]
    resultados = []
    for tam in tamanio:
        arreglo = marking.build_arreglo(tam)
        metodosOrdenamiento = { "Burbuja": metodos.sortByBuble,
                            "Seleccion": metodos.sort_seleccion
                          }
    
        for nombre, metodo in metodosOrdenamiento.items():
            tiempo = marking.medir_tiempo(metodo,arreglo)
            respuesta = (tam, nombre, tiempo)
            resultados.append(respuesta)

        for posicion in resultados:
            tam, nombre, tiempo = posicion
            print(f"Tamaño: {tam}, Metodo: {nombre}, tiempo: {tiempo:.6f} segundos")

        tiempos_by_metodo = {
            "Burbuja": [],
            "Seleccion": []
        }

        for tam,nombre,tiempo in resultados:
            tiempos_by_metodo[nombre].append(tiempo)
        print(tiempos_by_metodo)
    
    # graficar una linea de timepo para cada metodo
    # x sean los tamanios
    # y sean los tiempos

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanio, tiempos, label=nombre, marker="o")

    plt.grid()
    plt.title("Tiempos de Ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.show()
