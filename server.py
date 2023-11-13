import requests
from bs4 import BeautifulSoup
from dateutil import parser
from flask import Flask, request, render_template

app = Flask(__name__)

class CitationFormatter:
    def format_website_citation(self, title, authors, url, access_date, publication_date):
        author_str = ", ".join(authors)
        citation = f"{author_str}."
        
        if publication_date:
            citation += f" ({publication_date.strftime('%B %d, %Y')})."
        
        citation += f" {title}. Retrieved from {url}. Accessed on {access_date}."
        
        return citation

    def get_website_info(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract information from the website
                title = soup.title.string
                author_tags = soup.find_all("meta", {"name": "author"})
                authors = [tag.get("content") for tag in author_tags]

                # Extract the publication date
                date_tags = soup.find_all("meta", {"name": "pubdate"})
                publication_date = None
                if date_tags:
                    publication_date = date_tags[0].get("content")
                else:
                    date_element = soup.find("time")
                    if date_element:
                        publication_date = date_element.text.strip()

                # Parse the publication date using dateutil.parser
                parsed_date = None
                if publication_date:
                    try:
                        parsed_date = parser.parse(publication_date)
                    except ValueError:
                        print("Error parsing publication date")

                return title, authors, parsed_date
        except Exception as e:
            print("Error while fetching website information:", e)
        return None, [], None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website_urls_input = request.form.get('website_urls')
        access_date = request.form.get('access_date')
        
        if website_urls_input:
            website_urls = website_urls_input.split('\n')
            formatter = CitationFormatter()
            citations = []

            for website_url in website_urls:
                website_url = website_url.strip()
                if website_url:
                    website_title, website_authors, publication_date = formatter.get_website_info(website_url)

                    if website_title:
                        if not access_date:
                            access_date = "November 9, 2023"  # Default access date if not provided
                            
                        website_citation = formatter.format_website_citation(website_title, website_authors, website_url, access_date, publication_date)
                        citations.append(website_citation)
                    else:
                        citations.append(f"Error: Website information not found for {website_url}")

            return render_template('index.html', citations=citations)
    
    return render_template('index.html', citations=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
