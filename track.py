import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.in/dp/B09CG2P4Z2/?coliid=I38ZYXVJC2GBDI&colid=2OZCJT71QSEXL&ref_=lv_ov_lig_dp_it&th=1'
page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"})

print(page.status_code)
# print(page.text)
soup = BeautifulSoup(page.content,'html.parser')
price = soup.find('span', attrs={'class':'a-price-whole'}).get_text()
dec = soup.find('span', attrs={'class':'a-price-decimal'}).get_text()
print(price,dec)