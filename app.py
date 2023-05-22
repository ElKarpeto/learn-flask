from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
# ini itu URL nya, karna kita nge-set dia "/", maka ini tu home page nya (PATH nya masih di homepage)
def index():
    return render_template('index.html')

"""
untuk run code flask kita, kita menggunakan code :

flask --app (nama file) run

"""

if __name__ == '__main__' :
    app.run(debug=True)
