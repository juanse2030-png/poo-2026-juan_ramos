package rpgmanager.interfaces;

import rpgmanager.estructura.Personaje;

public interface Sanador {
    void sanar(Personaje objetivo);
    int getPotenciaSanacion();
}