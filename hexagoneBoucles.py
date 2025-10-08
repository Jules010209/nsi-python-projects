# Créé par CHENELAT, le 08/10/2025 en Python 3.7
from turtle import *

width(1)
espace=18

def drawHexagone(cote):
    right(60)
    down()
    for i in range(6):
        forward(cote)
        left(60)
    up()
    left(60)
    forward(2*long)

for long in [20, 25, 30, 35, 40, 35, 30]:
    drawHexagone(long)
    forward(espace)

done()
