package servicio;

import modelo.Libro;
import modelo.Usuario;

public class PrestamoService {

    private static final int MAX_LIBROS = 3;

    public void prestarLibro(Usuario usuario, Libro libro) {

        if (usuario.getLibrosPrestados() >= MAX_LIBROS) {
            System.out.println("Máximo de libros alcanzado");
            return;
        }

        if (!libro.isDisponible()) {
            System.out.println("Libro no disponible");
            return;
        }

        libro.prestar();
        usuario.aumentarPrestamos();

        System.out.println("Préstamo exitoso");
    }

    public void devolverLibro(Usuario usuario, Libro libro) {
        libro.devolver();
        usuario.disminuirPrestamos();
        System.out.println("Libro devuelto");
    }
}
