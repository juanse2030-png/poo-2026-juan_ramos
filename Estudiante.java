import java.util.ArrayList;

public class Estudiante {

    // Atributos privados (encapsulación)
    private String nombre;
    private int edad;
    private String carrera;
    private ArrayList<String> materias;

    // Constructor
    public Estudiante(String nombre, int edad, String carrera) {
        this.nombre = nombre;
        this.edad = edad;
        this.carrera = carrera;
        this.materias = new ArrayList<>();
    }

    // Método para inscribir materia
    public void inscribirMateria(String materia) {
        this.materias.add(materia);
        System.out.println(nombre + " se inscribió en " + materia);
    }

    // Método para presentarse
    public void presentarse() {
        System.out.println("Hola, soy " + nombre);
        System.out.println("Tengo " + edad + " años");
        System.out.println("Estudio " + carrera);
        System.out.println("Materias inscritas: " + materias.size());
    }

    // NUEVO método estudiar
    public void estudiar(int horas) {
        System.out.println(nombre + " estudió " + horas + " horas");
    }

    // Método main para probar
    public static void main(String[] args) {

        // Crear objetos del ejemplo
        Estudiante est1 = new Estudiante("Ana García", 20, "Ing. Sistemas");
        Estudiante est2 = new Estudiante("Carlos López", 22, "Ing. Sistemas");

        // Crear TU estudiante
        Estudiante est3 = new Estudiante(
            "Juan Sebastian Ramos Ovalle",
            17,
            "Sistematización de Datos"
        );

        est3.presentarse();

        System.out.println("---");

        // Inscribir tus 3 materias
        est3.inscribirMateria("Física Newtoniana");
        est3.inscribirMateria("Cálculo Integral");
        est3.inscribirMateria("Estructura de Datos");

        System.out.println("---");

        // Usar el método estudiar
        est3.estudiar(4);
    }
}