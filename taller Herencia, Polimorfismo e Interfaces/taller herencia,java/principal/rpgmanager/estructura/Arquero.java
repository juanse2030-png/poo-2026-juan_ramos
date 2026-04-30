package rpgmanager.estructura;

import rpgmanager.interfaces.Equipable;

public class Arquero extends Personaje implements Equipable {

    private int flechas;
    private int alcance;
    private String itemEquipado;

    public Arquero(String nombre, int nivel) {
        super(nombre, nivel, 75 + nivel * 7);
        this.flechas = 10 + nivel * 2;
        this.alcance = 30;
        this.itemEquipado = "Arco basico";
    }

    @Override
    public void atacar(Personaje objetivo) {
        if (flechas > 0) {
            int dano = 12 + nivel * 4;

            if (!itemEquipado.equals("Arco basico")) {
                dano += 5;
            }

            flechas--;

            System.out.println(nombre + " dispara una flecha con " + itemEquipado + " causando " + dano + " de daño.");
            objetivo.recibirDano(dano);
        } else {
            System.out.println(nombre + " no tiene flechas.");
        }
    }

    @Override
    public String getTipoPersonaje() {
        return "Arquero";
    }

    public void recargarFlechas(int cantidad) {
        flechas += cantidad;
        System.out.println(nombre + " recarga flechas. Flechas actuales: " + flechas);
    }

    @Override
    public void equiparItem(String item) {
        itemEquipado = item;
        System.out.println(nombre + " equipó " + itemEquipado);
    }

    @Override
    public String getItemEquipado() {
        return itemEquipado;
    }
}