from javascript import require, On
from time import sleep
import random
from pystyle import Colors, Colorate, Write

chars = 'QWERTYUIOPASDFGHJKLZXCVBNM'

print(Colorate.Vertical(Colors.purple_to_red, '''

┌┬┐┬┌┐┌┌─┐┌─┐┬─┐┌─┐┌─┐┌┬┐  ┌┐ ┌─┐┌┬┐
│││││││├┤ │  ├┬┘├─┤├┤  │   ├┴┐│ │ │ 
┴ ┴┴┘└┘└─┘└─┘┴└─┴ ┴└   ┴   └─┘└─┘ ┴  By Pąblo#4316   
Pąblo#4316 | https://github.com/palblo/minecraftbots
''', 1))

speed = int(Write.Input("Join Speed -> ", Colors.red_to_purple, interval=0.00005))
address = Write.Input("Address (without port) -> ", Colors.red_to_purple, interval=0.00005)
port = Write.Input("Port -> ", Colors.red_to_purple, interval=0.00005)
bots = int(Write.Input("How many bots? -> ", Colors.red_to_purple, interval=0.00005))
print()

mineflayer = require('mineflayer')

RANGE_GOAL = 1
for i in range(bots):
    BOT_USERNAME = ''.join(random.choice(chars) for i in range(10))
    bot = mineflayer.createBot({
      'host': address,
      'port': port,
      'username': BOT_USERNAME
    })
     
    @On(bot, 'spawn')
    def handle(*args):
      print(Colorate.Horizontal(Colors.yellow_to_red, f"{BOT_USERNAME} JOINED", 1))
      mcData = require('minecraft-data')(bot.version)
      print(Colorate.Horizontal(Colors.red_to_purple, f"SLEEP FOR {speed} SECONDS...", 1))
    sleep(speed)
print()
print(Colorate.Horizontal(Colors.green_to_white, f"DONE", 1))


    
