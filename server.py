from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
papers = []

# Define a mapping of difficulty levels to values for sorting
difficulty_mapping = {'Hard': 3, 'Moderate': 2, 'Easy': 1}

def save_data():
    with open('data.json', 'w') as f:
        json.dump(papers, f)

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    sorted_by_date = sorted(papers, key=lambda x: x['due_date'])
    sorted_by_difficulty = sorted(papers, key=lambda x: difficulty_mapping[x['difficulty']], reverse=True)

    return render_template('index.html', papers=sorted_by_date, papers_by_difficulty=sorted_by_difficulty)

@app.route('/submit', methods=['POST'])
def submit():
    paper = {
        'subject': request.form['subject'],
        'due_date': request.form['due_date'],
        'style': request.form['style'],
        'difficulty': request.form['difficulty'],
        'completed': False
    }
    papers.append(paper)
    save_data()
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    papers.pop(index)
    save_data()
    return redirect('/')

if __name__ == '__main__':
    papers = load_data()
    app.run(port=5000)
