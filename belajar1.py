from flask import Flask

app = Flask(__name__)

@app.route("/")
# ini itu URL nya, karna kita nge-set dia "/", maka ini tu home page nya (PATH nya masih di homepage)
def hello_world():
    return 'hello semua nya'

"""
untuk run code flask kita, kita menggunakan code :

flask --app (nama file) run

"""

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)

