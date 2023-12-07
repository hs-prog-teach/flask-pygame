from flask import Flask, render_template, request
from PIL import Image, ImageDraw
import random
import math
import os

from moviepy.editor import ImageSequenceClip

app = Flask(__name__)
@app.route("/")
def hello_world():
    default_radius = 100
    default_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    default_x = 150
    default_y = 150

    radius = request.args.get('radius', default=default_radius, type=int)
    color = request.args.get('color', default=default_color)
    x = request.args.get('x', default=default_x, type=int)
    y = request.args.get('y', default=default_y, type=int)

    if isinstance(color, str):
        color = tuple(map(int, color.split(',')))

    image = Image.new('RGB', (300, 300), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)

    image_name = "screen.jpg"
    image.save(f"static/{image_name}")

    return render_template('generated-image.html', image_file=image_name)

@app.route("/generate-video")
def generate_video():
    width, height = 300, 300
    frames = []

    # Generate frames
    for i in range(60):
        image = Image.new('RGB', (width, height), 'black')
        draw = ImageDraw.Draw(image)

        draw.rectangle([0, 0, width, height], fill='red')

        triangle_points = [(0, height), (width / 2, 0), (width, height)]
        draw.polygon(triangle_points, fill='blue')

        radius = 70
        angle = 2 * math.pi * (i / 60)

        circle_x = width / 2 + (width / 2 - radius) * math.cos(angle)
        circle_y = height / 2 + (height / 2 - radius) * math.sin(angle)

        draw.ellipse([circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius], fill='green')

        frame_path = f"static/frame_{i:02d}.jpg"
        image.save(frame_path)
        frames.append(frame_path)

    clip = ImageSequenceClip(frames, fps=10)
    video_file_name = 'generated_video.mp4'
    clip.write_videofile(f"static/{video_file_name}", codec='libx264', audio=False)

    for frame in frames:
        os.remove(frame)

    return render_template('generated-video.html', video_file_name=video_file_name)

@app.route("/board")
def show_board():
    return render_template('board-page.html', name="Serhii")

if __name__ == '__main__':
    app.run(debug=True)