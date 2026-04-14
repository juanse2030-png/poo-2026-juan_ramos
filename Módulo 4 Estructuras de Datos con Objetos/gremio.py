g = GremioRPG("Avengers")

p1 = Personaje("Thor", 12, 150)
p2 = Personaje("Hulk", 15, 200)
p3 = Personaje("Iron Man", 11, 140)
p4 = Personaje("Spiderman", 9, 100)
p5 = Personaje("Capitan America", 13, 160)
p6 = Personaje("Vision", 14, 170)
p7 = Personaje("black panther", 8, 90)
p8 = Personaje("Hawkeye", 7, 80)

g.unirse_al_equipo(p1)
g.unirse_al_equipo(p2)
g.unirse_al_equipo(p3)
g.unirse_al_equipo(p4)
g.unirse_al_equipo(p5)
g.unirse_al_equipo(p6)
g.unirse_al_equipo(p7)
g.unirse_al_equipo(p8)

g.colocar_en_dungeon(p1, 0, 0)
g.colocar_en_dungeon(p2, 0, 1)
g.colocar_en_dungeon(p3, 1, 1)
g.colocar_en_dungeon(p4, 2, 2)

# Simulación de batalla
p1.hp = 0
p2.hp = 0

g.limpiar_caidos()
g.reporte_gremio()
