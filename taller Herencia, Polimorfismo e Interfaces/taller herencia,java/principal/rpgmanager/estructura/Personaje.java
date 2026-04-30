package rpgmanager.estructura;

public abstract class Personaje {

    protected String nombre;
    protected int nivel;
    protected int puntosVida;
    protected int puntosVidaMax;

    public Personaje(String nombre, int nivel, int puntosVidaMax) {
        this.nombre = nombre;
        this.nivel = nivel;
        this.puntosVidaMax = puntosVidaMax;
        this.puntosVida = puntosVidaMax;
    }

    public void recibirDano(int dano) {
        puntosVida = puntosVida - dano;

        if (puntosVida < 0) {
            puntosVida = 0;
        }

        System.out.println(nombre + " recibe " + dano + " de daño. HP actual: "
                + puntosVida + "/" + puntosVidaMax);
    }

    public boolean estaVivo() {
        return puntosVida > 0;
    }

    public abstract void atacar(Personaje objetivo);

    public abstract String getTipoPersonaje();

    public void restaurarVida(int cantidad) {
    puntosVida += cantidad;

    if (puntosVida > puntosVidaMax) {
        puntosVida = puntosVidaMax;
    }
}

public String getNombre() {
    return nombre;
}
public int getPuntosVida() {
    return puntosVida;
}
    @Override
    public String toString() {
        return "[" + getTipoPersonaje() + "] " + nombre + " Nv." + nivel
                + " | HP: " + puntosVida + "/" + puntosVidaMax;
    }
}
