package rpgmanager.interfaces;

import rpgmanager.estructura.Personaje;

public interface Habilidoso {
    void usarHabilidadEspecial(Personaje objetivo);
    int getCostoHabilidad();
    String getNombreHabilidad();
}