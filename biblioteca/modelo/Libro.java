package modelo;

public class Libro implements Prestable {

    private String titulo;
    private String autor;
    private boolean disponible;

    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
        this.disponible = true;
    }

    public boolean isDisponible() {
        return disponible;
    }

    @Override
    public void prestar() {
        disponible = false;
    }

    @Override
    public void devolver() {
        disponible = true;
    }

    public void mostrarLibro() {
        System.out.println("Título: " + titulo +
                " | Autor: " + autor +
                " | Disponible: " + disponible);
    }
}
