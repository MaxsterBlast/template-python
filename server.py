from flask import Flask, render_template, request
from citation_formatter import CitationFormatter

app = Flask(__name__)
formatter = CitationFormatter()

@app.route('/', methods=['GET', 'POST'])
def index():
    citation = None
    if request.method == 'POST':
        website_url = request.form['website_url']
        website_title, website_authors = formatter.get_website_info(website_url)

        if website_title:
            access_date = "November 9, 2023"  # Replace with the actual access date
            citation = formatter.format_website_citation(website_title, website_authors, website_url, access_date)

    return render_template('index.html', citation=citation)

if __name__ == '__main__':
    app.run(debug=True)
