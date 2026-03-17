package modelo;

public class Usuario {

    private String nombre;
    private int librosPrestados;

    public Usuario(String nombre) {
        this.nombre = nombre;
        this.librosPrestados = 0;
    }

    public int getLibrosPrestados() {
        return librosPrestados;
    }

    public void aumentarPrestamos() {
        librosPrestados++;
    }

    public void disminuirPrestamos() {
        librosPrestados--;
    }
}
