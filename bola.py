# 01) Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
  def __init__(self, cor, circunferencia, material):
    self.cor = cor
    self.circunferencia = circunferencia
    self.material = material


  def trocaCor(self, novaCor):
    self.cor = novaCor


  def mostraCor(self):
    return self.cor
