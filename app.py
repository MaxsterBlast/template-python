from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('paper_uploaded')
def handle_paper_upload(data):
    # Here you can save the data to your computer
    # For demonstration, print the data
    print("Received paper data:", data)




if __name__ == '__main__':
    papers = load_data()
    app.run(port=5000)
