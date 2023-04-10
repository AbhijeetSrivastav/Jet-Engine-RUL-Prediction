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

