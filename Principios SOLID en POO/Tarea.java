public class Tarea {
    private String nombre;
    private String responsable;
    private EstadoTarea estado;

    public Tarea(String nombre, String responsable) {
        this.nombre = nombre;
        this.responsable = responsable;
        this.estado = EstadoTarea.PENDIENTE;
    }

    public String getNombre() {
        return nombre;
    }

    public String getResponsable() {
        return responsable;
    }

    public EstadoTarea getEstado() {
        return estado;
    }

    public void setEstado(EstadoTarea estado) {
        this.estado = estado;
    }

    public void mostrarInfo() {
        System.out.println("Tarea: " + nombre);
        System.out.println("Responsable: " + responsable);
        System.out.println("Estado: " + estado);
    }
}
