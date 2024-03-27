from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
import time
from urllib.parse import urlparse
from tkinter import messagebox

# messagebox.showinfo("Information", "食べログの仕様上一度に1200件までしか表示・収集できません。")
# exit(0)

url = "https://employment.en-japan.com/desc_eng_8039311/?aroute=17&arearoute=1&fromSearch=1"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
url_ = soup.find(id='recruitFrame')['src']
response = requests.get(url_)
soup = BeautifulSoup(response.content, 'html.parser')
try:
    en_HP_url_ = soup.find(lambda tag: tag.name == "th" and "企業ホームページ" in tag.text).find_next().text
except:
    en_HP_url_ = soup.find(lambda tag: tag.name == "th" and "事業内容" in tag.text).find_next().text
en_HP_url_ = en_HP_url_.replace('\n', '')
print(en_HP_url_)
# driver = webdriver.Chrome()
# driver.get("https://syukatsu-kaigi.jp/companies/search?company_form%5Bcompany_name%5D=&company_form%5Bexists_content%5D=not_specified&company_form%5Bindustry_middle_id%5D%5B%5D=1&company_form%5Bindustry_middle_id%5D%5B%5D=2&company_form%5Bindustry_middle_id%5D%5B%5D=3&company_form%5Bindustry_middle_id%5D%5B%5D=4&company_form%5Bindustry_middle_id%5D%5B%5D=5&company_form%5Bindustry_middle_id%5D%5B%5D=6&company_form%5Bindustry_middle_id%5D%5B%5D=7&company_form%5Bindustry_middle_id%5D%5B%5D=8&company_form%5Bindustry_middle_id%5D%5B%5D=9&company_form%5Bindustry_middle_id%5D%5B%5D=10&company_form%5Bindustry_middle_id%5D%5B%5D=11&company_form%5Bindustry_middle_id%5D%5B%5D=12&company_form%5Bindustry_middle_id%5D%5B%5D=13&company_form%5Bindustry_middle_id%5D%5B%5D=14&company_form%5Bindustry_middle_id%5D%5B%5D=15&company_form%5Bindustry_middle_id%5D%5B%5D=16&company_form%5Bindustry_middle_id%5D%5B%5D=17&company_form%5Bindustry_middle_id%5D%5B%5D=18&company_form%5Bindustry_middle_id%5D%5B%5D=34&company_form%5Bindustry_middle_id%5D%5B%5D=19&company_form%5Bindustry_middle_id%5D%5B%5D=20&company_form%5Bindustry_middle_id%5D%5B%5D=21&company_form%5Bindustry_middle_id%5D%5B%5D=22&company_form%5Bindustry_middle_id%5D%5B%5D=23&company_form%5Bindustry_middle_id%5D%5B%5D=24&company_form%5Bindustry_middle_id%5D%5B%5D=25&company_form%5Bindustry_middle_id%5D%5B%5D=26&company_form%5Bindustry_middle_id%5D%5B%5D=27&company_form%5Bindustry_middle_id%5D%5B%5D=28&company_form%5Bindustry_middle_id%5D%5B%5D=29&company_form%5Bindustry_middle_id%5D%5B%5D=30&company_form%5Bindustry_middle_id%5D%5B%5D=31&company_form%5Bjobtalk_evaluate_colmn_name%5D=all&company_form%5Bpoint_from%5D=0.0&company_form%5Bpoint_to%5D=5.0&company_form%5Bq%5D=&company_form%5Brecruitment_season%5D=not_specified&page=8")
# els = driver.find_elements(By.XPATH, '//*[@class="p-search-panel__block-link"]')
# print(len(els))
# els = driver.find_elements(By.CLASS_NAME, "p-search-panel__block-link")
# print(len(els))


exit(0)
main_ulr = 'https://monkichi.instatry.jp/'
driver.get(main_ulr)
a_tag_list_=[]
#a_tag_list_o=[]
mail_tag_list_=[]
toiawase_domain = ["contact","inquiry","form","faq","info"]
st = time.time()
name_=""
url_=""
domain=""
print("サイト内タグ検索")

while(1):
    now=  time.time()-st
    if(now>5):break
    els = driver.find_elements(By.XPATH,"//a")
    nt=0
    list_g=[]
    if(len(els)>0):
        for eln in els:
            
            name_=""
            url_=""
            domain=""
            try:
                url_ = eln.get_attribute("href")
                #print(url_)
                parsed_url = urlparse(main_ulr)
                http = parsed_url.scheme
                domain = parsed_url.netloc
                g_ok=1
                for a_tag_list_n in a_tag_list_:
                    if(a_tag_list_n == url_):
                        g_ok=0
                        break
                
                if("www." in domain):
                    domain = re.sub("www." ,"",domain)
                if(domain in url_):
                    temp=0
                else:
                    g_ok=0
                
                #print(g_ok,"::",domain,"::",url_,"::",(domain in url_))
                if(g_ok==1):
                    a_tag_list_.append(url_)

                #toiawase domain チェック
                g_ok=0
                for toiawase_domain_n in toiawase_domain:
                    #print(g_ok,"重複チェック",url_,toiawase_domain_n)
                    if(toiawase_domain_n in url_):
                        g_ok=1
                        break
                #print(g_ok,"ドメインチェック")
                for a_tag_list_n in mail_tag_list_:
                    if(a_tag_list_n == url_):
                        g_ok=0
                        break
                #print(g_ok,"重複チェック")
                
                if("www." in domain):
                    domain = re.sub("www." ,"",domain)
                if(domain in url_):
                    temp=0
                else:
                    g_ok=0
                
                #print(g_ok,"::",domain,"::",url_,"::",(domain in url_))
                if(g_ok==1):
                    mail_tag_list_.append(url_)

            except:
                #traceback.print_exc()
                temp=1
print("==================================================")
print(domain)
print('a_tag_list_: ', a_tag_list_)
print('mail_tag_list_: ', mail_tag_list_)
print("==================================================")

exit(0)
# category = driver.find_element(By.CLASS_NAME, 'TM-searchConditionBox__panelTextJob').text.split('すべて')[0]
# print(category)
next = driver.find_element(By.CLASS_NAME, 'c-pagination__arrow--next')
print(next.get_attribute('href'))
els = driver.find_elements(By.CLASS_NAME, 'list-rst__rst-name-target')
print(len(els))
for eln in els:
    url_ = eln.get_attribute('href')
    print(url_)
    try:
        print(eln.text)
    except:
        pass
    break
    # res = requests.get(url_)
    # soup = BeautifulSoup(res.content, 'html.parser')
    # try:
    #     # print(soup.find(lambda tag: tag.name == "dt" and "社名（店舗名）" in tag.text).find_next().text)
    #     print(soup.find(lambda tag: tag.name == "dt" and "社名" in tag.text).find_next().text.replace('\n', ''))
    # except:
    #     pass
    # try:
    #     print(soup.find(lambda tag: tag.name == "dt" and "会社事業内容" in tag.text).find_next().text).replace('\n', '')
    # except:
    #     pass
    # try:
    #     print(soup.find(lambda tag: tag.name == "dt" and "会社住所" in tag.text).find_next().text.replace('\n', ''))
    # except:
    #     pass
    # try:
    #     print(soup.find(lambda tag: tag.name == "dt" and "ホームページリンク" in tag.text).find_next().text.replace('\n', ''))
    # except:
    #     pass
    # try:
    #     print(soup.find(lambda tag: tag.name == "dt" and "代表者" in tag.text).find_next().text.replace('\n', ''))
    # except:
    #     pass
    # try:
    #     print(soup.find(lambda tag: tag.name == "dt" and "代表電話番号" in tag.text).find_next().text.replace('\n', ''))
    # except:
    #     pass
    print('==========================================')


url = 'https://itp.ne.jp/topic/?sort=01&sbmap=false&topic=1900153%3B833%3B1900064&area=01202'
print(url)

if 'area' in url:
    for i in range(36):
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        try:
            category = soup.find_all(class_='wixui-dev-only-search-pageTitle')[0].text
            category = category.split()[0].replace('「', '')
            print(category)
        except:
            pass

        try:
            search_num = soup.find_all(class_='wixui-ev-only-search-totalCount')
            if len(search_num):
                print(search_num[0].text)
            else:
                search_num = soup.find_all(class_='wixui-dev-only-search-totalCount')
                if len(search_num):
                    print(search_num[0].text)
        except:
            pass
        pos = re.findall(r'area=(\d+)', url)
        url = url.replace(f"area=0{int(pos[0])}", f"area=0{int(pos[0])+1}")
        print(url)
    
exit(0)


