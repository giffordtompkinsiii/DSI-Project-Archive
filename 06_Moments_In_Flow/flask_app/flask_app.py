import numpy as np
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns 
from PIL import Image 
from tensorflow.keras.models import load_model
# from sqlalchemy import create_engine
from flask import Flask, request, render_template, jsonify, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# initialize the flask app
app = Flask('myApp')
UPLOAD_FOLDER = './user_images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(image, model):
    poses = ['warrior_iii','warrior_ii','crow','downward_facing_dog','supported_shoulder_stand']

    image = np.array(image, dtype='float32')
    image = image/255
    pred_array = model.predict(image)

    result = poses[np.argmax(pred_array)]
    score = 30
    # score = float(f"{(max(pred_array[0]) * 100)}")
    print(f'Result: {result}, Score: {score}')
    return result, score

### route 1: home
@app.route('/')
def home():
    # return the view
    return render_template('home.html')

### route 2: show a form to the user
@app.route('/form')
def form():
    # return the view
    return render_template('form.html')

### route 3: upload file
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # load model
    poses = ['warrior_iii','warrior_ii','crow','downward_facing_dog','supported_shoulder_stand']

    model = load_model('assets/model.h5')

    img_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    im = Image.open(img_path)
    im_resize = im.resize((244,244))
    np_im = np.array(im_resize)
    np_im_reshape = np_im.reshape((1,244,244,3))

    result, score = predict_image(np_im_reshape,model)
    poses.remove(result)

    # return the prediction in the template
    print(filename)
    print(img_path)
    # img_path = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    return render_template('results.html', prediction=result, certainty=score, poses=poses)
    # return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# run the app
if __name__ == '__main__':
    # do something
    app.run(debug=True)