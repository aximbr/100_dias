#Esse é o meu projeto pessoal de refazer o jogo Space Invaders usando os conhecimentos adquiridos em Pytho
#Abaixo meu TODO List
# Criar uma classe para o Canhão
# Criar uma classe para a defesa/castelo/fortaleza
# Criar um método para criar e mover o míssil
# Criar uma classe para os monstros
#TODO: criar uma classe para a nave mãe
#TODO: Criar uma classe para o controle do placar
# Detectar quando o missil atinge um pedaço da fortaleza
# Detectar quando um míssil atingiu um monstro
#TODO: Detectar quando uma bomba atigiu o canhão ou a defesa

import time
from turtle import Screen
from cannon import Cannon
from fortress import Fortress
from monster import Monster
from scoreboard import Scoreboard



# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.addshape(name="monster1_up.gif" )
screen.addshape(name="monster1_down.gif" )

cannon = Cannon()
fortress = Fortress()
monster = Monster()
scoreboard = Scoreboard()

# scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(cannon.move_right, "Right")
screen.onkeypress(cannon.move_left, "Left")
screen.onkeypress(cannon.create_missil, "space")




game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cannon.missil_up()
    monster.move_monster()

    #detect if a missil reach the fortress
    for missil in cannon.missiles:
        for element in fortress.elements:
            if missil.distance(element) < 5:
                cannon.delete_missil(cannon.missiles.index(missil) )
                fortress.delete_element(fortress.elements.index(element))
#             game_is_on = False
#             scoreboard.game_over()

    #detect if a missil reach a monster
    for missil in cannon.missiles: 
        for monster_current in monster.monsters:
            if missil.distance(monster_current) <20:
                cannon.delete_missil(cannon.missiles.index(missil) )
                monster.delete_monster(monster.monsters.index(monster_current))
                scoreboard.increase_score()
            
#     #detect if the turtle reach the final line
#     if player.is_at_finish_line():
#         car_manager.increase_speed()
#         scoreboard.increase_level()
    
screen.exitonclick()
