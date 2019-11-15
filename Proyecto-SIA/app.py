from flask import Flask, flash, redirect, render_template, request, session, abort, , url_for, send_from_directory
import logging, os
from werkzeug import secure_filename

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
print("Esto es lo que se tiene {}".format(PROJECT_HOME))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route("/")
def index():
    return "Index!"

@app.route('/update', methods = ['POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.files['image']
        img_name = secure_filename(img.filename)
        create_new_folder(app.config['UPLOAD_FOLDER'])
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        return "ACEPTADO"
    else:
        return "Where is the image?"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)


if __name__ == "__main__":
    app.run("0.0.0.0",debug=False)
    #app.run("0.0.0.0",debug=True)
