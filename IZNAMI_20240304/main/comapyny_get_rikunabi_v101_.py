def val_list_rikunabi_get():
    import traceback
    try:
        import datetime
        import g_val
        g_val.list_init()
        
        import os,sys

        from time import sleep
        
        import math
        import random
        import requests
        from bs4 import BeautifulSoup
        import urllib.parse
        import re
        import time

        import pathlib
        
        from selenium import webdriver
        from time import sleep
        from selenium.webdriver.chrome.options import Options
        import copy
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        
        base_url = "https://next.rikunabi.com"
        
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
            # driver_t = webdriver.Chrome(g_val.d_path,options=option_t,service=chrome_service)#
            driver_t = webdriver.Chrome(options=option_t, service=chrome_service)#
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
        
        driver_t.quit()

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

        # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
        g_val.driver = webdriver.Chrome(options=g_val.option, service=chrome_service)
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
    
        print('g_val.re_run', g_val.re_run_)
        print('g_val.url_log_his', g_val.url_log_his)
        
        
        if(g_val.re_run_==1 and len(g_val.url_log_his)>4):
            #途中から再開
            g_val.reserch_url_log = g_val.url_log_his
            print("途中から再開",g_val.url_log_his)
            
            g_val.condition_type = remove_duplicates(g_val.condition_type)
            g_val.condition_area = remove_duplicates(g_val.condition_area)
            g_val.condition_other = remove_duplicates(g_val.condition_other)
            
            print(g_val.condition_type)
            print(g_val.condition_area)
            print(g_val.condition_other)
            print(g_val.page)
            
            ##################################### 保管した条件選択 #####################################
            try:
                # g_val.driver_t1 = webdriver.Chrome(g_val.d_path,options=option_t1,service=chrome_service)#
                g_val.driver_t1 = webdriver.Chrome(options=option_t1, service=chrome_service)#
            except:
                g_val.err_message_w(1,"error")
                return
            url_ = "https://next.rikunabi.com/lst/?leadtc=n_ichiran_panel_submit_btn"
            url_ = g_val.url_log_his

            g_val.driver_t1.get(url_)
            
            time.sleep(2)
            
            # if len(g_val.condition_type)>0:
            #     sel_element = g_val.driver_t1.find_elements(By.CLASS_NAME, "rn3-sideConditionalSearch__buttonAction")
            #     if len(sel_element)>1:
            #         job_element = sel_element[0]
            #         job_element.click()
                    
            #     for type1 in g_val.condition_type:    
            #         element = g_val.driver_t1.find_elements(By.XPATH, "//p[contains(text(),'" + type1 + "')]")
            #         if len(element)>0:
            #             job_element = element[0]
            #             job_element.click()
                    
            #     time.sleep(3)
                    
            #     g_val.driver_t1.find_element(By.XPATH, "//div[contains(text(),'件を検索')]").click()

            #     time.sleep(3)
            
            # area = g_val.condition_area
            # if len(area)>0:
            #     sel_element = g_val.driver_t1.find_elements(By.CLASS_NAME, "rn3-sideConditionalSearch__buttonAction")

            #     if len(sel_element)>1:
            #         area_element = sel_element[1]
            #         area_element.click()
                    
            #     time.sleep(3)

            #     element = g_val.driver_t1.find_elements(By.CLASS_NAME, "searchModalCategory__item--area")
            #     if len(element)>0:
            #         for els in element:
            #             els.click()
            #             xpath = "//span["
            #             for value in area:
            #                 xpath += "contains(text(),"
            #                 xpath += f" '{value}') or "
            #             xpath = xpath[:-4] + "]"
            #             check = g_val.driver_t1.find_elements(By.XPATH, xpath)
            #             if len(check) > 0:
            #                 check[0].click()
            #         time.sleep(5)
            #         g_val.driver_t1.find_element(By.XPATH, "//div[contains(text(),'件を検索')]").click()
            
            # if len(g_val.condition_other)>0:
            #     for condition in g_val.condition_other:
            #         element = g_val.driver_t1.find_element(By.XPATH, f"//span[contains(text(), '{condition}')]")
            #         g_val.driver_t1.execute_script("arguments[0].click();", element)
            #         print("clicked", condition)
            #         time.sleep(0.5)
            #     # g_val.driver_t1.find_element(By.XPATH, "//button[@type='submit']").click()
            #     # button = g_val.driver_t1.find_elements(By.XPATH, "//button[@class='rn3-sideConditionalSearch__buttonSearch js-searchButton rnn-textM rnn-textBold']")[0].click()
            #     button = g_val.driver_t1.find_elements(By.CLASS_NAME, "rn3-sideConditionalSearch__buttonSearch.js-searchButton.rnn-textM.rnn-textBold")
            #     print(len(button))
            #     button[0].click()
            #############################################################################################
            if int(g_val.page)>1:
                for i in range(int(g_val.page)-1):
                    g_val.driver_t1.find_elements(By.CLASS_NAME, "rnn-inlineBlock.rnn-pagination__button")[1].click()
                    time.sleep(1)
        else: 
            try:
                # g_val.driver_t1 = webdriver.Chrome(g_val.d_path,options=option_t1,service=chrome_service)#
                g_val.driver_t1 = webdriver.Chrome(options=option_t1, service=chrome_service)#
            except:
                g_val.err_message_w(1,"error")
                return
            
            g_val.condition_type = []
            g_val.condition_area = []
            g_val.condition_other = []
    
            messagebox.askyesno('確認', '条件を選択したら「この条件で検索する」を押してください。\n収集中リクナビNEXTの画面は閉じないでください。エラーになります。')
            url_ = "https://next.rikunabi.com/search/"
            g_val.driver_t1.get(url_)
            
            st = time.time()
            result = 0
            search_num = 1e7
            
            while(1):
                els = g_val.driver_t1.find_elements(By.CLASS_NAME, 'rnn-pageNumber')
                if(len(els)>0):
                    for eln in els:
                        
                        els0 = g_val.driver_t1.find_elements(By.XPATH, "//li[@class='rnn-pagination__next']/a")
                        #print("1ページ目",len(els0), els0[0].get_attribute('href'))
                        if len(els0)>0:
                            print(els0[0].get_attribute('href'))
                            g_val.reserch_url_log =re.sub( "page2", "page1", els0[0].get_attribute('href'))
                            
                        #1page目の保存URLを変更
                        else:
                            g_val.reserch_url_log = g_val.driver_t1.current_url
                        g_val.url_log_his = g_val.reserch_url_log
                        break
                    break
                
            # g_val.driver_t1.quit()
                
        print(g_val.reserch_url_log)
        
        ################################################### 検索条件を探す ###################################################
        print("検索条件")
        # 職種条件
        type_element = g_val.driver_t1.find_elements(By.XPATH, "//input[@class='rn3-selectedResults__change js-occupation_cd']")
        if len(type_element)>0:
            type_number = len(type_element)
            for els in type_element:
                g_val.condition_type.append(els.find_element(By.XPATH, "following-sibling::span/following-sibling::span").text)
            print("職種：", g_val.condition_type)
        # 勤務地条件       
        area_element = g_val.driver_t1.find_elements(By.XPATH, "//input[@class='rn3-selectedResults__change js-wrk_plc_long_cd']")
        if len(area_element)>0:
            area_number = len(area_element)
            for els in area_element:
                g_val.condition_area.append(els.find_element(By.XPATH, "following-sibling::span/following-sibling::span").text)
            print("勤務地：", g_val.condition_area)
        # 他の条件
        other_element = g_val.driver_t1.find_elements(By.XPATH, "//input[@checked='checked']")
        other_number = len(g_val.condition_type)+len(g_val.condition_area)
        if len(other_element)>other_number:
            for els in  other_element[other_number:]:
                g_val.condition_other.append(els.find_element(By.XPATH, "following-sibling::span/following-sibling::span").text)
            print("その他：", g_val.condition_other)
        #################################################################################################################### 
            
        while(1):
            
            main_url = g_val.reserch_url_log
            print("main_url:", main_url)
            #ログ書き込み
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="ログ書き込み"
            else:
                g_val.window_log["text"] ="Log Writing"
            
            print("ログ書き込み前")
            g_val.data_log_write(g_val.window_log["text"])

            print("ログ書き込み後")
            g_val.campany_list=[]
            
            g_val.conf_log_save()
            if(g_val.stop_==1):
                g_val.program1_end=1
                g_val.driver_t1.quit()
                sleep(1)
                return
            
            try:
                while(1):
                    handle_array = g_val.driver_t1.window_handles
                    if(len(handle_array)==1):break
                    else:
                        g_val.driver_t1.switch_to.window(g_val.driver_t1.window_handles[-1])
                        g_val.driver_t1.close()
                        sleep(0.5)
                g_val.driver_t1.switch_to.window(g_val.driver_t1.window_handles[-1])
                
                g_val.C_CODE="JA"
                try:    
                    current_page = g_val.driver_t1.find_elements(By.XPATH, "//li[@class='rnn-pagination__page is-current']")[0].text
                    print("現在のページ：", current_page)
                    g_val.page = current_page
                except:
                    g_val.err_message_w(2,"error")
                    return
                        
                if current_page == '1':
                    pass
                # else:
                #     g_val.driver_t1.get(main_url)
                
                ################################################### 検索条件数 ###################################################
                try:
                    search_num = g_val.driver_t1.find_elements(By.XPATH,'//span[@class="rnn-pageNumber rnn-textXl js-resultCount"]')[0].text
                except:
                    g_val.err_message_w(2,"error")
                    return
                
                print('検索件数：', search_num)
                #################################################################################################################
                    
                g_val.reserch_url_log = g_val.driver_t1.current_url
                
                
                ################################################### カテゴリ ###################################################
                kategory_=""                                                                                                 ##
                                                                                                                             ##
                try:                                                                                                         ##
                    if len(g_val.condition_type)>0:                                                                          ##
                        kategory_ = g_val.condition_type[0]                                                                  ##
                except:                                                                                                      ##
                    traceback.print_exc()                                                                                    ##
                                                                                                                             ##
                try:                                                                                                         ##
                    if(" (" in kategory_):                                                                                   ##
                        kategory_ = kategory_.split(" (")[0]                                                                 ##
                except:                                                                                                      ##
                    kategory_=""                                                                                             ##
                    traceback.print_exc()                                                                                    ##
                print("カテゴリ取得:", kategory_)                                                                             ##
                ###############################################################################################################
                
                page_number = math.ceil(int(search_num)/50)
                print("ページ数：", page_number)
                    
                result_url = []
                selected_part = g_val.driver_t1.find_elements(By.CLASS_NAME, "rnn-group.rnn-group--xm.rnn-jobOfferList")[0]
                els = selected_part.find_elements(By.CLASS_NAME, "rnn-linkText.rnn-linkText--black")
                if len(els)>0:
                    print(len(els))
                    for eln in els:
                        try:
                            a_tag = eln.get_attribute('href')
                            title_ = eln.text
                            sel = a_tag.split("/")[3]
                            list_a = []
                            print(sel)
                            if sel == "viewjob":
                                url = "/".join(a_tag.split("/", 5)[:5])
                            else:
                                url = "/".join(a_tag.split("/", 6)[:6])
                                url = re.sub(r'nx1_', 'nx2_', url)
                            print("リスト",url,"title",title_)
                            result_url.append(url)
                            cal =1
                            for list_all_n in g_val.campany_list:
                                if(list_all_n[0]==title_ or list_all_n[1]==url):
                                    cal=0
                                    break
                            if(cal==1):
                                list_a.append(title_)
                                list_a.append(url)
                                list_a.append(kategory_)
                                list_a.append(sel)
                                list_a.append("-  -")
                                g_val.campany_list.append(copy.deepcopy(list_a))
                                print("=========================list_get==================================")
                                print(list_a)
                                g_val.window_log["text"] =list_a
                                g_val.data_log_write(g_val.window_log["text"])
                                print("===================================================================")
                            # if len(result_url) == int(search_num):
                            #     break
                            try:
                                url_ = g_val.driver_t1.find_elements(By.CLASS_NAME, "rnn-inlineBlock.rnn-pagination__button")[1].get_attribute('href')
                            except:
                                pass
                        except:
                            traceback.print_exc()
                            g_val.data_log_write(datetime.datetime.now())
                            g_val.data_log_write(traceback.format_exc())

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
                    g_val.driver_t1.quit()
                    g_val.program1_end =1
                    sleep(1)
                    #exit()
                    return
                
                print("*******************************************")
                print(g_val.campany_list)
                print("*******************************************")
                
                val_get_rikunabi(g_val.campany_list)#######rest
                
                reserch_end = 1
                #次のページのURLを取得して次に渡す。
                #次のページがない場合は終了。
                g_val.driver_t1 = webdriver.Chrome(options=option_t1, service=chrome_service)
                g_val.driver_t1.get(main_url)
                els = g_val.driver_t1.find_elements(By.CLASS_NAME, "rnn-inlineBlock.rnn-pagination__button")
                
                st = time.time()
                while(1):
                    now = time.time() - st
                    if(now>20):break
                    if(len(els)>0):
                        print(els[1].get_attribute('href'))
                        if els[1].get_attribute('href'):
                            reserch_end=0
                            g_val.research_url_log = els[1].get_attribute('href')
                            els[1].click()
                        break

            except:
                #エラー時はリトライ
                traceback.print_exc()
                g_val.data_log_write(datetime.datetime.now())
                g_val.data_log_write(traceback.format_exc())

                if(g_val.stop_==1):
                    g_val.driver_t1.quit()
                    g_val.program1_end=1
                    sleep(1)
                    return
                while(1):
                    if(g_val.stop_==1):
                        g_val.driver_t1.quit()
                        g_val.program1_end=1
                        sleep(1)
                        return

                    try:
                        print("エラー待機111111")
                        try:
                            g_val.driver_t1.quit()
                        except:
                            temp_=1
                        #エラー時はリトライ
                        # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                        g_val.driver_t1 = webdriver.Chrome(options=g_val.option, service=chrome_service)
                        g_val.driver_t1.set_page_load_timeout(180)
                        g_val.driver_t1.get("https://www.google.co.jp/")
                        #break
                        
                        #siku_n-=1
                        break
                    except:
                        sleep(60)
                        temp_=1
                        print("エラー待機11111111")
                continue
    
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.window_log["text"] ="ログ保存"
            else:
                g_val.window_log["text"] ="Log saveing"
            g_val.data_log_write(g_val.window_log["text"])

            g_val.conf_log_save()
            
            if(reserch_end==1):#次のページがないとき検索完了
                break
            print("終了フラグ::",reserch_end)

        #print(campany_list)
        g_val.driver.quit()
        g_val.driver_t1.quit()
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

def val_get_rikunabi(campany_list_in):
    import traceback
    try:
        from urllib.parse import urlparse
        import re
        import g_val
        import g_val_rikunabi
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
        from googlesearch import search
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
                        
                        path_o_csv_cat  = g_val.path1+"\\..\\out\\result_リクナビNEXT"+str(campany_list_n[2])+".csv"
                    else:
                        #path_o_csv_cat  = g_val.path1+"/../out/result_"+str(campany_list_n[2])+".csv"
                        path_o_csv_cat  = g_val.path1+"/../out/result_リクナビNEXT"+str(campany_list_n[2])+".csv"

                else:
                    if("Windows"==g_val.OS_VERSION):
                        path_o_csv_cat  = g_val.path1+"\\..\\out\\result_リクナビNEXT_"+str(campany_list_n[2])+"_OP.csv"
                        #path_o_csv_cat  = g_val.path1+"\\..\\out\\result_DUDA_OP.csv"
                    else:
                        path_o_csv_cat  = g_val.path1+"/../out/result_リクナビNEXT_"+str(campany_list_n[2])+"_OP.csv"
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
                    # print(out_list_t)
                except:
                    out_list_t=[]

                if(n==0):
                    
                    open_out = open(path_o_csv_cat,'a',newline="", encoding='utf_8_sig')#utf_8_sig
                    file_o_csv = csv.writer(open_out, delimiter=',')
                    if(g_val.Op_ok==0):
                        file_o_csv.writerow(g_val_rikunabi.rikunabi_header_nominal)
                    else:
                        file_o_csv.writerow(g_val_rikunabi.rikunabi_header_op)
                            
                    
                    open_out.close()
                if(g_val.stop_==1):return 0   

                list_n = campany_list_n[1]
                url_get = list_n
                url_ = list_n

                cal_llist=1
                #用検討
                # for out_list_t_l in out_list_t:
                #     if(url_  in out_list_t_l[10]):
                #         cal_llist =0
                #         break
                # if cal_llist ==0 :
                #     #del campany_list[0]
                #     continue

                #企業URL取得
                g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                g_val.driver.get(url_get)
                titel_=campany_list_n[0]
                sel = campany_list_n[3]
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
                    # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option0,service=chrome_service)
                    g_val.driver = webdriver.Chrome(options=g_val.option0, service=chrome_service)
                    g_val.driver.set_page_load_timeout(180)
                    g_val.driver.get(url_)
                    sleep(1)
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        messagebox.askyesno('確認', 'ブラウザを確認してください')
                    else:
                        messagebox.askyesno('Confirmination', 'Please check your browser')
                    g_val.driver.quit()
                    # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                    g_val.driver = webdriver.Chrome(options=g_val.option, service=chrome_service)
                    g_val.driver.set_page_load_timeout(180)
                if(g_val.stop_==1):return 0      

                try:
                    
                    url_ = url_get
                    g_val.driver.get(url_)

                    #################RIKUNABIここにいれる######################################
                    try:
                        rikunabi_locate=""
                        rikunabi_HP_url_=""
                        rikunabi_established=""
                        rikunabi_president=""
                        rikunabi_employees=""
                        rikunabi_capital=""
                        rikunabi_sales=""
                        rikunabi_summary=""
                        rikunabi_office=""
                        rikunabi_industry_type=""
                        #設立　'established':
                        #代表者 'president':
                        #従業員数 'employees':
                        #資本金 'capital':
                        #売上高 'sales':
                        #事業概要'summary':
                        #業種　'type of industry':
                        #事業所　'office':

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"社名")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        company_=eln.text   
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"社名")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        company_=eln.text   
                                    break
                            elif(sel == "viewjob"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"社名")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        company_=eln.text   
                                    break
                            else:
                                els2 = g_val.driver.find_elements(By.CLASS_NAME, "rnn-offerCompanyName")
                                if(len(els2)>0):
                                    for eln in els2:
                                        company_=eln.text   
                                    break
                        print("rikunabi_社名:",company_)
                        
                        if (sel == "company"):
                            company_url = url_.split('/nx2')[0] + "/?leadtc=ngen_sgenlnk_cmpyarea"
                            r = requests.get(company_url) 
                            soup = BeautifulSoup(r.content, 'html.parser') 
                            rikunabi_HP_url_ = soup.find(class_="rnn-linkText--blue").get('href')
                        else:
                            for j in search(company_):
                                rikunabi_HP_url_ = "/".join(j.split("/")[:3])
                                break
                        print("rikunabi_url:",rikunabi_HP_url_)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == 'viewjob'):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"本社所在地")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_office=eln.text
                                        break
                                    break
                            elif(sel == "rnc"):
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"事業所")]/..//td')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_office=eln.text
                                        break
                                    break
                            else:
                                try:
                                    els2 = g_val.driver.find_element(By.XPATH, "//h3[@class='rn3-companyOfferCompany__heading' and contains(text(), '事業所')]")
                                    eln = els2.find_element(By.XPATH, "following-sibling::*[1]")
                                    rikunabi_office = eln.text
                                except:
                                    pass
                                break
                        try:
                            print("address:",  rikunabi_office)
                            if (re.search(" ", rikunabi_office)):
                                txt = rikunabi_office.split(" ")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("●", rikunabi_office)):
                                txt = rikunabi_office.split("●")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("◆", rikunabi_office)):
                                txt = rikunabi_office.split("◆")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("◆", rikunabi_office)):
                                txt = rikunabi_office.split("◆")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("■", rikunabi_office)):
                                txt = rikunabi_office.split("■")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("／", rikunabi_office)):
                                txt = rikunabi_office.split("／")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            if (re.search("　", rikunabi_office)):
                                txt = rikunabi_office.split("　")
                                for a in txt:
                                    if (re.search(r"[都道府県]", a)):
                                        rikunabi_office = a
                                        break
                            rikunabi_locate = rikunabi_office
                        except:
                            print("エラー住所")
                            traceback.print_exc()
                            rikunabi_locate ="-"
                            
                        print("rikunabi_住所:",rikunabi_locate)
                        #都道府県と市区町村を抽出
                        prefecture, location = extract_japanese_location(rikunabi_locate)
                        campany_list_n[4] = prefecture + "  " + location
                        print("rikunabi_住所:市区町村::",campany_list_n[4])
                        
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"設立")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_established=eln.text   
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"設立")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        rikunabi_established=eln.text     
                                    break
                        print("rikunabi_設立:",rikunabi_established)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"代表者")]/..//p')
                            if(len(els)>0):
                                for eln in els:
                                    rikunabi_president=eln.text
                                break
                            els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"代表者")]/..//td')
                            if(len(els1)>0):
                                for eln in els1:
                                    rikunabi_president=eln.text
                                break
                        print("rikunabi_代表者:",rikunabi_president)
                        
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"従業員数")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_employees=eln.text
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"従業員数")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        rikunabi_employees=eln.text
                                    break
                        print("rikunabi_従業員数:",rikunabi_employees)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"資本金")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_capital=eln.text
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"資本金")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        rikunabi_capital=eln.text
                                    break
                        print("rikunabi_資本金:",rikunabi_capital)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"売上高")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_sales=eln.text
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"売上高")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        rikunabi_sales=eln.text
                                    break
                        print("rikunabi_売上高:",rikunabi_sales)

                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"事業内容")]/..//p')
                            if(len(els)>0):
                                for eln in els:
                                    rikunabi_summary=eln.text
                                break
                            els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"事業内容")]/..//td')
                            if(len(els1)>0):
                                for eln in els1:
                                    rikunabi_summary=eln.text
                                break
                        print("rikunabi_事業内容:",rikunabi_summary)
                        
                        st = time.time()
                        while(1):
                            now = time.time() - st
                            if(now>3):break
                            if(sel == "company"):
                                els = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"業種")]/..//p')
                                if(len(els)>0):
                                    for eln in els:
                                        rikunabi_industry_type=eln.text
                                    break
                                els1 = g_val.driver.find_elements(By.XPATH, '//*[contains(text(),"業種")]/..//td')
                                if(len(els1)>0):
                                    for eln in els1:
                                        rikunabi_industry_type=eln.text
                                    break
                        print("rikunabi_業種:",rikunabi_industry_type)

                    except:
                        traceback.print_exc()
                        continue
                        
                    
                    ################ RIKUNABI END  ##########################################
                    #カテゴリ
                    #####################################################################
                    url_g ="https://www.google.co.jp/maps/search/"+company_+" "+rikunabi_locate + "?gl=jp&h1=jp&gws_rd=cr"
                    print(url_g)
                    while(1):
                        handle_array = g_val.driver.window_handles
                        if(len(handle_array)==1):break
                        else:
                            g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                            g_val.driver.close()
                            sleep(0.5)
                    g_val.driver.switch_to.window(g_val.driver.window_handles[-1])
                    g_val.driver.get(url_g)
                    
                except:
                    if(g_val.stop_==1):return 0
                    traceback.print_exc()
                    main_ulr ="-"
                #　　　　google 検索開始
                campany_list_n[0] = company_
                campany_list_n.pop(3)

                #url_g  = "https://www.google.co.jp/maps/search/株式会社FOOD & LIFE INNOVATIONS 東京都千代田区丸の内2-1-1?gl=jp&h1=jp&gws_rd=cr"
                #campany_list_n=['株式会社FOOD & LIFE INNOVATIONS','https://next.rikunabi.com/company/cmi3551186001/nx2_rq0021197121','飲食・フードサービス','東京都  千代田区']
                                  
                print("url_g", url_g)
                print("campany_list_n", campany_list_n)
                print("rikunabi_HP_url_", rikunabi_HP_url_)
                out_google_list = g_fnc_google.google_detail_reserch(url_g ,campany_list_n,rikunabi_HP_url_)
                print("out_google_list:", out_google_list)
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
                        
                print("out_ok", out_ok)
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

                    list_out_all_a.append(company_)
                    list_out_all_db.append(company_)
                    if campany_list_n[3].split("  ")[0] == '-':
                        prefecture, location = extract_japanese_location(jyuusyo_)
                        list_out_all_a.append(prefecture)
                        list_out_all_db.append(prefecture)
                        list_out_all_a.append(location)
                        list_out_all_db.append(location)
                    else:
                        list_out_all_a.append(campany_list_n[3].split("  ")[0])
                        list_out_all_db.append(campany_list_n[3].split("  ")[0])
                        list_out_all_a.append(campany_list_n[3].split("  ")[1])
                        list_out_all_db.append(campany_list_n[3].split("  ")[1])
                    list_out_all_a.append(jyuusyo_)
                    list_out_all_db.append(jyuusyo_)

                    # list_out_all_a.append(rikunabi_industry_type)
                    # list_out_all_db.append(rikunabi_industry_type)
                    # list_out_all_a.append(rikunabi_locate)
                    # list_out_all_db.append(rikunabi_locate)
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
                        # print("Fax:", o_)
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


                    
                    list_out_all_a.append(rikunabi_established)
                    list_out_all_db.append(rikunabi_established)
                    list_out_all_a.append(rikunabi_president)
                    list_out_all_db.append(rikunabi_president)
                    list_out_all_a.append(rikunabi_employees)
                    list_out_all_db.append(rikunabi_employees)
                    list_out_all_a.append(rikunabi_capital)
                    list_out_all_db.append(rikunabi_capital)
                    list_out_all_a.append(rikunabi_sales)
                    list_out_all_db.append(rikunabi_sales)
                    list_out_all_a.append(rikunabi_summary)
                    list_out_all_db.append(rikunabi_summary)
                    list_out_all_a.append(rikunabi_industry_type)
                    list_out_all_db.append(rikunabi_industry_type)
                    list_out_all_a.append(rikunabi_locate)
                    list_out_all_db.append(rikunabi_locate)

                    list_out_all_a.append(campany_list_n[1])#27比較できるようにURL表示
                    list_out_all_db.append(campany_list_n[1])#27
                    
                    print("list_out_all_a", list_out_all_a)
                    print("list_out_all_db", list_out_all_db)

                
                    
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
                    #'type of industry':list_out_all_db[27],
                    #'address':list_out_all_db[28],
                    'dudaurl':list_out_all_db[29],
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
                    
                    # print("CSV result:", list_out_all_a)
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
                        # g_val.driver = webdriver.Chrome(g_val.d_path,options=g_val.option,service=chrome_service)
                        g_val.driver = webdriver.Chrome(options=g_val.option, service=chrome_service)
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

def remove_duplicates(list):
    unique_list = []
    
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
            
    return unique_list

def extract_japanese_location(text):
    from janome.tokenizer import Tokenizer
    import re
    
    prefecture_names = [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県",
        "岐阜県", "静岡県", "愛知県", "三重県",
        "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県",
        "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県",
        "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県",
        "沖縄県"
    ]
    pattern = re.compile("|".join(prefecture_names))
    matches = pattern.findall(text)
    if len(matches):
        prefecture = matches[0]
        
        ############################## 市区郡町村 ##############################
        t = Tokenizer()

        # Tokenize the text
        tokens = t.tokenize(text)
        temp = ''
        location = ''
        flag = ['0']
        
        # Look for city, town, and village names in the tokens
        for token in tokens:
            if token.part_of_speech.split(',')[0] == '名詞' and token.part_of_speech.split(',')[2] == '地域':
                # print(token.part_of_speech)
                # print(token.surface)
                if token.surface == '市' and not flag.__contains__('1'):
                    location = location + temp + '市'
                    flag.append('1')
                    break
                if token.surface == '区' and not flag.__contains__('2'):
                    location = location + temp + '区'
                    flag.append('2')
                    break
                if token.surface == '郡' and not flag.__contains__('3'):
                    location = location + temp + '郡'
                    flag.append('3')
                    break
                if token.surface == '町' and not flag.__contains__('4'):
                    location = location + temp + '町'
                    flag.append('4')
                    break
                if token.surface == '村' and not flag.__contains__('5'):
                    location = location + temp + '村'
                    flag.append('5')
                    break
                temp = token.surface
                
        if location == '':
            if re.findall(r'(県|都|府|県)(.*?)(?=市)', text):
                location = re.findall(r'(県|都|府|県)(.*?)(?=市)', text)[0][1] + '市'
            elif re.findall(r'(県|都|府|県)(.*?)(?=区)', text):
                location = re.findall(r'(県|都|府|県)(.*?)(?=区)', text)[0][1] + '区'
            elif re.findall(r'(県|都|府|県)(.*?)(?=郡)', text):
                location = re.findall(r'(県|都|府|県)(.*?)(?=郡)', text)[0][1] + '郡'
            elif re.findall(r'(県|都|府|県)(.*?)(?=町)', text):
                location = re.findall(r'(県|都|府|県)(.*?)(?=町)', text)[0][1] + '町'
            elif re.findall(r'(県|都|府|県)(.*?)(?=村)', text):
                locatoin = re.findall(r'(県|都|府|県)(.*?)(?=村)', text)[0][1] + '村'
                
        ############################################################
            
    else:
        prefecture = '-' 
        location = '-'
        
    
    return prefecture, location

############################################################################################################################
#########################################################################################################################################

