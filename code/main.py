from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.mutualfundindia.com/MF/return/TopFunds?id=3').text
soup = BeautifulSoup(html_text,'lxml')
print(html_text)