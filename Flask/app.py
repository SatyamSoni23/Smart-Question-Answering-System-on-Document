from flask import *
import pyrebase
import os

import pandas as pd
from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline
import joblib

config = {
	"apiKey": "Put Your Firebase Api Key Here",
    "authDomain": "Put Your Firebase AuthDomain Here",
    "projectId": "Put Your Project Id Here",
	"databaseURL" : "",
    "storageBucket": "Put Your Storage Bucket Link Here",
    "messagingSenderId": "Put Your Message Sender Id Here",
    "appId": "Put Your App Id Here",
    "measurementId": "Put Your Measurement Id Here"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def fine_tuning_drive(question, file_name):
  storage.child("docs/" + file_name).download("/docs/", "docs/" + file_name)
  df = pdf_converter(directory_path="docs/")
  pd.set_option('display.max_colwidth', -1)
  df.head()
  cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)
  cdqa_pipeline.fit_retriever(df=df)
  joblib.dump(cdqa_pipeline, './models/bert_qa_custom.joblib')
  cdqa_pipeline=joblib.load('./models/bert_qa_custom.joblib')
  prediction = cdqa_pipeline.predict(question, 1)
  os.remove("docs/"+file_name)
  return prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if(request.form.get('btn') == 'index'):
		  upload = request.files['upload']
		  path = "docs"
		  global file_name
		  file_name = upload.filename
		  #print(file_name)
		  storage.child("docs/"+file_name).put(upload)
		  return redirect(url_for('qa'))
		elif (request.form.get('btn') == 'qa'):
		  print(file_name)
		  question = request.form.get('question')
		  answer = fine_tuning_drive(question, file_name)
		return render_template('qa.html', answer = answer, question = question)
	return render_template('index.html')
  
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    global func
    func = request.args.get('type')
    return render_template('upload.html')

@app.route('/qa/', methods=['GET', 'POST'])
def qa():
    return render_template('qa.html')
	
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
