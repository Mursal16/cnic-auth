
from flask import Flask,request
import os
from face_match import get_embeddings,is_match
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    embeddings=get_embeddings(['Bob1.jpeg','Idcard.jpg'])
    final=is_match(embeddings[0],embeddings[1])
    if (final==1):
        return '<h3>match</h3>'
    else:
        return '<h3>not match </h3>'


app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = '/path'



# @app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    name1 = request.files['file']
    name2=  request.files['file2']
    print (name1)
    print(name2)
    embeddings=get_embeddings([name1,name2])
    final=is_match(embeddings[0],embeddings[1])
    if (final==1):
        print("match")
        return 1
    else:
        print("no match")
        return 0
    # file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file

