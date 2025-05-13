import click
import requests



QUOTE_URL = 'https://quotes.rest/qod?category=inspire'
REQUEST_HEADERS = {'content-type': 'application/json'}
	   
@click.command()
def inspire():
    """Returns an inspirational quote."""
    response = requests.get(QUOTE_URL, headers=REQUEST_HEADERS)
    quote = response.json()['contents']['quotes'][0]

    quote_text = quote['quote']
    author = quote['author']

    print(quote_text)
    print(f"    - {author}")