import json
import requests
from bs4 import BeautifulSoup

response = requests.get('https://gov.ro/en/news')
soup = BeautifulSoup(response.text, 'html.parser')
h2s = soup.find_all('h2', {'class': 'w425 left nofloat'})
links = [h2.find('a').get('href') for h2 in h2s]
nextPages = [page.find('a').get('href') for page in soup.find("ul", {'id': "pagination"}).find_all('li') if
             page.find('a') is not None]
response = requests.get(nextPages[0])
soup = BeautifulSoup(response.text, 'html.parser')
sixthEntryLink = soup.find('h2', {'class': 'w425 left nofloat'}).find('a').get('href')
links.append(sixthEntryLink)
output = [
    {
        'title': soup.find('h2').text if soup.find('h2') else 'Not found',
        'date': div.find('span').text if (div := soup.find('div', {'class': 'imgTitle'})) and (
            div.find('span')) else 'Not found',
        'text': soup.find('div', {'class': 'pageDescription'}).text if
        soup.find('div', {'class': 'pageDescription'}) else 'Not found'
    }
    for link in links
    if (response := requests.get(link)).ok and (soup := BeautifulSoup(response.text, 'html.parser'))
]
with open('output.json', "w") as json_file:
    json.dump(output, json_file, indent=4)
