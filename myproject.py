import requests
import bs4

def MyScrap(site):

 try:
    res= requests.get(site)
 except Exception as e:
    print("ERROR, >>",e)
    exit()
 soup = bs4.BeautifulSoup(res.text, 'html.parser')
 for link in soup.find_all('a', href=True):
     print(link['href'])


if __name__ == "__main__":
    full_path='http://example.webscraping.com'
    #site = input("please enter the the HOSTNAME you want to scarp :")
    #path = input("please enter from where you want to start the scarping ")
    #full_path = site + path
    MyScrap(full_path)

