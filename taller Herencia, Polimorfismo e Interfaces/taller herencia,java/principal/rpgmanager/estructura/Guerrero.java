package rpgmanager.estructura;

import rpgmanager.interfaces.Habilidoso;
import rpgmanager.interfaces.Equipable;

public class Guerrero extends Personaje implements Habilidoso, Equipable {

    private int fuerza;
    private int defensa;
    private String itemEquipado;
    private int costoHabilidad;

    public Guerrero(String nombre, int nivel) {
        super(nombre, nivel, 100 + nivel * 10);
        this.fuerza = 15 + nivel * 3;
        this.defensa = 10 + nivel * 2;
        this.itemEquipado = "Sin equipo";
        this.costoHabilidad = 30;
    }

    @Override
    public void atacar(Personaje objetivo) {
        System.out.println(nombre + " golpea con su espada causando " + fuerza + " de daño.");
        objetivo.recibirDano(fuerza);
    }

    @Override
    public String getTipoPersonaje() {
        return "Guerrero";
    }

    public void usarEscudo() {
        System.out.println(nombre + " bloquea con su escudo. Defensa: " + defensa);
    }

    @Override
    public void usarHabilidadEspecial(Personaje objetivo) {
        System.out.println(nombre + " usa Golpe Devastador causando 50 de daño.");
        objetivo.recibirDano(50);
    }

    @Override
    public int getCostoHabilidad() {
        return costoHabilidad;
    }

    @Override
    public String getNombreHabilidad() {
        return "Golpe Devastador";
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