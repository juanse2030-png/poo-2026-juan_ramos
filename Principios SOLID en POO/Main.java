public class Main {
    public static void main(String[] args) {
        Tarea t1 = new Tarea("Guardar partida", "Carlos");
        Tarea t2 = new Tarea("Revisar inventario", "Laura");

        t1.setEstado(EstadoTarea.EN_PROGRESO);
        t2.setEstado(EstadoTarea.EN_REVISION);

        t1.mostrarInfo();
        System.out.println("------------------");
        t2.mostrarInfo();
    }
}
