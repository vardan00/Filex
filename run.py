import os
from flask import *
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
	return render_template("index.html")
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	file = request.files['file']
	if request.method == 'POST':	
		to_disk_file_name = os.path.join(app.config['UPLOAD_DIR'], file.filename)
		print(to_disk_file_name)
		file.save(to_disk_file_name)
	return ""
if __name__ == '__main__':
	app.config['UPLOAD_DIR'] = os.getcwd()
	app.run(host = '0.0.0.0', port = 5555, debug = True)