from crypt import methods
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def random_number():
    # session['code'] = 'N'
    session['random_number'] = random.randint(0,100)
    print("The random intiger is ", session['random_number'])
    print(session)
    return render_template('index.html')


@app.route('/output', methods=['POST'])
def evaluate_guess():
    print("The guess was: ", request.form['guess'])
    user_guess = int(request.form['guess'])
    session['guess'] = user_guess
    if user_guess == int(session['random_number']):
        session['output'] = str(session['random_number']) + " was the number!"
        session['code'] ='T'
    elif user_guess > int(session['random_number']):
        session['output'] = "Too High!"
        session['code'] = 'F'
    else:
        session['output'] = "Too Low!"
        session['code'] = 'F'
    print("The guess output is", session['output'])
    print("session is :", session)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)