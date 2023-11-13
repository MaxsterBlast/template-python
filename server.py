from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

class CitationFormatter:
    def format_website_citation(self, title, authors, url, access_date):
        author_str = ", ".join(authors)
        citation = f"{author_str}. ({access_date}). {title}. Retrieved from {url}."
        return citation

    def get_website_info(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string
                author_tags = soup.find_all("meta", {"name": "author"})
                authors = [tag.get("content") for tag in author_tags]
                return title, authors
        except Exception as e:
            print("Error while fetching website information:", e)
        return None, []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website_url = request.form.get('website_urls')
        formatter = CitationFormatter()
        website_title, website_authors = formatter.get_website_info(website_url)

        if website_title:
            access_date = "November 9, 2023"  # Replace with the actual access date
            website_citation = formatter.format_website_citation(website_title, website_authors, website_url, access_date)
            return render_template('index.html', website_citation=website_citation)
        else:
            return render_template('index.html', error_message="Website information not found.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
