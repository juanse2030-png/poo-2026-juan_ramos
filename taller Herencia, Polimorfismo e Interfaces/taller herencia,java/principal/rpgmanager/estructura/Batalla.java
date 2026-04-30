package rpgmanager.estructura;

import java.util.ArrayList;

public class Batalla {

    public static void iniciar() {

        ArrayList<Personaje> heroes = new ArrayList<>();

        heroes.add(new Guerrero("Thorin", 3));
        heroes.add(new Mago("Gandalf", 5));
        heroes.add(new Arquero("Legolas", 4));

        Personaje orco = new Guerrero("Orco", 1);

        int turno = 1;

        while (orco.estaVivo()) {
            System.out.println("\n--- Turno " + turno + " ---");

            for (Personaje h : heroes) {
                if (orco.estaVivo()) {
                    h.atacar(orco);
                }
            }

            turno++;
        }

        System.out.println("\nLa batalla terminó en " + (turno - 1) + " turno(s).");

        System.out.println("\nEstado final de los heroes:");
        for (Personaje h : heroes) {
            System.out.println(h);
        }

        System.out.println("\nEstado final del enemigo:");
        System.out.println(orco);
    }
}