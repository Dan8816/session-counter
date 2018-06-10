from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below


@app.route('/')
def Visit():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit']=0
    return render_template("index.html", visit=session['visit'])

@app.route('/countup', methods=['POST'])
def countup():
    print("user pressed the crazy button")
    session['visit'] += 100
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    print("user pressed the bye button")
    session['visit'] = 0
    return redirect('/')

app.run(debug=True)
