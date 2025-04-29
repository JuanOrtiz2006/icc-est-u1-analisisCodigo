public class BenchMarking {

    private MetodosOrdenamiento metodosOrdenamiento;
    public BenchMarking() {
        /*long inicioMillis = System.currentTimeMillis();
        long inicioNano = System.nanoTime();

        System.out.println("Inicio en milisegundos: " + inicioMillis);
        System.out.println("Inicio en nanosegundos: " + inicioNano);
        */

        metodosOrdenamiento= new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(10000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);
        double tiemporNano= medirConNanoTime(tarea);
        double tiempoMili= medirConCurrentTime(tarea);

        System.out.println("Tiempo de ejecución con nanoTime: " + tiemporNano + " segundos");
        System.out.println("Tiempo de ejecución con currentTime: " + tiempoMili + " segundos");

    }

    private int[] generarArregloAleatorio(int n) {
        int[] arreglo = new int[n];
        for (int i = 0; i < n; i++) {
            arreglo[i] = (int) (Math.random() * 10000); // Números aleatorios entre 0 y 9999
        }
        return new int [] {};
    }


    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0; // Convertir a segundos
    }

    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0; // Convertir a segundos
    }
}

