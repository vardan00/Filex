import os
from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    print(request.files['file'])
    file_name = request.files['file']
    print(file_name)
    if request.method == 'POST':
        disk_file_name = os.path.join(os.getcwd(), file_name.filename)
        file_name.save(disk_file_name)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555, debug = True)
