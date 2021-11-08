from p5 import setup, draw, size, background, run
import p5

def setup():
    size(400,400)


def draw():
    background(30,30,47)

    p5.fill('red')
    p5.triangle(20,20,30,30,40,40)



run()