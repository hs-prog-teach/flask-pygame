import random

from flask import Flask, render_template

import pygame

app = Flask(__name__)

pygame.init()

screen = pygame.display.set_mode((300, 300))

@app.route("/<color>" )
def hello_world(color):
    
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill((0,0,0))
    pygame.draw.circle(screen, color, (150, 150), 100)
    pygame.display.flip()


@app.route("/circle")
def say_hi():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill((0,0,0))
    pygame.draw.circle(screen, color, (150, 150), 100)
    pygame.display.flip()

@app.route("/image")
def show_board():
    image_name = "screen.jpg"
    pygame.image.save(screen, f"static/{image_name}")

    return render_template('generated-image.html', image_file=image_name)