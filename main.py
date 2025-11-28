# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from flask import Flask, render_template, send_from_directory, abort
from werkzeug.utils import secure_filename

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

PDF_DIR = os.path.join(app.root_path, 'resources')
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    return render_template('index.html')

@app.route('/devis/<id>')
def devis(id):
    filename = "devis" + secure_filename(id) + ".pdf"
    try:
        # 'as_attachment=False' tells the browser to open it inline
        return send_from_directory(
            directory=PDF_DIR,
            path=filename,
            mimetype='application/pdf',
            as_attachment=False
        )
    except FileNotFoundError:
        abort(404)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
