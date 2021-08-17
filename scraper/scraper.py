import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    # print(response.headers)

    html_text = response.text
    with open("file.html",'w') as file:
        file.write(html_text)
    
    soup = BeautifulSoup(html_text, 'html.parser')
    result = soup.findAll('a')
    return(len(result))

def get_citations_needed_report(url):
    domain = 'https://en.wikipedia.org/'
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    result = soup.find('div', class_="mw-parser-output")
    result_p = result.find('p')
    result_a = result_p.findAll('a')

    output=[]
    for i in result_a:
        output.append(domain + i.get('href'))
    return str(output)

if __name__ == '__main__':
    print(get_citations_needed_count(url = 'https://en.wikipedia.org/wiki/History_of_Mexico'))
    print(get_citations_needed_report(url = 'https://en.wikipedia.org/wiki/History_of_Mexico'))