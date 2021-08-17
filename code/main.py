from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.mutualfundindia.com/MF/return/TopFunds?id=3').text
soup = BeautifulSoup(html_text,'lxml')

#Category of the fund

aum = soup.find_all('td',style = "text-align:right; padding-right:30px;")
for i in aum:
    j = i.find_previous_sibling("td")
    print(j.text.replace(' ',''))
#aum

aum = soup.find_all('td',style = "text-align:right; padding-right:30px;")
for i in aum:
    print(i.text.replace(' ',''))


#Name of the fund
fund_link = soup.find_all('td')
for i in fund_link:
    fund_name = i.find('a')
    if(fund_name is not  None):
        print(fund_name.text)

# data of 1 week

one_week = soup.find_all('td',class_="css1Week")
for i in one_week :
    print(i.text)

# data of 1 month

one_month=soup.find_all('td',class_="css1Month")
for i in one_month:
    print(i.text)

# data of 3 months
three_month=soup.find_all('td',class_="css3Month")
for i in three_month:
    print(i.text)

# data of 6 months
six_month=soup.find_all('td',class_="css6Month")
for i in six_month:
    print(i.text)

# data of 1 year

one_year=soup.find_all('td',class_="css1Year")
for i in one_year:
    print(i.text)

# data of 5 years

five_year=soup.find_all('td',class_="css5Year")
for i in five_year:
    print(i.text)
