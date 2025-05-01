class MetodosOrdenamiento:

    def sortByBuble(self, array):
        array = array.copy()
        n = len(array)
        for i in range(n):
            for j in range(i+1, n):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array
    
    def sort_seleccion(self,array):
        array = array.copy()
        n = len(array)
        for i in range(n):
            posicion=1
            for j in range(i+1,n):
                if array[j] < array[posicion]:
                    posicion = j
            array[i], array[posicion] = array[posicion], array[i]
        return array