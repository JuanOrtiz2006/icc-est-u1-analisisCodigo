from metodos_ordenamiento import MetodosOrdenamiento
from benchmarking import Benchmarking
if __name__ == "__main__":
    print("Funciona")
    marking=Benchmarking()
    metodos = MetodosOrdenamiento()
    tam=10
    arreglo = marking.build_arreglo(tam)
    metodosOrdenamiento = { "Burbuja": metodos.sortByBuble,
                            "Seleccion": metodos.sort_seleccion
                          }
    
    resultados = []
    for nombre, metodo in metodosOrdenamiento.items():
        tiempo = marking.medir_tiempo(metodo,arreglo)
        respuesta = (tam, nombre, tiempo)
        resultados.append(respuesta)

    for posicion in resultados:
        tam, nombre, tiempo = posicion
        print(f"Tamaño: {tam}, Metodo: {nombre}, tiempo: {tiempo:.6f} segundos")

