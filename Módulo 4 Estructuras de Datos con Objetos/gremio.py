class Personaje:
    def __init__(self, nombre, nivel, hp):
        self.nombre = nombre
        self.nivel = nivel
        self.hp = hp
        self.estado = "activo"
        class GremioRPG:
    def __init__(self, nombre):
        self.nombre_gremio = nombre
        self.equipo_principal = [None] * 6
        self.dungeon = [[None]*3 for _ in range(3)]
        self.espera = []

    def unirse_al_equipo(self, p):
        for i in range(len(self.equipo_principal)):
            if self.equipo_principal[i] is None:
                self.equipo_principal[i] = p
                print(f'{p.nombre} se unió al equipo.')
                return True
        self.espera.append(p)
        print(f'{p.nombre} en espera.')
        return False

    def colocar_en_dungeon(self, p, fila, col):
        if self.dungeon[fila][col] is None:
            self.dungeon[fila][col] = p

    def limpiar_caidos(self):
        for i in range(len(self.equipo_principal)):
            p = self.equipo_principal[i]
            if p is not None and p.hp == 0:
                print(f'{p.nombre} ha caído.')
                self.equipo_principal[i] = None

        self.espera = [p for p in self.espera if p.hp > 0]

    def reporte_gremio(self):
        activos = sum(1 for p in self.equipo_principal if p is not None)
        hp_total = sum(p.hp for p in self.equipo_principal if p is not None)

        print(f'\n=== GREMIO: {self.nombre_gremio} ===')
        print(f'Equipo activo: {activos}/6')
        print(f'HP total equipo: {hp_total}')
        print(f'En espera: {len(self.espera)}')
        g = GremioRPG("Avengers")

p1 = Personaje("Thor", 12, 150)
p2 = Personaje("Hulk", 15, 200)

g.unirse_al_equipo(p1)
g.unirse_al_equipo(p2)

g.reporte_gremio()