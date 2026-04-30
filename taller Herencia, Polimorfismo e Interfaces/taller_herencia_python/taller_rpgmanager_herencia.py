from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre, nivel, vida_max):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_vida_max = vida_max
        self.puntos_vida = vida_max

    def recibir_dano(self, dano):
        self.puntos_vida -= dano
        if self.puntos_vida < 0:
            self.puntos_vida = 0
        print(f"{self.nombre} recibe {dano} de daño. HP actual: {self.puntos_vida}/{self.puntos_vida_max}")

    def esta_vivo(self):
        return self.puntos_vida > 0

    def restaurar_vida(self, cantidad):
        self.puntos_vida += cantidad
        if self.puntos_vida > self.puntos_vida_max:
            self.puntos_vida = self.puntos_vida_max

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def get_tipo_personaje(self):
        pass

    def __str__(self):
        return f"[{self.get_tipo_personaje()}] {self.nombre} Nv.{self.nivel} | HP: {self.puntos_vida}/{self.puntos_vida_max}"


class Habilidoso(ABC):
    @abstractmethod
    def usar_habilidad_especial(self, objetivo):
        pass

    @abstractmethod
    def get_costo_habilidad(self):
        pass

    @abstractmethod
    def get_nombre_habilidad(self):
        pass


class Equipable(ABC):
    @abstractmethod
    def equipar_item(self, item):
        pass

    @abstractmethod
    def get_item_equipado(self):
        pass


class Sanador(ABC):
    @abstractmethod
    def sanar(self, objetivo):
        pass

    @abstractmethod
    def get_potencia_sanacion(self):
        pass


class Guerrero(Personaje, Habilidoso, Equipable):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 100 + nivel * 10)
        self.fuerza = 15 + nivel * 3
        self.defensa = 10 + nivel * 2
        self.item_equipado = "Sin equipo"
        self.costo_habilidad = 30

    def atacar(self, objetivo):
        print(f"{self.nombre} golpea con su espada causando {self.fuerza} de daño.")
        objetivo.recibir_dano(self.fuerza)

    def get_tipo_personaje(self):
        return "Guerrero"

    def usar_escudo(self):
        print(f"{self.nombre} bloquea con su escudo. Defensa: {self.defensa}")

    def usar_habilidad_especial(self, objetivo):
        print(f"{self.nombre} usa Golpe Devastador causando 50 de daño.")
        objetivo.recibir_dano(50)

    def get_costo_habilidad(self):
        return self.costo_habilidad

    def get_nombre_habilidad(self):
        return "Golpe Devastador"

    def equipar_item(self, item):
        self.item_equipado = item
        print(f"{self.nombre} equipó {self.item_equipado}")

    def get_item_equipado(self):
        return self.item_equipado


class Mago(Personaje, Habilidoso, Sanador):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 60 + nivel * 5)
        self.mana_max = 80 + nivel * 10
        self.mana = self.mana_max

    def atacar(self, objetivo):
        if self.mana >= 20:
            dano = 25 + self.nivel * 5
            self.mana -= 20
            print(f"{self.nombre} lanza un hechizo causando {dano} de daño.")
            objetivo.recibir_dano(dano)
        else:
            print(f"{self.nombre} no tiene mana suficiente.")

    def get_tipo_personaje(self):
        return "Mago"

    def recuperar_mana(self, cantidad):
        self.mana += cantidad
        if self.mana > self.mana_max:
            self.mana = self.mana_max
        print(f"{self.nombre} recupera mana. Mana actual: {self.mana}/{self.mana_max}")

    def usar_habilidad_especial(self, objetivo):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.nombre} lanza Bola de Fuego causando 40 de daño.")
            objetivo.recibir_dano(40)
        else:
            print(f"{self.nombre} no tiene mana suficiente para Bola de Fuego.")

    def get_costo_habilidad(self):
        return 20

    def get_nombre_habilidad(self):
        return "Bola de Fuego"

    def sanar(self, objetivo):
        objetivo.restaurar_vida(25)
        print(f"{self.nombre} sana a {objetivo.nombre} con 25 puntos de vida.")

    def get_potencia_sanacion(self):
        return 25


class Arquero(Personaje, Equipable):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 75 + nivel * 7)
        self.flechas = 10 + nivel * 2
        self.alcance = 30
        self.item_equipado = "Arco basico"

    def atacar(self, objetivo):
        if self.flechas > 0:
            dano = 12 + self.nivel * 4
            if self.item_equipado != "Arco basico":
                dano += 5
            self.flechas -= 1
            print(f"{self.nombre} dispara una flecha con {self.item_equipado} causando {dano} de daño.")
            objetivo.recibir_dano(dano)
        else:
            print(f"{self.nombre} no tiene flechas.")

    def get_tipo_personaje(self):
        return "Arquero"

    def recargar_flechas(self, cantidad):
        self.flechas += cantidad
        print(f"{self.nombre} recarga flechas. Flechas actuales: {self.flechas}")

    def equipar_item(self, item):
        self.item_equipado = item
        print(f"{self.nombre} equipó {self.item_equipado}")

    def get_item_equipado(self):
        return self.item_equipado


def verificacion_1_1():
    print("=== VERIFICACIÓN 1.1 ===")
    try:
        p = Personaje("test", 1, 100)
        print(p)
    except TypeError as error:
        print("Error correcto al intentar crear Personaje directamente:")
        print(error)


def verificacion_2():
    print("\n=== VERIFICACIÓN 2 ===")
    thorin = Guerrero("Thorin", 3)
    gandalf = Mago("Gandalf", 5)
    legolas = Arquero("Legolas", 4)

    print(thorin)
    print(gandalf)
    print(legolas)


def batalla():
    print("\n=== BATALLA CON POLIMORFISMO ===")
    heroes = [
        Guerrero("Thorin", 3),
        Mago("Gandalf", 5),
        Arquero("Legolas", 4)
    ]

    orco = Guerrero("Orco", 1)
    turno = 1

    while orco.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        for h in heroes:
            if orco.esta_vivo():
                h.atacar(orco)
        turno += 1

    print(f"\nLa batalla terminó en {turno - 1} turno(s).")
    print("\nEstado final de los heroes:")
    for h in heroes:
        print(h)

    print("\nEstado final del enemigo:")
    print(orco)


def batalla_completa():
    print("\n=== BATALLA COMPLETA CON INTERFACES ===")
    heroes = [
        Guerrero("Thorin", 3),
        Mago("Gandalf", 5),
        Arquero("Legolas", 4)
    ]

    orco = Guerrero("Orco", 1)

    print("=== FASE 1: EQUIPAR ===")
    for h in heroes:
        if isinstance(h, Equipable):
            if h.nombre == "Thorin":
                h.equipar_item("Espada Legendaria")
            elif h.nombre == "Legolas":
                h.equipar_item("Arco Elfico")

    print("\n=== FASE 2: BATALLA ===")
    turno = 1

    while orco.esta_vivo():
        print(f"\n--- Turno {turno} ---")

        for h in heroes:
            if not orco.esta_vivo():
                break

            if turno == 2 and isinstance(h, Habilidoso):
                h.usar_habilidad_especial(orco)

            if orco.esta_vivo():
                h.atacar(orco)

        turno += 1

    print(f"\nLa batalla terminó en {turno - 1} turno(s).")

    print("\n=== FASE 3: SANACIÓN POST BATALLA ===")
    heroe_menos_vida = min(heroes, key=lambda h: h.puntos_vida)

    for h in heroes:
        if isinstance(h, Sanador):
            h.sanar(heroe_menos_vida)

    print("\n=== ESTADO FINAL ===")
    for h in heroes:
        print(h)
    print(orco)


if __name__ == "__main__":
    verificacion_1_1()
    verificacion_2()
    batalla()
    batalla_completa()
