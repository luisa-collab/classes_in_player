

class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"o {self.tipo} atacou usando {ataque}")

# Exemplo de uso
heroi1 = Heroi("Gandalf", 100, "mago")
heroi1.atacar()

heroi2 = Heroi("Conan", 30, "guerreiro")
heroi2.atacar()

heroi3 = Heroi("Shifu", 50, "monge")
heroi3.atacar()

heroi4 = Heroi("Naruto", 20, "ninja")
heroi4.atacar()
