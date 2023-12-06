import random

from flask import Flask, render_template

import pygame

app = Flask(__name__)
pygame.init()
screen = pygame.display.set_mode((300, 300))
@app.route("/<radius>/<color>/<x>/<y>")
def hello_world(radius,color,x,y):
    screen.fill((0,0,0))
    pygame.draw.circle(screen, color, (int(x), int(y)), int(radius))
    pygame.display.flip()

    image_name = "screen.jpg"
    pygame.image.save(screen, f"static/{image_name}")

    return render_template('generated-image.html', image_file=image_name)


@app.route("/say-hi/<name>")
def say_hi(name):
    # my_name = input("Enter your name: ")
    return f"<b>Hi, {name} from!</b>"

@app.route("/board")
def show_board():
    return render_template('board-page.html', name="Serhii")

if __name__ == "__main__":
    app.run()