def val_list_duda_get():
    import traceback
    try:
        import datetime
        import g_val
        g_val.list_init()
        
        import os,sys

        from time import sleep

        import random
        import re
        import time
        from time import sleep

        import pathlib
        
        from selenium import webdriver
        from time import sleep
        from selenium.webdriver.chrome.options import Options
        import copy
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        if("Windows"==g_val.OS_VERSION):
            from subprocess import CREATE_NO_WINDOW

        # xcel操作
        # xcel操作
        #import openpyxl as px
        import openpyxl as px
        import shutil
        from tkinter import messagebox
        import tkinter
        #クロームドライバ
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"] ="収集開始"
        else:
            g_val.window_log["text"] ="Listing Start"

        proxy_="--proxy-server="+g_val.proxy_txt_rntry.get().replace('\\n', '').replace('\n', '')
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"] ="プロキシチェック"
        else:
            g_val.window_log["text"] ="Proxy Checking"
        
        print("プロキシ",proxy_)
        print("プロキシチェック")
       
        g_val.proxy_try_ok=0
        option_t = Options()  
        if(g_val.dbg_==0):
            option_t.add_argument('--headless')

        option_t.add_argument(proxy_)
        option_t.add_argument('log-level=3') 
        option_t.add_argument('--disable-gpu')
        option_t.add_argument('--no-sandbox')
        option_t.add_argument('--disable-dev-shm-usage')

        chrome_service = Service(g_val.d_path)
        if("Windows"==g_val.OS_VERSION):
            chrome_service.creationflags = CREATE_NO_WINDOW 
        
        try:
            driver_t = webdriver.Chrome(g_val.d_path,options=option_t,service=chrome_service)#
        except:
            g_val.err_message_w(1,"error")
            
            return
        
        proxy_get = g_val.proxy_txt_rntry.get().replace('\\n', '').replace('\n', '')
        if(proxy_get == ""or proxy_get =="TEST_PROXY"):
            g_val.window_log["text"] ="Proxy check skip"
            print("Proxy check skip")

        else:
            try:
                driver_t.get("http://google.com")
                st =time.time()
                while(1):
                    now = time.time() -st
                    if(now>=3 or re.sub("-| |  ","",g_val.proxy_txt_rntry.get().replace('\\n', '').replace('\n', ''))==""):
                        break
                    el = driver_t.find_elements(By.XPATH,'//*[@value="Google 検索"]')
                    if(len(el)>0):
                        g_val.proxy_try_ok=1
                        break
                driver_t.quit()
            except:
                g_val.proxy_try_ok=0

        if(g_val.proxy_try_ok==1):
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="プロキシ設定OK"
                print("プロキシ設定OK")
                g_val.text_st_f1["text"]="プロキシ設定：有効"
            else:
                g_val.window_log["text"] ="Proxy setting OK"
                g_val.text_st_f1["text"]="Proxy setting : Valid"

        else:
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="プロキシ設定NG"
                print("プロキシ設定NG")
                g_val.text_st_f1["text"]="プロキシ設定：無効"
            else:
                g_val.window_log["text"] ="Proxy setting NG"
                g_val.text_st_f1["text"]="Proxy setting : Invalid"



        g_val.option = Options()                          # オプションを用意
        g_val.option.page_load_strategy = 'eager'
        
        #g_val.dbg_=1#################test

        if(g_val.dbg_==0):
            g_val.option.add_argument('--headless')           # ヘッドレスモードの設定を付与
        g_val.option.add_argument('--disable-gpu')
        g_val.option.add_argument('--no-sandbox')
        g_val.option.add_argument('--disable-dev-shm-usage')
        g_val.option.add_argument('--ignore-certificate-errors')
        g_val.option.add_argument('--allow-running-insecure-content')
        g_val.option.add_argument('--disable-web-security')
        g_val.option.add_argument('--disable-desktop-notifications')
        g_val.option.add_argument("--disable-extensions")
        g_val.option.add_argument('--blink-settings=imagesEnabled=false')
        g_val.option.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36') 
        g_val.option.add_argument('log-level=3')

        if(g_val.proxy_try_ok==1):   
            g_val.option.add_argument(proxy_)
        #エラ-のとき
        g_val.option0 = Options()                          # オプションを用意
        #option.page_load_strategy = 'eager'
        #option0.page_load_strategy = 'none'
        g_val.option0.add_argument('--disable-gpu')
        g_val.option0.add_argument('--no-sandbox')
        g_val.option.add_argument('--disable-dev-shm-usage')
        g_val.option0.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36') 
        g_val.option0.add_argument('log-level=3')
        if(g_val.proxy_try_ok==1):  
            g_val.option0.add_argument(proxy_)
        #g_val.option0.add_argument("--proxy-server=socks5://127.0.0.1:9150")

        
        g_val.campany_list=[]
        campany_list_ipage=[]
        
        if not os.path.isfile(g_val.log_tem_f):
            with open(g_val.log_tem_f, mode='w',encoding="utf_8_sig") as f:#,newline='\n'
                f.write("IZANAMI LOG ")

        g_val.data_log_write(datetime.datetime.now())
        g_val.data_log_write(g_val.window_log["text"])
        
        g_val.driver =""

        if(g_val.stop_==1):
            #g_val.driver.quit()
            g_val.program1_end=1
            sleep(1)
            return

        g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
        # ページロードされるまでのタイムアウトを 30秒 に設定
        g_val.driver.set_page_load_timeout(180)
        g_val.driver.maximize_window()
        
        if(g_val.stop_==1):
           
            g_val.program1_end=1
            g_val.driver.quit()
            sleep(1)
            return

        randamu_n=0
        randum_t_=0
        randum_t_max=5

        kyuukei_t=0
        kyuukei_t_max=50
            
        skip_ok=0
        skip_ok1=0

        skip_ok=0
        skip_ok1=0

        #検索画面に遷移
        option_t1 = Options()  
        #option_t1.add_argument('--headless')

        #option_t1.add_argument(proxy_)
        option_t1.add_argument('log-level=3') 
        option_t1.add_argument('--disable-gpu')
        option_t1.add_argument('--no-sandbox')
        option_t1.add_argument('--disable-dev-shm-usage')

        chrome_service = Service(g_val.d_path)
        if("Windows"==g_val.OS_VERSION):
            chrome_service.creationflags = CREATE_NO_WINDOW 
    
        if(g_val.re_run_==1 and len(g_val.url_log_his)>4):
            #途中から再開
            g_val.reserch_url_log = g_val.url_log_his
            print("途中から再開",g_val.url_log_his)
        else: 
            try:
                driver_t1 = webdriver.Chrome(g_val.d_path,options=option_t1,service=chrome_service)#
            except:
                g_val.err_message_w(1,"error")
                return
    
            messagebox.askyesno('確認', '条件を選択したら「この条件で検索する」を押して下さい。')
            url_ ="https://doda.jp/DodaFront/View/JobSearchTop.action?usrclk=PC_logout_kyujinSearchArea_kyujinSearchDetail"
            driver_t1.get(url_)

            
            st = time.time()
            while(1):
                #now = time.time() - st
                #if(now>3600):break

                els = driver_t1.find_elements_by_xpath('//p[contains(text(),"該当求人数")]')
                if(len(els)>0):
                    for eln in els:
                        g_val.reserch_url_log = driver_t1.current_url
                        break
                    break
            #driver_t1.get(main_ulr)
            driver_t1.quit()

        print(g_val.reserch_url_log)
        
        
        #sleep(100)
        while(1):#カテゴリ

            main_ulr = g_val.reserch_url_log
            #ログ書き込み
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="ログ書き込み"
            else:
                g_val.window_log["text"] ="Log Writing"
            
            print("ログ書き込み前")
            g_val.data_log_write(g_val.window_log["text"])

            print("ログ書き込み後")
            g_val.campany_list=[]
            campany_list_old=[]

            if(g_val.stop_==1):
                
                g_val.program1_end=1
                g_val.driver.quit()
                sleep(1)
                return
            #ログとり
            g_val.conf_log_save()
            
            try:
                
                
                while(1):
                    handle_array = g_val.driver.window_handles
                    if(len(handle_array)==1):break
                    else:
                        g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                        g_val.driver.close()
                        sleep(0.5)
                g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                #g_val.driver.get(log_url_)
                #
                #driver.switch_to.window(driver.window_handles[-1])
                g_val.C_CODE="JA"
                g_val.driver.get(main_ulr)
                url_ =main_ulr#"https://www.google.co.jp/maps/search/"+category_n+" "+re.sub("  "," ",sikutyouson_n)
                kategory_=""
                #カテゴリとURLリストをわたす
                #次のページをログURL
                
                if(g_val.stop_==1):
                    
                    g_val.program1_end=1
                    g_val.driver.quit()
                    sleep(1)
                    return

                try:
                    st = time.time()
                    while(1):
                        now = time.time() - st
                        if(now>3):break

                        #els = g_val.driver.find_elements_by_xpath('//span[@class="ckWrapB_Lbox"]/label')

                        els = g_val.driver.find_elements(By.XPATH,'//span[@class="ckWrapB_Lbox"]/label')
                        #els = g_val.driver.find_elements(By.XPATH,'//section[@id="shStart"]//h1')
                        if(len(els)>0):
                            for eln in els:
                                print(eln.text)
                                kategory_ = eln.text#(eln.text).split(" の")[0]
                                break
                            break
                except:
                    traceback.print_exc()
                
               
                try:
                    if("正社員" in eln.text):
                        kategory_=""

                    print(kategory_)

                    if(" (" in kategory_):
                        kategory_ = kategory_.split(" (")[0]
                except:
                    kategory_=""
                    traceback.print_exc()
                print("カテゴリ取得",kategory_)
                els =g_val.driver.find_elements(By.XPATH,'//*[@class="title clrFix"]')
                
                st = time.time()
                while(1):
                    now = time.time() - st
                    if(now>20):break
                    if(len(els)>0):
                        print(len(els))
                        for eln in els:
                            try:
                                url_= re.sub("-tab__pr","-tab__jd",eln.find_element_by_xpath('a').get_attribute('href'))
                                titel_=re.sub("NEW","",eln.find_element_by_xpath('a/span').text)
                                if("締切間近" in titel_):
                                    titel_ = titel_.split("締切間近")[0]
                                if("("in titel_):
                                     titel_ = titel_.split("(")[0]
                                if("（"in titel_):
                                     titel_ = titel_.split("（")[0]
                                
                                print("リスト",url_,"title",titel_)
                                list_all_a=[]
                                cal =1
                                for list_all_n in g_val.campany_list:
                                    if(list_all_n[0]==titel_ or list_all_n[1]==url_):
                                        cal=0
                                        break
                                if(cal==1):
                                    list_a=[]
                                    list_a.append(titel_)
                                    list_a.append(url_)
                                    list_a.append(kategory_)
                                    list_a.append("-  -")
                                    g_val.campany_list.append(copy.deepcopy(list_a))
                                    print("=========================list_get==================================")
                                    print(list_a)
                                    g_val.window_log["text"] =list_a
                                    g_val.data_log_write(g_val.window_log["text"])
                                    print("===================================================================")
                            except:
                                traceback.print_exc()
                                g_val.data_log_write(datetime.datetime.now())
                                g_val.data_log_write(traceback.format_exc())
                        break

                #g_val.driver.re
                #break##################(test)########################################
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"] ="キーワード検索 終了 "
                else:
                    g_val.window_log["text"] ="Key word reserch end "
                g_val.data_log_write(g_val.window_log["text"])
                print("キーワード検索 終了 ")
                #詳細検索開始
                print(g_val.campany_list)
                g_val.window_log["text"] =g_val.campany_list
                g_val.data_log_write(g_val.window_log["text"])
                print("====================================================")

               
                #############test#####################################################
                if(0):
                    list_a=[]
                    g_val.campany_list=[]
                    list_a.append("東洋水産㈱ 北海道第一工場")
                    list_a.append("https://www.google.co.jp/maps/place/%E6%9D%B1%E6%B4%8B%E6%B0%B4%E7%94%A3%E3%88%B1+%E5%8C%97%E6%B5%B7%E9%81%93%E7%AC%AC%E4%B8%80%E5%B7%A5%E5%A0%B4/data=!4m7!3m6!1s0x5f0b2408a850c113:0x6193816e4c89c310!8m2!3d43.1772104!4d141.2681148!16s%2Fg%2F11c6cq_b7v!19sChIJE8FQqAgkC18REMOJTG6Bk2E?authuser=0&hl=ja&rclk=1")
                    list_a.append("企業オフィス")
                    list_a.append("北海道  小樽市")
                    g_val.campany_list.append(copy.deepcopy(list_a))

                

                if(g_val.stop_==1):
                    #wb_i.close
                    g_val.driver.quit()
                    g_val.program1_end =1
                    sleep(1)
                    #exit()
                    return
                
                
                reserch_end=1
                #次のページのURLを取得して次に渡す。
                #次のページがない場合は終了。
                reserch_url_log_=""
                els =g_val.driver.find_elements(By.XPATH,'//li[@class="btn_r last"]/a')
                
                st = time.time()
                while(1):
                    now = time.time() - st
                    if(now>20):break
                    if(len(els)>0):
                        print(len(els))
                        for eln in els:
                            reserch_end=0
                            reserch_url_log_ = eln.get_attribute('href')
                            break
                        break

                val_get_duda(g_val.campany_list)#######rest
                print("詳細完了")
                
                
            except:
                #エラー時はリトライ
                traceback.print_exc()
                g_val.data_log_write(datetime.datetime.now())
                g_val.data_log_write(traceback.format_exc())

                if(g_val.stop_==1):
                    g_val.driver.quit()
                    g_val.program1_end=1
                    sleep(1)
                    return
                while(1):
                    if(g_val.stop_==1):
                        g_val.driver.quit()
                        g_val.program1_end=1
                        sleep(1)
                        return

                    try:
                        print("エラー待機111111")
                        try:
                            g_val.driver.quit()
                        except:
                            temp_=1
                        #エラー時はリトライ
                        g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                        g_val.driver.set_page_load_timeout(180)
                        g_val.driver.get("https://www.google.co.jp/")
                        #break
                        
                        #siku_n-=1
                        break
                    except:
                        sleep(60)
                        temp_=1
                        print("エラー待機11111111")
                continue
                    
            
            
            g_val.reserch_url_log = reserch_url_log_
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="ログ保存"
            else:
                g_val.window_log["text"] ="Log saveing"
            g_val.data_log_write(g_val.window_log["text"])
    
            g_val.conf_log_save()

            if(reserch_end==1):#次のページがないとき検索完了
                break
            print("終了フラグ::",reserch_end)
            #break#####################test

        #print(campany_list)
        g_val.driver.quit()
        g_val.program1_end=1
        #wb_i.close
        print("検索終了")
        return
    except:
        traceback.print_exc()
        g_val.data_log_write(datetime.datetime.now())
        g_val.data_log_write(traceback.format_exc())

        #エラー時はリトライ
            
        try:
            g_val.driver.quit()
        except:
            temp_=1

    
#dudaの詳細ページを検索
#そのあと、住所とurlで企業検索

#リスト取得
#情報収集
#詳細ページから企業名と住所取得
#googleアースで検索して企業URL取得
#企業URLから電話番号とEメールを取得

def val_get_duda(campany_list_in):
    import traceback
    try:
        from urllib.parse import urlparse
        import re
        import g_val
        import g_val_duda
        import g_fnc_google
        import random
        import csv
        import time
        from bs4 import BeautifulSoup,Comment
        
        from time import sleep
        import re
        from selenium import webdriver
        from time import sleep
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        if("Windows"==g_val.OS_VERSION):
            from subprocess import CREATE_NO_WINDOW
        chrome_service = Service(g_val.d_path)
        if("Windows"==g_val.OS_VERSION):
            chrome_service.creationflags = CREATE_NO_WINDOW

        import copy
        from tkinter import messagebox
        import datetime
        import requests
        import mojimoji
        from urllib.parse import urlparse

        if(g_val.conf_email):
            toiawase_page=["概要","会社","campany","CAMPANY","Campany","問い合わせ","問合わせ","問合せ","contact","Contact","CONTACT","contatto"]
        
        else:
            toiawase_page=["問い合わせ","問合わせ","問合せ","contact","Contact","CONTACT","contatto"]
        toiawase_domain=["contact","inquiry","form",]

        campany_list =campany_list_in

        #return#tet
        #揺らぎ設定
        randamu_n=0
        randum_t_=0
        randum_t_max=5

        kyuukei_t=0
        kyuukei_t_max=50
    
        jyuusyo_="-"
        yubin_="-"
        bango_="-"
        No=0
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.window_log["text"] ="詳細検索init"
        else:
            g_val.window_log["text"] ="Detail reserching"
        g_val.data_log_write(g_val.window_log["text"])
        print("詳細検索init")
        print(campany_list)
        cal_eria_num=0
        li_n0=0
        while(1):
            li_n0+=1
            if(li_n0>len(campany_list)):
                break
            print(li_n0)
            campany_list_n = campany_list[li_n0-1]
            print(campany_list_n)
        #for campany_list_n in campany_list:#if(len(campany_list)>0):
            try:
                if(g_val.stop_==1):return 0       
                #x = random.randint(2,5)
                #sleep(x)
                #ゆらぎ
                #1秒で10回やったら次はランダム回数で4秒
                if(g_val.bl_yuragi.get()== 0):
                    print("ゆらぎあり")
                    if(randamu_n==0):
                        sleep(1)
                        randum_t_ +=1
                        if(randum_t_>=4):
                            randum_t_max=random.randint(5,10)
                            randamu_n=1
                            randum_t_=0
                    else:
                        randum_t_+=1
                        sleep(4)
                        if(randum_t_>=randum_t_max):
                            randamu_n=0
                            randum_t_=0
                            
                    if(kyuukei_t >kyuukei_t_max):
                        kyuukei_t=0
                        kyuukei_t_max=random.randint(50,150)
                        sleep(10)
                    #休憩50から150らんだむで10秒休憩

                
                campany_name =""
                yubin_ ="-"
                jyuusyo_ ="-"
                mail_ ="-"
                bangou_ ="-"
                Fax_="-"
                daihyousya_="-"
                get_list_a=[]
                No +=1

                #csvファイルを読み込み
                out_list_t=[]
                if(g_val.Op_ok==0):
                    if("Windows"==g_val.OS_VERSION):
                        #path_o_csv_cat  = g_val.path1+"\\..\\out\\result_"+str(campany_list_n[2])+".csv"
                        
                        path_o_csv_cat  = g_val.path1+"\\..\\out\\result_doda"+str(campany_list_n[2])+".csv"
                    else:
                        #path_o_csv_cat  = g_val.path1+"/../out/result_"+str(campany_list_n[2])+".csv"
                        path_o_csv_cat  = g_val.path1+"/../out/result_doda"+str(campany_list_n[2])+".csv"

                else:
                    if("Windows"==g_val.OS_VERSION):
                        path_o_csv_cat  = g_val.path1+"\\..\\out\\result_doda_"+str(campany_list_n[2])+"_OP.csv"
                        #path_o_csv_cat  = g_val.path1+"\\..\\out\\result_DUDA_OP.csv"
                    else:
                        path_o_csv_cat  = g_val.path1+"/../out/result_doda_"+str(campany_list_n[2])+"_OP.csv"
                        #path_o_csv_cat  = g_val.path1+"/../out/result_DUDA_OP.csv"
                n=0
                try:
                    with open(path_o_csv_cat,newline='', encoding='utf_8_sig') as f:

                        reader = csv.reader(f)
                        #print(reader)
                        #csvファイルのデータをループ
                        n=0
                        for row in reader:
                            n+=1
                            if(n==1):continue#ヘッダー飛ばす
                            out_list_t.append(row)#A列
                            #g_val.list_out_all.append(row)
                            #print(row)
                    #print(out_list_t)
                except:
                    out_list_t=[]

                if(n==0):
                    
                    open_out = open(path_o_csv_cat,'a',newline="", encoding='utf_8_sig')#utf_8_sig
                    file_o_csv = csv.writer(open_out, delimiter=',')
                    if(g_val.Op_ok==0):
                        file_o_csv.writerow(g_val_duda.duda_header_nominal)
                    else:
                        file_o_csv.writerow(g_val_duda.duda_header_op)
                            
                    
                    open_out.close()
                if(g_val.stop_==1):return 0   

                list_n = campany_list_n[1]
                url_get = list_n
                url_ = list_n

                cal_llist=1
                for out_list_t_l in out_list_t:
                    if(url_  in out_list_t_l[10]):
                        cal_llist =0
                        break
                if cal_llist ==0 :
                    #del campany_list[0]
                    continue

                #企業URL取得
                g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                g_val.driver.get(url_get)
                titel_=campany_list_n[0]
                print("===========================================================")
                print("詳細解析",campany_list_n)
                g_val.window_log["text"] =campany_list_n
                g_val.data_log_write(g_val.window_log["text"])
                print("===========================================================")
                #ggogl earthで検索
                if(g_val.stop_==1):return 0      
                sisetu_   = titel_
                
                main_ulr ="-"
                toiawase_url ="-"

                #ロボットの可能性あり。
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    els = g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"このページが表示された理由")]')
                else:
                    els = g_val.driver.find_elements(By.XPATH,'//*[contains(text(),"Why this page was displayed")]')
                if(len(els)>0):
                    #ロボットの可能性アリ
                    g_val.driver.quit()
                    g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option0,service=chrome_service)
                    g_val.driver.set_page_load_timeout(180)
                    g_val.driver.get(url_)
                    sleep(1)
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        messagebox.askyesno('確認', 'ブラウザを確認してください')
                    else:
                        messagebox.askyesno('Confirmination', 'Please check your browser')
                    g_val.driver.quit()
                    g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                    g_val.driver.set_page_load_timeout(180)
                if(g_val.stop_==1):return 0      

                try:
                    
                    url_ = url_get
                    g_val.driver.get(url_)

                    #################DUDAここにいれる######################################
                    try:
                        duda_locate_=""
                        duda_HP_url_=""
                        duda_established=""
                        duda_president=""
                        duda_employees=""
                        duda_capital=""
                        duda_sales=""
                        duda_summary=""
                        #設立　'established':
                        #代表者 'president':
                        #従業員数 'employees':
                        #資本金 'capital':
                        #売上高 'sales':
                        #事業概要'summary':


                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break

                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"企業URL")]/..//a')
                            if(len(els)>0):
                                for eln in els:
                                    duda_HP_url_=eln.get_attribute('href')
                                    break
                                break
                        print("duda HP:",duda_HP_url_)

                        duda_locate_t=""
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            #els = g_val.driver.find_elements_by_xpath('//th[contains(text(),"勤務地")]/../td//*[contains(text(),"住所：")]')
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"所在地")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_locate_t=eln.text
                                    break
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"所在地")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_locate_t=eln.text
                                break
                        try:

                            t="(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村|日野)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)"
                            ret = re.compile(t)
                            temp= duda_locate_t
                            
                            if(re.search(" ",temp)):
                                tmp0= temp.split(" ")
                                for a in tmp0:
                                    if(re.search(t,a) ):
                                        duda_locate =re.search(t,a).group()
                                        break
                            else: 
                                if(re.search(t,temp)):
                                    duda_locate =re.search(t,temp).group()
                            duda_locate = re.sub("／|/|※","",duda_locate)
                        except:
                            print("エラー住所")
                            traceback.print_exc()
                            duda_locate ="-"
                            
                        print("duda住所:",duda_locate)
                        #都道府県と市区町村を抽出
                        matches = re.match(t, duda_locate)
                        campany_list_n[3] =matches[1]+"  "+matches[2]
                        print("duda住所:市区町村::",campany_list_n[3])
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"設立")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_established=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"設立")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_established=eln.text
                                break

                        print("duda設立:",duda_established)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"代表者")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_president=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"代表者")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_president=eln.text
                                break

                        print("duda代表者:",duda_president)
                        
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"従業員数")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_employees=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"従業員数")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_employees=eln.text
                                break

                        print("duda従業員数:",duda_employees)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"資本金")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_capital=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"資本金")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_capital=eln.text
                                break

                        print("duda_資本金:",duda_capital)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"売上高")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_sales=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"売上高")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_sales=eln.text
                                break

                        print("duda_売上高:",duda_sales)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements_by_xpath('//*[contains(text(),"事業概要")]/..//td')
                            if(len(els)>0):
                                for eln in els:
                                    duda_summary=eln.text
                                break
                            els1 = g_val.driver.find_elements_by_xpath('//*[contains(text(),"事業概要")]/..//dd')
                            if(len(els1)>0):
                                for eln in els1:
                                    duda_summary=eln.text
                                break

                        print("duda_事業概要:",duda_summary)

                        

                        
                    except:
                        traceback.print_exc()
                        continue
                        
                    
                    ################ DUDA END  ##########################################
                    #カテゴリ
                    #####################################################################
                    url_g ="https://www.google.co.jp/maps/search/"+titel_+" "+duda_locate
                    while(1):
                        handle_array = g_val.driver.window_handles
                        if(len(handle_array)==1):break
                        else:
                            g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                            g_val.driver.close()
                            sleep(0.5)
                    g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                    #g_val.driver.get(url_g)
                    
                except:
                    if(g_val.stop_==1):return 0
                    traceback.print_exc()
                    main_ulr ="-"
                #　　　　google 検索開始
                out_google_list = g_fnc_google.google_detail_reserch(url_g ,campany_list_n,duda_HP_url_)
                if(g_val.stop_==1):return 0
                if(out_google_list==0):continue #検索エラー
                elif(out_google_list==1):
                    li_n0-=1
                    continue #リトライ
                ##ここまで
                out_ok=out_google_list[0]
                main_ulr=out_google_list[2]#2会社HP
                url_get=out_google_list[3]#3google サイトURL
                url_gaiyou=out_google_list[4]#4問い合わせURL
                kategori_=out_google_list[5]#5:kategori_
                jyuusyo_=out_google_list[6]#6住所
                mail_=out_google_list[7]#7メール
                bangou_=out_google_list[8]#8電話
                Fax_=out_google_list[9]#9FAX
                h_hyouka=out_google_list[10]#10評価
                kuchikomi_=out_google_list[11]#11口コミ
                eigyou_mon=out_google_list[12]#12月
                eigyou_tue=out_google_list[13]#13火
                eigyou_wed=out_google_list[14]#14水
                eigyou_thu=out_google_list[15]#15木
                eigyou_fri=out_google_list[16]#16金
                eigyou_sta=out_google_list[17]#17土
                eigyou_sun=out_google_list[18]#18日
                
                if(g_val.Op_ok==1):#csv重複チェック
                    for out_list_t_l in out_list_t:
                        if(url_gaiyou=="-"or url_gaiyou=="" or url_gaiyou==None):break
                        if(url_gaiyou  in out_list_t_l[7]):
                        
                            out_ok =0
                            print(url_gaiyou,out_list_t_l[7])
                            break
                        
                if(out_ok==1):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        g_val.window_log["text"]="出力OK"
                    else:
                        g_val.window_log["text"]="Out OK"

                    g_val.data_log_write(g_val.window_log["text"])
                    
                    now = datetime.datetime.now()
                    get_year=str(now.year)
                    get_month = "00"+str(now.month)
                    get_day   ="00"+ str(now.day)
                    
                    today_ =get_year[-2:]+"/"+get_month[-2:]+"/"+get_day[-2:]

                    list_out_all_a=[]
                    list_out_all_db=[]
                    #header_ = ["設定カテゴリ","収集カテゴリ","ビジネス名","県","市","住所","URL","メール","フォーム","電話番号", "FAX","参照URL"]
                    #No = len(g_val.list_out_all)+1
                    list_out_all_a.append(campany_list_n[2])
                    list_out_all_db.append(campany_list_n[2])
                    list_out_all_a.append(kategori_.replace('の','',1) )
                    list_out_all_db.append(kategori_.replace('の','',1) )

                    list_out_all_a.append(titel_)
                    list_out_all_db.append(titel_)
                    list_out_all_a.append(campany_list_n[3].split("  ")[0])
                    list_out_all_db.append(campany_list_n[3].split("  ")[0])
                    list_out_all_a.append(campany_list_n[3].split("  ")[1])
                    list_out_all_db.append(campany_list_n[3].split("  ")[1])
                    list_out_all_a.append(jyuusyo_)
                    list_out_all_db.append(jyuusyo_)

                    if(g_val.login_ok == "free"):
                        
                        try:
                            parsed_url = urlparse(main_ulr)
                            http = parsed_url.scheme
                            domain = parsed_url.netloc
                            print(http)
                            test_ = main_ulr.split(http+"://",1)[1]
                            
                            o_=""
                            for s in test_:

                                if(s =="." or s =="/"):
                                    o_ = o_ +s
                                else:
                                    o_ = o_ +"*"

                            list_out_all_a.append(http+"://"+o_)
                        except:
                            traceback.print_exc()
                            list_out_all_a.append(main_ulr)
                        list_out_all_db.append(main_ulr)

                        o_=""
                        for s in mail_:

                            if(s =="." or s =="@"):
                                o_ = o_ +s
                            else:
                                o_ = o_ +"*"

                        list_out_all_a.append(o_)
                        list_out_all_db.append(mail_)
                        try:
                            parsed_url = urlparse(url_gaiyou)
                            http = parsed_url.scheme
                            domain = parsed_url.netloc
                            test_ = url_gaiyou.split(http+"://",1)[1]
                            print()
                            o_=""
                            for s in test_:

                                if(s =="." or s =="/"):
                                    o_ = o_ +s
                                else:
                                    o_ = o_ +"*"

                            if(g_val.Op_ok==1):
                                list_out_all_a.append(http+"://"+o_)
                        
                        except:
                            traceback.print_exc()
                            if(g_val.Op_ok==1):
                                list_out_all_a.append(url_gaiyou)

                        list_out_all_db.append(url_gaiyou)

                        o_=""
                        for s in bangou_:

                            if(s =="-"):
                                o_ = o_ +s
                            else:
                                o_ = o_ +"*"

                        list_out_all_a.append(o_)
                        list_out_all_db.append(bangou_)

                        o_=""
                        for s in Fax_:

                            if(s =="-"):
                                o_ = o_ +s
                            else:
                                o_ = o_ +"*"
                        list_out_all_a.append(o_)
                        list_out_all_db.append(Fax_)
                        
                        try:
                            parsed_url = urlparse(url_get)
                            http = parsed_url.scheme
                            domain = parsed_url.netloc
                            test_ = url_get.split(http+"://",1)[1]

                            o_=""
                            for s in test_:

                                if(s =="." or s =="/"):
                                    o_ = o_ +s
                                else:
                                    o_ = o_ +"*"

                            list_out_all_a.append(http+"://"+o_)
                        except:
                            traceback.print_exc()
                            list_out_all_a.append(url_get)
                            
                        list_out_all_db.append(url_get)

                    else:

                        
                        list_out_all_a.append(main_ulr)
                        list_out_all_db.append(main_ulr)
                        list_out_all_a.append(mail_)
                        list_out_all_db.append(mail_)

                        if(g_val.Op_ok==1):
                            list_out_all_a.append(url_gaiyou)
                        list_out_all_db.append(url_gaiyou)

                        list_out_all_a.append(bangou_)
                        list_out_all_db.append(bangou_)
                        list_out_all_a.append(Fax_)
                        list_out_all_db.append(Fax_)
                        
                        list_out_all_a.append(url_get)
                        list_out_all_db.append(url_get)

                    list_out_all_a.append(h_hyouka)
                    list_out_all_db.append(h_hyouka)
                    list_out_all_a.append(kuchikomi_)
                    list_out_all_db.append(kuchikomi_)
                    
                    list_out_all_a.append(eigyou_mon)
                    list_out_all_db.append(eigyou_mon)
                    list_out_all_a.append(eigyou_tue)
                    list_out_all_db.append(eigyou_tue)
                    list_out_all_a.append(eigyou_wed)
                    list_out_all_db.append(eigyou_wed)
                    list_out_all_a.append(eigyou_thu)
                    list_out_all_db.append(eigyou_thu)
                    list_out_all_a.append(eigyou_fri)
                    list_out_all_db.append(eigyou_fri)
                    list_out_all_a.append(eigyou_sta)
                    list_out_all_db.append(eigyou_sta)
                    list_out_all_a.append(eigyou_sun)
                    list_out_all_db.append(eigyou_sun)


                    list_out_all_a.append(duda_established)
                    list_out_all_db.append(duda_established)
                    list_out_all_a.append(duda_president)
                    list_out_all_db.append(duda_president)
                    list_out_all_a.append(duda_employees)
                    list_out_all_db.append(duda_employees)
                    list_out_all_a.append(duda_capital)
                    list_out_all_db.append(duda_capital)
                    list_out_all_a.append(duda_sales)
                    list_out_all_db.append(duda_sales)
                    list_out_all_a.append(duda_summary)
                    list_out_all_db.append(duda_summary)

                    list_out_all_a.append(campany_list_n[1])#27比較できるようにURL表示
                    list_out_all_db.append(campany_list_n[1])#27

                
                    
                    #g_val.list_out_all.append(copy.deepcopy(list_out_all_a))
                    import requests
    
                    # defining the api-endpoint 
                    API_ENDPOINT = "https://system.izanami.link/api/registerData"
                    data = {
                    'user_name':'TEST_DUDA',
                    'email':g_val.E_mail,

                    'country_code': g_val.C_CODE,
                    'setting_category':list_out_all_db[0],
                    'getting_category':list_out_all_db[1],
                    'business_name':list_out_all_db[2],
                    'province':list_out_all_db[3],
                    'city':list_out_all_db[4],
                    'address':list_out_all_db[5],
                    'url':list_out_all_db[6],
                    'mail_address':list_out_all_db[7],
                    'form_url':list_out_all_db[8],
                    'phone_number':list_out_all_db[9],
                    'fax_number':list_out_all_db[10],
                    'ref_url':list_out_all_db[11],
                    'average_count':list_out_all_db[12],
                    'logo_count':list_out_all_db[13],
                    'business_hours_mon':list_out_all_db[14],
                    'business_hours_tue':list_out_all_db[15],
                    'business_hours_wed':list_out_all_db[16],
                    'business_hours_thu':list_out_all_db[17],
                    'business_hours_fri':list_out_all_db[18],
                    'business_hours_sat':list_out_all_db[19],
                    'business_hours_sun':list_out_all_db[20],
                    'established':list_out_all_db[21],
                    'president':list_out_all_db[22],
                    'employees':list_out_all_db[23],
                    'capital':list_out_all_db[24],
                    'sales':list_out_all_db[25],
                    'summary':list_out_all_db[26],
                    'dudaurl':list_out_all_db[27],
                    }
                    try:
                        if(1):#test_
                            r = requests.post(url = API_ENDPOINT, data = data)###############test
                            res = r.json()
                            print("===SERVER===================")
                            print(res["result"],res["value"])
                            print("===SERVER===================")

                            print(data)
                            #g_val.time_now_err = time.time()
                            #g_val.time_now_err_old = g_val.time_now_err
                        time_now_mum=0
                    except:
                        if(time_now_mum==0):
                            time_now_mum=1
                            g_val.time_now_err_old = time.time()

                        g_val.time_now_err = time.time()
                        if(g_val.time_now_err- g_val.time_now_err_old )>=3600:
                            print("認証失敗")
                            cm="認証に失敗しました"
                            cm+="\nIZANAMIはその特性上、収集時にデータ整合性を保つために認証を行っております。"
                            cm+="\n詳しくは以下のFAQをご覧ください。"
                            cm+="\n\nhttps://izanami.link/faq/howtouse/shuushuu/ninshou-error.html"

                            cm_e="Certification failed."
                            cm_e+="\nIZANAMI performs authentication to maintain data integrity at the time of collection."
                            cm_e+="\nRefer to  the FAQ below for details."
                            cm_e+="\n\nhttps://izanami.link/faq/howtouse/shuushuu/ninshou-error.html"

                            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                                messagebox.showinfo("警告", cm)
                            else:
                                messagebox.showinfo("Attention",cm_e)
                
                    print("====================CSVOUT====================")
                    
                    #print(list_out_all_a)
                    g_val.window_log["text"]=list_out_all_a
                    g_val.data_log_write(g_val.window_log["text"])
                    #free
                    #g_val.csv_free_ok=1
                    if(g_val.Flag_free_licence==0):
                        if(res["result"]=="error" and res["value"]=="expired"):
                            g_val.csv_free_ok=0
                    print("GET FREE JUDGE : ",g_val.csv_free_ok)
                    #print("Free num:",g_val.list_out_num,"OKNG:",g_val.csv_free_ok)
                    if(g_val.csv_free_ok==1):       
                        open_out = open(path_o_csv_cat,'a',newline="", encoding='utf_8_sig')
                        file_o_csv = csv.writer(open_out, delimiter=',')
                        file_o_csv.writerow(list_out_all_a)
                        open_out.close()
                    
                    #open_out = open(path_o_csv_cat,'a',newline="", encoding='utf_8_sig')
                    #file_o_csv = csv.writer(open_out, delimiter=',')
                    #file_o_csv.writerow(list_out_all_a)
                    #open_out.close()

                    print("==============================================")
                g_val.retry_=0
                if(g_val.stop_==1):return 0
                while(1):
                    handle_array = g_val.driver.window_handles
                    if(len(handle_array)==1):break
                    else:
                        g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                        
                        g_val.driver.close()
                        sleep(0.5)
                ##########################################################
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    g_val.window_log["text"]="詳細検索 完了"
                else:
                    g_val.window_log["text"]="Finish detail reserch"
                g_val.data_log_write(g_val.window_log["text"])
                ##########################################################

                
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
                        g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                        g_val.driver.set_page_load_timeout(180)
                        g_val.driver.get("https://www.google.co.jp/")
                        #break
                        
                        li_n0-=1
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

        return 0
    except:
        traceback.print_exc()
        g_val.data_log_write(datetime.datetime.now())
        g_val.data_log_write(traceback.format_exc())

        #エラー時はリトライ
            
        try:
            g_val.driver.quit()
        except:
            temp_=1




############################################################################################################################
#########################################################################################################################################

