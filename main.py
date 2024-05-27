from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kiwi')
def kiwi():
    return render_template('animals/kiwi.html')

@app.route('/kea')
def kea():
    return render_template('animals/kea.html')

@app.route('/tuatara')
def tuatara():
    return render_template('animals/tuatara.html')

@app.route('/NZsealion')
def nzsealion():
    return render_template('animals/NZsealion.html')

if __name__ == '__main__':
    app.run(debug=True)