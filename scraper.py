import requests
from bs4 import BeautifulSoup
url="https://pypi.org/project/requests/"
content = requests.get(url)
html_content=content.content
print(html_content)