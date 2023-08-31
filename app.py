from flask import Flask, request

app = Flask(__name__)

@app.route('/upload-paper', methods=['POST'])
def upload_paper():
    paper_data = request.form
    # Process the paper data and save it to a text file
    with open('received_data.txt', 'a') as f:
        f.write(str(paper_data) + '\n')
    return 'Data received and processed successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



if __name__ == '__main__':
    papers = load_data()
    app.run(port=5000)
