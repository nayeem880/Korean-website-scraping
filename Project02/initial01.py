# importing the required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
base = "https://class101.net"
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999

urls = pd.read_csv('parent_links.csv')
urls = urls.drop(['Unnamed: 0'], axis = 1) 

b = list(urls['0'])
b = b[:5]
a = []

all_links = []
l_links = []


for i in range(len(b)):
    url = b[i]
    print(url)
    
    ##########defininf function
    def scroll(url):
        count = 0
        driver = webdriver.Chrome(r'C:\Users\USER\chromedriver_win32\chromedriver.exe')
        scroll_pause_time = 5
        driver.get(url)
        time.sleep(3)
        source_code = driver.page_source
        soup = BeautifulSoup(source_code, 'html.parser')
        
            ######################################### basic section
        # top 10
        iii = []
        bb = []
        outsidenav = soup.find_all("div", class_=['SectionWithOutSideNavigationCarousel__Content-laj44i-0', 'cTNIGb'])
        for do in outsidenav:
            d = do.find_all('div', class_ =["OutSideNavigationCarousel2__Content-lxp9vi-0","fhZyLW"])
            for i in d:
                ii = i.find_all('a', ["ProductCardfragment__HoverStyledLink-jvv2ql-0", "lmeJlb"])
                for ai in ii:
                    if base+ai.attrs['href'] not in bb:
                        if count < 10 and url == "https://class101.net/creative":
                            bb.append(["creative","Top10", base+ai.attrs['href']])
                        elif count >= 10 and url == "https://class101.net/creative":
                            bb.append(["creative","New" ,base+ai.attrs['href']])
                        elif count < 10 and url == "https://class101.net/money":
                            bb.append(["money","Top10", base+ai.attrs['href']])
                        elif count >= 10 and url == "https://class101.net/money":
                            bb.append(["money","New" ,base+ai.attrs['href']])

                        elif count < 10 and url == "https://class101.net/career":
                            bb.append(["career","Top10", base+ai.attrs['href']])
                        elif count >= 10 and url == "https://class101.net/career":
                            bb.append(["career","New" ,base+ai.attrs['href']])

                        elif count < 10 and url == "https://class101.net/kids":
                            bb.append(["kids","Top10" ,base+ai.attrs['href']])
                        elif count >= 10 and url == "https://class101.net/kids":
                            bb.append(["kids","New" ,base+ai.attrs['href']])

                        elif count < 10 and url == "https://class101.net/signature":
                            bb.append(["signature","Top10", base+ai.attrs['href']])
                        elif count >= 10 and url == "https://class101.net/signature":
                            bb.append(["signature","New" ,base+ai.attrs['href']])
                    count+=1
        a.append(bb)
        
        
        #######################################################
        #######################################################
        href = []
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
    
            # Wait to load page

            source_code = driver.page_source
            soup = BeautifulSoup(source_code, 'html.parser')
            infinitediv = soup.find_all("div", class_=['SectionWithInfiniteScrollGridList__Content-sc-1b8v326-0', 'exzfmE'])
            infItems = []

            for y in infinitediv:
                infItems.append(y.find_all('a', class_ = ['ProductCardWithLastUpdatedInformationfragment__HoverStyledLink-sc-146ouht-0', 'hVwDSX']))

            for yy in infItems:
                for yyy in yy:
                    if len(href) < 100:
                        if base+yyy.attrs['href'] not in href:
                            if url == "https://class101.net/creative":   
                                href.append(["creative",base+yyy.attrs['href']])
                            elif url == "https://class101.net/money":   
                                href.append(["money",base+yyy.attrs['href']])
                            elif url == "https://class101.net/career":   
                                href.append(["career",base+yyy.attrs['href']])
                            elif url == "https://class101.net/kids":   
                                href.append(["kids",base+yyy.attrs['href']])
                            elif url == "https://class101.net/signature":   
                                href.append(["signature",base+yyy.attrs['href']])
                            

            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            if (len(href) > 100) or (new_height == last_height):
                driver.quit()
                break
            last_height = new_height  
        all_links.append(href)
        return
    
    #####whole function
    scroll(url)

    
final_links = []
for i in all_links:
    for j in i:
        final_links.append(j) 
linkdf = pd.DataFrame(final_links)
linkdf.to_csv("alllinks.csv")

    
linkdf.insert(1, "sub-category", " ") 
linkdf.columns = ["0","1","2"]
frame = [n, linkdf]
test = pd.concat(frame, axis = 0, join="outer",ignore_index=True)

test.to_csv("testdf.csv")