class Animal:
    def sonido(self):
        print("el animal hace un sonido")


class Vaca(Animal):
    def sonido(self):
        print("la vaca muuuuuu")


class Gallina(Animal):
    def sonido(self):
        print("la gallina corocoo")


class Pollito(Animal):
    def sonido(self):
        print("el pollito hace piooooooo")


class Cordero(Animal):
    def sonido(self):
        print("el cordero hace beeeee")


def main():
    a = Animal()
    b = Vaca()
    c = Gallina()
    d = Pollito()
    e = Cordero()

    a.sonido()
    b.sonido()
    c.sonido()
    d.sonido()
    e.sonido()


if __name__ == "__main__":
    main()