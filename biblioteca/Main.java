import modelo.Libro;
import modelo.Usuario;
import servicio.PrestamoService;

public class Main {
    public static void main(String[] args) {

        Usuario u = new Usuario("Juan");
        Libro l = new Libro("El Quijote", "Cervantes");

        PrestamoService ps = new PrestamoService();

        ps.prestarLibro(u, l);
        l.mostrarLibro();
    }
}
