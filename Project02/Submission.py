import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
base = "https://class101.net"
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999

options = webdriver.ChromeOptions()
options.add_argument("headless")

# ######################################
## Starting DATA scraping
# ######################################

al = pd.read_csv("testdf.csv")
al = al.drop(['Unnamed: 0'], axis = 1)
nlink = list(al["2"])

# importing the required modules
all_item = []
topitems = []
pro_item = []
topmain = []
topheading = []
toptext = []
pname = []
plink = []
ptext = []
urllink = []

for i in range(len(nlink)):
    url = nlink[i]
    item = []
    
    toprightheading = []
    toprighttext = []
    toprightmain = []
    
    textitem = []
    nameitem = []
    linkitem = []
    
    driver = webdriver.Chrome(r'C:\Users\David\chromedriver_win32\chromedriver.exe', chrome_options=options)
    top = [] 
    
    def getdata(url):
        try:
            print(url)
            driver.get(url)
            time.sleep(3)
            # Wait to load page
            source_code = driver.page_source
            soup = BeautifulSoup(source_code, 'html.parser')
            
        except:
            print("Driver error")
            return
            
        initial = soup.find_all("div", class_=['sc-dkiTmt', 'cQiUWe'])
        urllink.append(url)
        #top right div data
        for y in initial:
            ydiv = y.find_all("div", class_ = ["commonStyles__MobileBlockContianer-sc-6jqw77-0","gWtjdw"])
            for jj in ydiv:
                initialdiv = jj.find_all('div', class_ = ['ProductHeader__Header-az1cmu-0','leqDJG'])
                for p in initialdiv:              
                    top2 = p.find_all('div', class_ = ['sc-bdnylx','gGpzAi','ProductHeader__Tag-az1cmu-1','iOzkLq'])
                    for k in top2:
                        if k.text not in toprightmain:
                            tt = k.text 
                            tlist = tt.split("·")
                            for e in tlist:
                                if e == None or e == "":
                                    toprightmain.append(" ")
                                else:
                                    toprightmain.append(e)
                                                                
                    heading = p.find_all('h2', class_ = ['sc-bdnylx','cOMiUB','ProductHeader__Title-az1cmu-2','fkqBP'])
                    for j in heading:
                        if j.text not in toprightheading:
                            if j.text == None or j.text == "":
                                toprightheading.append(" ")
                            else:
                                toprightheading.append(j.text)
                            
                    rowdiv = p.find_all("div", class_ = ["SalesProductInfoTable__Container-sc-1uyx5v1-0","jrokem"])
                    for r in rowdiv:
                        recommend = r.find_all('div', class_=["SalesProductInfoTable__Row-sc-1uyx5v1-1", "gOzdaG"])
                    for r in recommend:
                        t2 = r.find_all('div', class_ = ['SalesProductInfoTable__ButtonContainer-sc-1uyx5v1-5','jOtFPR','SalesProductInfoTable__StyledExperiment-sc-1uyx5v1-4','diAwWT'])
                        for t in t2:
                            each = t.find_all('button', class_ = ["sc-ksluoS", "dyNqkJ" ,"sc-kfYqjs", "kpPRTM","SalesProductInfoTable__WishlistButton-sc-1uyx5v1-2", "fxUQsM"])
                            for e in each:                        
                                if e.text not in toprighttext:
                                    if e.text == None or e.text == "":
                                        toprighttext.append(" ")
                                    else:
                                        toprighttext.append(e.text)        
    
######################## profile section                            
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            ###########name item
            if new_height == last_height:
                try:
                    a = driver.find_element_by_xpath('//*[@id="product-view-creator"]/div/div[1]/div[1]/h3')
                    nameitem.append(a.text)
                except:
                    nameitem.append(" ")
                    
        ################text item
                try:
                    alltext = '//*[@id="product-view-creator"]/div/div[2]/div[4]'
                    b = driver.find_element_by_xpath(alltext)
                    textitem.append(b.text)
                except:
                    textitem.append(" ")
            
            #######Link item
                a1 = '//*[@id="product-view-creator"]/div/div[1]/div[1]/div/div[1]/span/a'
                a2 = '//*[@id="product-view-creator"]/div/div[1]/div[1]/div/div[2]/span/a'
                a3 = '//*[@id="product-view-creator"]/div/div[1]/div[1]/div/div[3]/span/a'
                    
                try:
                    alink1 = driver.find_element_by_xpath(a1)
                    val = alink1.get_attribute("href")
                    linkitem.append(val)
                except:
                    linkitem.append(" ")
                    
                try:
                    alink2 = driver.find_element_by_xpath(a2)
                    val = alink1.get_attribute("href")
                    linkitem.append(val)
                except:
                    linkitem.append(" ")
                
                try:
                    alink3 = driver.find_element_by_xpath(a3)
                    val = alink1.get_attribute("href")
                    linkitem.append(val)
                except:
                    linkitem.append(" ")
                
                driver.quit()
                break
            last_height = new_height
        return
   
    getdata(url) 
    ############################
    topmain.append(toprightmain)
    topheading.append(toprightheading)
    toptext.append(toprighttext)
    
    ############################
    pname.append(nameitem)
    plink.append(linkitem)
    ptext.append(textitem)
    
udf = pd.DataFrame(urllink)
t = pd.DataFrame(topmain)
t1 = pd.DataFrame(topheading)
t2 = pd.DataFrame(toptext)

p = pd.DataFrame(pname)
p1 = pd.DataFrame(plink)
p2 = pd.DataFrame(ptext)

frame = [udf,t,t1,t2]
rdf = pd.concat(frame, axis = 1)
pframe = [p,p1,p2]
pdf = pd.concat(pframe, axis = 1)

dff = [rdf, pdf]
df = pd.concat(dff, axis = 1)

col = []
for i in range(len(df.columns)):
    col.append(i)
df.columns = col

df = df.drop([3,4,5,6,7,8,9,10,13,14], axis = 1)
df.columns = ["Url", "Category", "Name","Title", "Recommend","Profile_Title", "Link1", "Link2", "Link3","Profile_Details"]

df.to_csv("Data.csv")