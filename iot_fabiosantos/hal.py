# IOT 
# Big Data e Inteligência analítica
# Aluno: Fábio Henrique dos Santos

from random import choice 
from console_logging.console import Console
console = Console()


class mudanca_temperatura:
  @staticmethod
  def temperature():
    return choice(range(20,35))

  @staticmethod
  def umidade():
    return choice(range(50,80))

  @staticmethod
  def aquecedor(status: str):
    if status == 'on':
          console.info("Aquecedor LIGADO")
    else:
          console.info("Aquecedor DESLIGADO")

if __name__ == "__main__":
  hal = mudanca_temperatura()
  hal.aquecedor("on")
 
  hal.aquecedor("off")

  console.log(hal.umidade())
  console.log(hal.temperature())