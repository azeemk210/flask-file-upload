from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Create the upload directory if it doesn't exist
UPLOAD_FOLDER = 'file_uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create directory if it doesn't exist

@app.route('/')
def upload():
    return render_template("file_upload_form.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        if 'file' not in request.files: # Check if file is present in the request
            return "No file part" , 400 #return error code 400 and error message

        f = request.files['file']

        if f.filename == '': #check if user has selected any file or not
            return "No selected file", 400 #return error code 400 and error message

        if f:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)  # Correct path
            f.save(filepath)
            return render_template("success.html", name=f.filename)
        else:
            return "File not saved", 500 #return error code 500 and error message

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)