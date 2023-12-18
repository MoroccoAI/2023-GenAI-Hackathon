import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

file_path = 'urls.txt'

with open(file_path, 'rt') as file:
    for url in file:
        soup = get_soup(url.strip())
        spans = soup.find_all('span', style="color: #000000;")
        spans = [span.text.strip() for span in spans]

        output_file_path = 'nechfate_articles/' + url.split('/')[3] + '.txt'
        with open(output_file_path, 'w') as output_file:
            output_file.write('\n\n'.join(spans))
