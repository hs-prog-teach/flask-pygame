import random
from flask import Flask, render_template, request
import pygame

app = Flask(__name__)

pygame.init()
screen = pygame.display.set_mode((300, 300))

@app.route("/")
def hello_world():
    default_radius = random.randint(10, 100)
    default_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    default_x = random.randint(0, 255)
    default_y = random.randint(0, 255)

    # Getting parameters from the URL
    radius = request.args.get('radius', default=default_radius, type=int)
    color = request.args.get('color', default=default_color)
    x = request.args.get('x', default=default_x, type=int)
    y = request.args.get('y', default=default_y, type=int)

    if isinstance(color, str):
        color = tuple(map(int, color.split(',')))

    screen.fill((0,0,0))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

    image_name = "screen.jpg"
    pygame.image.save(screen, f"static/{image_name}")

    return render_template('generated-image.html', image_file=image_name)

# Other routes remain the same
