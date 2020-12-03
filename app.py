from flask import (
    Flask,
    render_template,
    request,
    redirect,
    current_app,
    url_for,
    send_from_directory
)
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone
import os


app=Flask(__name__)
app.config['UPLOAD_PATH']='uploads'


dz=Dropzone(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def upload_image():
    if request.files:
        image=request.files['file']
        image.save(app.config['UPLOAD_PATH'],image.filename)

        return "FILE SAVED SUCESSFULLY"

    return redirect(url_for('index'))
