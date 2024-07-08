#scrape paper from google scholar
from scholarly import scholarly
import pandas as pd
from datetime import datetime


def retrieve_papers(keyterms, paper_count, years_back=10):
    search_keyterms = scholarly.search_pubs(keyterms)
    papers = []
    current_year = datetime.now().year
    year_threshold = current_year - years_back

    for _ in range(paper_count):
        try:
            paper = next(search_keyterms)
            pub_year = paper.get('bib', {}).get('pub_year', 'N/A')
            # Check if pub_year is a number and within the desired range
            if pub_year.isdigit() and int(pub_year) >= year_threshold:
                papers.append([
                    paper.get('bib', {}).get('title', 'N/A'), ', '.join(paper.get('bib', {}).get('author', 'N/A')),
                    pub_year, paper.get('bib', {}).get('venue', 'N/A'), paper.get('bib', {}).get('abstract', 'N/A'),
                    ', '.join(paper.get('bib', {}).get('keywords', 'N/A')), paper.get('pub_url', 'N/A')
                ])
        except StopIteration:
            print(f"Only {_} papers found for keyterms '{keyterms}'.")
            break

    return papers


def export_to_excel(papers, filename):
    df = pd.DataFrame(papers, columns=['Title', 'Authors', 'Year', 'Journal/Conference', 'Abstract', 'Keywords', 'URL'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Customize your search keyterms and number of papers to fetch
keyterms = "Data sharing concerns in AI"
paper_count = 500
filename = 'DataSharingConcernsinAI.xlsx'

papers = retrieve_papers(keyterms, paper_count)
export_to_excel(papers, filename)
