package rpgmanager.estructura;

import java.util.ArrayList;
import rpgmanager.interfaces.Equipable;
import rpgmanager.interfaces.Habilidoso;
import rpgmanager.interfaces.Sanador;

public class BatallaCompleta {

    public static void iniciar() {

        ArrayList<Personaje> heroes = new ArrayList<>();

        Personaje thorin = new Guerrero("Thorin", 3);
        Personaje gandalf = new Mago("Gandalf", 5);
        Personaje legolas = new Arquero("Legolas", 4);

        heroes.add(thorin);
        heroes.add(gandalf);
        heroes.add(legolas);

        Personaje orco = new Guerrero("Orco", 1);

        System.out.println("=== FASE 1: EQUIPAR ===");

        if (thorin instanceof Equipable) {
            ((Equipable) thorin).equiparItem("Espada Legendaria");
        }

        if (legolas instanceof Equipable) {
            ((Equipable) legolas).equiparItem("Arco Elfico");
        }

        System.out.println("\n=== FASE 2: BATALLA ===");

        int turno = 1;

        while (orco.estaVivo()) {
            System.out.println("\n--- Turno " + turno + " ---");

            for (Personaje h : heroes) {

                if (!orco.estaVivo()) {
                    break;
                }

                if (turno == 2 && h instanceof Habilidoso) {
                    ((Habilidoso) h).usarHabilidadEspecial(orco);
                }

                if (orco.estaVivo()) {
                    h.atacar(orco);
                }
            }

            turno++;
        }

        System.out.println("\nLa batalla terminó en " + (turno - 1) + " turno(s).");

        System.out.println("\n=== FASE 3: SANACION POST BATALLA ===");

        Personaje heroeMenosVida = buscarHeroeMenosVida(heroes);

        for (Personaje h : heroes) {
            if (h instanceof Sanador) {
                ((Sanador) h).sanar(heroeMenosVida);
            }
        }

        System.out.println("\n=== ESTADO FINAL ===");

        for (Personaje h : heroes) {
            System.out.println(h);
        }

        System.out.println(orco);
    }

    public static Personaje buscarHeroeMenosVida(ArrayList<Personaje> heroes) {
        Personaje menor = heroes.get(0);

        for (Personaje h : heroes) {
            if (h.getPuntosVida() < menor.getPuntosVida()) {
                menor = h;
            }
        }

        return menor;
    }
}