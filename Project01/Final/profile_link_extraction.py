# importing the required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

df = pd.read_csv('Intermediate_links.csv')
df = df.drop(['Unnamed: 0'], axis = 1) 
li = list(df["0"])
b_url = "https://m.kin.naver.com"
profile_links = []
item = []


def ps(url):
    driver.get(url)
    time.sleep(5)
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, 'html.parser')

    # how many times the loop will run
    span = soup.find_all('span', class_ = 'currentPage')
    for a in span:
        min = int(a.next.next.next)
        max = int(a.next.next.next.next.next.next.next.next)
        print("MIN :", min, "MAX :",max)

def start():
    a=[]
    print(driver.current_url)
    ss = driver.page_source
    sou = BeautifulSoup(ss, 'html.parser') 
    content = sou.find_all('div', class_="content--jBp3G")
    for ii in content:
        aa = ii.find_all('div', class_= ["itemCard--2Whvq","ItemSmallThumbnail_itemCard--cIT1M"])
        for j in aa:
            aaa = j.find_all('div', class_= ["itemLink--2ljnw"])
            for ki in aaa:
                lk = ki.find_all('a', class_= ["profileLink--16bta"])
                for o in lk:
                    a.append(b_url+str(o.attrs['href']))
                    

    for li in a:
        if li not in profile_links:
            profile_links.append(li)

    click()
    print("start")
    
    
def click():
    
    script = 'document.querySelector("#app > div > div > div.content--jBp3G > div.expertNextPage > a.pageLink.linkNext > span").click()'
#     path = u"//a[@class='pageLink linkNext']"
#     driver.find_element_by_css_selector(path).click()

    driver.execute_script(script)
    
    time.sleep(3)
    start()
    print("click")  #app > div > div > div.content--jBp3G > div.expertNextPage > a.pageLink.linkNext > span
    
for i in range(len(li)):
    try:
        print("Serial:", i)
        min = 0
        max = 0 
        # program running here # program running here 
        # program running here # program running here 
        driver = webdriver.Chrome(r'C:\Users\USER\chromedriver_win32\chromedriver.exe')
        url = "https://"+li[i]
        plinks = []
        ps(url)    
        try:
            start()
        except:
            driver.quit()
            continue
        driver.quit()
    except:
        print("ERROR")
        
profiles = pd.DataFrame(profile_links)
profiles.to_csv("../Data/profile_links.csv")
def ps(url):
    driver.get(url)
    time.sleep(5)
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, 'html.parser')

    # how many times the loop will run
    span = soup.find_all('span', class_ = 'currentPage')
    for a in span:
        min = int(a.next.next.next)
        max = int(a.next.next.next.next.next.next.next.next)
        print("MIN :", min, "MAX :",max)

def start():
    a=[]
    print(driver.current_url)
    ss = driver.page_source
    sou = BeautifulSoup(ss, 'html.parser') 
    content = sou.find_all('div', class_="content--jBp3G")
    for ii in content:
        aa = ii.find_all('div', class_= ["itemCard--2Whvq","ItemSmallThumbnail_itemCard--cIT1M"])
        for j in aa:
            aaa = j.find_all('div', class_= ["itemLink--2ljnw"])
            for ki in aaa:
                lk = ki.find_all('a', class_= ["profileLink--16bta"])
                for o in lk:
                    a.append(b_url+str(o.attrs['href']))
                    

    for li in a:
        if li not in profile_links:
            profile_links.append(li)

    click()
    print("start")
    
    
def click():
    
    script = 'document.querySelector("#app > div > div > div.content--jBp3G > div.expertNextPage > a.pageLink.linkNext > span").click()'
#     path = u"//a[@class='pageLink linkNext']"
#     driver.find_element_by_css_selector(path).click()

    driver.execute_script(script)
    
    time.sleep(3)
    start()
    print("click")  #app > div > div > div.content--jBp3G > div.expertNextPage > a.pageLink.linkNext > span
    
for i in range(len(li)):
    try:
        print("Serial:", i)
        min = 0
        max = 0 
        # program running here # program running here 
        # program running here # program running here 
        driver = webdriver.Chrome(r'C:\Users\USER\chromedriver_win32\chromedriver.exe')
        url = "https://"+li[i]
        plinks = []
        ps(url)    
        try:
            start()
        except:
            driver.quit()
            continue
        driver.quit()
    except:
        print("ERROR")

try:
    profiles = pd.DataFrame(profile_links) 
    profiles.to_csv("new_profile_links.csv")

    old = pd.read_csv('old_profile_links.csv')
    old = old.drop(['Unnamed: 0'], axis = 1) 
    #use profile_link_extraction.py to generate new_profile_links
    new = pd.read_csv('new_profile_links.csv')
    new = new.drop(['Unnamed: 0'], axis = 1) 


    oldlinks = []
    for k in range(len(old)):
        oldlinks.append(old["0"][k])

    update = []
    for i in range(len(new)):
        if new["0"][i] not in oldlinks:
            update.append(new["0"][i])


    updated_profile_links = pd.DataFrame(update)
    updated_profile_links.to_csv("updated_profile_links.csv")
    
except:
    print("Error during working with df")
    
