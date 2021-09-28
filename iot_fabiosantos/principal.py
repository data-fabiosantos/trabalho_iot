# IOT 
# Big Data e Inteligência analítica
# Aluno: Fábio Henrique dos Santos

# Importação de bibliotecas e funções de arquivos complementares
from time import sleep
import paho.mqtt.client as mqtt 
from random import choice 
from hal import mudanca_temperatura
from definitions import user, password, client_id, server, port 

software =  mudanca_temperatura()

def mensagem(client, userdata, msg):
  valor = msg.payload.decode().split(",")
  software.aquecedor("on" if valor[1] == '1' else 'off')
  client.publish(''.format(user,client_id),
  f'ok,{valor[0]}')



client = mqtt.Client(client_id)
client.username_pw_set(user,password)
client.connect(server,port)


client.on_message = mensagem
client.subscribe(''.format(user,client_id))
client.loop_start()


def main():
  while True:
      client.publish(''.format(user,client_id), hardware.temperature())
      client.publish(''.format(user,client_id),hardware.umidade())

      sleep(10)
