import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b"secret"

ALLOWED_EXTENSIONS = {'txt','pdf','jpg','png','jpeg','gif'}
BASE_PATH = os.path.abspath(os.environ.get('HOME'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files.get('file')

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(BASE_PATH,'code/flask/basic-flask/upload_flask/files', filename))
            flash('File upload successfully')
            return redirect(url_for('download'))

    return render_template('index.html')

@app.route('/download',methods=['GET'])
def download():
    return 'Download Page'

if __name__ == "__main__":
    app.run(debug=True)
