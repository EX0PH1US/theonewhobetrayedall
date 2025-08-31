from flask import Flask, render_template, request, flash, redirect, send_from_directory, url_for
import hashlib

PASSHASH = '35ad15b2d691a1f51ce3fc7205e31dc0632587d910952c9e3cd4bef9340d1919b2778841b0e72ae22228d50967595f0e8a0fa5cadb6c80a4981cb9d47b536898' #seven

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        pwd = request.form['sec']
        hahsedvalue = hashlib.sha512(pwd.encode()).hexdigest()
        if (hahsedvalue == PASSHASH):
            print('Wokring')
            return send_from_directory('static', 'theonewithdante.zip', as_attachment=True)
        else:
            print("Wrong PWD")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()