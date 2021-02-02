# importing the required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
pd.options.display.max_columns = 999


df = pd.read_csv('new_profile_links.csv')
df = df.drop(['Unnamed: 0'], axis = 1) 
df["0"]
pl = list(df["0"])
all_user = []


for i in range(100):
    try:
        one_user = []
        print("Loop :",i)
        url = pl[i]
        print(url)
        driver = webdriver.Chrome(r'C:\Users\USER\chromedriver_win32\chromedriver.exe')
        driver.get(url)
        time.sleep(3)

           # basic data extraction
        basic = []
        source_code = driver.page_source
        soup = BeautifulSoup(source_code, 'html.parser')

        name = soup.find_all('strong', class_ = 'userName--1ZA07')
        for n in name:
            basic.append(n.text)

        sp = soup.find_all('div', class_ = 'categoryName--1zWtA')
        category = soup.find_all('strong', class_ = 'introCategory--F81Ky')
        for e in category:
            basic.append(e.text)

        sp = soup.find_all('div', class_ = 'categoryName--1zWtA')    
        for m in sp:
            basic.append(m.text)

        rating = soup.find_all('div', class_ = 'itemRating--360UA itemRating--2-rFv typeLarge--1cEMN')
        for k in rating:
            a = k.text
            if "평균 평점" in a:
                a = a.replace("평균 평점", "")
            basic.append(a)


        #profile informations
        profile = []
        heading = soup.find_all('strong', class_ = 'introduceMainTitle--2MZc-')
        for h in heading:
            profile.append(h.text)

        text = soup.find_all('p', class_ = 'introduceText--2R5pY')
        for e in text:
            profile.append(e.text)
            
        #new section
        recom = soup.find_all('ul', class_ = 'listDisc--1Cc80')
        for rc in recom:
            profile.append(rc.text)
            

        rest = soup.find_all('div', class_ = ['profileCareer--3_uFh','isExpert--2GkDA'])     
#         for mm in rest:  
#             mm.find_all('div', class_ = 'profileBox--1jlog')
        for m in rest:
            m.find_all('div', class_ = "careerJob--2-hX4")
            for i in m:
                profile.append(i.text)
                

        ### Project data for one user
        maininfo = []
        infos = soup.find_all('ul', class_ = 'productInfoList--1-H-D')
        for f in infos:   
            li = f.find_all('li')
            for ll in li:
                uh = ["대표자","상호명","사업자등록번호","통신판매업번호-", "사업장 주소", "고객센터",'메일']
                for u in range(len(uh)):
                    if uh[u] in ll.text:
                        b = uh[u]
                        la = ll.text
                        maininfo.append(la.replace(b , ""))   



        #count product and review section
        products = []
        tt = soup.find_all('div', class_ = "list--e6w5E")
        for t in tt:  
            cc = t.find_all('div', class_='count--2w5o6')
            for cd in cc:
                cd.find_all('div', class_ = "count--2w5o6")
                ce = cd.text
                products.append(ce)


        ### Project data for one user
        projects = soup.find_all('div', class_ = 'listArea--peDdh')
        #projects  and consultations 
        all_project = []
        for y in projects:
            one = []
            yy = y.find_all('div', class_ = 'item--1ZJSx')
            for t in yy:
                project_item = []
                tdiv = t.find_all('div', class_ =['itemTitle--2vWBq','elip2--nFWXY'])
                for td in tdiv:
                    project_title = td.text
                    project_item.append(project_title)

                ratdiv = t.find_all('div', class_ =['itemGroup--2RnIL','ItemGroup_itemGroup--1f-on'])
                for rd in ratdiv:
                    ratscore = rd.find_all("div", class_ = "itemRating--360UA")
                    for r in ratscore:
                        b = r.text
                        if "평균 평점" in b:
                            b = b.replace("평균 평점", " ")
                            project_item.append(b)

                    ratreview = rd.find_all("div", class_ = "itemCount--2HsJv")
                    for rr in ratreview:
                        c = rr.text
                        if "후기" in c:
                            c = c.replace("후기", " ")
                            project_item.append(c)

                feediv = t.find_all('span', class_ =['priceInner--1HE2v'])
                for fd in feediv:
                    fee = fd.find_all("span", class_=["priceNum--1rXJI","ItemPrice_priceNum--2OFHI"])
                    for f in fee:
                        project_item.append(f.text)

                    discount = fd.find_all("em", class_="discountPercent--3n0bl")
                    for dis in discount:
                        project_item.append(dis.text)

                    actualPrize = fd.find_all("span", class_="beforeDiscount--W1C4G")
                    for fp in actualPrize:
                        project_item.append(fp.text)

                one.append([*project_item])   
            all_project.append([*one])

        proj = []
        for i in range(len(all_project)):
            data = all_project[i]
            for j in range(len(data)):
                dj = data[j]
                for k in range(len(dj)):
                    bb = dj[k]
                    proj.append(bb) 

        lis = ["평균 평점","후기","판매가","원할인률","할인 전 가격", "할인률"]
        for i in range(len(proj)):
            for j in range(len(lis)):
                if lis[j] in proj[i]:
                    proj[i] = proj[i].replace(lis[j], " ")



        rdiv = soup.find_all('div', class_ = "listSection--kViCl")
        reviews_user = []
        reviews_rating = []
        reviews_heading = []
        reviews_text = []

        for eachr in rdiv:
            ee = eachr.find_all('div', class_ = "reviewItem--1OwNO")
            for each in ee:
                name = each.find_all('span', class_ = ["item--3sQA9 ","nickname--2OOe6"])
                for nm in name:
                    reviews_user.append(nm.text)

                rating = each.find_all('div', class_ = ["expertPoint--2Zrvr","expertPoint--13H3V"])
                for r in rating:
                    b = r.text
                    if "평점" in b:
                        b = b.replace("평점", "")
                    reviews_rating.append(b)

                head = each.find_all('div', class_ = "reviewTitle--qv3Pk")
                for r in head:
                    reviews_heading.append(r.text)

                commentdiv = each.find_all('p', class_ = "reviewText--28mzN")
                for ecom in commentdiv:
                    reviews_text.append(ecom.text)


        review_obj = []
        for i in range(len(reviews_user)):
            review_obj.append(reviews_user[i])
            review_obj.append(reviews_heading[i])
            review_obj.append(reviews_rating[i])
            review_obj.append(reviews_text[i])
        #final works  
        all_user.append([url,*basic, *maininfo, *profile, *products, *review_obj ,*proj])    
        driver.quit()
    except :
        driver.quit()
        print("Error")
    

try:

    df = pd.DataFrame(all_user)
    main = []
    for index, row in df.iterrows():
        if row[3] in ['법률','노동/노무','지식재산/특허',"등기/공탁/법무",'민원/행정']:
            main.append("법률")

        elif row[3] in ['세금/세무','회계/감사','통관/관세','온라인 마케팅','온라인쇼핑몰','엑스퍼트 사업','경영/기술컨설팅','유통관리','가맹점창업','건축','번역/통역','날씨컨설팅','원가 분석']:
            main.append('비즈니스',)

        elif row[3] in ['자산컨설팅','부동산 상담','손해사정','신용상담','감정평가']:
            main.append("금융/재테크")

        elif row[3] in ['심리상담','영양/다이어트','MBTI ']:
            main.append("건강")

        elif row[3] in ['운세/사주','타로카드','작명','꿈해몽','관상','풍수']:
            main.append("운세")

        elif row[3] in ['펫 관리','연애','육아','명상','패션/스타일','뷰티','요리/홈쿠킹','커피/주류','인테리어','청소/세탁','교통사고 분석','자동차수리']:
            main.append("생활")

        elif row[3] in ['음악/악기','미술/디자인','공예/공방','무용/ 발레','사진','실용/방송댄스','뮤지컬/공연','낚시','원예/홈가드닝','여행','글쓰기/논술']:
            main.append("취미")


        elif row[3] in ['외국어학습','입시/진학','해외유학','대학교학습','고등학교학습','중학교학습','초등학교학습']:
            main.append( '교육/학습')

        elif row[3] in ['피트니스','골프','필라테스','요가','생활스포츠','자전거','수상 스포츠','동계 스포츠','유아체육']:
            main.append('운동/스포츠')

        elif row[3] in ['게임하우투','IT노하우','코딩','오피스문서','동영상 제작']:
            main.append('IT/컨텐츠')

        elif row[3] in ['라이프 코칭','취업','자기PR','공무원시험 ','자격증시험']:
            main.append('자기계발')

        else:
            main.append('네이버고객센터')

    df.insert(3, "main_category", main)
    df.to_csv("DATA.csv")

except:
    print("Error occured during data load to pd df")