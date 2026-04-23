from abc import ABC, abstractmethod


class Habilidoso(ABC):
    @abstractmethod
    def usar_habilidad_especial(self, objetivo):
        pass


class Equipable(ABC):
    @abstractmethod
    def equipar(self, item):
        pass


class Sanador(ABC):
    @abstractmethod
    def sanar(self, aliado):
        pass


class Personaje(ABC):
    def __init__(self, nombre, nivel, puntos_vida):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_vida = puntos_vida

    def recibir_dano(self, dano):
        self.puntos_vida = max(0, self.puntos_vida - dano)

    def curar(self, puntos):
        self.puntos_vida += puntos

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {{nombre='{self.nombre}', nivel={self.nivel}, vida={self.puntos_vida}}}"


class Guerrero(Personaje, Habilidoso, Equipable):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 100 + nivel * 10)
        self.fuerza = 15 + nivel * 2
        self.defensa = 10 + nivel

    def atacar(self, objetivo):
        dano = self.fuerza
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} ataca con espada y hace {dano} de daño.")

    def usar_habilidad_especial(self, objetivo):
        dano = self.fuerza + 20
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} usa Golpe Devastador y hace {dano} de daño.")

    def equipar(self, item):
        self.defensa += 5
        print(f"{self.nombre} equipa {item} y sube su defensa a {self.defensa}.")


class Mago(Personaje, Habilidoso, Sanador):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 60 + nivel * 5)
        self.mana_max = 100 + nivel * 10
        self.mana = self.mana_max

    def atacar(self, objetivo):
        dano = 12 + self.nivel * 3
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} lanza hechizo y hace {dano} de daño.")

    def usar_habilidad_especial(self, objetivo):
        if self.mana >= 20:
            dano = 30 + self.nivel * 4
            self.mana -= 20
            objetivo.recibir_dano(dano)
            print(f"{self.nombre} usa Bola de Fuego y hace {dano} de daño. Mana restante: {self.mana}")
        else:
            print(f"{self.nombre} no tiene suficiente mana para Bola de Fuego.")

    def sanar(self, aliado):
        if self.mana >= 15:
            cura = 25 + self.nivel * 2
            self.mana -= 15
            aliado.curar(cura)
            print(f"{self.nombre} sana a {aliado.nombre} por {cura} puntos. Mana restante: {self.mana}")
        else:
            print(f"{self.nombre} no tiene suficiente mana para sanar.")


class Arquero(Personaje, Equipable):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, 75 + nivel * 7)
        self.flechas = 10 + nivel
        self.alcance = 20 + nivel * 2

    def atacar(self, objetivo):
        if self.flechas > 0:
            dano = 14 + self.nivel * 2
            self.flechas -= 1
            objetivo.recibir_dano(dano)
            print(f"{self.nombre} dispara una flecha y hace {dano} de daño. Flechas restantes: {self.flechas}")
        else:
            print(f"{self.nombre} no tiene flechas.")

    def equipar(self, item):
        self.alcance += 5
        self.flechas += 3
        print(f"{self.nombre} equipa {item}, aumenta su alcance a {self.alcance} y ahora tiene {self.flechas} flechas.")


class Enemigo:
    def __init__(self, nombre, puntos_vida):
        self.nombre = nombre
        self.puntos_vida = puntos_vida

    def recibir_dano(self, dano):
        self.puntos_vida = max(0, self.puntos_vida - dano)

    def __str__(self):
        return f"Enemigo {{nombre='{self.nombre}', vida={self.puntos_vida}}}"


def mostrar_estado(heroes, enemigo):
    for heroe in heroes:
        print(heroe)
    print(enemigo)


def main():
    guerrero = Guerrero("Thor", 5)
    mago = Mago("Merlín", 4)
    arquero = Arquero("Legolas", 6)
    orco = Enemigo("Orco Jefe", 120)

    heroes = [guerrero, mago, arquero]

    print("=== ESTADO INICIAL ===")
    mostrar_estado(heroes, orco)

    print("\n=== ATAQUES NORMALES (POLIMORFISMO) ===")
    for heroe in heroes:
        heroe.atacar(orco)

    print("\n=== HABILIDADES ESPECIALES E INTERFACES ===")
    for heroe in heroes:
        if isinstance(heroe, Habilidoso):
            heroe.usar_habilidad_especial(orco)

        if isinstance(heroe, Sanador):
            heroe.sanar(guerrero)

        if isinstance(heroe, Equipable):
            heroe.equipar("Ítem épico")

    print("\n=== ESTADO FINAL ===")
    mostrar_estado(heroes, orco)


if __name__ == "__main__":
    main()
