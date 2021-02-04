# importing the required modules
# importing the required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")
base = "https://class101.net"


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
        driver = webdriver.Chrome(r'C:\Users\David\chromedriver_win32\chromedriver.exe', chrome_options=options)
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

ne = []
for i in a:
    for j in i:
        ne.append(j)
n = pd.DataFrame(ne)

n.columns = ["0","1","2"]

final_links = []
for i in all_links:
    for j in i:
        final_links.append(j) 
        
linkdf = pd.DataFrame(final_links)  
linkdf.insert(1, "sub-category", " ") 
linkdf.columns = ["0","1","2"]
linkdf.to_csv("alllinks.csv")

frame = [n, linkdf]
test = pd.concat(frame, axis = 0, join="outer",ignore_index=True)
test.to_csv("testdf.csv")

######################################
######################################
######################################

al = pd.read_csv("testdf.csv")
al = al.drop(['Unnamed: 0'], axis = 1)
nlink = list(al["2"])

all_item = []
for i in range(len(nlink)):
    url = nlink[i]
    item = []
    driver = webdriver.Chrome(r'C:\Users\David\chromedriver_win32\chromedriver.exe', chrome_options=options)
    
    def getdata(url):
        print(url)
        driver.get(url)
        time.sleep(2)

        # Wait to load page
        print('while...')

        source_code = driver.page_source
        soup = BeautifulSoup(source_code, 'html.parser')

        initial = soup.find_all("div", class_=['sc-dkiTmt', 'cQiUWe'])
        for y in initial:
            initialdiv = y.find_all('div', class_ = ['ProductHeader__Header-az1cmu-0 leqDJG','AffixProductHeader__StyledProductHeader-sc-1l73jdk-1','idfLTb'])
            for p in initialdiv:              
                top2 = p.find_all('div', class_ = ['sc-bdnylx','gGpzAi','ProductHeader__Tag-az1cmu-1','iOzkLq'])
                for k in top2:
                    if k.text not in item:
                        item.append(k.text)

                heading = p.find_all('h2', class_ = ['sc-bdnylx','cOMiUB','ProductHeader__Title-az1cmu-2','fkqBP'])
                for j in heading:
                    if j.text not in item:
                        item.append(j.text)

                recommend = p.find_all('div', class_="SalesProductInfoTable__Row-sc-1uyx5v1-1 gOzdaG")
                for r in recommend:
                    t2 = r.find_all('div', class_ = ['SalesProductInfoTable__ButtonContainer-sc-1uyx5v1-5','jOtFPR','SalesProductInfoTable__StyledExperiment-sc-1uyx5v1-4','diAwWT'])
                    for t in t2:
                        each = t.find_all('button', class_ = ["sc-ksluoS", "dyNqkJ" ,"sc-kfYqjs", "kpPRTM","SalesProductInfoTable__WishlistButton-sc-1uyx5v1-2", "fxUQsM"])
                        for e in each:
                            if e.text not in item:
                                item.append(e.text)                               
        
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            source_code = driver.page_source
            soup = BeautifulSoup(source_code, 'html.parser')
            
            ########left section
            initial = soup.find_all("div", class_=['sc-dkiTmt', 'cQiUWe'])
            for y in initial:
                left = y.find_all('div', class_ = ['sc-eiQXzm','cSojtf', 'commonStyles__StaticPositionedColumn-sc-6jqw77-1', 'bvouQZ'])
                for l in left:
                    pro = l.find_all('div', class_ = ['commonStyled__ContentArea-sc-17rimc7-0','ACCCm'])
                    for pr in pro:
                        p = pr.find_all('div', class_ = ['sc-dkiTmt','cQiUWe'])

                        #pro heading section
                        for i in p:
                            pi = i.find_all('div', class_ = ['CreatorIntroSection__Title-sc-18c4e1x-0','bdBflQ'])
                            for p in pi:
                                #name section
                                pname = p.find_all('div', class_ = ['sc-bdnylx','jckokO',  'ContentSectionStyle__SectionTitle-sc-1oywcqb-1', "CreatorIntroSection__WordBrokenSectionTitle-sc-18c4e1x-1","iJQLEl" ,"bSBRTB"])
                                for pn in pname:
                                    if pn not in item:
                                        item.append(pn)

                                #link section
                                plink = p.find_all('div', class_ = ['ChannelButtonGroup__Container-sc-1yqg9fu-0','zUbfY'])
                                for pl in plink:
                                    pm = pl.find_all('a', class_ = ['sc-hcmsuR','ARwUf','sc-dlnjPT','sc-fFSRdu','cuIYFB','goHICw'])
                                    for a in pm:
                                        if a.attrs['href'] not in item:
                                            item.append(a.attrs['href'])
                        
                    #pro info section
                    for j in l:  
                        pp = j.find_all('div', class_ = ['ContentSectionStyle__SectionBodyColumn-sc-1oywcqb-3','cNvNAk'])
                        for jj in pp:
                            mm = jj.find_all('div', class_ = ['FoldableContent__Container-eh1nn2-0','lmAXPf'])
                            for j in mm:
                                nn = j.find_all('div', class_ = ['FoldableContent__ViewContainer-eh1nn2-1','jPwmCe'])
                                for jj in nn:
                                    i = jj.find_all('div', class_ = ['FoldableContent__InnerContainer-eh1nn2-2','ionrXH'])
                                    for pp in i:
                                        co = pp.find_all('div', class_ = ['SanitizeHtml__SanitizeHtmlContainer-ldtmln-0','gNRtXt'])
                                        for c in co:
                                            coo = c.find_all('ul')
                                            for nm in coo:
                                                if nm.text not in item:
                                                    item.append(nm.text)

            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                driver.quit()
                break
            last_height = new_height
        return
    getdata(url)
    all_item.append(item)
dd = pd.DataFrame(all_item)

frames = [test, dd]
data = pd.concat(frames, axis = 1)
data.to_csv("DATA.csv")