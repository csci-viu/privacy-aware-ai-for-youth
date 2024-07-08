#fetch papers from CrossRef
import requests
import pandas as pd
from datetime import datetime


# Function to fetch papers from CrossRef
def retrieve_papers(keyterms, paper_count, years_back=10):
    papers = []
    current_year = datetime.now().year
    year_threshold = current_year - years_back
    url = 'https://api.crossref.org/works'

    params = {
        'keyterms': keyterms,
        'filter': f'from-pub-date:{year_threshold}-01-01',
        'rows': paper_count,
        'sort': 'relevance'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['message']['items']:
            title = item.get('title', ['N/A'])[0]
            authors = ', '.join([author.get('given', '') + ' ' + author.get('family', '') for author in item.get('author', [])])
            pub_year = item.get('published-print', {}).get('date-parts', [[None]])[0][0]
            journal = item.get('container-title', ['N/A'])[0]
            abstract = item.get('abstract', 'N/A')
            keywords = ', '.join(item.get('subject', []))
            url = item.get('URL', 'N/A')
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers. HTTP Status code: {response.status_code}")

    return papers


# Function to save the fetched papers to an Excel file
def export_to_excel(papers, filename):
    df = pd.DataFrame(papers, columns=['Title', 'Authors', 'Year', 'Journal/Conference', 'Abstract', 'Keywords', 'URL'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Customize your search keyterms and number of papers to fetch
keyterms = "AI and digital natives"
paper_count = 100
filename = 'AIanddigitalnatives.xlsx'

# Fetch the papers
papers = retrieve_papers(keyterms, paper_count)
if papers:
    export_to_excel(papers, filename)
else:
    print("No papers fetched.")
