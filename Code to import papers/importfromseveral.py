import requests
import pandas as pd
from datetime import datetime


# Function to fetch papers from ScienceDirect
def fetch_sciencedirect(query, num_papers, years_back=10):
    papers = []
    # Replace with actual ScienceDirect API endpoint and parameters
    url = 'https://api.elsevier.com/content/search/sciencedirect'
    api_key = 'SCIENCEDIRECT_API_KEY'  #Replace with you api key
    headers = {
        'Accept': 'application/json',
        'X-ELS-APIKey': api_key
    }
    params = {
        'query': query,
        'count': num_papers,
        'date': f'after {datetime.now().year - years_back}'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['search-results']['entry']:
            title = item.get('dc:title', 'N/A')
            authors = ', '.join([author['$'] for author in item.get('authors', {}).get('author', [])])
            pub_year = item.get('prism:coverDate', 'N/A').split('-')[0]
            journal = item.get('prism:publicationName', 'N/A')
            abstract = item.get('dc:description', 'N/A')
            keywords = 'N/A'  # ScienceDirect API may not provide keywords directly
            url = item.get('link', [{'@href': 'N/A'}])[0]['@href']
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers from ScienceDirect. HTTP Status code: {response.status_code}")
    return papers


# Function to fetch papers from Springer
def fetch_springer(query, num_papers, years_back=10):
    papers = []
    url = 'http://api.springernature.com/meta/v2/json'
    api_key = 'YOUR_SPRINGER_API_KEY'                 #Replace with you api key
    params = {
        'q': query,
        'api_key': api_key,
        's': 1,
        'p': num_papers,
        'date-facet-mode': 'between',
        'date-facet-value': f'{datetime.now().year - years_back}-01-01'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['records']:
            title = item.get('title', 'N/A')
            authors = ', '.join([author['creator'] for author in item.get('creators', [])])
            pub_year = item.get('publicationDate', 'N/A').split('-')[0]
            journal = item.get('publicationName', 'N/A')
            abstract = item.get('abstract', 'N/A')
            keywords = 'N/A'  # Springer API may not provide keywords directly
            url = item.get('url', 'N/A')
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers from Springer. HTTP Status code: {response.status_code}")
    return papers


# Function to fetch papers from IEEE Xplore
def fetch_ieee(query, num_papers, years_back=10):
    papers = []
    url = 'https://ieeexploreapi.ieee.org/api/v1/search/articles'
    api_key = 'YOUR_IEEE_API_KEY'                  #Replace with you api key
    params = {
        'querytext': query,
        'max_records': num_papers,
        'start_year': datetime.now().year - years_back,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['articles']:
            title = item.get('title', 'N/A')
            authors = ', '.join(item.get('authors', 'N/A'))
            pub_year = item.get('publication_year', 'N/A')
            journal = item.get('publication_title', 'N/A')
            abstract = item.get('abstract', 'N/A')
            keywords = ', '.join(item.get('index_terms', {}).get('ieee_terms', {}).get('terms', []))
            url = item.get('pdf_url', 'N/A')
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers from IEEE Xplore. HTTP Status code: {response.status_code}")
    return papers


# Function to fetch papers from ACM Digital Library
def fetch_acm(query, num_papers, years_back=10):
    papers = []
    url = 'https://dl.acm.org/action/doSearch'
    headers = {
        'Accept': 'application/json',
    }
    params = {
        'AllField': query,
        'startYear': datetime.now().year - years_back,
        'pageSize': num_papers
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            title = item.get('title', 'N/A')
            authors = ', '.join([author['name'] for author in item.get('authors', [])])
            pub_year = item.get('publicationDate', 'N/A').split('-')[0]
            journal = item.get('source', 'N/A')
            abstract = item.get('abstract', 'N/A')
            keywords = ', '.join(item.get('keywords', []))
            url = item.get('url', 'N/A')
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers from ACM Digital Library. HTTP Status code: {response.status_code}")
    return papers


# Function to fetch papers from Scopus
def fetch_scopus(query, num_papers, years_back=10):
    papers = []
    url = 'https://api.elsevier.com/content/search/scopus'
    api_key = 'YOUR_SCOPUS_API_KEY'              #Replace with you api key
    headers = {
        'Accept': 'application/json',
        'X-ELS-APIKey': api_key
    }
    params = {
        'query': query,
        'count': num_papers,
        'date': f'after {datetime.now().year - years_back}'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['search-results']['entry']:
            title = item.get('dc:title', 'N/A')
            authors = ', '.join([author['$'] for author in item.get('author', [])])
            pub_year = item.get('prism:coverDate', 'N/A').split('-')[0]
            journal = item.get('prism:publicationName', 'N/A')
            abstract = item.get('dc:description', 'N/A')
            keywords = 'N/A'  # Scopus API may not provide keywords directly
            url = item.get('link', [{'@href': 'N/A'}])[0]['@href']
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])
    else:
        print(f"Failed to fetch papers from Scopus. HTTP Status code: {response.status_code}")
    return papers


# Function to save the fetched papers to an Excel file
def save_to_excel(papers, filename):
    df = pd.DataFrame(papers, columns=['Title', 'Authors', 'Year', 'Journal/Conference', 'Abstract', 'Keywords', 'URL'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Customize your search query and number of papers to fetch
query = "machine learning"
num_papers = 10
filename = 'literature_review.xlsx'

# Fetch papers from different databases
papers_sciencedirect = fetch_sciencedirect(query, num_papers)
papers_springer = fetch_springer(query, num_papers)
papers_ieee = fetch_ieee(query, num_papers)
papers_acm = fetch_acm(query, num_papers)
papers_scopus = fetch_scopus(query, num_papers)

# Combine all papers
all_papers = papers_sciencedirect + papers_springer + papers_ieee + papers_acm + papers_scopus

# Save the combined papers to an Excel file
if all_papers:
    save_to_excel(all_papers, filename)
else:
    print("No papers fetched.")
