"Main Flask app for RUL package"

from flask import Flask, render_template, request
from flask import send_file, session
from flask import url_for, redirect
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

import os
import pandas as pd

from rul.pipeline.batch_prediction import start_batch_prediction
from rul.pipeline.training_pipeline import start_training_pipeline


# APP configuration and global variables
app = Flask(__name__,template_folder="templates",static_folder="static")
UPLOAD_FOLDER = 'static\\files\\'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 30 * 1000 * 1000
app.secret_key ="xy"


@app.route('/', methods=['GET'])  
@cross_origin()
def homePage():
    """
    Route for homepage
    ------------------------------------------------------------
    input: 
    - `None`
    ------------------------------------------------------------
    return: `render_template("home.html")`
    """
    return render_template("home.html")


@app.route('/batch_prediction', methods=['POST', 'GET'])
def run_batch_prediction():
    """
    Route for Batch Prediction
    -------------------------------------------------------------------------------
    input: 
    - `None`
    -------------------------------------------------------------------------------
    return: `render_template("output.html")` else `render_template("warning.html")`
    """

    if request.method == "POST":
        try:
            # Running batch prediction on base dataset
            run_batch_prediction.prediction_file_path = start_batch_prediction(input_file_path='rul.csv')

            prediction_df = pd.read_csv(run_batch_prediction.prediction_file_path).head(1000)

            return render_template("output.html", tables=[prediction_df.to_html(classes="dataframe", header=True)], titles=prediction_df.columns.values)

        except Exception as e:
            message = "Batch Prediction Failed! Issue occurred at our end!"
        return render_template("warning.html", message=message)