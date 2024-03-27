from optparse import Option


############################################################################################################################
def get_campany(soup_i,yubin_i,jyuusyo_i,mail_i,bangou_i,Fax_i):
    import traceback
    import g_val
    from selenium import webdriver
    try:
        from bs4 import BeautifulSoup,Comment
        import mojimoji
        import re
        import copy
        
        print("Function_i",yubin_i,jyuusyo_i,mail_i,bangou_i,Fax_i)
        
        yubin_o="-"
        jyuusyo_o="-"
        mail_o ="-"
        bangou_o="-"
        Fax_o_="-"
        
        daihyousya_="-"
        list_o =[]
        jyuusyo_o=jyuusyo_i
        yubin_o=yubin_i
        list_out=[]
        print("メールチェック")
        try:
            #########メール
            pattern = r'[A-Za-z0-9Ａ-Ｚ０-９._-]+@[A-Za-z0-9Ａ-Ｚ０-９-_.]+\.[A-Za-z0-9Ａ-Ｚ０-９-.]{2,4}'

            ret = re.compile(pattern)
            #print(soup_i)
            #temp= soup_i.find(text=ret)
            print("メールget")
            
            #print(re.findall(pattern, str(soup_i)))
            temp = re.findall(pattern, str(soup_i))[0]
            #print(temp)
            
            if(mail_i !="-"):mail_o=mail_i
            elif(temp == None ):
                if(mail_i !="-"):mail_o=mail_i


            elif( " "in str(temp)):
                tmp0= temp.split(" ")

                for tmp1 in tmp0:
                
                    if(re.search(ret,tmp1)):
                        if(mail_i =="-"):
                            mail_o0 =re.search(ret,tmp1).group()
                            mail_o1 = (mojimoji.zen_to_han(mail_o0)).lower()
                            if("?" in mail_o1):
                                mail_o2 = mail_o1.split("?",1)[0]
                            else:mail_o2=mail_o1
                            if("mail.info" in mail_o2):
                                mail_o= "info"+mail_o2.split("mail.info",1)[1]
                            else:mail_o=mail_o2
                        else:mail_o = mail_i

                        break
            else:
                if(re.search(ret,temp)):
                    if(mail_i =="-"):
                        print("メールget2")
                        mail_o0 =re.search(ret,temp).group()
                        mail_o1 = (mojimoji.zen_to_han(mail_o0)).lower()
                        if("?" in mail_o1):
                            mail_o2 = mail_o1.split("?",1)[0]
                        else:mail_o2=mail_o1
                        if("mail.info" in mail_o2):
                            mail_o= "info"+mail_o2.split("mail.info",1)[1]
                        else:mail_o=mail_o2

                    else:mail_o = mail_i
        except:
            #traceback.print_exc()
            if(mail_i !="-"):mail_o=mail_i
        
        cal_ok=0
        mail_d =""
        
        if("@" in mail_o):
            
            mail_d =mail_o.split("@",1)[1]
            print("ドメインチェック開始",mail_d)
            for b_mail_n in g_val.b_mail_ex:
                if(b_mail_n in mail_d):
                    print(b_mail_n,"::",mail_d)
                    cal_ok=1#見つかったらOKにする。
                    break
            
            if("example" in mail_o):
                cal_ok=0
            if("sample" in mail_o):
                cal_ok=0
            print("ブラックドメインリスト",cal_ok)
            if re.search(r'[a-zA-Z]',mail_d):
                temp=0
            else:
                cal_ok=0
            print("ブラックドメインリスト 英語チェック",cal_ok)
        
        
        print(g_val.blacklist_mail)
        for blacklist_mail_n in g_val.blacklist_mail:
            if(blacklist_mail_n=="-"or blacklist_mail_n=="" or blacklist_mail_n==None):break

            if(mail_o=="-"or mail_o=="" or mail_o==None):break

            if(blacklist_mail_n in mail_o):
                cal_ok=0#みつかったら0にする。
                break

        if(g_val.language_get_value==g_val.Lnagage_list[1]):    
            g_val.window_log["text"]="ブラックリストmailチェック"+str(cal_ok)
        else:
            g_val.window_log["text"]="Mail check"+str(cal_ok)
        g_val.data_log_write(g_val.window_log["text"])
        print("ブラックリストmeilチェック",cal_ok)

        if(cal_ok==0):#ドメインチェックエラー
            mail_o=mail_i
        else:
            try:
                print("文字列チェック")
                print(mail_o)
                g_val.window_log["text"]="Reserch word mail"
                g_val.data_log_write(g_val.window_log["text"])
                #spou_t = (soup_i.get_text()).replace("\r|\n|\r\n| |　|    ", "")
                spou_t = re.sub("\r|\n| |　|","",soup_i.get_text()).strip()
                
                # コメントタグの除去
                for comment in soup_i(text=lambda x: isinstance(x, Comment)):
                    comment.extract()

                # scriptタグの除去
                for script in soup_i.find_all('script', text=False):
                    #print("=======================script============================")
                    #print(script)
                    
                    if("function()" in str(script)):

                        script.decompose()#functionのところのみ削除
                        #print("削除")
                    #print("=======================script============================")
                # styleタグの除去
                #for style in soup_i.find_all('style', src=False):
                #    style.decompose()

                spou_t = re.sub("\r|\n| |　|","",str(soup_i)).strip()
                #spou_t = soup_i.contents#.strip().replace("\n", "")

                #print(spou_t)

                sou_d=0
                test_soup=""
                for spou_t_n in spou_t:
                    if(sou_d==0 and spou_t_n==">"):
                        sou_d=1
                        continue
                    elif(sou_d==1 and spou_t_n=="<"):
                        sou_d=0
                        continue
                    elif(sou_d==1 and spou_t_n!="<"):
                        test_soup += spou_t_n
                    else:
                        continue

                print("=============TESTETSTET===========================")
                spou_t = str(test_soup).replace("\n", "")
                print(spou_t)
                print("================TESTETSTET========================")
                try:
                    bnum_domain = int(g_val.ng_dword_rntry.get().replace('\\n', '').replace('\n', ''))
                except:
                    bnum_domain = int(100)

                print(spou_t.find(mail_o),"::",bnum_domain)
                
                if(spou_t.find(mail_o) !=-1):
                    st_num = int(spou_t.find(mail_o)) - int( bnum_domain)
                    if(st_num<=0):st_num=0
                    stop_num = int(spou_t.find(mail_o)) + int(bnum_domain) +len(mail_o)
                    if(stop_num>=len(spou_t)):stop_num = len(spou_t)-1
                    print("=================TESTETSTET=======================")
                    print("ST::",st_num,"::STOP::",stop_num)
                    print(g_val.blacklist_dword)
                    print("=================TESTETSTET=======================")

                    ok_bmail=1
                    for blacklist_dword_n in g_val.blacklist_dword:
                        dword_n = re.sub(" |　|\n","",blacklist_dword_n)

                        print(blacklist_dword_n)
                        if(len(blacklist_dword_n)==0):continue

                        if(blacklist_dword_n in spou_t[st_num:stop_num]):
                            print("NGワード発見")
                            print(blacklist_dword_n,"::",spou_t[st_num:stop_num])
                            print("NGワード発見")
                            ok_bmail =0
                            break

                    if(ok_bmail==1):
                        g_val.window_log["text"]="Result OK"
                        g_val.data_log_write(g_val.window_log["text"])
                    else:
                        mail_o=mail_i
                        
                        g_val.window_log["text"]="==Find NG word mail"
                        g_val.data_log_write(g_val.window_log["text"])
                        print("NGワード発見")


            except:
                traceback.print_exc()
                #g_val.g_val.data_log_write(datetime.datetime.now())
                g_val.data_log_write(traceback.format_exc())

        
        print(mail_o)
        print("FAX 番号チェック")
        try:
            ############番号
            pattern1 = r'[\(]{0,1}[0-9０-９]{2,4}[\)\- 　－\(]{0,1}[0-9０-９]{2,4}[\)\- 　－]{1,2}[0-9０-９]{3,4}'
            #temp_t= soup_i.find(text=re.compile(pattern1))
            temp_t= soup_i.find(text=re.compile("FAX|ＦＡＸ"))

            ret = re.compile(r'[\(]{0,1}[0-9０-９]{2,4}[\)\- 　－\(]{0,1}[0-9０-９]{2,4}[\)\- 　－]{1,2}[0-9０-９]{3,4}')
            print(temp_t)
            if "FAX" in str(temp_t) or "ＦＡＸ" in str(temp_t):
                
                if "FAX" in str(temp_t):

                    temp = temp_t.split("FAX" )[1]
                elif "ＦＡＸ" in str(temp_t):
                    temp = temp_t.split("ＦＡＸ")[1]

                if(Fax_i !="-"):Fax_o_=Fax_i
                elif(temp == None ):Fax_o_="-"
                elif(" " in temp):
                    tmp0= temp.split(" ")

                    for tmp1 in tmp0:
                        
                        if(re.search(ret,tmp1)):
                            if(Fax_i =="-"):
                                bangou_o0 =re.search(ret,tmp1).group()
                                if( re.fullmatch( re.compile(r'[0-9０-９]{4}[\-]{0,1}[0-9０-９]{4}'),str(bangou_o0))== None and len(bangou_o0)!=9):
                                    Fax_o_ = mojimoji.zen_to_han(bangou_o0)
                                    
                            else:Fax_o_ = Fax_i
                            break
                else:
                    if(re.search(ret,temp)):
                        if(Fax_i =="-"):
                            bangou_o0 =re.search(ret,temp).group()
                            if( re.fullmatch( re.compile(r'[0-9０-９]{4}[\-]{0,1}[0-9０-９]{4}'),str(bangou_o0))== None  and len(bangou_o0)!=9):
                                Fax_o_ = mojimoji.zen_to_han(bangou_o0)
                            
                        else:Fax_o_ = Fax_i
        except:
            if(Fax_i =="-"):Fax_o_ ="-"

        try:
            #電話番号チェック
            pattern1 = r'[\(]{0,1}[0-9０-９]{2,4}[\)\- 　－\(]{0,1}[0-9０-９]{2,4}[\)\- 　－]{1,2}[0-9０-９]{3,4}'
            temp= soup_i.find(text=re.compile(pattern1))

            if(bangou_i !="-"):bangou_o=bangou_i
            elif(temp == None ):bangou_o="-"
            elif(" " in temp):
                tmp0= temp.split(" ")

                for tmp1 in tmp0:
                    if(re.search(ret,tmp1)):
                        if(bangou_i =="-"):
                            bangou_o0 =re.search(ret,tmp1).group()
                            if( re.fullmatch( re.compile(r'[0-9０-９]{4}[\-]{0,1}[0-9０-９]{4}'),str(bangou_o0))== None and len(bangou_o0)!=9):
                                bangou_o = mojimoji.zen_to_han(bangou_o0)
                                print(bangou_o0)
                        else:bangou_o = bangou_i
                        break
            else:
                if(re.search(ret,temp)):

                    if(bangou_i =="-"):
                        bangou_o0 =re.search(ret,temp).group()
                        if( re.fullmatch( re.compile(r'[0-9０-９]{4}[\-]{0,1}[0-9０-９]{4}'),str(bangou_o0))== None  and len(bangou_o0)!=9):
                            bangou_o = mojimoji.zen_to_han(bangou_o0)
                            print(bangou_o0)

                    else:bangou_o = bangou_i
                #break

        except:
            if(bangou_i =="-"):bangou_o ="-"

        print("情報出力")
        list_o.append(copy.deepcopy(yubin_o))
        list_o.append(copy.deepcopy(jyuusyo_o))
        list_o.append(copy.deepcopy(mail_o))
        list_o.append(copy.deepcopy(bangou_o))
        list_o.append(copy.deepcopy(Fax_o_))
        print(list_o)
        print("==============================================")
        return list_o
    except:
        traceback.print_exc()
        #g_val.g_val.data_log_write(datetime.datetime.now())
        g_val.data_log_write(traceback.format_exc())

    



#########################################################################################################################################
#############################google 検索#################################################################################################
def google_detail_reserch(url_in_ ,campany_list_n,HP_url_):
    #2023 09 20 メインURLなしでも出力するように修正

    import g_val
    import mojimoji
    import time
    import traceback
    from time import sleep
    from urllib.parse import urlparse
    from tkinter import messagebox
    import re
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup,Comment
    import datetime
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    yubin_ ="-"
    jyuusyo_ ="-"
    mail_ ="-"
    bangou_ ="-"
    Fax_="-"
    main_ulr="-"
    url_gaiyou="-"
    
    if("Windows"==g_val.OS_VERSION):
        from subprocess import CREATE_NO_WINDOW
    chrome_service = Service(g_val.d_path)
    if("Windows"==g_val.OS_VERSION):
        chrome_service.creationflags = CREATE_NO_WINDOW

    list_out=[]
    if(g_val.conf_email):
        toiawase_page=["概要","会社","campany","CAMPANY","Campany","問い合わせ","問合わせ","問合せ","contact","Contact","CONTACT","contatto"]
    
    else:
        toiawase_page=["問い合わせ","問合わせ","問合せ","contact","Contact","CONTACT","contatto"]
    toiawase_domain=["contact","inquiry","form","inquire"]
    
    try:
        try:
            titel_ = campany_list_n[0]
            url_get = url_in_
            if(g_val.stop_==1):return 0   
            kategori_=""
            g_val.driver.get(url_in_)

            #ロボットの可能性あり。
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                els = g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"このページが表示された理由")]')
            else:
                els = g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"Why this page was displayed")]')
            if(len(els)>0):
                #ロボットの可能性アリ
                g_val.driver.quit()
                # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option0,service=chrome_service)
                g_val.driver = webdriver.Chrome(options=g_val.option0,service=chrome_service)
                g_val.driver.set_page_load_timeout(180)
                g_val.driver.get(url_)
                sleep(1)
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    messagebox.askyesno('確認', 'ブラウザを確認してください')
                else:
                    messagebox.askyesno('Confirmination', 'Please check your browser')
                g_val.driver.quit()
                # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                g_val.driver = webdriver.Chrome(options=g_val.option,service=chrome_service)
                g_val.driver.set_page_load_timeout(180)
            if(g_val.stop_==1):return 0      
            try:
                
                url_ = url_get
                #g_val.driver.get(url_)
            except:
                if(g_val.stop_==1):return 0
                traceback.print_exc()
                main_ulr="-"

            #もし複数でてきたら、クリック
            st = time.time()
            while(1):
                now = time.time() - st 
                els =  g_val.driver.find_elements(By.XPATH,'//div[@role="feed"]//a')
                if(now>5):break
                elif(len(els)>0):
                    for eln in els:
                            print("クリック")
                            #g_val.driver.execute_script("arguments[0].click();",eln)
                            url=eln.get_attribute("href")
                            g_val.driver.get(url)
                            break
                    break


            #sleep(30)
            st = time.time()
            while(1):
                now = time.time() - st 
                #els =  g_val.driver.find_elements(By.XPATH,'//button[@jsaction="pane.rating.category"]')
                els =  g_val.driver.find_elements(By.XPATH,'//button[contains(@jsaction,"category")]')#2023.01.27                               
                els1 =  g_val.driver.find_elements(By.XPATH,'//div[@class="fontBodyMedium dmRWX"]//span[contains(text(),"ホテル")]')

                if(now>5):break
                elif(len(els)>0):
                    
                    kategori_= els[0].text
                    print("カテゴリ",kategori_)
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="カテゴリ"+kategori_
                    else:
                        g_val.window_log["text"]="Category"+kategori_
                    g_val.data_log_write(g_val.window_log["text"])
                    break
                elif(len(els1)>0):    
                    kategori_= els1[0].text
                    print("カテゴリ",kategori_)
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="カテゴリ"+kategori_
                    else:
                        g_val.window_log["text"]="Category"+kategori_
                    g_val.data_log_write(g_val.window_log["text"])
                    break
            if(g_val.stop_==1):return 0
            #if(conf_kate):
            if(g_val.mode_get_value==g_val.mode_list[1] and g_val.conf_kate):#google検索のみ実施
                if(campany_list_n[2] in kategori_ ):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="カテゴリOK"
                    else:
                        g_val.window_log["text"]="Category OK"
                    print("カテゴリOK")
                else:
                    print("カテゴリ該当なし")
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="カテゴリ該当なし"
                    else:
                        g_val.window_log["text"]="No Category"
                    
                    g_val.data_log_write(g_val.window_log["text"])

                    while(1):
                        handle_array = g_val.driver.window_handles
                        if(len(handle_array)==1):break
                        else:
                            g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                            
                            g_val.driver.close()
                            sleep(0.5)
                    return 0
                
            else:
                print("カテゴリチェックなし")
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="カテゴリチェックスキップ"
                else:
                    g_val.window_log["text"]="Category Check skip"
                g_val.data_log_write(g_val.window_log["text"])

            if(kategori_ ==""):
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    kategori_ = "(不明)"+campany_list_n[2]
                else:
                    kategori_ = "(Non Clear)"+campany_list_n[2]
            st = time.time()
            while(1):
                now = time.time() - st 
                els =  g_val.driver.find_elements(By.XPATH,'//input[@name="q"]')

                if(now>5):break
                elif(len(els)>0):
                    break
            try:
                
                j_es=""
                els0 = g_val.driver.find_elements(By.XPATH,'//button[@data-item-id="address"]')
                els1 = g_val.driver.find_elements(By.XPATH,'//div[@data-tooltip="住所をコピーします"]')

                if(len(els0)>0):
                    j_es = els0[0].get_attribute('aria-label')
                elif(len(els1)>0):
                    j_es = els1[0].get_attribute('aria-label')    
                else:j_es=""

                print("GET google elemnet","::",j_es,j_es)
                tj1 =""
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    if("住所: " in j_es):
                        tj1=j_es.split("住所: ")[1]
                    elif("住所、" in j_es):
                        tj1=j_es.split("住所、")[1]
                else:
                    tj1=j_es.split("Address: ")[1]
                print(tj1)
                if('〒' in tj1 ):

                    jyuusyo_=tj1.split(" ",1)[1]
                else:
                    jyuusyo_=tj1            
            except:
                traceback.print_exc()
                jyuusyo_="-"
                
            if(g_val.stop_==1):return 0   
            print("グーグル住所",jyuusyo_)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="グーグル住所"+jyuusyo_
            else:
                g_val.window_log["text"]="Address"+jyuusyo_
            g_val.data_log_write(g_val.window_log["text"])

            try:
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    j_es=g_val.driver.find_element(By.XPATH,'//button[@data-tooltip="電話番号をコピーします"]').get_attribute('aria-label')
                    tj1=j_es.split("電話番号: ")[1]
                    bangou_=tj1
                else:
                    j_es=g_val.driver.find_element(By.XPATH,'//button[@data-tooltip="Copy phone number"]').get_attribute('aria-label')
                    tj1=j_es.split("Phone: ")[1]
                    bangou_=tj1

                

            except:
                bangou_="-"
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="グーグル番号"+bangou_
            else:
                g_val.window_log["text"]="Tell"+bangou_
            g_val.data_log_write(g_val.window_log["text"])
            print("グーグル番号",bangou_)
            
            #if(g_val.language_get_value==g_val.Lnagage_list[1]):
            if(1):
                cal_eria_num=0
                print("住所チェック",jyuusyo_)
                print("住所",campany_list_n)
                print("住所",campany_list_n[3] .split("  ")[0])
                if(campany_list_n[3] .split("  ")[0] in jyuusyo_ ):
                    #都道府県のみ　campany_list_n[3] .split("  ")[1] in jyuusyo_ and 

                    print("住所OK")
                    cal_eria_num=0
                else:
                    print("住所該当なし")
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="住所該当なし"
                    else:
                        g_val.window_log["text"]="No Eria"
                    
                    g_val.data_log_write(g_val.window_log["text"])

                    cal_eria_num+=1
                    if(cal_eria_num>=3):
                        print("=================")
                        print("地域該当なし")
                        print("=================")
                        #return #dudaはこれなし
                    
                    if(g_val.bt_genimu_eria.get()):#都道府県一致検索なし。
                        print("住所該当スキップ")
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="住所検索スキップ"
                        else:
                            g_val.window_log["text"]="Eria Reserch SKIP"
                    else:

                        while(1):
                            handle_array = g_val.driver.window_handles
                            if(len(handle_array)==1):break
                            else:
                                g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                                
                                g_val.driver.close()
                                sleep(0.5)

                        return 0

            if(g_val.stop_==1):return 0     
            #"平均評価数","口コミ数","営業時間(月)","営業時間(火)","営業時間(水)","営業時間(木)","営業時間(金)","営業時間(土)","営業時間(日)"]
            h_hyouka=""
            try:

                #住所チェック
                #番号チェック
                st = time.time()
                while(1):
                    if(g_val.get_hyouka_bln.get()==False):
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="評価　skip"
                        else:
                            g_val.window_log["text"]="Average reviews skip"
                        g_val.data_log_write(g_val.window_log["text"])
                        print("評価　skip")
                        break
                    now = time.time() - st 
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        els =  g_val.driver.find_elements(By.XPATH,'//span[contains(@aria-label,"つ星")]')
                    else:
                        els =  g_val.driver.find_elements(By.XPATH,'//span[contains(@aria-label,"stars")]')
                    
                    if(now>5):break
                    elif(len(els)>0):
                        h_hyouka_c= els[0].get_attribute("aria-label")
                        h_hyouka = re.sub(r"[^\d.]", "", h_hyouka_c)

                        print("平均評価",h_hyouka)
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"] ="平均評価"+h_hyouka
                        else:
                            g_val.window_log["text"] ="Average reviews "+h_hyouka

                        g_val.data_log_write(g_val.window_log["text"])
                        break
            except:
                temp=0

            if(g_val.stop_==1):return 0

            kuchikomi_=""
            try:
                st = time.time()
                while(1):

                    if(g_val.get_kutikomi_bln.get()==False):
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="口コミ　skip"
                        else:
                            g_val.window_log["text"]="All reviews　skip"
                        g_val.data_log_write(g_val.window_log["text"])
                        print(g_val.window_log["text"])
                        break
                    now = time.time() - st 
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        els =  g_val.driver.find_elements(By.XPATH,'//button[contains(@aria-label,"件のクチコミ")]')
                    else:
                        els =  g_val.driver.find_elements(By.XPATH,'//button[contains(@aria-label,"reviews")]')
                
                    if(now>5):break
                    elif(len(els)>0):
                        kuchikomi_c= els[0].get_attribute("aria-label")
                        kuchikomi_=re.sub(r"[^\d.]", "", kuchikomi_c)
                        print("口コミ",kuchikomi_)
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"] ="口コミ"+kuchikomi_
                        else:
                            g_val.window_log["text"] ="All reviews"+kuchikomi_
                        g_val.data_log_write(g_val.window_log["text"])

                        break
            except:
                temp=0
            if(g_val.stop_==1):return 0   

            if(g_val.language_get_value!=g_val.Lnagage_list[1]):
                st = time.time()
                while(1):
                    now = time.time() - st 
                    els =  g_val.driver.find_elements(By.XPATH,'//button[@data-item-id="oh"]')
                    if(now>5):break
                    elif(len(els)>0):
                        for eln in els: 
                            g_val.driver.execute_script("arguments[0].click();",eln)
                            sleep(1)
                            break
                        break
            
            eigyou_sun=""
            st = time.time()
            while(1):
                if(g_val.get_sun_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(日)　skip"
                    else:
                        g_val.window_log["text"]="Sunday　skip"
                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                now = time.time() - st 
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"日曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Sunday")]/../../td[2]/ul/li')
                
                if(now>5):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_sun ==""):eigyou_sun = els_n.get_attribute("textContent")
                        else:eigyou_sun = eigyou_sun +","+els_n.get_attribute("textContent")
                    break
            print("日曜日　営業時間",eigyou_sun)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="日曜日　営業時間"+eigyou_sun
            else:
                g_val.window_log["text"] ="Sunday"+eigyou_sun

            g_val.data_log_write(g_val.window_log["text"])
            
            if(g_val.stop_==1):return 0   
            eigyou_mon=""
            st = time.time()
            while(1):
                now = time.time() - st 
                if(g_val.get_mon_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(月)　skip"
                    else:
                        g_val.window_log["text"]="Monday　skip"
                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"月曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Monday")]/../../td[2]/ul/li')
                

                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_mon ==""):eigyou_mon = els_n.get_attribute("textContent")
                        else:eigyou_mon = eigyou_mon +","+els_n.get_attribute("textContent")
                    break
            print("月曜日　営業時間",eigyou_mon)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="月曜日　営業時間"+eigyou_mon
            else:
                g_val.window_log["text"] ="Monday"+eigyou_mon
            g_val.data_log_write(g_val.window_log["text"])

            if(g_val.stop_==1):return 0   
            eigyou_tue=""
            st = time.time()
            while(1):
                now = time.time() - st 
                if(g_val.get_tue_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(火)　skip"
                    else:
                        g_val.window_log["text"]="Tuesday　skip"
                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"火曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Tuesday")]/../../td[2]/ul/li')
                
                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_tue ==""):eigyou_tue = els_n.get_attribute("textContent")
                        else:eigyou_tue = eigyou_tue +","+els_n.get_attribute("textContent")
                    break
            print("火曜日　営業時間",eigyou_tue)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="火曜日　営業時間"+eigyou_tue
            else:
                g_val.window_log["text"] ="Tuesday"+eigyou_tue
            
            g_val.data_log_write(g_val.window_log["text"])
            if(g_val.stop_==1):return 0   
            eigyou_wed=""
            st = time.time()
            while(1):
                now = time.time() - st 
                if(g_val.get_wed_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(水)　skip"
                    else:
                        g_val.window_log["text"]="Wednsday　skip"

                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"水曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Wednesday")]/../../td[2]/ul/li')
                
                
                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_wed ==""):eigyou_wed = els_n.get_attribute("textContent")
                        else:eigyou_wed = eigyou_wed +","+els_n.get_attribute("textContent")
                    break
            if(g_val.stop_==1):return 0 

            print("水曜日　営業時間",eigyou_wed)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="水曜日　営業時間"+eigyou_wed
            else:
                g_val.window_log["text"] ="Wednesday"+eigyou_wed
            g_val.data_log_write(g_val.window_log["text"])
            eigyou_thu=""   
            st = time.time()
            while(1):
                now = time.time() - st 
                if(g_val.get_thu_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(木)　skip"
                    else:
                        g_val.window_log["text"]="Thursday　skip"

                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"木曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Thursday")]/../../td[2]/ul/li')
                
                
                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_thu ==""):eigyou_thu = els_n.get_attribute("textContent")
                        else:eigyou_thu = eigyou_thu +","+els_n.get_attribute("textContent")
                    break
            print("木曜日　営業時間",eigyou_thu)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="木曜日　営業時間"+eigyou_thu
            else:
                g_val.window_log["text"] ="Thursday"+eigyou_thu

            if(g_val.stop_==1):return 0    
            eigyou_fri=""
            st = time.time()
            while(1):
                now = time.time() - st 
                if(g_val.get_fri_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(金)　skip"
                    else:
                        g_val.window_log["text"]="Friday　skip"

                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"金曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Friday")]/../../td[2]/ul/li')
                
                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_fri ==""):eigyou_fri = els_n.get_attribute("textContent")
                        else:eigyou_fri = eigyou_fri +","+els_n.get_attribute("textContent")
                    break

            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="金曜日　営業時間"+eigyou_fri
            else:
                g_val.window_log["text"] ="Friday"+eigyou_fri
            g_val.data_log_write(g_val.window_log["text"])
            print("金曜日　営業時間",eigyou_fri)
            if(g_val.stop_==1):return 0    
            eigyou_sta=""
            st = time.time()
            while(1):
                now = time.time() - st 
                
                                                        
                if(g_val.get_sat_bln.get()==False):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="営業(土)　skip"
                    else:
                        g_val.window_log["text"]="Saturday　skip"
                    g_val.data_log_write(g_val.window_log["text"])
                    print(g_val.window_log["text"])
                    break
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"土曜日")]/../../td[2]/ul/li')
                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//tbody/tr/td/div[contains(text(),"Saturday")]/../../td[2]/ul/li')
                

                if(now>1):break
                elif(len(els)>0):
                    for els_n in els:
                        if(eigyou_sta ==""):eigyou_sta = els_n.get_attribute("textContent")
                        else:eigyou_sta = eigyou_sta +","+els_n.get_attribute("textContent")
                    break
            print("土曜日　営業時間",eigyou_sta)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="土曜日　営業時間"+eigyou_sta
            else:
                g_val.window_log["text"] ="Saturday"+eigyou_sta
            g_val.data_log_write(g_val.window_log["text"])
            
            if(g_val.stop_==1):return 0 

            #ホームページチェック
            st0 = time.time()
            while(1):
                now0 = time.time() - st0
                #print("検索中",now0)
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els =  g_val.driver.find_elements(By.XPATH,'//img[@alt="ウェブサイトを開きます"]')
                    els1 =  g_val.driver.find_elements(By.XPATH,'//span[contains(text(),"閉業")]')
                    els2 =  g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"ウェブサイトを追加")]')

                else:
                    els =  g_val.driver.find_elements(By.XPATH,'//img[@alt="Open website"]')
                    els1 =  g_val.driver.find_elements(By.XPATH,'//span[contains(text(),"Completely closed")]')
                    els2 =  g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"Add website")]')


                #if(now0>10):break                    
                if(len(els2)>0 or now0>5):
                    main_ulr="-"

                    break

                elif(len(els1)>0):
                    print("el1")
                    #main_ulr ="閉業"
                    main_ulr="-"
                    break
                elif(len(els)>0):
                    for el in els:
                        print("el0")
                        
                        if(0):########TESTETSTETSE###########################################
                            el_ulr = "https://store.shopping.yahoo.co.jp/bc-direct/shop-info.html"##############################
                            g_val.driver.get(el_ulr)
                        else:
                            g_val.driver.execute_script("arguments[0].click();",el)
                        g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                        break

                    break


            if(g_val.stop_==1):return 0

            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="検索終了"
            else:
                g_val.window_log["text"]="Reserch End"

            g_val.data_log_write(g_val.window_log["text"])
            print("検索終了")

            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="詳細検索開始"
            else:
                g_val.window_log["text"]="Reserch Detail Start"

            g_val.data_log_write(g_val.window_log["text"])
            print("詳細検索開始")

            if(len(els)>0 ):
                #driver.get("https://www."+main_ulr)
                try:
                    if("https://www.google.com/url?"in g_val.driver.current_url):
                        
                        print("リダイレクト対策")
                        
                        st2 =time.time()
                        while(1):
                            now2 = time.time() - st2
                            els = g_val.driver.find_elements(By.XPATH,"//a")
                            if(now2>3):break
                            elif(len(els)>0):
                                el_ulr = g_val.driver.find_element(By.XPATH,"//a").get_attribute('href')
                                g_val.driver.get(el_ulr)
                                sleep(1)
                except:
                    temp=0
                main_ulr = g_val.driver.current_url

                
            if(g_val.stop_==1):return 0

        except:
            if(g_val.stop_==1):return 0
            traceback.print_exc()
            main_ulr ="-"

        if("https://www.google.com/maps/place" in main_ulr):
            print("グーグルマップURLあり")
            main_ulr="-"

        if( main_ulr == "-" or main_ulr == "" or main_ulr == None):
            main_ulr = HP_url_#他のサイトで取得したやつを代入
            if( main_ulr != "-" and main_ulr != "" and main_ulr != None):
                try:
                    print(main_ulr)
                    g_val.driver.get(main_ulr)#URLがあれば代入
                except:
                    traceback.print_exc()
                    return 0
                print("==========外部URL代入====================")

        if( main_ulr != "-" and main_ulr != "" and main_ulr != None):

            print("詳細検索")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="詳細検索"+main_ulr
            else:
                g_val.window_log["text"]="Detail listing"+main_ulr
            g_val.data_log_write(g_val.window_log["text"])
            print(main_ulr)

            #exit()
            print("サイト内検索")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="サイト内検索"
            else:
                g_val.window_log["text"]="Internay Listing"

            g_val.data_log_write(g_val.window_log["text"])
            #スクロール
            try:
                #g_val.driver.find_element_by_tag_name('body').click()
                g_val.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                temp=0

            sleep(3)
            #先にaタグを検索する。
            a_tag_list_=[]
            #a_tag_list_o=[]
            mail_tag_list_=[]
            st = time.time()
            name_=""
            url_=""
            domain=""
            print("サイト内タグ検索")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="サイト内タグ検索"
            else:
                g_val.window_log["text"]="Detail site tag"
            g_val.data_log_write(g_val.window_log["text"])

            while(1):
                now=  time.time()-st
                if(now>5):break
                els = g_val.driver.find_elements(By.XPATH,"//a")
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
            print(a_tag_list_)
            print(mail_tag_list_)
            print("==================================================")

            print("サイト内タグ個数")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="サイト内タグ個数"+str(len(a_tag_list_))
            else:
                g_val.window_log["text"]="Site tag num"+str(len(a_tag_list_))
            g_val.data_log_write(g_val.window_log["text"])
            #1ページも行う。
            url_gaiyou="-"
            source = g_val.driver.page_source.encode('utf-8')
            soup = BeautifulSoup(source,'html.parser')
            #print(soup)
            print("=======================================================")
            list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
            yubin_ = list_get[0]
            jyuusyo_= list_get[1]
            mail_= list_get[2]
            bangou_= list_get[3]
            Fax_= list_get[4]
            print("1ページ目",list_get)

            #sleep(100)################################################################################
            nnn=0
            for li in toiawase_page:
                if(g_val.stop_==1):return    
                nnn+=1

                t = "//*[contains(text(), '"+li+"')]"
                els = g_val.driver.find_elements(By.XPATH,t)

                ############################################################################
                print("サイト内検索問い合わせ中")
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="サイト内問い合わせ検索中No:"+str(nnn)
                else:
                    g_val.window_log["text"]="SiteInqueryNo:"+str(nnn)
                g_val.data_log_write(g_val.window_log["text"])
                ############################################################################
                if(len(els))>0:
                    for eln in els: 
                        #print("問い合わせ検索1")
                        if(g_val.stop_==1):return 0
                        try:
                            #element0  = g_val.driver.find_element(By.XPATH,t)
                            url_gaiyou1 = eln.get_attribute("href")
                            #print(url_gaiyou1)
                            if("mailto:" in str(url_gaiyou1)):
                                
                                mail_o0 = re.sub("mailto:","",url_gaiyou1)
                                mail_o1 = (mojimoji.zen_to_han(mail_o0)).lower()
                                if("?" in mail_o1):
                                    mail_o2 = mail_o1.split("?",1)[0]
                                else:mail_o2=mail_o1
                                #if("mail.info" in mail_o2):
                                #    mail_= "info"+mail_o2.split("mail.info",1)[1]
                                #else:mail_=mail_o2

                                continue
                            elif("tel" in str(url_gaiyou1)):
                                continue

                            if(url_gaiyou1 ==None or url_gaiyou1==""):#:continue
                                try:
                                    g_val.driver.execute_script("arguments[0].click();",eln)
                                except:
                                    temp=0

                                sleep(5)
                                url_gaiyou1 = g_val.driver.current_url

                                

                            else:
                                g_val.driver.get(url_gaiyou1)

                            print("ページ遷移")
                            if(url_gaiyou=="-"):
                                els_i1 = g_val.driver.find_elements(By.XPATH,'//input[@type="text"]')
                                els_i2 = g_val.driver.find_elements(By.XPATH,'//textarea')
                                
                                if(len(els_i1)>0 or len(els_i2)>0):

                                    for toiawase_domain_n in toiawase_domain:
                                        if(toiawase_domain_n in url_gaiyou1):

                                            url_gaiyou=url_gaiyou1
                                            break
                            source = g_val.driver.page_source.encode('utf-8')
                            soup = BeautifulSoup(source,'html.parser')

                            print("testtest")
                            #print(soup)

                            list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
                            yubin_ = list_get[0]
                            jyuusyo_= list_get[1]
                            mail_= list_get[2]
                            bangou_= list_get[3]
                            Fax_= list_get[4]
                            #daihyousya_= list_get[4]
                            #もとに戻す。
                            g_val.driver.get(main_ulr)
                        except:
                            temp=0
                            #traceback.print_exc()
            if(g_val.stop_==1):return
            print("問い合わせ確認::",url_gaiyou)
            print(mail_tag_list_)
            print("================================--")
            ##########################################################
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"]="問い合わせ検索再リサーチ"
            else:
                g_val.window_log["text"]="Re-reserch InqueySite::"
            g_val.data_log_write(g_val.window_log["text"])
            ##########################################################
            no_0 =0
            if(url_gaiyou == "-"):
                #もしとれてなかったら再度検索する。精度アップ
                no_0+=1
                print("================================--")
                print("問い合わせ開始")
                print("================================--")
                for eln in mail_tag_list_: 
                    try:

                        ##########################################################
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="問い合わせ検索再リサーチNO:"+str(no_0)
                        else:
                            g_val.window_log["text"]="Re-reserch InqueySiteNO:"+str(no_0)
                        g_val.data_log_write(g_val.window_log["text"])
                        ##########################################################

                        url_gaiyou1 = eln
                        if(url_gaiyou1 ==None or url_gaiyou1==""):#:continue
                            try:
                                g_val.driver.execute_script("arguments[0].click();",eln)
                            except:
                                temp=0

                            sleep(5)
                            url_gaiyou1 = g_val.driver.current_url

                        else:
                            g_val.driver.get(url_gaiyou1)
                                #スクロール
                            try:
                                #g_val.driver.find_element_by_tag_name('body').click()
                                g_val.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            except:
                                temp=0
                        
                        print("ページ遷移",url_gaiyou1)
                        if(url_gaiyou=="-"):
                            els_i1 = g_val.driver.find_elements(By.XPATH,'//input[@type="text"]')
                            els_i2 = g_val.driver.find_elements(By.XPATH,'//textarea')
                                
                            if(len(els_i1)>0 or len(els_i2)>0):
                                for toiawase_domain_n in toiawase_domain:
                                    if(toiawase_domain_n in url_gaiyou1):

                                        url_gaiyou=url_gaiyou1
                                        break
                                    
                        print("問い合わせホーム",url_gaiyou)
                        source = g_val.driver.page_source.encode('utf-8')
                        #soup = BeautifulSoup(source,'xml')#'html.parser')
                        soup = BeautifulSoup(source,'html.parser')
                        #soup = source
                        print("testtest")
                        #print(soup)
                        list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
                        yubin_ = list_get[0]
                        jyuusyo_= list_get[1]
                        mail_= list_get[2]
                        bangou_= list_get[3]
                        Fax_= list_get[4]
                        if(url_gaiyou!="-"):break
                        #daihyousya_= list_get[4]
                        
                    except:
                        temp=0
                        traceback.print_exc()

            if(g_val.stop_==1):return

            if(g_val.conf_email and mail_=="-"):
                print("メール厳密")
                print(a_tag_list_)
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="メール詳細検索"
                else:
                    g_val.window_log["text"]="Mail Detail Listing"

                g_val.data_log_write(g_val.window_log["text"])

                n_emal=0
                for eln in a_tag_list_: 
                    #print("問い合わせ検索1")
                    n_emal +=1

                    try:
                        #element0  = g_val.driver.find_element(By.XPATH,t)

                        ##########################################################
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="メール詳細検索No:"+str(n_emal)
                        else:
                            g_val.window_log["text"]="Mail Detail ListingNo:"+str(n_emal)
                        g_val.data_log_write(g_val.window_log["text"])
                        ##########################################################

                        try:
                            url_gaiyou1 = eln
                        except:
                            url_gaiyou1==""
                        
                        g_val.driver.get(url_gaiyou1)
                        sleep(1)
                        url_gaiyou1 = g_val.driver.current_url
                        print("ページ遷移")
                        
                        source = g_val.driver.page_source.encode('utf-8')
                        #soup = BeautifulSoup(source,'xml')#'html.parser')
                        soup = BeautifulSoup(source,'html.parser')
                        #soup = source
                        print("testtest")
                        #print(soup)
                        list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
                        yubin_ = list_get[0]
                        jyuusyo_= list_get[1]
                        mail_= list_get[2]
                        bangou_= list_get[3]
                        Fax_= list_get[4]
                        #daihyousya_= list_get[4]
                        #URLをメインURLに戻す。

                        #g_val.driver.get(main_url)
                        if(mail_ !="-"):
                            break
                    except:
                        temp=0
                        #traceback.print_exc()
                print(mail_)
                if(mail_ =="-"):
                    ###maiが取得できない場合、追加で検索
                    ##########################################################
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="メール詳細検索(外部サイト検索)"
                    else:
                        g_val.window_log["text"]="Mail Detail Listing at outsie:"
                    g_val.data_log_write(g_val.window_log["text"])
                    ##########################################################

                    load_url = "https://www.google.com/search?q="+jyuusyo_+"  "+titel_ +"  email"
                    g_val.driver.get(load_url)
                    #sleep(10)
                    st = time.time()
                    while(1):
                        now=  time.time()-st
                        if(now>5):break
                        els = g_val.driver.find_elements(By.XPATH,"//a")
                        nt=0
                        list_g=[]
                        if(len(els)>0):
                            for eln in els:
                                
                                name_=""
                                url_=""
                                try:
                                    url_ = eln.get_attribute("href")
                                    name_ =eln.find_element(By.XPATH,"h3").text
                                    print(url_)
                                    
                                    list_g.append(url_)
                                    nt+=1
                                    if(nt>=2 ):
                                        #or (mail_!="" and mail_!="-")):
                                        print("end",nt)
                                        break
                                except:
                                    temp=0
                                    #traceback.print_exc()
                            break
                    print(list_g)
                    ##########################################################
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="メール詳細検索(外部サイト検索)数"+str(len(list_g))
                    else:
                        g_val.window_log["text"]="Mail Detail Listing at outsie num:"+str(len(list_g))
                    g_val.data_log_write(g_val.window_log["text"])
                    ##########################################################
                    list_g_n_C=0
                    for list_g_n in list_g:
                        list_g_n_C +=1
                        g_val.driver.get(list_g_n)
                        source = g_val.driver.page_source.encode('utf-8')
                        ##########################################################
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            g_val.window_log["text"]="メール詳細検索(外部サイト検索)No:"+str(list_g_n_C)
                        else:
                            g_val.window_log["text"]="Mail Detail Listing at outsie No:"+str(list_g_n_C)
                        g_val.data_log_write(g_val.window_log["text"])
                        ##########################################################

                        sleep(1)
                        soup = BeautifulSoup(source,'html.parser')
                        #soup = source
                        print("testtest")
                        #print(soup)
                        list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
                        yubin_ = list_get[0]
                        jyuusyo_= list_get[1]
                        mail_= list_get[2]
                        bangou_= list_get[3]
                        Fax_= list_get[4]
                        if(mail_!="" and mail_!="-"):
                            print("end",nt)
                            break
                print("====================================")
                print(mail_)
                print("====================================")

        if(g_val.get_fax_bln and Fax_=="-" and bangou_ !="-"):
            #番号を使って詳細検索
            print("FAX厳密")

            lit_url_n_0 ="https://www.google.com/search?q=" + titel_ +"　FAX　"  +bangou_
            g_val.driver.get(lit_url_n_0)
            list_fax=[]
            st = time.time()
            while(1):
                now=  time.time()-st
                if(now>5):break
                els = g_val.driver.find_elements(By.XPATH,"//a")
                nt=0
                list_g=[]
                if(len(els)>0):
                    for eln in els:
                        
                        fax_name_=""
                        fax_url_=""
                        try:
                            fax_url_ = eln.get_attribute("href")
                            fax_name_ =eln.find_element(By.XPATH,"h3").text
                            print(fax_url_)
                            list_fax.append(fax_url_)
                            nt+=1
                            if(nt>=3 ):
                                #or (mail_!="" and mail_!="-")):
                                print("end",nt)
                                break
                            
                            #break
                        except:
                            temp=0
                            #traceback.print_exc()
                    break
            for list_fax_n in list_fax:
                try:
                    print("FAX収集" , list_fax_n)
                    if(Fax_ !="-"):
                        break
                    g_val.driver.get(list_fax_n)
                    print("FAX収集" , "ソース解析")
                    source = g_val.driver.page_source.encode('utf-8')
                    soup = BeautifulSoup(source,'html.parser')
                    print("FAX収集" , "ソース解析2")
                    list_get = get_campany(soup,yubin_,jyuusyo_,mail_,bangou_,Fax_)
                    #print("OUT :Dribv2" ,"会社名" ,titel_ ,"住所",jyuusyo_,"サイトURL",url_get)
                    #FAXのみ更新
                    
                    Fax_= list_get[4]
                except:
                    traceback.print_exc()
                    
            print("FAX END")

        if(g_val.stop_==1):return 0
        print("==========================================================================================================")
        #print("OUT :Dribv2" ,"会社名" ,titel_ ,"URL", main_ulr ,"〒番号:",yubin_,"住所",jyuusyo_,"E-mail",mail_,"番号",bangou_,"代表者",daihyousya_)
        print("OUT :Dribv2" ,"会社名" ,titel_ ,"住所",jyuusyo_,"サイトURL",url_get)
        print("URL", main_ulr ,"E-mail",mail_,"番号",bangou_,"FAX",Fax_,'問い合わせURL',url_gaiyou)#"問い合わせ",daihyousya_)

        g_val.window_log["text"]="OUT :Dribv2" +"Campany Nanme" +titel_ 
        g_val.data_log_write(g_val.window_log["text"])
        g_val.window_log["text"]="Address"+jyuusyo_
        g_val.data_log_write(g_val.window_log["text"])
        g_val.window_log["text"]="Site URL"+url_get
        g_val.data_log_write(g_val.window_log["text"])
        g_val.window_log["text"]="URL"+main_ulr
        g_val.data_log_write(g_val.window_log["text"])
        g_val.window_log["text"]="mail"+mail_
        g_val.data_log_write(g_val.window_log["text"])
        g_val.window_log["text"]="Tell"+bangou_
        g_val.data_log_write(g_val.window_log["text"])

        if(g_val.get_fax_bln.get()==False):
            Fax_=""
            g_val.window_log["text"]="FAX SKIP"
            g_val.data_log_write(g_val.window_log["text"])
            print(g_val.window_log["text"])

        g_val.window_log["text"]="FAX"+Fax_
        g_val.data_log_write(g_val.window_log["text"])
        print("==========================================================================================================")
        out_ok=1
        if(g_val.stop_==1):return 0

        for blacklist_bangou1_n in g_val.blacklist_bangou1:
            if(blacklist_bangou1_n=="-"or blacklist_bangou1_n=="" or blacklist_bangou1_n==None):break
            if(bangou_=="-"or bangou_=="" or bangou_==None):break

            if(blacklist_bangou1_n in bangou_):
                out_ok=0
                break
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"]="ブラックリスト番号1チェック"+str(out_ok)
        else:
            g_val.window_log["text"]="Tell Check"+str(out_ok)
        g_val.data_log_write(g_val.window_log["text"])
        print("ブラックリスト番号1チェック",out_ok)


        for blacklist_bangou2_n in g_val.blacklist_bangou2:
            #print(blacklist_bangou2_n,bangou_)
            if(bangou_=="-"or bangou_=="" or bangou_==None):break
            if(blacklist_bangou2_n=="-"or blacklist_bangou2_n=="" or blacklist_bangou2_n==None):break
            
            if(blacklist_bangou2_n in re.sub("-|‐| |　","",bangou_)):
                out_ok=0
                break
        print("ブラックリスト番号2チェック",out_ok) 
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"]="ブラックリスト番号2チェック"+str(out_ok)
        else:
            g_val.window_log["text"]="Tell Check2"+str(out_ok)

        for blacklist_domain_n in g_val.blacklist_domain:
            #print(blacklist_domain_n,main_ulr)
            if(main_ulr=="-"or main_ulr=="" or main_ulr==None):break
            if(blacklist_domain_n=="-"or blacklist_domain_n=="" or blacklist_domain_n==None):break

            if(blacklist_domain_n in main_ulr):
                out_ok=0
                break

        print("ブラックリストdomainチェック",out_ok) 
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"]="ブラックリストdomainチェック"+str(out_ok)
        else:
            g_val.window_log["text"]="Domain check"+str(out_ok)
        g_val.data_log_write(g_val.window_log["text"])
        for blacklist_domain_n in g_val.blacklist_domain:
            print(blacklist_domain_n,url_gaiyou)
            if(blacklist_domain_n=="-"or blacklist_domain_n=="" or blacklist_domain_n==None):break
            if(url_gaiyou=="-"or url_gaiyou=="" or url_gaiyou==None):break
            if(blacklist_domain_n in url_gaiyou):

                url_gaiyou=""
                break

        if("https://www.google.com/maps/place" in main_ulr):
            main_ulr="-"

        # if(mail_=="-" or mail_=="" or mail_==None):
        #     if(url_gaiyou=="-" or url_gaiyou=="" or url_gaiyou==None):
        #         if(bangou_=="-" or bangou_=="" or bangou_==None):
        #             out_ok=0
        g_val.data_log_write("Old List check"+str(out_ok))

        if(mail_=="-"):mail_=""
        if(url_gaiyou=="-" ):url_gaiyou=""
        if(bangou_=="-" ):bangou_=""
        if(Fax_=="-" ):Fax_=""


        g_val.data_log_write("SYS_ERR Check"+str(out_ok))

        if(g_val.stop_==1):return 0

        if(main_ulr=="-"):
            main_ulr =""
            
        
        out_googel_list = []
        out_googel_list.append(out_ok)#0:OK_NG
        out_googel_list.append(titel_)#会社名
        out_googel_list.append(main_ulr)#会社HP
        out_googel_list.append(url_get)#google サイトURL
        out_googel_list.append(url_gaiyou)#問い合わせURL
        out_googel_list.append(kategori_)#1:kategori_
        out_googel_list.append(jyuusyo_)#住所
        out_googel_list.append(mail_)#メール
        out_googel_list.append(bangou_)#電話
        out_googel_list.append(Fax_)#FAX
        out_googel_list.append(h_hyouka)#評価
        out_googel_list.append(kuchikomi_)#口コミ
        out_googel_list.append(eigyou_mon)#月
        out_googel_list.append(eigyou_tue)#火
        out_googel_list.append(eigyou_wed)#水
        out_googel_list.append(eigyou_thu)#木
        out_googel_list.append(eigyou_fri)#金
        out_googel_list.append(eigyou_sta)#土
        out_googel_list.append(eigyou_sun)#日
        print("out_google_list: ", out_googel_list)
        print("**************")
        return out_googel_list
    
    except:
        if(g_val.stop_==1):return 0
        sleep(1)
        traceback.print_exc()
        g_val.data_log_write(datetime.datetime.now())
        g_val.data_log_write(traceback.format_exc())
        g_val.retry_+=1
        #エラー時はリトライ
        ##########################################################
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"]="検索エラーリトライ中"
        else:
            g_val.window_log["text"]="Rety reserch because of error"
        g_val.data_log_write(g_val.window_log["text"])
        ##########################################################

        

        while(1):
            if(g_val.stop_==1):return 0
            if(g_val.retry_>=2):
                g_val.retry_=0
                break
            try:
                ##########################################################
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="検索エラー立ち上げ中"
                else:
                    g_val.window_log["text"]="ReopenDrive for recovery error"
                g_val.data_log_write(g_val.window_log["text"])
                ##########################################################

                try:
                    g_val.driver.quit()
                except:
                    temp_=1
                #エラー時はリトライ
                # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                g_val.driver = webdriver.Chrome(options=g_val.option,service=chrome_service)
                g_val.driver.set_page_load_timeout(180)
                g_val.driver.get("https://www.google.co.jp/")
                #break
                
                #li_n0-=1
                break
            except:
                sleep(60)
                temp_=1
                print("エラー待機")
                traceback.print_exc()
                g_val.data_log_write(datetime.datetime.now())
                g_val.data_log_write(traceback.format_exc())
                ##########################################################
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="検索エラー待機中"
                else:
                    g_val.window_log["text"]="Withing for recovery error"
                g_val.data_log_write(g_val.window_log["text"])
                ##########################################################
        return 1 #リトライ

