from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Mark Dave Tenio \n BSIT-III-2nd 25 \n System Integration \n Semi-final Exam"

if __name__ == "__main__":
    port = int (os.environ.get("PORT",5000))
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=port)
