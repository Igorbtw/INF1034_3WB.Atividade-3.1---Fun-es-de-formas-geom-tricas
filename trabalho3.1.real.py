from turtle import *
from random import randint

t = Turtle()


def plano_cartesiano():
    t.fd(300)
    t.stamp()
    t.goto(0, 0)
    t.pd()
    t.lt(90)
    t.fd(300)
    t.goto(0, 0)
    t.pd()
    t.lt(90)
    t.fd(300)
    t.goto(0, 0)
    t.pd()
    t.lt(90)
    t.fd(300)

plano_cartesiano()    


def desenhar_triangulo(x, y, tamanho, nome):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.lt(90)
    for _ in range(3):
         t.fd(tamanho)
         t.lt(120) 
    t.end_fill()

x = randint(-150, 50)
y = randint(50, 150)
tamanho = randint(10, 200)

color = textinput('obter cor', 'Digite a cor desejada')
desenhar_triangulo(x, y, tamanho, color)

def desenhar_hexagono(x, y, tamanho, nome):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(6):
      t.fd(tamanho)
      t.rt(60)
t.end_fill()

x = randint(-150, -50)
y = randint(-150, -50)
tamanho = randint(10, 100)
color = textinput('obter cor', 'Digite a cor desejada')
desenhar_hexagono(x, y, tamanho, color)


def desenhar_pentagono(x, y, tamanho, nome):
      t.pu()
      t.goto(x,y)
      t.pd()
      t.begin_fill()
      t.fillcolor(color)
      for _ in range(6):
       t.fd(tamanho)
       t.rt(72)
t.end_fill()
    
x = randint(-100, 200)
y = randint(-100, 200)
tamanho = randint(10, 100)
color = textinput('obter cor', 'Digite a cor desejada')
desenhar_pentagono(x, y, tamanho, color)

def desenhar_octagono(x, y, tamanho, nome):
      t.pu()
      t.goto(x,y)
      t.pd()
      t.begin_fill()
      t.fillcolor(color)
      for _ in range(8):
        t.fd(tamanho)
        t.rt(45)
    t.end_fill()

x = randint(100, 200)
y = randint(-200, -100)
tamanho = randint(10, 135)
color = textinput('obter cor', 'Digite a cor desejada')
desenhar_octagono(x, y, tamanho, color)

mainloop()

