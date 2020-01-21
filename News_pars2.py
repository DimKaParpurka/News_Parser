from bs4 import BeautifulSoup
import requests
from datetime import time
from datetime import datetime
import datetime
import time

headers = {'accept':'*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
  
url = 'https://www.seattletimes.com/nation-world/nation-politics/'

find_words = ['Democratic','Republican']


def check_list(text):
    for stop_word in find_words:
        if stop_word in text:
            return True
        else:
            pass
    return False


def news_pars(url, headers):
    article=[]
    session = requests.Session()
    request = session.get(url, headers=headers)
    start_time = datetime.datetime.now() - datetime.timedelta(hours=14)
    now = datetime.datetime.now().hour
    if (now != 19):       
        now = datetime.datetime.now().hour
        soup = BeautifulSoup(request.content, 'lxml')    
        div = soup.find_all('article', attrs={'class': 'results-story'})
        for divs in div:
            art_date = datetime.datetime.strptime(divs.find('time').text,'%B %d, %Y at %I:%M %p')
            if (art_date > start_time):
                #print(art_date,' ',now)
                title = divs.find('h3').text 
                art = divs.find('p').text
                text1 =  title + ' ' + art
                if check_list(text1):     
                    print(art_date, '\n',title, '\n' ,art,'\n')
                    if check_list(art):
                        article.append({
                            'date' : art_date,
                            'text' : art })
                        #print(article)
        time.sleep(3*60)
news_pars(url, headers)  