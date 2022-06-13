# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:46:30 2021

@author: user
"""
import glob
import os
import pandas as pd
import json
from flask import Flask, flash, request, redirect, render_template,send_file,send_from_directory,url_for
from werkzeug.utils import secure_filename
from Wrapper_to_reduce_execution_time import wrapper_main


app=Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

path = os.getcwd()

UPLOAD_FOLDER = os.path.join(path, 'uploads')
IMAGES_FOLDER = os.path.join(path,"images")
static_FOLDER = os.path.join(path,"static")

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
    
if not os.path.isdir(IMAGES_FOLDER):
    os.mkdir(IMAGES_FOLDER)
    
if not os.path.isdir(static_FOLDER):
    os.mkdir(static_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER
app.config['static_FOLDER'] = static_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':

        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        

        files = request.files.getlist('image')
        
       
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        
        
        try:
            test = r'D:/otimised_poc_ocr/images/*'
            r = glob.glob(test)
            for i in r:
                os.remove(i)
            df = wrapper_main()
            # json_obj = df.to_json(orient='records')
            # j = json.loads(json_obj)
            
        except:
            pass 
       
        try:
            print("intry")
            filelist = glob.glob(os.path.join(UPLOAD_FOLDER, "*"))
            for f in filelist:
                os.remove(f)  
        except:
            pass           
        flash("Data Extraction is Completed and csv is been generated")
        # return json.dumps(j)
        return redirect('/')
        
        # return redirect(url_for('http://127.0.0.1:5000/'))
    else:
        return redirect('/')

@app.route('/getPlotCSV') # this is a job for GET, not POST
def plot_csv():
    
    
    try:
        return send_file('D:\otimised_poc_ocr\images\Final_Invoice_Data.csv',
                         mimetype='text/csv',
                         download_name='Final_Invoice_Data.csv',
                         as_attachment=True)
    except:
        return send_file('D:/otimised_poc_ocr/images/Invoice_Details.csv',
                         mimetype='text/csv',
                         download_name='Invoice_Details.csv',
                         as_attachment=True)
    
    
if __name__ == "__main__":
    app.run()
    

