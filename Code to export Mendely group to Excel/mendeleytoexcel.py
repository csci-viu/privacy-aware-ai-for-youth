import requests
import pandas as pd
from flask import Flask, request, redirect, url_for
import threading

# Replace these with your actual client ID, client secret, and group ID
client_id = '18717'
client_secret = '7cjzcACcxedzdcZa'
redirect_uri = 'http://localhost:5000/callback'
group_id = 'f07c889d-80c4-3728-9559-0a426312769c'
access_token = None

app = Flask(__name__)


@app.route('/')
def home():
    auth_url = 'https://api.mendeley.com/oauth/authorize'
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': 'all'
    }
    # Redirect the user to the authorization URL
    return redirect(requests.Request('GET', auth_url, params=params).prepare().url)


@app.route('/callback')
def callback():
    global access_token
    authorization_code = request.args.get('code')
    access_token = get_access_token(client_id, client_secret, redirect_uri, authorization_code)

    # After obtaining the access token, fetch the documents and save to Excel
    papers = fetch_group_documents(access_token, group_id)
    if papers:
        save_to_excel(papers, 'mendeley_review.xlsx')
    else:
        print("No papers fetched.")

    # Shut down the server after processing
    threading.Thread(target=shutdown_server).start()
    return "Authorization complete and data saved to 'mendeley_review.xlsx'. You can now close this window."


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def get_access_token(client_id, client_secret, redirect_uri, authorization_code):
    token_url = 'https://api.mendeley.com/oauth/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'code': authorization_code
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status()  # Raise an error if the request failed
    return response.json()['access_token']


def fetch_group_documents(access_token, group_id):
    papers = []
    url = f'https://api.mendeley.com/documents?group_id={group_id}&limit=100'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/vnd.mendeley-document.1+json'
    }

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error if the request failed
        data = response.json()

        for item in data:
            title = item.get('title', 'N/A')
            authors = ', '.join(
                [f"{author.get('first_name', '')} {author.get('last_name', '')}".strip() for author in
                 item.get('authors', [])]
            ) if item.get('authors') else 'N/A'
            pub_year = item.get('year', 'N/A')
            journal = item.get('source', 'N/A')
            abstract = item.get('abstract', 'N/A')
            keywords = ', '.join(item.get('keywords', [])) if item.get('keywords') else 'N/A'
            url = ', '.join(item.get('websites', [])) if item.get('websites') else 'N/A'
            papers.append([title, authors, pub_year, journal, abstract, keywords, url])

        # Get next page of results if available
        url = response.links.get('next', {}).get('url')

    return papers


def save_to_excel(papers, filename):
    df = pd.DataFrame(papers, columns=['Title', 'Authors', 'Year', 'Journal/Conference', 'Abstract', 'Keywords', 'URL'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    import webbrowser

    # Open the authorization URL in the browser
    webbrowser.open('http://localhost:5000')
    # Start the Flask server in a separate thread
    threading.Thread(target=app.run, kwargs={'port': 5000}).start()
