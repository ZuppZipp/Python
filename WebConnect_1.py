from flask import Flask

app = Flask(__name__)

@app.route('/first')

def anything():
    return "Sucessfull web Connection"

if __name__ =="__main__":
    app.run(port=5002)
