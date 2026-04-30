package rpgmanager.estructura;

import rpgmanager.interfaces.Habilidoso;
import rpgmanager.interfaces.Sanador;

public class Mago extends Personaje implements Habilidoso, Sanador {

    private int mana;
    private int manaMax;

    public Mago(String nombre, int nivel) {
        super(nombre, nivel, 60 + nivel * 5);
        this.manaMax = 80 + nivel * 10;
        this.mana = manaMax;
    }

    @Override
    public void atacar(Personaje objetivo) {
        if (mana >= 20) {
            int dano = 25 + nivel * 5;
            mana -= 20;

            System.out.println(nombre + " lanza un hechizo causando " + dano + " de daño.");
            objetivo.recibirDano(dano);
        } else {
            System.out.println(nombre + " no tiene mana suficiente.");
        }
    }

    @Override
    public String getTipoPersonaje() {
        return "Mago";
    }

    public void recuperarMana(int cantidad) {
        mana += cantidad;

        if (mana > manaMax) {
            mana = manaMax;
        }

        System.out.println(nombre + " recupera mana. Mana actual: " + mana + "/" + manaMax);
    }

    @Override
    public void usarHabilidadEspecial(Personaje objetivo) {
        if (mana >= 20) {
            mana -= 20;
            System.out.println(nombre + " lanza Bola de Fuego causando 40 de daño.");
            objetivo.recibirDano(40);
        } else {
            System.out.println(nombre + " no tiene mana suficiente para Bola de Fuego.");
        }
    }

    @Override
    public int getCostoHabilidad() {
        return 20;
    }

    @Override
    public String getNombreHabilidad() {
        return "Bola de Fuego";
    }

    @Override
    public void sanar(Personaje objetivo) {
        objetivo.restaurarVida(25);
        System.out.println(nombre + " sana a " + objetivo.getNombre() + " con 25 puntos de vida.");
    }

    @Override
    public int getPotenciaSanacion() {
        return 25;
    }
}