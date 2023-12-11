import random
from flask import Flask, render_template
from PIL import Image, ImageDraw
from moviepy.editor import ImageSequenceClip

app = Flask(__name__)

@app.route("/")
def hello_world():
    frames = []

    for _ in range(30):
        img = generate_image()
        frames.append(img)

    image_names = save_frames(frames)

    video_name = "generated_video.mp4"
    create_video(image_names, video_name)

    return render_template('generated-video.html', video_file_name=video_name)

def generate_image():
    image = Image.new("RGB", (300, 300), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse((100, 100, 200, 200), fill=color)

    return image

def save_frames(frames):
    image_names = []

    for i, frame in enumerate(frames):
        image_name = f"frame_{i}.png"
        frame.save(f"static/{image_name}")
        image_names.append(f"static/{image_name}")

    return image_names

def create_video(image_names, video_name):
    clip = ImageSequenceClip(image_names, fps=10)
    clip.write_videofile(f"static/{video_name}", codec="libx264", audio=False)

# @app.route("/say-hi/<name>")
# def say_hi(name):
#     return f"<b>Hi, {name}!</b>"

# @app.route("/board")
# def show_board():
#     return render_template('board-page.html', name="Serhii")
