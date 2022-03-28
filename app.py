from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

def get_images():
    images_directory = Path("./static/images")
    images = []
    for path in images_directory.glob("*.png"):
        images.append(str(path.name))

    images.sort()
    return images


@app.route("/images")
def images():
    images = get_images()
    return render_template("images.jinja2", images=images)