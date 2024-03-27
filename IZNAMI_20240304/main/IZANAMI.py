import traceback
try:

    #最初にduda か　googlaか選ぶ
    #今後追加の可能性あり。
    #dudaで企業検索ごに住所と企業名でgoogle検索

    
    from PIL import Image
    import tkinter
    import g_val
    import g_val_country
    import shutil
    import comapyny_get_v101
    import comapyny_get_duda_v101
    import comapyny_get_rikunabi_v101_
    import comapyny_get_rikunabi_v101_
    import comapyny_get_duda_company_v101
    import comapyny_get_mynabi_v101
    import comapyny_get_shuukatsu_v101
    import comapyny_get_en_v101
    import comapyny_get_townwork_v101
    import comapyny_get_tabelog_v101

    import g_val_duda

    import os,sys

    import random
    import tkinter
    from tkinter import E, Canvas, ttk,filedialog ,messagebox
    import re
    import time
    from time import sleep

    import threading
    import pathlib

    import webbrowser
    from time import sleep
    import copy
    #クロームドライバ
    path1=os.path.dirname(os.path.abspath(__file__))
    path_p= pathlib.Path(path1).parent
    import datetime
    import pathlib
    
    import csv
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    # xcel操作
    import openpyxl as px
    import tkinter.font as ttkFont

    import logging


    #path1=os.path.dirname(os.path.abspath(__file__))
    import platform
    g_val.OS_VERSION = platform.system()

    name = os.path.abspath(sys.argv[0])

    if("Windows" ==g_val.OS_VERSION):
        g_val.path1=os.path.dirname(sys.argv[0])#.split("main")[0]+"main"
        import winshell
        from pystray import Icon, Menu, MenuItem
        import pystray

    else:
        g_val.path1=name.split("dist")[0]+"dist"

    path_p= pathlib.Path(path1).parent


    if("Windows"==g_val.OS_VERSION):
        g_val.log_tem_f = g_val.path1+"\\..\\conf\\"
    else:
        g_val.log_tem_f = g_val.path1+"/../conf/"#mac
    print(g_val.OS_VERSION)
    
    if(os.path.isdir(g_val.log_tem_f) ==False):#パス存在なし
        g_val.err_message_w(0,g_val.path1)
        os._exit(1)
    print("PASTH確認",os.path.isdir(g_val.log_tem_f))

    #exel読み込み
    from ttkthemes import *
    root = ThemedTk()


    if("Windows" !=g_val.OS_VERSION):
        s = ttk.Style()
        s.theme_use('arc')

    if getattr(sys, 'frozen', False):
        # 実行ファイルのパスを取得
        application_path = sys._MEIPASS
    else:
        # 通常のPythonスクリプトと同様にカレントディレクトリを取得
        application_path =  g_val.path1

    print(application_path)
    data_file_path = os.path.join(application_path, "IZANAMI.ico")

    root.iconbitmap(default=data_file_path)

    #s.theme_use('winnative')
    #if("Windows"!=g_val.OS_VERSION):
    #    s.theme_use('breeze')
    #s.theme_use('breeze')
    #root = ttk.ttk()
    # ウィンドウのサイズを設定
    if("Windows"==g_val.OS_VERSION):
        root.geometry('450x450')
    else:
        root.geometry('550x450')
        
    # 画面タイトル
    root.title('IZANAMI　営業リスト収集ツール')
    root.attributes('-topmost', True)
    init_mode_f =ttk.Frame(root)


    init_lang_mac_f =ttk.Frame(root)
    init_lang_f =ttk.Frame(root)

    login_form = ttk.Frame(root)
    init_freeversion =ttk.Frame(root)
    init_expire =ttk.Frame(root)
    init_new_version =ttk.Frame(root)

    init_f =ttk.Frame(root)
    notebook = ttk.Notebook(root)

    tab_st = ttk.Frame(notebook)
    tab_cf = ttk.Frame(notebook)#, bg='gray')
    tab_op = ttk.Frame(notebook)#, bg='gray')
    tab_help = ttk.Frame(notebook)#, bg='gray')

    notebook.add(tab_st, text="開始/終了")
    notebook.add(tab_cf, text="収集設定")
    notebook.add(tab_op, text="オプション")
    notebook.add(tab_help, text="ヘルプ")

    #フレームにNotebookを追加
    notebook_1_1 = ttk.Notebook(tab_cf)
    notebook_1_2 = ttk.Notebook(tab_op)
    notebook_1_3 = ttk.Notebook(tab_help)
    # フレームを作ってそのNotebookに追加
    cf_kategory = ttk.Frame(notebook_1_1)#, bg='gray')
    cf_erea = ttk.Frame(notebook_1_1)#, bg='gray')
    cf_bl_list = ttk.Frame(notebook_1_1)#, bg='gray')
    cf_domain= ttk.Frame(notebook_1_1)#, bg='gray')
    cf_dword = ttk.Frame(notebook_1_1)

    notebook_1_1.add(cf_kategory, text="カテゴリ・進捗設定")
    notebook_1_1.add(cf_erea, text="エリア設定")
    notebook_1_1.add(cf_bl_list, text="拒否リスト")
    notebook_1_1.add(cf_dword, text="拒否ワード")
    notebook_1_1.add(cf_domain, text="拒否ドメイン")




    op_tyouhuku = ttk.Frame(notebook_1_2)#, bg='gray')
    op_yuragi = ttk.Frame(notebook_1_2)#, bg='gray')
    op_proxy = ttk.Frame(notebook_1_2)#, bg='gray')
    op_logdl= ttk.Frame(notebook_1_2)#, bg='gray')
    op_ex= ttk.Frame(notebook_1_2)#, bg='gray')
    get_item= ttk.Frame(notebook_1_2)#, bg='gray')

    notebook_1_2.add(op_tyouhuku, text="重複削除")
    notebook_1_2.add(op_yuragi, text="ゆらぎ設定")
    notebook_1_2.add(op_proxy, text="プロキシ設定")
    notebook_1_2.add(get_item, text="収集項目")
    notebook_1_2.add(op_logdl, text="ログDL")
    notebook_1_2.add(op_ex, text="拡張")

    help_faq = ttk.Frame(notebook_1_3)
    help_veision = ttk.Frame(notebook_1_3)
    notebook_1_3.add(help_faq, text="FAQ")
    notebook_1_3.add(help_veision, text="バージョン情報")

    #label = ttk.Label(tab_one, text="Notebook ウィジットの作成", backgsround='white')
    #init

    text_ini0=ttk.Label(init_f,anchor=tkinter.E,justify="left",font=("","11",""))
    text_ini0.place(x=75, y=150)
    text_ini0["text"]="起動時のチェックを行っています。\nしばらくお待ちください。"

    text_ini1=ttk.Label(init_f,anchor=tkinter.E,justify="left",font=("","11",""))
    text_ini1.place(x=75, y=230)
    text_ini1["text"]=""

    if("Windows"==g_val.OS_VERSION):
        pro_bar = ttk.Progressbar(init_f,length=300)
    else:
        pro_bar = ttk.Progressbar(init_f,length=400)

    #pro_bar.place(x=20, y=150)
    pro_bar.grid(row=0,column=0,sticky=(E))

    if("Windows"==g_val.OS_VERSION):
        pro_bar.pack(padx=10, pady=200)
    else:
        pro_bar.pack(padx=5, pady=200)
    #init_f.pack(expand=True, fill='both')
    #init_lang_mac_f.pack(expand=True, fill='both')
    #init_lang_f.pack(expand=True, fill='both')



    try:
        if("Windows"==g_val.OS_VERSION):
            g_val.log_tem_f = g_val.path1+"\\..\\conf\\log00000000000temp.txt"
            #init_lang_mac_f.pack(expand=True, fill='both')
            #init_lang_f.pack(expand=True, fill='both')
            init_mode_f.pack(expand=True, fill='both')

        else:
            g_val.log_tem_f = g_val.path1+"/../conf/log00000000000temp.txt"#mac
            init_lang_mac_f.pack(expand=True, fill='both')
    except:
        g_val.err_message_w(0,g_val.path1)
        os._exit(1)
    if not os.path.isfile(g_val.log_tem_f):
        with open(g_val.log_tem_f, mode='w',encoding="utf_8_sig") as f:#,newline='\n'
            f.write("IZANAMI LOG ")
        #os._exit(1)
        #init_lang_f.pack(expand=True, fill='both')

    #logging.basicConfig(filename=g_val.path1+"/../conf/log_dbg.txt",level=logging.NOTSET)#logging.DEBUG)

    #notebook.pack(expand=True, fill='both')#, padx=10, pady=10)
    #notebook_1_1.pack(expand=True, fill='both')#, padx=10, pady=10)
    #notebook_1_2.pack(expand=True, fill='both')#, padx=10, pady=10)
    #認証チェック
    #1無料版
    #2ライセンス切れ
    #3最新バージョン
    #init_freeversion =ttk.Frame(root)
    #init_expire =ttk.Frame(root)
    #init_new_version =ttk.Frame(root)
    text_ini_free=ttk.Label(init_freeversion,anchor=tkinter.E,font=("","11",""))#justify="center"
    text_ini_free.place(x=50, y=80)
    #text_ini_free["text"]="現在は無料ライセンス版となっております。\n収集は無制限に行えますが、csv出力できるのは2000件までと\nなっております。"

    import struct
    from uuid import getnode


    def Login(email):

        #email = entries['Email'].get()

        # password = entries['Password'].get()

            # defining the api-endpoint 
        # API_ENDPOINT = "http://localhost/izanami/public/api/login"
        API_ENDPOINT = "https://system.izanami.link/api/login"
        print(email)
        print('mac_address:',g_val._mac)
        
        data = {
        'email':email,
        'mac_address':g_val._mac,

        # 'password':password,
        }
        r = requests.post(url = API_ENDPOINT, data = data)
        res = r.json()
        print("===acc===================")
        print(res)
        #'period': '2022-08-03T15:23:44.000000Z'

        print(res["result"],res["value"])
        print("===acc===================")

        if res["value"] == "wrong":
            print("please verify your account")
            g_val.login_ok = "wrong"
        
        elif res["value"] == "active":
            print("successfully login.")
            g_val.login_ok = "active"
            f = open("session.txt", "w")
            f.write(email)
            f.close()
            #return

        elif res["value"] == "free":
            temp=res["period"].split("T")[0]
            
            temp_y = temp.split("-")[0]
            temp_m = temp.split("-")[1]
            temp_d = temp.split("-")[2]
            g_val.login_date = temp_y+"."+temp_m+"."+temp_d
            print(g_val.login_date)
            if(g_val.language_get_value==g_val.Lnagage_list[1]):

                text_ini_free["text"]="現在は試用期間です。"
                text_ini_free["text"]+="\n試用期間中は全ての機能をご利用いただけます。"
                text_ini_free["text"]+="\n\n有効期限："+g_val.login_date
            else:
                text_ini_free["text"]="This app is currently in trial."
                text_ini_free["text"]+="\nAll features are available during the trial period."
                text_ini_free["text"]+="\n\nExpire Date："+g_val.login_date
                


            print("successfully login. your account will be expired within 7 days")
            g_val.login_ok = "free"

        elif res["value"] == "wrong_mac":
            g_val.login_ok = "wrong_mac"

        elif res["value"] == "collect_user":
            g_val.login_ok = "collect_user"

        elif res["value"] == "expired":
            g_val.login_ok = "expired"

            #g_val.login_ok = "free"

        else:
            g_val.login_ok = "active"

        #g_val.login_ok = "free"####test

        g_val.E_mail=email

        return

    login_form = ttk.Frame(root)

    def loginform(login_form):

        entries = {}
        row = ttk.Frame(login_form)
        if("Windows"==g_val.OS_VERSION):
            ft = ttkFont.Font(family='Times',size=15)
            lab = ttk.Label(row, width=15, text="Email: ", anchor='w')
        else:
            ft = ttkFont.Font(family='Times',size=20)
            lab = ttk.Label(row, width=10, text="Email: ", anchor='w')   
        
        ent = tkinter.Entry(row)
        row.place(x=50,y=200,width=350,height=40)
        lab["font"] = ft
        lab.pack(side=tkinter.LEFT)
        ent["font"] = ft
        ent.pack(side=tkinter.RIGHT, 
                    expand=tkinter.YES, 
                    fill=tkinter.BOTH)
        entries['Email'] = ent

        # row = ttk.Frame(login_form)
        # lab = ttk.Label(row, width=15, text="Password: ", anchor='w')
        # ent = tkinter.Entry(row,show="*")
        # row.place(x=30,y=200,width=390,height=40)
        # lab["font"] = ft
        # lab.pack(side=tkinter.LEFT)
        # ent["font"] = ft
        # ent.pack(side=tkinter.RIGHT, 
        #             expand=tkinter.YES, 
        #             fill=tkinter.BOTH)
        # entries['Password'] = ent

        return entries

    login_form_ent = loginform(login_form)

    button_login_submit = ttk.Button(login_form,
                    text = 'LOGIN',
                    command=(lambda e=login_form_ent: Login(e['Email'].get()))
                    )
    if("Windows"==g_val.OS_VERSION):
        button_login_submit.place(x=160, y=310,width=112,height=48)
    else:
        button_login_submit.place(x=220, y=310,width=112,height=48)
    # ボタンの作成と配置
    def botton_ini_free_ok():

        g_val.init_freeversion_end=1
        g_val.init_expire_end=1
        g_val.init_new_version_end=1
        return
    def botton_ini_Paid():

        webbrowser.open("https://system.izanami.link/charge-form")
        g_val.init_sys_end=1
        g_val.init_freeversion_end=1
        g_val.init_expire_end=1
        return
    def botton_ini_Download():
        webbrowser.open("https://system.izanami.link/user/index", new=0, autoraise=True)
        g_val.init_sys_end=1
        g_val.init_new_version_end=1
        
        return

    button_free_ok = ttk.Button(init_freeversion,
                    text = 'OK',
                    command=botton_ini_free_ok
                    )
    button_free_ok.place(x=300, y=200,width=100,height=50)

    button_free_paid = ttk.Button(init_freeversion,
                    text = '有料ライセンスを契約',
                    command=botton_ini_Paid
                    )
    button_free_paid.place(x=50, y=200,width=200,height=50)


    text_ini_expire=ttk.Label(init_expire,anchor=tkinter.E,justify="left",font=("","11",""))
    text_ini_expire.place(x=75, y=150)
    text_ini_expire["text"]="ライセンスの有効期限がきれています。"

    button_expire_ok = ttk.Button(init_expire,
                    text = 'OK',
                    command=botton_ini_free_ok
                    )
    button_expire_ok.place(x=300, y=200,width=100,height=50)

    button_expire = ttk.Button(init_expire,
                    text = '有料ライセンスを契約',
                    command=botton_ini_Paid
                    )
    button_expire.place(x=50, y=200,width=200,height=50)

    text_ini_newversion=ttk.Label(init_new_version,anchor=tkinter.E,justify="left",font=("","11",""))
    text_ini_newversion.place(x=75, y=150)
    #new_v = int(new_version.text.replace(".",""))

    text_ini_newversion["text"]="最新バージョンがあります。\n現在のバージョン　"+g_val.SOFT_VERSION
    button_download_ok = ttk.Button(init_new_version,
                    text = 'OK',
                    command=botton_ini_free_ok
                    )
    button_download_ok.place(x=300, y=200,width=100,height=50)

    button_new_version = ttk.Button(init_new_version,
                    text = 'ダウンロード',
                    command=botton_ini_Download
                    )
    button_new_version.place(x=50, y=200,width=200,height=50)

    from os import path
    import subprocess
    #_ = ["設定カテゴリ","収集カテゴリ","ビジネス","都道府県","市区町村","住所","URL","メール","フォーム","電話番号", "FAX","参照URL","平均評価数","口コミ数","営業時間(月)","営業時間(火)","営業時間(水)","営業時間(木)","営業時間(金)","営業時間(土)","営業時間(日)"]
    import requests
    # 2重起動を防ぐ

    import os
    #多重起動禁止
    import psutil

    def init_():
        #初期値設定

        #ログ確認 
        tyouhuku_conf_log_init()
        #g_val.Jyoutu_Mode_=0#取り下げ

        try:
            if("Windows"!=g_val.OS_VERSION and g_val.Jyoutu_Mode_==0):
                #MAC
                #init_lang_mac_f.pack(expand=True, fill='both')
                while(1):
                    if(g_val.language_init_mac_end==1):
                        try:
                            init_lang_mac_f.destroy()
                            canvas_mac.delete("all")
                            canvas_mac.place_forget()
                        except:
                            temp=0
                        break

                #sleep(1)
                
                #init_lang_f.pack(expand=True, fill='both')
                #init_lang_f.destroy()
                init_mode_f.pack(expand=True, fill='both')

            g_val.init_ok=0
            g_val.program1_end=1 
            g_val.program2_end=0

            #MAC ADDRESS
            _mac = getnode()                                # MACアドレス
            g_val._mac=str(f'{_mac:_X}')
            #g_val._mac=str("3C97_0E63_5731")
            print("Mac Address",g_val._mac)
            
            
            
            while(1):
                if(g_val.stop_sys_==1):os._exit(1)
                if(g_val.mode_init_end==1 or g_val.Jyoutu_Mode_==1):break

            #sleep(100)
            sleep(1)
            if(g_val.Jyoutu_Mode_==0):
                g_val.mode_get_value = combo_mode.get()
            #else:
                #g_val.language_get_value =
            print(combo_mode.get())
            init_mode_f.destroy()

            if(g_val.mode_get_value !=g_val.mode_list[1]):
                notebook_1_1.tab(cf_kategory,state="hidden")
                notebook_1_1.tab(cf_erea,state="hidden")

            if(g_val.mode_get_value ==g_val.mode_list[1]):
                init_lang_f.pack(expand=True, fill='both')
            #init mode
            #sleep(2)
            while(1):
                if(g_val.stop_sys_==1):os._exit(1)
                if(g_val.language_init_end==1 or g_val.Jyoutu_Mode_==1 or g_val.mode_get_value !=g_val.mode_list[1]):break

            sleep(1)
            if(g_val.Jyoutu_Mode_==0):
                if(g_val.mode_get_value ==g_val.mode_list[1]):
                    g_val.language_get_value = combo.get()
                else:
                    g_val.language_get_value = language_get_value=g_val.Lnagage_list[1]
            #else:
                #g_val.language_get_value =
            print(combo.get())
            if(g_val.mode_get_value ==g_val.mode_list[1]):

                init_lang_f.destroy()
            init_langage_()
            
            #4最新バージョン
            # API_ENDPOINT = "http://localhost/izanami/public/api/VersionCheck"
            API_ENDPOINT = "https://system.izanami.link/api/VersionCheck"
            
            new_version = requests.get(url = API_ENDPOINT)

            new_v = int(new_version.text.replace(".",""))
            now_v = int(g_val.SOFT_VERSION.replace(".",""))
            
            # res = r.json()
            print("version:",new_v,now_v)
            
            if(1):
                if new_v > now_v :
                    g_val.init_new_version_end=0
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        text_ini_newversion["text"]="最新バージョン "+new_version.text+" があります。\n現在のバージョン　"+g_val.SOFT_VERSION
                    else:
                        text_ini_newversion["text"]="A new version "+new_version.text+"  is available. \n Current ver. is　"+g_val.SOFT_VERSION
                
                    init_new_version.pack(expand=True, fill='both')
                    while(1):
                        print("new version")
                        if(g_val.stop_sys_==1):os._exit(1)
                        if(g_val.init_new_version_end==1):
                            if(g_val.init_sys_end==1):
                                os._exit(1)
                            break
                    os._exit(1)
                    sleep(1)
                    init_new_version.destroy()

            if(g_val.Jyoutu_Mode_==0):
                file_exists = os.path.exists('session.txt')
                print(file_exists)
                re_email = ""
                if file_exists:
                    f = open("session.txt", "r")
                    re_email = f.read()
                    print(f.read())
                print(os.path)
                print(re_email)
                if re_email == "":

                    g_val.login_ok = "no"
                    login_form.pack(expand=True, fill='both')
                    while(1):
                        print("init")
                        if(g_val.stop_sys_==1):os._exit(1)
                        if g_val.login_ok == "wrong":
                            wrong_text=ttk.Label(login_form,anchor=tkinter.E,justify="left",font=("","11",""))
                            wrong_text.place(x=100, y=170)
                            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                                wrong_text["text"]="認証情報と一致するレコードがありません。"
                            else:
                                wrong_text["text"]="Invalid your credentials."

                            
                        elif g_val.login_ok != "no" :break

                        sleep(1)
                    login_form.destroy()
                else:
                    print("email exist")
                    Login(re_email)
            
            
                if( g_val.login_ok == "free"):
                #if( g_val.login_ok == "active"):
                    g_val.Flag_free_licence =0
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        root.title('IZANAMI　営業リスト収集ツール-体験版')
                    else:
                        root.title('IZANAMI　Sales listing tool-trial')
                
                elif(g_val.login_ok == "collect_user"):#収集ユーザ時は管理者アカウントにする。
                    g_val.Flag_free_licence =1
                    #g_val.Op_ok=1
                    #if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    #    root.title('IZANAMI　営業リスト収集ツール【管理者】')
                    #else:
                    #    root.title('IZANAMI　Sales listing tool【Adomin】')
                
                else:    
                    g_val.Flag_free_licence =1
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        root.title('IZANAMI　営業リスト収集ツール')
                    else:
                        root.title('IZANAMI　Sales listing tool')


            print("アカウント",g_val.login_ok)
            print("アカウント",g_val.Op_ok)

            init_f.pack(expand=True, fill='both')
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_ini1["text"]="初期化開始"
            else:
                text_ini1["text"]="Initializing"
            sleep(1)#window表示待ち
            pro_bar["value"]=10
            
            #クロームドライバチェック
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_ini1["text"]="ドライバーチェック"
            else:
                text_ini1["text"]="Driver Checking"
                
            pro_bar["value"]=20
            #url = 'https://www.google.co.jp/search'
            #req = requests.get(url, params={'q': 'google'},timeout=3.5)
            #print(req)
            #g_val.d_path  = ChromeDriverManager(path= g_val.path1,print_first_line=False).install()
            
            #temp_path = ChromeDriverManager().install()
            #print(temp_path)
            #if("Windows"==g_val.OS_VERSION):
            #    g_val.d_path = g_val.path1+"\\chromedriver.exe"
            #else:
            #    g_val.d_path = g_val.path1+"/chromedriver.exe"#mac
            #shutil.copy(temp_path,g_val.path1)

            #2024.01.17 driverが残ってるとエラーになるので停止させる。
            for proc in psutil.process_iter():
                try:
                    print("----------------------")
                    print("プロセスID:" + str(proc.pid))

                    print("実行モジュール：" + proc.exe())
                    
                    if("chromedriver" in proc.exe()):
                        print("chromedriver 停止")
                        proc.kill()
                except :
                    traceback.print_exc()
                    print("このプロセスへのアクセス権がありません。")

            g_val.d_path  = ChromeDriverManager().install()
            print(g_val.d_path)
            pro_bar["value"]=50
            #認証チェック
            pro_bar["value"]=75

            #ログ確認    
            conf_log_init()
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_ini1["text"]="設定ファイルチェック"
            else:
                text_ini1["text"]="Checking the configuration file"
            #画面切り替え
            pro_bar["value"]=100
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_ini1["text"]="初期化完了"
            else:
                text_ini1["text"]="Initialization is complete"
            init_f.destroy()
    
            #2無料版
            print(g_val.login_ok)
            if g_val.login_ok == "free":
                g_val.init_freeversion_end=0
                init_freeversion.pack(expand=True, fill='both')
                while(1):
                    print("free")
                    if(g_val.stop_sys_==1):os._exit(1)
                    if(g_val.init_freeversion_end==1):
                        if(g_val.init_sys_end==1):
                            os._exit(1)
                        break
                    sleep(1)
                init_freeversion.destroy()
            #3ライセンス切れ
            print("ライセンス切れ")

            if g_val.login_ok == "expired":
                g_val.init_expire_end=0
                init_expire.pack(expand=True, fill='both')
                while(1):
                    print("expire")
                    if(g_val.stop_sys_==1):os._exit(1)
                    if(g_val.init_expire_end==1):
                        if(g_val.init_sys_end==1):
                            os._exit(1)
                        break
                    sleep(1)
                
                os._exit(1)

            #if g_val.login_ok == "free" or g_val.login_ok == "active":
            notebook.pack(expand=True, fill='both')#, padx=10, pady=10)
            notebook_1_1.pack(expand=True, fill='both')#, padx=10, pady=10)
            notebook_1_2.pack(expand=True, fill='both')#, padx=10, pady=10)
            notebook_1_3.pack(expand=True, fill='both')#, padx=10, pady=10)
            g_val.init_ok=1

            if(g_val.Jyoutu_Mode_==1):#常駐モード
                botton2_clicked()
        except:
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_ini1["text"]="初期化エラー"
            else:
                text_ini1["text"]="Initialization error"

            traceback.print_exc()
            g_val.data_log_write(datetime.datetime.now())
            g_val.data_log_write(traceback.format_exc())
            g_val.err_message_w(100,traceback.print_exc())

        
        return


    def botton_clicked():
        #設定保存
        g_val.f_jyouty_end =1#開始1:停止0
        g_val.conf_log_save()
        
        if(check_multiple()==0 and g_val.Jyoutu_Mode_==0):
            return

        if(check_select()==0):
            return

        button.config(state="disable")
        button2.config(state="disable")
        button1.config(state="able")

        #chk.config(state="disable")
        chk0.config(state="disable")
        chk0_todohuken.config(state="disable")
        chk0_app.config(state="able")
        g_val.stat_ =1
        g_val.stop_ =0
        g_val.re_run_=0
        g_val.search_list=[]
        g_val.program1_end =0
        #初期化
        g_val.get_imform["text"]="-  -  -"
        #設定保存
        #g_val.conf_log_save()
        g_val.conf_kate = bt_genimu_.get()
        g_val.conf_email = bt_genimu_mail.get()
        g_val.conf_todohuken = g_val.bt_genimu_eria.get()

        if(g_val.mode_get_value==g_val.mode_list[1]):#google
            g_val.thread2 = threading.Thread(target=comapyny_get_v101.val_list_get)
        elif(g_val.mode_get_value==g_val.mode_list[2]):#duda
            g_val.thread2 = threading.Thread(target=comapyny_get_duda_v101.val_list_duda_get)
        elif(g_val.mode_get_value==g_val.mode_list[3]):#rikunabi
            g_val.thread2 = threading.Thread(target=comapyny_get_duda_company_v101.val_list_dud_campany_get)
        elif(g_val.mode_get_value==g_val.mode_list[4]):#rikunabi
            g_val.thread2 = threading.Thread(target=comapyny_get_rikunabi_v101_.val_list_rikunabi_get)
        elif(g_val.mode_get_value==g_val.mode_list[5]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_mynabi_v101.val_list_mynabi_get)
        elif(g_val.mode_get_value==g_val.mode_list[6]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_shuukatsu_v101.val_list_shuukatsu_get)
        elif(g_val.mode_get_value==g_val.mode_list[7]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_en_v101.val_list_en_get)
        elif(g_val.mode_get_value==g_val.mode_list[8]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_townwork_v101.val_list_townwork_get)
        elif(g_val.mode_get_value==g_val.mode_list[9]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_tabelog_v101.val_list_tabelog_get)

        
        g_val.thread2.setDaemon(True)
        g_val.thread2.start()
        notebook.tab(1,state='disabled')#config() ["state"]="disabled"#, bg='gray')
        notebook.tab(2,state='disabled')#, bg='gray')

        sleep(1)

        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            text_st_f["text"]="\n\n\n収集中。。。 \n\n終了する場合は「終了」ボタンをおしてください。"
            g_val.window_log["text"]="収集開始"
        else:
            text_st_f["text"]="\n\n\nNow listing... \n\nClick End to stop."
            g_val.window_log["text"]="Now listing..."
        #g_val.Jyoutu_Mode_=0#取り下げ
        pb.start(2)

    def botton1_clicked():

        g_val.f_jyouty_end =0#開始1:停止0
        g_val.Jyoutu_Mode_=0#取り下げ
        #g_val.thread2.stop()
        #print(text_st_f["text"])
        #sleep(100)
        g_val.stat_ =0
        g_val.stop_ =1
        g_val.re_run_=0
        g_val.conf_log_save()
        print("g_val.url_log_his", g_val.url_log_his)
        print("button1_count: ", g_val.count)
        

    def botton2_clicked():
        #設定保存
        g_val.f_jyouty_end =1#開始1:停止0
        g_val.conf_log_save()
        print("g_val.url_log_his", g_val.url_log_his)
        print("button2_count", g_val.count)
        if(check_multiple()==0 and g_val.Jyoutu_Mode_==0):
            return

        if(check_select()==0):
            return

        button.config(state="disable")
        button2.config(state="disable")
        button1.config(state="able")
        #chk.config(state="disable")
        chk0.config(state="disable")
        chk0_todohuken.config(state="disable")
        chk0_app.config(state="able")
        g_val.stat_ =0
        g_val.stop_ =0
        g_val.re_run_=1
            
        print("==============================================")  

        program1_end =0
        g_val.program1_end =0
        g_val.conf_kate = bt_genimu_.get()
        g_val.conf_email = bt_genimu_mail.get()
        g_val.conf_todohuken = g_val.bt_genimu_eria.get()

        if(g_val.mode_get_value==g_val.mode_list[1]):
            g_val.thread2 = threading.Thread(target=comapyny_get_v101.val_list_get)
        elif(g_val.mode_get_value==g_val.mode_list[2]):
            g_val.thread2 = threading.Thread(target=comapyny_get_duda_v101.val_list_duda_get)
        elif(g_val.mode_get_value==g_val.mode_list[3]):#rikunabi
            g_val.thread2 = threading.Thread(target=comapyny_get_duda_company_v101.val_list_dud_campany_get)
        elif(g_val.mode_get_value==g_val.mode_list[4]):#rikunabi
            g_val.thread2 = threading.Thread(target=comapyny_get_rikunabi_v101_.val_list_rikunabi_get)
            # g_val.thread2 = threading.Thread(target=comapyny_get_rikunabi_v101_.val_get_rikunabi, args=(g_val.campany_list,))
        elif(g_val.mode_get_value==g_val.mode_list[5]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_mynabi_v101.val_list_mynabi_get)
        elif(g_val.mode_get_value==g_val.mode_list[6]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_shuukatsu_v101.val_list_shuukatsu_get)
        elif(g_val.mode_get_value==g_val.mode_list[7]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_en_v101.val_list_en_get)
        elif(g_val.mode_get_value==g_val.mode_list[8]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_townwork_v101.val_list_townwork_get)
        elif(g_val.mode_get_value==g_val.mode_list[9]):#mainabi
            g_val.thread2 = threading.Thread(target=comapyny_get_tabelog_v101.val_list_tabelog_get)

        #thread3 = threading.Thread(target=val_get)
        g_val.thread2.start()
        notebook.tab(1,state='disabled')#config() ["state"]="disabled"#, bg='gray')
        notebook.tab(2,state='disabled')#, bg='gray')
        sleep(1)
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            text_st_f["text"]="\n\n\n収集中。。。 \n\n終了する場合は「終了」ボタンをおしてください。"
            g_val.window_log["text"]="収集開始"
        else:
            text_st_f["text"]="\n\n\nNow listing... \n\nClick End to stop."
            g_val.window_log["text"]="Now listing..."
        pb.start(2)
        #g_val.Jyoutu_Mode_=0#取り下げ

    def check_select():
        
        result=1

        if(g_val.mode_get_value!=g_val.mode_list[1]):
            return result

        #カテゴリ選択チェック
        category_n0 =g_val.cate_box_all[0][0].get().replace('\\n', '').replace('\n', '')
        kate_tree_get=g_val.tree_kate.get_checked()
        if(len(kate_tree_get)>0):
            category_n1=kate_tree_get[0].split("  ")[2]
        else:
            category_n1=""

        if(category_n0==""):
            if(category_n1==""):
                result=0
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    messagebox.showinfo("確認", "カテゴリを入力してください。")
                else:
                    messagebox.showinfo("confirmation", "Please select the category.")

                return result
        #市区町村選択チェック
        siku_ok=0
        for siku_n in range(0,len(g_val.sikutyouson)):
            if(g_val.sikutyouson[siku_n][2]==1):
                siku_ok=1
                break
        if(siku_ok==0):
            result=0
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    messagebox.showinfo("確認", "市区町村を入力してください。")
            else:
                messagebox.showinfo("confirmation", "Please select the aria.")

            return result
        return result

    def check_multiple():
        result =1
        list_exe=[]
        if(g_val.Op_ok==0 and g_val.login_ok != "collect_user"):
            for proc in psutil.process_iter():
                
                try:
                    print("----------------------")
                    print("プロセスID:" + str(proc.pid))

                    print("実行モジュール：" + proc.exe())
                    
                    if("IZANAMI" in proc.exe()):
                        list_exe.append( proc.exe())
                    
                    #if("chromedriver" in proc.exe()):
                        #proc.exe().kill()
                        #proc.kill()

                    #print("コマンドライン:" + str(proc.cmdline()))
                    #print("カレントディレクトリ:" + proc.cwd())
                except :
                    traceback.print_exc()
                    print("このプロセスへのアクセス権がありません。")
            print(list_exe)
            if(len(list_exe)>=3):
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        messagebox.askyesno('確認', 'すでにアプリが開かれています。')
                else:
                    messagebox.askyesno('Confirmination', 'The app is already open.')
                result =0
            elif(g_val.login_ok == "wrong_mac"):
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        messagebox.askyesno('確認', 'すでに他のPCでアプリが開かれています。')
                else:
                    messagebox.askyesno('Confirmination', 'The app is already open in other PC.')
                result =0
        
        return result

    def status_wach_v():
        
        init_version_ok=0
        init_version_ok_old=0
        while(1):
            #print(g_val.stop_sys_,g_val.program1_end)
            if(g_val.stop_sys_==1 ):
                break
            sleep(60)

            API_ENDPOINT = "https://system.izanami.link/api/VersionCheck"
            new_version = requests.get(url = API_ENDPOINT)

            new_v = int(new_version.text.replace(".",""))
            now_v = int(g_val.SOFT_VERSION.replace(".",""))
            
            # res = r.json()
            print("version:",new_v,now_v)
            dt_now = datetime.datetime.now()
            dt_now_h = dt_now.hour
            date_now = datetime.date.today()
            youbi_ = date_now.weekday()

            
            print("現在の時間,曜日",dt_now_h,youbi_)
            #if(youbi_==4 and dt_now_h>=16):#金曜日だけ16時以降
            #    init_version_ok=1
            if(dt_now_h>=16 and g_val.init_ok==1):#そのほかは22時以降
                init_version_ok=1
            else:
                init_version_ok=0
                
            print("チェックOK",init_version_ok)

            if new_v > now_v and init_version_ok==1 and init_version_ok_old==0 :
                
                print("バージョンチェック")
                cm="最新バージョンがあります。\n現在のバージョン　"+g_val.SOFT_VERSION
                cm_e="A new version is available. \n Current ver. is　"+g_val.SOFT_VERSION


                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    messagebox.showinfo("警告", cm)
                else:
                    messagebox.showinfo("Attention",cm_e)

                webbrowser.open("https://system.izanami.link/user/index", new=0, autoraise=True)
                print("終了プロセス")

                #root.destroy()
                g_val.stop_sys_=1
                g_val.stop_=1
                while(1):
                    sleep(1)
                    try:
                        #print(g_val.program1_end,g_val.program2_end)
                        if(g_val.program1_end==1 and g_val.program2_end==1):
                            
                            break
                    except:
                        temp=0
                os._exit(1)
                sys.exit(1)
                root.destroy()

                #root.destroy()
            init_version_ok_old = init_version_ok

            print("=====スレッド=====")
            for thread in threading.enumerate():
                print(thread)
                    

        #print("STWACH END2")
        return

    def status_wach_():
        end_old=g_val.program1_end
        csv_free_ok_old=1
        while(1):
            #print("STWACH",g_val.stop_sys_,g_val.program1_end)
            if(g_val.stop_sys_==1 ):
                g_val.program2_end=1
                text_st_f["text"]="終了処理中。。。。"
                print("STWACH終了")

                sleep(1)
                break
            
            sleep(1)
            
            if(csv_free_ok_old ==1 and g_val.csv_free_ok==0):
                if(g_val.language_get_value==g_val.Lnagage_list[1]):
                    messagebox.showinfo("確認", "無料期間が切れました。有料アカウントを登録してください。")
                else:
                    messagebox.showinfo("confirmation", "Your free trial has expired. Please register a paid account.")
            csv_free_ok_old = g_val.csv_free_ok

            #終了監視
            #print("STWACH終了2")
            if(g_val.program1_end==1 and end_old==0 and g_val.stop_sys_==0):
                try:
                    print("program1 END")
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        text_st_f["text"]="終了処理中。。。"
                    else:
                        text_st_f["text"]="End listing..."

                    #g_val.thread2.join()
                    #sleep(1)
                    button.config(state="able")
                    button2.config(state="able")
                    button1.config(state="disable")
                    #chk.config(state="able")
                    chk0.config(state="able")
                    chk0_todohuken.config(state="able")
                    chk0_app.config(state="able")
                    notebook.tab(1,state='normal')#config() ["state"]="disabled"#, bg='gray')
                    notebook.tab(2,state='normal')#, bg='gray')


                    #print("STWACH終了2")
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):

                        if(g_val.mode_get_value==g_val.mode_list[1]):
                            temp="開始:新規で収集を始めます。\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp+="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[2]):
                            temp="開始:duda検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[3]):
                            temp="開始:duda検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[4]):
                            temp="開始:リクナビNEXT検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[5]):
                            temp="開始:マイナビ検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[6]):
                            temp="開始:就活会議検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[7]):
                            temp="開始:エン転職検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[8]):
                            temp="開始:タウンワーク検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
                        elif(g_val.mode_get_value==g_val.mode_list[9]):
                            temp="開始:食べログ検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
                            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
                            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"


                        text_st_f["text"] = temp

                        if(g_val.stop_==1):#一次停止の時

                            messagebox.showinfo('IZANAMI', '一時停止しました。')
                            g_val.window_log["text"]="収集一時停止"
                        else:
                            messagebox.showinfo('IZANAMI', '収集が終了しました。')
                            g_val.window_log["text"]="収集完了"
                            
                    else:
                        temp = "Start: Create a new listing.\nEnd: Stop listing.\nContinue: Restart listing where you left off.\n\n\nExact listing: It may include items not related to your categories.\nChecking in the Exact listing allows it to collect the exactly \nsame names of your categories. \nNote the number of listing items will decrease."
                        #temp="Start: Create a new listing.\nEnd: Stop listing.\nContinue: Restart listing where you left off.\n\n\nExact listing: It may include items not related to your categories.\nChecking in the Exact listing allows it to collect the exactly \nsame names of your categories. \nNote the number of listing items will decrease."
                        temp +="\n\n\nEmail Exact listing:Collect email addresses strictly. \nCollection speed may decrease."
                        text_st_f["text"]=temp

                        if(g_val.stop_==1):#一次停止の時
                            messagebox.showinfo('IZANAMI', 'Listing has paused.')
                            g_val.window_log["text"]="Listing has paused."
                        
                        else:
                            messagebox.showinfo('IZANAMI', 'Listing has stopped.')
                            g_val.window_log["text"]="Listing has stopped."
                    g_val.csv_free_ok=1

                    print("program1 END2")
                    pb.stop()
                    program_end=1
                except:
                    temp=0

                print("STWACH終了4")

            end_old = g_val.program1_end
        #g_val.program2_end=1
        #print("STWACH END")
        #sleep(1)

        #ログアウト
        print("メール",g_val.E_mail)
        API_ENDPOINT = "https://system.izanami.link/api/logout"
        data = {
        #'email':g_val.E_mail,
        'email':g_val.E_mail,

        # 'password':password,
        }
        r = requests.post(url = API_ENDPOINT, data = data)
        res = r.json()
        print("===LOG_OUT===================")
        #print(res["result"],res["value"])
        print(res)
        print("===LOG_OUT===================")
        #root.destroy()

        while(1):
            sleep(1)
            #break
            try:
                print(g_val.program1_end,g_val.program2_end)
                if(g_val.program1_end==1 and g_val.program2_end==1):
                    
                    break
            except:
                temp=0
        print("収集END")
        
        print("終了プロセス")
        if(g_val.init_ok==1):
            g_val.conf_log_save()
        #root.destroy()
        #sys.exit(1)
        #os._exit(1)
        #root.destroy()
        
        print("終了プロセス100")
        os._exit(1)
        sys.exit(1)
        root.destroy()
        return

    # ボタンの作成と配置
    button = ttk.Button(tab_st,
                    text = '開始',
                    # クリック時にval()関数を呼ぶpy
                    #height = 50,
                    #width = 15,
                    
                    command=botton_clicked
                    )
    button.place(x=50, y=40,width=100,height=50)

    button1 = ttk.Button(tab_st,
                    text = '一時停止',
                    # クリック時にval()関数を呼ぶpy
                    command=botton1_clicked
                    )
    button1.place(x=175, y=40,width=100,height=50)

    #button2 = tkinter.Entry(width=10)
    button2 = ttk.Button(tab_st,
                    text = '途中から再開',
                    # クリック時にval()関数を呼ぶpy
                    command=botton2_clicked
                    )
    button2.place(x=300, y=40,width=100,height=50)

    pb = ttk.Progressbar(tab_st, length=100, mode='determinate')

    #pb.grid(row=0,column=0,sticky=(E))
    #pb.pack(padx=10, pady=350
    if("Windows"==g_val.OS_VERSION):
        pb.place(x=300, y=100)
    else:
        pb.place(x=400, y=100)
    ############################################################################################
    ## mac init
    def mac_init_clicked():

        g_val.language_init_mac_end=1

    button_mac = ttk.Button(init_lang_mac_f,
                    text = 'OK',
                    # クリック時にval()関数を呼ぶpy
                    command=mac_init_clicked
                    )
    button_mac.place(x=200,y=400,width=75,height=25)

    text_ini_mac=ttk.Label(init_lang_mac_f,anchor=tkinter.E,justify="left",font=("","11",""))#,bg="#f8f8f8")
    text_ini_mac.place(x=10, y=20)
    text_ini_mac["text"]="セキュリティの関係上、初回起動時にIZANAMI.appファイルの場所が"
    text_ini_mac["text"]+="\n移動している場合があります。"
    text_ini_mac["text"]+="\ndistフォルダの中にIZANAMI.appファイルを移動して実行してください。"

    text_ini_mac["text"]+="\n\nFor security reasons, the location of the IZANAMI.app" 
    text_ini_mac["text"]+="\nfile may have moved when you first start up."
    text_ini_mac["text"]+="\nMove the IZANAMI.app file into the dist folder and run it."

    if("Windows"!=g_val.OS_VERSION):
        try:
            haruna = tkinter.PhotoImage(file=g_val.path1+"/../conf/init_mac_.png")
            canvas_mac = tkinter.Canvas(width=400, height=150,bg="gray")
            canvas_mac.place(x=75, y=200)
            canvas_mac.create_image(0, 0, image=haruna, anchor=tkinter.NW)
        except:
            traceback.print_exc()
            g_val.data_log_write(datetime.datetime.now())
            g_val.data_log_write(traceback.format_exc())

    #langage : init
    def lang_clicked():
        #sleep(1)
        g_val.language_get_value = combo.get()
        print(combo.get())
        if(g_val.language_get_value==g_val.Lnagage_list[0]):

            messagebox.showinfo('Confirmation', '言語を選択してください。\n'+'Please select language.')
            
            return
        g_val.language_init_end=1


    button3 = ttk.Button(init_lang_f,
                    text = 'SAVE',
                    # クリック時にval()関数を呼ぶpy
                    command=lang_clicked
                    )
    if("Windows"==g_val.OS_VERSION):
        button3.place(x=20,y=130,width=75,height=25)
    else:
        button3.place(x=20,y=130,width=75,height=25)
    text_ini_lang=ttk.Label(init_lang_f,anchor=tkinter.E,justify="left",font=("","11",""))#,bg="#f8f8f8")
    text_ini_lang.place(x=10, y=5)
    text_ini_lang["text"]="Language and Country.\n言語・エリア選択"

    text_ini_lang=ttk.Label(init_lang_f,anchor=tkinter.E,justify="left",font=("","10",""))
    if("Windows"==g_val.OS_VERSION):
        text_ini_lang.place(x=10, y=50)
    else:
        text_ini_lang.place(x=20, y=53)
        
    text_ini_lang["text"]="Select a country where you wish to make a list.\nリストを収集する国を選びください。"


    variable = tkinter.StringVar ( ) #A~Dが文字列の場合
    if("Windows"==g_val.OS_VERSION):
        combo = ttk.Combobox ( init_lang_f ,width=30,height=5, values = g_val.Lnagage_list , textvariable = variable,state="readonly")
    else:
        combo = ttk.Combobox ( init_lang_f ,width=20,height=5, values = g_val.Lnagage_list , textvariable = variable,state="readonly")

    combo.place(x=20, y=90)
    combo.current(0)
    


    #init_mode_f
    #init modde
    def mode_clicked():
        #sleep(1)
        g_val.mode_get_value = combo_mode.get()
        print(combo_mode.get())
        if(g_val.mode_get_value==g_val.mode_list[0]):

            messagebox.showinfo('Confirmation', '検索モードを選択してださい。')
            
            return
        g_val.mode_init_end=1


    button3_mode = ttk.Button(init_mode_f,
                    text = 'SAVE',
                    # クリック時にval()関数を呼ぶpy
                    command=mode_clicked
                    )
    if("Windows"==g_val.OS_VERSION):
        #button3_mode.place(x=20,y=130,width=75,height=25)
        button3_mode.place(x=190,y=230,width=75,height=25)
    else:
        #button3_mode.place(x=20,y=130,width=75,height=25)
        button3_mode.place(x=190,y=230,width=75,height=25)

    variable = tkinter.StringVar ( ) #A~Dが文字列の場合
    if("Windows"==g_val.OS_VERSION):
        combo_mode = ttk.Combobox ( init_mode_f ,width=30,height=13, values = g_val.mode_list , textvariable = variable,state="readonly")
    else:
        combo_mode = ttk.Combobox ( init_mode_f ,width=20,height=13, values = g_val.mode_list , textvariable = variable,state="readonly")

    combo_mode.place(x=120, y=190)
    combo_mode.current(0)

    text_ini_mode=ttk.Label(init_mode_f,anchor=tkinter.E,justify="left",font=("","10",""))
    if("Windows"==g_val.OS_VERSION):
        text_ini_mode.place(x=120, y=150)
    else:
        text_ini_mode.place(x=120, y=153)
        
    text_ini_mode["text"]="収集する検索モードを選択してください。"


    #############################################################################################

    #厳密収集
    # チェックONにする
    bt_genimu_ = tkinter.BooleanVar()
    #bt_genimu_.set(True)

    # チェックボタン作成
    #chk = ttk.Checkbutton(tab_st, variable=bt_genimu_, text='厳密取集')
    #chk.place(x=50, y=100)#height=100)

    #Mail詳細取集
    bt_genimu_mail = tkinter.BooleanVar()
    #bt_genimu_.set(True)

    # チェックボタン作成
    chk0 = ttk.Checkbutton(tab_st, variable=bt_genimu_mail, text='メール収集をさらに強化')
    chk0.place(x=50, y=155)#height=100)

    g_val.bt_genimu_eria = tkinter.BooleanVar()
    # チェックボタン作成
    chk0_todohuken = ttk.Checkbutton(tab_st, variable=g_val.bt_genimu_eria, text='都道府県が一致しない企業も収集する')
    chk0_todohuken.place(x=50, y=175)#height=100)

    #常駐
    def bn_creat_strat():
        if("Windows"==g_val.OS_VERSION):
            if(g_val.bt_app_jyoutyu_.get()):
                # スタートアップフォルダのパスを取得
                startup = winshell.startup()

                # ショートカットのパスを作成
                path = os.path.join(startup, "shortcut.lnk")
                print(path)
                # ショートカットを作成
                with winshell.shortcut(path) as link:
                    link.path = g_val.path1+"\\IZANAMI.exe"
                    link.description = "IZNAMI"
                    # オプション：ショートカットアイコンを変更する
                    # link.icon_location = "C:\\path\\to\\icon.ico"
            else:
                try:
                    startup = winshell.startup()
                    # ショートカットのパスを作成
                    path = os.path.join(startup, "shortcut.lnk")
                    os.remove(path) # ショートカットを削除
                except:
                    temp=0
        else:
            if(g_val.bt_app_jyoutyu_.get()):
                # 追加するアプリケーションのパス
                app_path = g_val.path1+"/IZANAMI.app"
                # ログイン項目に追加するためのコマンドを作成
                cmd = 'osascript -e \'tell application "System Events" to make login item at end with properties {{path:"{}"}}\''.format(app_path)
                # コマンドを実行
                subprocess.Popen(cmd, shell=True)
            else:
                app_name = "IZANAMI"
                # ログイン項目から削除するためのコマンドを作成
                cmd = 'osascript -e \'tell application "System Events" to delete login item "{}"\''.format(app_name)
                # コマンドを実行
                subprocess.Popen(cmd, shell=True)
        #conf保存
        g_val.conf_log_save()

    g_val.bt_app_jyoutyu_ = tkinter.BooleanVar()
    chk0_app = ttk.Checkbutton(tab_st, variable=g_val.bt_app_jyoutyu_, text='アプリを常駐（自動リトライ。不具合がある場合は外してください）',command=bn_creat_strat)
    chk0_app.place(x=50, y=135)#height=100)

    

    ########重複削除##############################################################

    def bn_tyouhuku_sansyou():
        
        typ = [('result','*.csv')] 
        if("Windows"==g_val.OS_VERSION):
            dir = path1+"\\..\\out"
        else:
            dir = path1+"/../out"
        g_val.fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
        text_tyouhuku_f["text"]=os.path.basename(g_val.fle) 

    def bn_tyouhuku_togo():
        #チェックボタンを取得
        #ファイル読み込んで形式チェック
        #NGの場合テキストで出力
        #OKの場合csvデータを新しいリストにして名前を変えて保存
        g_val.fle
        err_=""
        if(bln1.get() or bln2.get()):
            #ファイル読み込み
            out_list_t=[]
            n=0
            try:
                with open(g_val.fle,newline='', encoding='utf_8_sig',) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        out_list_t.append(row)#A列
                out_list=[]
                #形式チェック
                #print(out_list_t)
                i=0
                h_ok=1
                #print(len(g_val.header_op))
                #print()
                print(len( out_list_t[0]))
                for out_list_t_h in out_list_t[0]:
                    if(len(out_list_t[0])==21):
                        print(out_list_t_h,g_val.header_op[i] )
                        if(g_val.header_op[i] != out_list_t_h):
                            
                            h_ok=0
                            break
                    else:
                        print(out_list_t_h,g_val.header_nominal[i] )
                        if(g_val.header_nominal[i] != out_list_t_h):
                            
                            h_ok=0
                            break
                    i+=1
                if(h_ok==0):
                    err_ ="out_h"  
                #重複削除
                o_file=(g_val.fle).rsplit(".csv",1)[0]
                if(bln1.get()):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        o_file =o_file+"(電話番号統合)"
                    else:
                        o_file =o_file+"(tell)"
                if(bln2.get()):
                    if(g_val.language_get_value==g_val.Lnagage_list[1]):
                        o_file =o_file+"(メール統合)"
                    else:
                        o_file =o_file+"(mail)"
                o_file =o_file+".csv"
                out_list =[]
                for out_list_t_n in out_list_t:
                    cal_ok=1
                    for out_list_n in out_list:
                        if(bln1.get()):#電話番号
                            if(len(out_list_t[0])==21):
                                if(out_list_n[9] == out_list_t_n[9] and out_list_t_n[9]!=""):
                                    cal_ok=0
                            else:
                                if(out_list_n[8] == out_list_t_n[8] and out_list_t_n[8]!=""):
                                    cal_ok=0

                                break
                        if(bln2.get()):#メール
                            if(out_list_n[7] == out_list_t_n[7]and out_list_t_n[7]!=""):
                                cal_ok=0
                                break

                    if(cal_ok==1):
                        out_list.append(out_list_t_n)

                #print(out_list)
                #書き込み
                if(err_==""):
                    with open(o_file,'w',newline="", encoding='utf_8_sig') as file_w:
                        for out_list_n in out_list:
                            
                            file_o_csv = csv.writer(file_w, delimiter=',')
                            file_o_csv.writerow(out_list_n)
                            #print("======================")
                            #print(out_list_n)
                        #print(o_file)
                        file_w.close()
            except:
                traceback.print_exc()
                err_ ="out_err"    


        else :err_ ="btn_err"
        if(err_==""):
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                messagebox.showinfo('確認', '統合が完了しました。')
            else:
                messagebox.showinfo('Confirmation', 'Completed.')
        else:
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                text_tyouhuku_e["text"]="エラーが発生しました。以下を確認してください。\n・電話番号、メールアドレスどちらで統合するか選択されていない。\n・csvファイルがIZANAMIの形式でない。(加工していると統合できません。)"
            else:
                text_tyouhuku_e["text"]="Error has occurred. Check the following.\n・It is not selected whether to integrate by phone number or email address.\n・The csv file is not in IZANAMI format. (It cannot be integrated if it is processed.)"
        return


    text_tyouhuku_=ttk.Label(op_tyouhuku,
                    text = '重複している行を統合します。重複している場合は、上にある行を優先します。',
                    )
    text_tyouhuku_.place(x=10, y=0)


    bln1 = tkinter.BooleanVar()
    #bln1.set(True)
    bln2 = tkinter.BooleanVar()
    #bln2.set(True)

    # チェックボタン作成
    chk_tell = ttk.Checkbutton(op_tyouhuku, variable=bln1, text='電話番号')
    chk_tell.place(x=10, y=30)#height=100)
    # チェックボタン作成
    chk_mail = ttk.Checkbutton(op_tyouhuku, variable=bln2, text='メールアドレス')
    chk_mail.place(x=100, y=30)#height=100)
    #button2 = tkinter.Entry(width=10)
    button_tyohuku = ttk.Button(op_tyouhuku,
                    text = '参照',
                    # クリック時にval()関数を呼ぶpy
                    command=bn_tyouhuku_sansyou
                    )
    button_tyohuku.place(x=10, y=70,width=75,height=25)

    button_tyohuku_2 = ttk.Button(op_tyouhuku,
                    text = '実行(事前にバックアップをとることをお勧めします。)',
                    # クリック時にval()関数を呼ぶpy
                    command=bn_tyouhuku_togo
                    )
    button_tyohuku_2.place(x=50, y=125,width=300,height=25)

    text_tyouhuku_e=ttk.Label(op_tyouhuku,anchor=tkinter.E,justify="left")
    text_tyouhuku_e.place(x=10, y=200)
    #text_tyouhuku_e["text"]="エラーが発生しました。以下を確認してください。\n・電話番号、メールアドレスどちらで統合するか選択されていない。\n・csvファイルがIZANAMIの形式でない。(加工していると統合できません。)"

    text_tyouhuku_f=ttk.Label(op_tyouhuku,anchor=tkinter.E,justify="left")
    text_tyouhuku_f.place(x=100, y=70)
    text_tyouhuku_f["text"]="ファイルを選択してください。"

    ########重複削除 END##############################################################
    ########起動停止#################################################################
    text_st_f=ttk.Label(tab_st,anchor=tkinter.E,justify="left")
    text_st_f.place(x=60, y=220)
    #text_st_f["text"]="開始:新規で収集を始めます。\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。
    # \n\n\n *「カテゴリを厳密に収集する」にチェックが入っているとカテゴリとほぼ同じ \n名前のURLのみ収集します。件数は少ないですが、収集精度が高くなり \nます。チェックを外すとすべてのカテゴリを収集します。精度は低いですが、 \n大量のリストを収集できます。"
    temp="開始:新規で収集を始めます。"
    temp +="\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
    
    temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"

    text_st_f["text"]=temp
    g_val.text_st_f1=ttk.Label(tab_st,anchor=tkinter.E,justify="left")

    if("Windows"==g_val.OS_VERSION):
        g_val.text_st_f1.place(x=200, y=155)
    else:
        g_val.text_st_f1.place(x=250, y=160)

    
    g_val.text_st_f1["text"]="プロキシ設定：無効"

    g_val.window_log=ttk.Label(tab_st,anchor="w",justify="left",width=30)#ステータス
    if("Windows"==g_val.OS_VERSION):
        g_val.window_log.place(x=50, y=100)
    else:
        g_val.window_log.place(x=40, y=100)
    g_val.window_log["text"]="準備完了"


    #text_st_f2=ttk.Label(tab_st,anchor=tkinter.E,justify="left")
    #text_st_f2.place(x=60, y=170)
    #text_st_f["text"]="開始:新規で収集を始めます。\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。
    # \n\n\n *「カテゴリを厳密に収集する」にチェックが入っているとカテゴリとほぼ同じ \n名前のURLのみ収集します。件数は少ないですが、収集精度が高くなり \nます。チェックを外すとすべてのカテゴリを収集します。精度は低いですが、 \n大量のリストを収集できます。"
    #temp="※開始ボタンを押すとDUDA検索画面が表示されます。条件を入力が完了すると開始されます。"
    #text_st_f2["text"]=temp

    ##################################################################################
    #######OPtion####################################################################
    KEY = "74ujfur@"
    KEY0 = "tester@12345"
    KEY_DBG="dbg12345"
    KEY_COLLECT ="freedommm"

    def ex_otion_cal():
        #print(g_val.op_ex_txt_rntry.get())

        if(KEY == g_val.op_ex_txt_rntry.get().replace('\\n', '').replace('\n', '') or KEY0 == g_val.op_ex_txt_rntry.get().replace('\\n', '').replace('\n', '')):
            button_op_ex["text"] = "OK"
            button_op_ex['bg'] = "#DDFFFF"
            button_op_ex['state'] = "disable"
            g_val.Op_ok=1
            g_val.Flag_free_licence=1  
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                root.title('IZANAMI　営業リスト収集ツール【管理者】')
            else:
                root.title('IZANAMI　Sales listing tool【Adomin】')
                
        else:
            button_op_ex["text"] = "NG"
            button_op_ex["bg"]= "#FADBDA"

        if(button_op_ex["text"] == "OK"):
            return
            
        if(KEY_COLLECT == g_val.op_ex_txt_rntry.get().replace('\\n', '').replace('\n', '')):
            g_val.CL_INIT_=1
            button_op_ex["text"] = "OK"
            button_op_ex['bg'] = "#DDFFFF"
            #button_op_ex['state'] = "disable"
            g_val.dbg_=0
            g_val.login_ok = "collect_user"
            #g_val.Op_ok=1
            g_val.Flag_free_licence=1
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                root.title('IZANAMI　営業リスト収集ツール【FREEDOM】')
            else:
                root.title('IZANAMI　Sales listing tool【FREEDOM】')
        else:
            button_op_ex["text"] = "NG"
            button_op_ex["bg"]= "#FADBDA"

        if(button_op_ex["text"] == "OK"):
            return
        #DBG
        if(KEY_DBG == g_val.op_ex_txt_rntry.get().replace('\\n', '').replace('\n', '')):
            button_op_ex["text"] = "OK"
            button_op_ex['bg'] = "#DDFFFF"
            #button_op_ex['state'] = "disable"
            g_val.dbg_=1
            #g_val.Op_ok=1
            #g_val.Flag_free_licence=1
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                root.title('IZANAMI　営業リスト収集ツール【DEBUG】')
            else:
                root.title('IZANAMI　Sales listing tool【DEBUG】')
        else:
            button_op_ex["text"] = "NG"
            button_op_ex["bg"]= "#FADBDA"



        print("パスワード")
    text_op_ex_f=ttk.Label(op_ex,anchor=tkinter.E,justify="left")
    text_op_ex_f.place(x=10, y=10)
    text_op_ex_f["text"]="パスワードを入力してください。"
    #s_op_ex = tkinter.Style()
    #s_op_ex.theme_use('classic')
    #s_op_ex.configure('MyWidget.TButton', background="blue")

    button_op_ex = tkinter.Button(op_ex,
                    text = '送信',
                    # クリック時にval()関数を呼ぶpy
                    command=ex_otion_cal,
                    #bg="#DDFFFF"
                    )
    if("Windows"==g_val.OS_VERSION):
        button_op_ex.place(x=260, y=41,width=50,height=25)
        g_val.op_ex_txt_rntry = tkinter.Entry(op_ex,width=40)
    else:
        button_op_ex.place(x=310, y=45,width=60,height=30)
        g_val.op_ex_txt_rntry = tkinter.Entry(op_ex,width=30)

    g_val.op_ex_txt_rntry.place(x=10, y=45)
    #######OPtion and####################################################################
    #######エリア設定########################################################################
    def eria_sentaku_():
        #print(check_eria_bln.get())
        check_eria_clr_bln.set(False)
        check_eria_popular_bln.set(False)
        for todouhulen_ in g_val.todo_huken_:
            id0 = todouhulen_
            if(check_eria_bln.get()):
                g_val.tree.change_state(id0, "tristate")
                t=0
            for sikutyouson_n in g_val.sikutyouson_:
                if(sikutyouson_n[0]==todouhulen_):
                    id = todouhulen_+"  "+sikutyouson_n[1]
                    #print(id)
                    if(check_eria_bln.get()):
                        g_val.tree.change_state(id, "checked")
                        t=0
    def eria_sentaku_clr():
        #print(check_eria_bln.get())
        check_eria_bln.set(False)
        check_eria_popular_bln.set(False)
        for todouhulen_ in g_val.todo_huken_:
            id0 = todouhulen_
            g_val.tree.change_state(id0, "unchecked")
            for sikutyouson_n in g_val.sikutyouson_:
                if(sikutyouson_n[0]==todouhulen_):
                    id = todouhulen_+"  "+sikutyouson_n[1]
                    g_val.tree.change_state(id, "unchecked")
                    
    def eria_popular():
        #print(check_eria_bln.get())
        check_eria_bln.set(False)
        check_eria_clr_bln.set(False)
        #check_eria_popular_bln.set(False)
        #一回クリア
        for todouhulen_ in g_val.todo_huken_:
            id0 = todouhulen_
            g_val.tree.change_state(id0, "unchecked")
            for sikutyouson_n in g_val.sikutyouson_:
                if(sikutyouson_n[0]==todouhulen_):
                    id = todouhulen_+"  "+sikutyouson_n[1]
                    g_val.tree.change_state(id, "unchecked")

        #セット
        for eria_n in g_val.default_eria:
            todouhuken_=eria_n[1]
            sikutyouson_= eria_n[2]
            #print(todouhuken_,sikutyouson_)
            if(todouhuken_ !="-" and todouhuken_ !=""):
                try:
                    g_val.tree.change_state(todouhuken_, "tristate")
                    g_val.tree.change_state(todouhuken_+"  "+sikutyouson_, "checked")
                except:
                    traceback.print_exc()
                    temp=0
        

    # ツリービューの作成
    from ttkwidgets import CheckboxTreeview
    #tree = ttk.Treeview(cf_erea, height=10)
    g_val.tree = CheckboxTreeview(cf_erea,height=15,show='tree')
    g_val.tree.column("#0", minwidth=0, width=350) #コラムをつけるか否か

    def set_todohuken():
        for todouhulen_ in g_val.todo_huken_:

            g_val.tree.insert("", "end", todouhulen_, text=todouhulen_)
            #tree.change_state(todouhulen_, "checked")
            for sikutyouson_n in g_val.sikutyouson_:
                if(sikutyouson_n[0]==todouhulen_):
                    #print(todouhulen_,sikutyouson_n)
                    try:
                        #if(g_val.mode_get_value==g_val.mode_list[1]):
                        id=todouhulen_+"  "+sikutyouson_n[1]
                        g_val.tree.insert(todouhulen_, "end",id , text=sikutyouson_n[1])
                        #tree.change_state(id, "checked")
                    except:
                        temo=0
    g_val.tree.pack()
    # ツリービューの配置
    #tree.place(x=10, y=500)

    g_val.tree.grid(row=0, column=0,padx=10,pady=40)

    #ysb = ttk.Scrollbar(cf_erea, orient=tkinter.VERTICAL, width=16, command=g_val.tree.yview)

    ysb = ttk.Scrollbar(cf_erea, orient=tkinter.VERTICAL, command=g_val.tree.yview)


    g_val.tree.configure(yscrollcommand=ysb.set)
    ysb.grid(row=0, column=1, pady=40,sticky='news')

    #text_op_ex_f=ttk.Label(cf_erea,anchor=tkinter.E,justify="left")
    #text_op_ex_f.place(x=10, y=10)
    #text_op_ex_f["text"]="エリアをチェックしてください"
    check_eria_bln = tkinter.BooleanVar()

    check_eria = ttk.Checkbutton(
        cf_erea,
        text="全選択",
        command=eria_sentaku_,
        variable=check_eria_bln,
    )
    check_eria.place(x=10, y=10)

    check_eria_clr_bln = tkinter.BooleanVar()

    check_eria_clr = ttk.Checkbutton(
        cf_erea,
        text="全解除",
        command=eria_sentaku_clr,
        variable=check_eria_clr_bln,
    )
    check_eria_clr.place(x=100, y=10)

    check_eria_popular_bln = tkinter.BooleanVar()
    check_eria_popular= ttk.Checkbutton(
        cf_erea,
        text="人気都市のみ",
        command=eria_popular,
        variable=check_eria_popular_bln,
    )
    check_eria_popular.place(x=200, y=10)

    #######エリア設定終了########################################################################
    #######カテゴリ##############################################################################

    def kate_sentaku_():
        #print(check_eria_bln.get())
        kate_clr_bln.set(False)
        if(kate_bln.get()):
            for daikate_n in g_val.dai_kate_:
                id0 = daikate_n
                g_val.tree_kate.change_state(id0, "tristate")
            for tyuu_kate_n in g_val.tyuu_kate_:
                id = tyuu_kate_n[0]+"  "+tyuu_kate_n[1]
                g_val.tree_kate.change_state(id, "tristate")
            for syou_kate_n in g_val.syou_kate_:
                id = syou_kate_n[0]+"  "+syou_kate_n[1]+"  "+syou_kate_n[2]
                g_val.tree_kate.change_state(id, "checked")

    def kate_sentaku_clr_():
        #print(check_eria_bln.get())
        kate_bln.set(False)
        if(kate_clr_bln.get()):
            for daikate_n in g_val.dai_kate_:
                id0 = daikate_n
                g_val.tree_kate.change_state(id0, "unchecked")
            for tyuu_kate_n in g_val.tyuu_kate_:
                id = tyuu_kate_n[0]+"  "+tyuu_kate_n[1]
                g_val.tree_kate.change_state(id, "unchecked")
            for syou_kate_n in g_val.syou_kate_:
                id = syou_kate_n[0]+"  "+syou_kate_n[1]+"  "+syou_kate_n[2]
                g_val.tree_kate.change_state(id, "unchecked")

    #キャンバスエリア
    canvas_kate = tkinter.Canvas(cf_kategory, width = 200, height = 250)
    canvas_kate["scrollregion"]=(0, 0, 150, 150)
    canvas_kate.pack()
    canvas_kate.grid(row=0, column=0,pady=80)
    #canvas_kate.pack()

    ysb_kate = ttk.Scrollbar(cf_kategory, orient=tkinter.VERTICAL, command=canvas_kate.yview)
    #ysb_kate.pack()
    canvas_kate.configure(yscrollcommand = ysb_kate.set)

    ysb_kate.grid(row=0, column=1, pady = 80 , sticky=tkinter.N + tkinter.S)
    #canvas_kate.pack()

    kate_bln = tkinter.BooleanVar()
    check_kate0 = ttk.Checkbutton(
        cf_kategory,
        text="すべてチェック",
        command=kate_sentaku_,
        variable=kate_bln,

    )
    check_kate0.place(x=225, y=50)

    kate_clr_bln = tkinter.BooleanVar()
    check_clr_kate0 = ttk.Checkbutton(
        cf_kategory,
        text="すべて外す",
        command=kate_sentaku_clr_,
        variable=kate_clr_bln,

    )
    check_clr_kate0.place(x=350, y=50)

    text_kate=ttk.Label(cf_kategory,anchor=tkinter.E,justify="left",font=("", "12", "bold"))
    text_kate.place(x=30, y=25)
    text_kate["text"]="キーワードから収集"

    text_kate0=ttk.Label(cf_kategory,anchor=tkinter.E,justify="left",font=("", "12", "bold"))
    text_kate0.place(x=250, y=25)
    text_kate0["text"]="カテゴリから収集"

    text_kate1=ttk.Label(cf_kategory,anchor=tkinter.E,justify="left",font=("", "11", ""))
    text_kate1.place(x=10, y=2.5)
    text_kate1["text"]="収集中"

    g_val.get_imform = ttk.Label(cf_kategory,justify="left",anchor="w",font=("", "11", ""),relief="ridge",width=45)#width=40,anchor=tkinter.E
    g_val.get_imform.place(x=70, y=2.5)
    #g_val.get_imform["text"]="--------"
    #g_val.get_imform["state"]='disabled'


    #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)

    text_kate2=ttk.Label(cf_kategory,anchor=tkinter.E,justify="left",font=("", "8", ""))
    text_kate2.place(x=30, y=50)
    text_kate2["text"]="*Google地図表示されるものが収集\nされます。"

    text_kate3=ttk.Label(cf_kategory,anchor=tkinter.E,justify="left",font=("", "8", ""))
    text_kate3.place(x=30, y=350)
    text_kate3["text"]="*キーワードの上から優先的に収集し、すべて終わるとチェックしたカテゴリの上\nから順に収集していきます。"


    #Frameを作成
    frame_kate = ttk.Frame(canvas_kate)#,bg='white') #背景を白に
    #frameをcanvasに配置
    canvas_kate.create_window((0,0),window=frame_kate,anchor=tkinter.NW,width=200,height=300)#canvas_kate.cget('width')) 

    #frameをcanvasに配置
    #canvas_kate.create_window((0,0),window=frame_kate,anchor=tkinter.NW,width=canvas_kate.cget('width'))   #anchor<=NWで左上に寄せる
    g_val.cate_box_all=[]
    g_val.chk_kate_bln = []
    for i in range(0,20):
        cate_box =[""]
        g_val.cate_box_all.append(copy.deepcopy(cate_box))
        
        g_val.cate_box_all[i][0] = ttk.Label(frame_kate)
        if(i<9):
            g_val.cate_box_all[i][0].place(x=7.5, y=(5+i*20))
        else:
            g_val.cate_box_all[i][0].place(x=5, y=(5+i*20))

        g_val.cate_box_all[i][0]["text"]=i+1

        g_val.cate_box_all[i][0] = tkinter.Entry(frame_kate,width=25)
        g_val.cate_box_all[i][0].place(x=30, y=(7.5+i*20))
        #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
        #g_val.cate_box_all[i][3].insert(tkinter.END,"CATEGORY TEST TEST "+str(i))

        if(50+i*20)>=300:
            canvas_kate["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
            canvas_kate.create_window((0,0),window=frame_kate,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 

    # ツリービューの作成

    g_val.tree_kate = CheckboxTreeview(cf_kategory,height=12,show='tree')
    g_val.tree_kate.column("#0", minwidth=0, width=200) #コラムをつけるか否か
    #g_val.tree_kate.insert("", "0", "ID", text="食品")
    #g_val.tree_kate.insert("ID", "end", "ID0", text="イタリア")

    def cate_set():
        daikate_n_old=""
        daikate_n_old1=""
        daikate_n_old2=""
        
        for syou_kate_n in g_val.syou_kate_:
            cnt=0
            try:
                if(daikate_n_old!=syou_kate_n[0]):
                    g_val.tree_kate.insert("", "end", syou_kate_n[0], text=syou_kate_n[0])
                #tree.change_state(todouhulen_, "checked")
                daikate_n_old=syou_kate_n[0]

                if(daikate_n_old1!=syou_kate_n[1]):
                    g_val.tree_kate.insert(syou_kate_n[0], "end", syou_kate_n[0]+"  "+syou_kate_n[1], text=syou_kate_n[1])
                #tree.change_state(todouhulen_, "checked")
                daikate_n_old1=syou_kate_n[1]

                g_val.tree_kate.insert(syou_kate_n[0]+"  "+syou_kate_n[1], "end", syou_kate_n[0]+"  "+syou_kate_n[1]+"  "+syou_kate_n[2], text=syou_kate_n[2])
            
            except:
                #traceback.print_exc()
                temo=0


                
    #g_val.tree_kate.pack()
    # ツリービューの配置
    #tree.place(x=10, y=500)

    g_val.tree_kate.grid(row=0, column=2,padx=0,pady=75)

    ysb1 = ttk.Scrollbar(cf_kategory, orient=tkinter.VERTICAL, command=g_val.tree_kate.yview)
    g_val.tree_kate.configure(yscrollcommand=ysb1.set)
    ysb1.grid(row=0, column=3, pady=80,sticky='news')

    #####################################################################################################
    ###################################拒否ドメイン#######################################################

    canvas_bdomomein = tkinter.Canvas(cf_domain, width = 200, height = 300)
    canvas_bdomomein["scrollregion"]=(0, 0, 300, 300)
    canvas_bdomomein.pack()
    canvas_bdomomein.grid(row=0, column=0,pady=50)
    #canvas_kate.pack()

    ysb_bdomain = ttk.Scrollbar(cf_domain, orient=tkinter.VERTICAL, command=canvas_bdomomein.yview)
    #ysb_kate.pack()
    canvas_bdomomein.configure(yscrollcommand = ysb_bdomain.set)

    ysb_bdomain.grid(row=0, column=1, pady = 50 , sticky=tkinter.N + tkinter.S)
    #canvas_kate.pack()
    text_bdomain_f=ttk.Label(cf_domain,anchor=tkinter.E,justify="left")
    text_bdomain_f.place(x=10, y=10)
    text_bdomain_f["text"]="拒否ドメインをご指定下さい。(最大1000個)\n例）izanami.link"

    #Frameを作成text_bdomain_f
    frame_domain = ttk.Frame(canvas_bdomomein)#,bg='white') #背景を白に
    #frameをcanvasに配置

    canvas_bdomomein.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=200,height=300)#canvas_kate.cget('width')) 

    def button_bdomain():
        global canvas_bdomomein
        global ysb_bdomain
        #print("AAAAA")
        g_val.list_bdomain_bln.append("")
        i = len(g_val.list_bdomain_bln)-1
        if(i<=1000):
            g_val.list_bdomain_bln[i] = tkinter.Entry(frame_domain,width=28)
            g_val.list_bdomain_bln[i].place(x=10, y=(10+i*20))
            if(50+i*20)>=300:
                canvas_bdomomein["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                #frame_domain["height"]=(50+i*20)
                canvas_bdomomein.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
    def button_bdomain_csv():

        #①dialog 開く
        #➁csv読み込み
        #③listごとに追加

        typ = [('csvファイル','*.csv')]
        if("Windows"==g_val.OS_VERSION):
            ini_dir = g_val.path1+"\\..\\conf\\"
        else:
            ini_dir = g_val.path1+"/../conf/"

        fle = filedialog.askopenfilename(filetypes = typ, initialdir = ini_dir) 

        print(fle)
        list_n=[]
        with open(fle,newline='', encoding='utf_8_sig') as f:

            reader = csv.reader(f)

            #csvファイルのデータをループ
            for row in reader:

                #A列を配列へ格納
                list_n.append(str(row[0]))
        
        cal_ok=1
        
        for list_nnn in list_n:
            if(cal_ok==1):
                cal_ok_li=0
                for i0 in range(0,len(g_val.list_bdomain_bln)):
                    print(g_val.list_bdomain_bln[i0].get(),"0",list_nnn)
                    if(g_val.list_bdomain_bln[i0].get()==""):
                        print(i0,"wite")
                        g_val.list_bdomain_bln[i0].insert(tkinter.END,list_nnn)
                        cal_ok_li=1
                        break
                if(cal_ok_li==0):
                    cal_ok=0
                print("====")
            #break
            print(cal_ok,len(g_val.list_bdomain_bln))
            if(cal_ok==0):
                #追加して代入。
                g_val.list_bdomain_bln.append("")
                i = len(g_val.list_bdomain_bln)-1
                if(i<=1000):#1000
                    g_val.list_bdomain_bln[i] = tkinter.Entry(frame_domain,width=28)
                    g_val.list_bdomain_bln[i].place(x=10, y=(10+i*20))
                    #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
                    #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))
                    g_val.list_bdomain_bln[i].insert(tkinter.END,list_nnn)
                    
                    if(50+i*20)>=300:
                        canvas_bdomomein["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_bdomomein.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
        
        return

    button_domain = ttk.Button(cf_domain,
                    text = '追加',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bdomain,
                    #bg="#DDFFFF"
                    )
    button_domain.place(x=10, y=360,width=80,height=30)

    button_domain_csv = ttk.Button(cf_domain,
                    text = 'csv',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bdomain_csv,
                    #bg="#DDFFFF"
                    )
    button_domain_csv.place(x=155, y=360,width=50,height=30)

    def button_domain_clr():
        n0=0
        for bln in g_val.list_bdomain_bln:
            if(n0<=20):
                bln.delete(0, tkinter.END)
            else:
                bln.place_forget()
            n0+=1

        #g_val.list_bmail_bln=[]
        return
    button_dmomain_clr = ttk.Button(cf_domain,
                    text = 'clear',
                    # クリック時にval()関数を呼ぶpy
                    command=button_domain_clr,
                    #bg="#DDFFFF"
                    )
    button_dmomain_clr.place(x=100, y=360,width=50,height=30)

    g_val.list_bdomain_bln = []
    for i in range(0,20):
        g_val.list_bdomain_bln.append("")

        g_val.list_bdomain_bln[i] = tkinter.Entry(frame_domain,width=28)
        g_val.list_bdomain_bln[i].place(x=10, y=(10+i*20))
        #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
        #g_val.list_bdomain_bln[i].insert(tkinter.END,"拒否ドメイン TEST TEST "+str(i))

        if(50+i*20)>=300:
            canvas_bdomomein["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
            #frame_domain["height"]=(50+i*20)
            canvas_bdomomein.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 

    #####################################################################################################
    ##############################拒否ワード##################################################
    #cf_dword
    
    canvas_bword = tkinter.Canvas(cf_dword, width = 400, height = 300)
    canvas_bword["scrollregion"]=(0, 0, 300, 300)
    canvas_bword.pack()
    canvas_bword.grid(row=0, column=0,pady=50)
    #canvas_kate.pack()

    ysb_bword = ttk.Scrollbar(cf_dword, orient=tkinter.VERTICAL, command=canvas_bword.yview)
    #ysb_kate.pack()
    canvas_bword.configure(yscrollcommand = ysb_bword.set)

    ysb_bword.grid(row=0, column=1, pady = 50 , sticky=tkinter.N + tkinter.S)
    #canvas_kate.pack()
    text_bword_f=ttk.Label(cf_dword,anchor=tkinter.E,justify="left")
    text_bword_f.place(x=10, y=3)
    text_bword_f["text"]="拒否文字列をご指定下さい。(最大1000個)\n例）お断り\n*メールアドレス前後に以下の文字列があった場合収集しません。"

    #Frameを作成text_bword_f
    frame_dword = ttk.Frame(canvas_bword)#,bg='white') #背景を白に
    #frameをcanvasに配置

    canvas_bword.create_window((0,0),window=frame_dword,anchor=tkinter.NW,width=400,height=300)#canvas_kate.cget('width')) 

    def button_bword():
        global canvas_bword
        global ysb_bword
        #print("AAAAA")
        g_val.list_bword_bln.append("")
        i = len(g_val.list_bword_bln)-1
        if(i<=1000):
            g_val.list_bword_bln[i] = tkinter.Entry(frame_dword,width=70)
            g_val.list_bword_bln[i].place(x=10, y=(10+i*20))
            if(50+i*20)>=300:
                canvas_bword["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                
                canvas_bword.create_window((0,0),window=frame_dword,anchor=tkinter.NW,width=400,height=(50+i*20))#canvas_kate.cget('width')) 
    
    def button_bword_csv():

        #①dialog 開く
        #➁csv読み込み
        #③listごとに追加

        typ = [('csvファイル','*.csv')]
        if("Windows"==g_val.OS_VERSION):
            ini_dir = g_val.path1+"\\..\\conf\\"
        else:
            ini_dir = g_val.path1+"/../conf/"

        fle = filedialog.askopenfilename(filetypes = typ, initialdir = ini_dir) 

        print(fle)
        list_n=[]
        with open(fle,newline='', encoding='utf_8_sig') as f:

            reader = csv.reader(f)

            #csvファイルのデータをループ
            for row in reader:

                #A列を配列へ格納
                list_n.append(str(row[0]))
        
        cal_ok=1
        
        for list_nnn in list_n:
            if(cal_ok==1):
                cal_ok_li=0
                for i0 in range(0,len(g_val.list_bword_bln)):
                    print(g_val.list_bword_bln[i0].get(),"0",list_nnn)
                    if(g_val.list_bword_bln[i0].get()==""):
                        print(i0,"wite")
                        g_val.list_bword_bln[i0].insert(tkinter.END,list_nnn)
                        cal_ok_li=1
                        break
                if(cal_ok_li==0):
                    cal_ok=0
                print("====")
            #break
            print(cal_ok,len(g_val.list_bword_bln))
            if(cal_ok==0):
                #追加して代入。
                g_val.list_bword_bln.append("")
                i = len(g_val.list_bword_bln)-1
                if(i<=1000):#1000
                    g_val.list_bword_bln[i] = tkinter.Entry(frame_dword,width=70)
                    g_val.list_bword_bln[i].place(x=10, y=(10+i*20))
                    #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
                    #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))
                    g_val.list_bword_bln[i].insert(tkinter.END,list_nnn)
                    
                    if(50+i*20)>=300:
                        canvas_bword["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_bword.create_window((0,0),window=frame_dword,anchor=tkinter.NW,width=400,height=(50+i*20))#canvas_kate.cget('width')) 
        
        return

    button_dword = ttk.Button(cf_dword,
                    text = '追加',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bword,
                    #bg="#DDFFFF"
                    )
    button_dword.place(x=10, y=360,width=80,height=30)

    button_dword_csv = ttk.Button(cf_dword,
                    text = 'csv',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bword_csv,
                    #bg="#DDFFFF"
                    )
    button_dword_csv.place(x=155, y=360,width=50,height=30)

    def button_dword_clr():
        n0=0
        for bln in g_val.list_bword_bln:
            if(n0<=20):
                bln.delete(0, tkinter.END)
            else:
                bln.place_forget()
            n0+=1

        #g_val.list_bmail_bln=[]
        return
    button_dword_clr = ttk.Button(cf_dword,
                    text = 'clear',
                    # クリック時にval()関数を呼ぶpy
                    command=button_dword_clr,
                    #bg="#DDFFFF"
                    )
    button_dword_clr.place(x=100, y=360,width=50,height=30)

    g_val.list_bword_bln = []
    for i in range(0,20):
        g_val.list_bword_bln.append("")

        g_val.list_bword_bln[i] = tkinter.Entry(frame_dword,width=70)#28
        g_val.list_bword_bln[i].place(x=10, y=(10+i*20))
        #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
        #g_val.list_bword_bln[i].insert(tkinter.END,"拒否ドメイン TEST TEST "+str(i))

        if(50+i*20)>=300:
            canvas_bword["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
            #frame_domain["height"]=(50+i*20)
            canvas_bword.create_window((0,0),window=frame_dword,anchor=tkinter.NW,width=400,height=(50+i*20))#canvas_kate.cget('width')) 


    text_ng_dword_f=ttk.Label(cf_dword,anchor=tkinter.E,justify="left")
    text_ng_dword_f.place(x=310, y=15)
    text_ng_dword_f["text"]="前後検索数:"
    
    if("Windows"==g_val.OS_VERSION):
        g_val.ng_dword_rntry = tkinter.Entry(cf_dword,width=5)
    else:
        g_val.ng_dword_rntry = tkinter.Entry(cf_dword,width=4)

    g_val.ng_dword_rntry.place(x=380, y=15)

    ###################################bmail######################################################

    canvas_bmail = tkinter.Canvas(cf_bl_list, width = 200, height = 300)
    canvas_bmail["scrollregion"]=(0, 0, 300, 300)
    canvas_bmail.pack()
    canvas_bmail.grid(row=0, column=0,pady=60)
    #canvas_kate.pack()

    ysb_bmail = ttk.Scrollbar(cf_bl_list, orient=tkinter.VERTICAL, command=canvas_bmail.yview)
    #ysb_kate.pack()
    canvas_bmail.configure(yscrollcommand = ysb_bmail.set)

    ysb_bmail.grid(row=0, column=1, pady = 60 , sticky=tkinter.N + tkinter.S)
    #canvas_kate.pack()
    text_bmail0_f=ttk.Label(cf_bl_list,anchor=tkinter.E,justify="left")
    text_bmail0_f.place(x=10, y=10)
    text_bmail0_f["text"]="収集したくない情報を入力してください。"

    text_bmail_f=ttk.Label(cf_bl_list,anchor=tkinter.E,justify="left")
    text_bmail_f.place(x=10, y=35)
    text_bmail_f["text"]="メールアドレス(最大1000個)\n*以下の文字列が含まれる場合収集しません。"

    #Frameを作成text_bdomain_f
    frame_dmail = ttk.Frame(canvas_bmail)#,bg='white') #背景を白に
    #frameをcanvasに配置

    canvas_bmail.create_window((0,0),window=frame_dmail,anchor=tkinter.NW,width=200,height=300)#canvas_kate.cget('width')) 

    def button_bmail():
        global canvas_bmail
        global ysb_bmail
        g_val.list_bmail_bln.append("")
        i = len(g_val.list_bmail_bln)-1
        
        if(i<=1000):
            g_val.list_bmail_bln[i] = tkinter.Entry(frame_dmail,width=28)
            g_val.list_bmail_bln[i].place(x=10, y=(10+i*20))
            #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
            #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))

            
            if(50+i*20)>=300:
                canvas_bmail["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                canvas_bmail.create_window((0,0),window=frame_dmail,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
    
    def button_bmail_csv() :
        #①dialog 開く
        #➁csv読み込み
        #③listごとに追加

        typ = [('csvファイル','*.csv')]
        if("Windows"==g_val.OS_VERSION):
            ini_dir = g_val.path1+"\\..\\conf\\"
        else:
            ini_dir = g_val.path1+"/../conf/"

        fle = filedialog.askopenfilename(filetypes = typ, initialdir = ini_dir) 

        print(fle)
        list_n=[]
        with open(fle,newline='', encoding='utf_8_sig') as f:

            reader = csv.reader(f)

            #csvファイルのデータをループ
            for row in reader:

                #A列を配列へ格納
                list_n.append(str(row[0]))
        
        cal_ok=1
        
        for list_nnn in list_n:
            if(cal_ok==1):
                cal_ok_li=0
                for i0 in range(0,len(g_val.list_bmail_bln)):
                    print(g_val.list_bmail_bln[i0].get(),"0",list_nnn)
                    if(g_val.list_bmail_bln[i0].get()==""):
                        print(i0,"wite")
                        g_val.list_bmail_bln[i0].insert(tkinter.END,list_nnn)
                        cal_ok_li=1
                        break
                if(cal_ok_li==0):
                    cal_ok=0
                print("====")
            #break
            print(cal_ok,len(g_val.list_bmail_bln))
            if(cal_ok==0):
                #追加して代入。
                g_val.list_bmail_bln.append("")
                i = len(g_val.list_bmail_bln)-1
                if(i<=1000):#1000
                    g_val.list_bmail_bln[i] = tkinter.Entry(frame_dmail,width=28)
                    g_val.list_bmail_bln[i].place(x=10, y=(10+i*20))
                    #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
                    #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))
                    g_val.list_bmail_bln[i].insert(tkinter.END,list_nnn)
                    
                    if(50+i*20)>=300:
                        canvas_bmail["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_bmail.create_window((0,0),window=frame_dmail,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
            
        return
    

    button_bl = ttk.Button(cf_bl_list,
                    text = '追加',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bmail,
                    #bg="#DDFFFF"
                    )
    button_bl.place(x=10, y=365,width=80,height=30)

    button_bl_csv = ttk.Button(cf_bl_list,
                    text = 'csv',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bmail_csv,
                    #bg="#DDFFFF"
                    )
    button_bl_csv.place(x=155, y=365,width=50,height=30)

    def button_bmail_clr():
        n0=0
        for bln in g_val.list_bmail_bln:
            if(n0<=20):
                bln.delete(0, tkinter.END)
            else:
                bln.place_forget()
            n0+=1

        #g_val.list_bmail_bln=[]
        return
    button_bl_clr = ttk.Button(cf_bl_list,
                    text = 'clear',
                    # クリック時にval()関数を呼ぶpy
                    command=button_bmail_clr,
                    #bg="#DDFFFF"
                    )
    button_bl_clr.place(x=100, y=365,width=50,height=30)

    g_val.list_bmail_bln = []
    for i in range(0,20):
        g_val.list_bmail_bln.append("")

        g_val.list_bmail_bln[i] = tkinter.Entry(frame_dmail,width=28)
        g_val.list_bmail_bln[i].place(x=10, y=(10+i*20))
        #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
        #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))

        if(50+i*20)>=300:
            canvas_bmail["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
            canvas_bmail.create_window((0,0),window=frame_dmail,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 

    #####################################################################################################
    ###################################btel######################################################

    canvas_btel = tkinter.Canvas(cf_bl_list, width = 200, height = 300)
    canvas_btel["scrollregion"]=(0, 0, 300, 300)
    #canvas_btel.pack()
    canvas_btel.grid(row=0, column=2,pady=60)
    #canvas_kate.pack()

    ysb_btel = tkinter.Scrollbar(cf_bl_list, orient=tkinter.VERTICAL, width=16, command=canvas_btel.yview)
    #ysb_kate.pack()
    canvas_btel.configure(yscrollcommand = ysb_btel.set)

    ysb_btel.grid(row=0, column=3, pady = 60 , sticky=tkinter.N + tkinter.S)

    text_btel_f=ttk.Label(cf_bl_list,anchor=tkinter.E,justify="left")
    text_btel_f.place(x=225, y=35)
    text_btel_f["text"]="電話番号(ハイフンなし) (最大1000個)"

    #Frameを作成text_bdomain_f
    frame_btel = ttk.Frame(canvas_btel)#,bg='white') #背景を白に
    #frameをcanvasに配置

    canvas_btel.create_window((0,0),window=frame_btel,anchor=tkinter.NW,width=200,height=300)#canvas_kate.cget('width')) 

    def button_btell():
        global canvas_btel
        global ysb_btel
        g_val.list_btell_bln.append("")
        i = len(g_val.list_btell_bln)-1
        if(i<=1000):
            g_val.list_btell_bln[i] = tkinter.Entry(frame_btel,width=28)
            g_val.list_btell_bln[i].place(x=10, y=(10+i*20))
            #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
            #g_val.list_btell_bln[i].insert(tkinter.END,"拒否TEL TEST TEST "+str(i))

            
            if(50+i*20)>=300:
                canvas_btel["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                canvas_btel.create_window((0,0),window=frame_btel,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 

    def button_btell_csv():
        typ = [('csvファイル','*.csv')]
        if("Windows"==g_val.OS_VERSION):
            ini_dir = g_val.path1+"\\..\\conf\\"
        else:
            ini_dir = g_val.path1+"/../conf/"

        fle = filedialog.askopenfilename(filetypes = typ, initialdir = ini_dir) 

        print(fle)
        list_n=[]
        with open(fle,newline='', encoding='utf_8_sig') as f:

            reader = csv.reader(f)

            #csvファイルのデータをループ
            for row in reader:

                #A列を配列へ格納
                list_n.append(str(row[0]))
        
        cal_ok=1
        
        for list_nnn in list_n:
            if(cal_ok==1):
                cal_ok_li=0
                for i0 in range(0,len(g_val.list_btell_bln)):
                    print(g_val.list_btell_bln[i0].get(),"0",list_nnn)
                    if(g_val.list_btell_bln[i0].get()==""):
                        print(i0,"wite")
                        g_val.list_btell_bln[i0].insert(tkinter.END,list_nnn)
                        cal_ok_li=1
                        break
                if(cal_ok_li==0):
                    cal_ok=0
                print("====")
            #break
            print(cal_ok,len(g_val.list_btell_bln))
            if(cal_ok==0):
                #追加して代入。
                g_val.list_btell_bln.append("")
                i = len(g_val.list_btell_bln)-1
                if(i<=1000):#1000
                    g_val.list_btell_bln[i] = tkinter.Entry(frame_btel,width=28)
                    g_val.list_btell_bln[i].place(x=10, y=(10+i*20))
                    #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
                    #g_val.list_bmail_bln[i].insert(tkinter.END,"拒否メール TEST TEST "+str(i))
                    g_val.list_btell_bln[i].insert(tkinter.END,list_nnn)
                    
                    if(50+i*20)>=300:
                        canvas_btel["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_btel.create_window((0,0),window=frame_btel,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
            
    button_bl0 = ttk.Button(cf_bl_list,
                    text = '追加',
                    # クリック時にval()関数を呼ぶpy
                    command=button_btell,
                    #bg="#DDFFFF"
                    )
    button_bl0.place(x=230, y=365,width=80,height=30)


    button_bl0_csv = ttk.Button(cf_bl_list,
                    text = 'csv',
                    # クリック時にval()関数を呼ぶpy
                    command=button_btell_csv,
                    #bg="#DDFFFF"
                    )
    button_bl0_csv.place(x=375, y=365,width=50,height=30)
    
    def button_btell_clr():
        n0=0
        for bln in g_val.list_btell_bln:
            if(n0<=20):
                bln.delete(0, tkinter.END)
            else:
                bln.place_forget()
            n0+=1

        #g_val.list_bmail_bln=[]
        return
    button_bl0_clr = ttk.Button(cf_bl_list,
                    text = 'clear',
                    # クリック時にval()関数を呼ぶpy
                    command=button_btell_clr,
                    #bg="#DDFFFF"
                    )
    button_bl0_clr.place(x=320, y=365,width=50,height=30)

    g_val.list_btell_bln = []
    for i in range(0,20):
        g_val.list_btell_bln.append("")

        g_val.list_btell_bln[i] = tkinter.Entry(frame_btel,width=28)
        g_val.list_btell_bln[i].place(x=10, y=(10+i*20))
        #g_val.cate_box_all[i][3]["text"]="CATEGORY TEST TEST "+str(i)
        #g_val.list_btell_bln[i].insert(tkinter.END,"拒否TEL TEST TEST "+str(i))

        if(50+i*20)>=300:
            canvas_btel["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
            canvas_btel.create_window((0,0),window=frame_btel,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 

    #####################################################################################################
    ##############################################ゆらぎ#################################################
    text_yuragi_f=ttk.Label(op_yuragi,anchor=tkinter.E,justify="left")
    text_yuragi_f.place(x=10, y=10)
    #yragi_txt = "機能が自動収集をするとGoogleからブロックされるリスクがあるため、より人間に近い収集\nを行うゆらぎを設定します。よくわからない場合はONのままにしてください。"
    #yragi_txt += "\n\nゆらぎを設定している場合でも定期的にシステムを停止し、休憩を挟むようにしてください。\n＊ゆらぎ機能をOFFにすると検索スピードは早くなります。早くなる分検索先からブロック\nされる可能性があります。その際の責任は負い兼ねます。"


    yragi_txt ="自動収集を行うとGoogleから一時的にブロックされることがあります。\n"
    yragi_txt +="その可能性を減らすためにIZANAMIではより人間の動きに近い動作（ゆらぎ）を行います。\n\n"

    yragi_txt +="ゆらぎ機能をOFFにすると検索スピードは少し速くなります。\n"
    yragi_txt +="早くなる分検索先からブロックされる可能性が上がります。\n\n"

    yragi_txt +="ゆらぎのON/OFFに関わらず定期的にシステムを停止し、休憩を挟むようにしてください。\n"
    yragi_txt +="ブロックされた場合の責任は負いかねます。"

    text_yuragi_f["text"]=yragi_txt
    def yuragi_btn():
        print("A",g_val.bl_yuragi.get())
        return
        g_val.bl_yuragi.set=0
        
    def yuragi_btn1():
        print("B",g_val.bl_yuragi.get())
        return
        g_val.bl_yuragi.set=1

        
    g_val.bl_yuragi = tkinter.IntVar()
    btn_yuragi = ttk.Radiobutton(op_yuragi,value=0, text='ON',variable=g_val.bl_yuragi, command=yuragi_btn)

    btn_yuragi.place(x=10, y=150)

    btn_yuragi1 = ttk.Radiobutton(op_yuragi,value=1, text='OFF', command=yuragi_btn1,variable=g_val.bl_yuragi)
    btn_yuragi1.place(x=100, y=150)
    #g_val.bl_yuragi.set(1)
    #############################################################################################################
    #プロキシ設定
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    if("Windows"==g_val.OS_VERSION):
        from subprocess import CREATE_NO_WINDOW
    def proxy_check_f():

        g_val.text_proxy_ck_f=1

        proxy_="--proxy-server="+g_val.proxy_txt_rntry.get()
        print("Proxy checked",proxy_)
        sleep(1)
        option_t = Options()  
        option_t.add_argument('--headless')
        option_t.add_argument(proxy_)
        option_t.add_argument('log-level=3') 
        option_t.add_argument('--disable-gpu')
        option_t.add_argument('--no-sandbox')
        option_t.add_argument('--disable-dev-shm-usage')

        try:
            g_val.proxy_try_ok=0
            chrome_service = Service(g_val.d_path)
            if("Windows"==g_val.OS_VERSION):
                chrome_service.creationflags = CREATE_NO_WINDOW 

            driver_t = webdriver.Chrome(g_val.d_path,options=option_t,service=chrome_service)#
            # driver_t = webdriver.Chrome(options=option_t, service=chrome_service)

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
        g_val.text_proxy_ck_f=0
        sleep(1)
        if(g_val.proxy_try_ok==1):
            print("proxy OK")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.text_proxy_ck["text"]="有効です。"
                g_val.text_st_f1["text"]="プロキシ設定：有効"

            else:
                g_val.text_proxy_ck["text"]="Valid"
                g_val.text_st_f1["text"]="Proxy setting : Valid"

        else:
            g_val.proxy_try_ok=0
            print("proxy OK")
            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                g_val.text_proxy_ck["text"]="無効です。\n別のプロキシを設定してください。"
                g_val.text_st_f1["text"]="プロキシ設定：無効"
            else:
                g_val.text_proxy_ck["text"]="Invalid　\nSet another Proxy"
                g_val.text_st_f1["text"]="Proxy setting : Invalid"
        return

            
    def proxy_check():
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.text_proxy_ck["text"]="チェック中。。。"
        else:
            g_val.text_proxy_ck["text"]="Proxy Checking"
        thread_proxy = threading.Thread(target=proxy_check_f)
        thread_proxy.start()


        

        
    text_proxy_f=ttk.Label(op_proxy,anchor=tkinter.E,justify="left")
    text_proxy_f.place(x=10, y=10)
    text_proxy_f["text"]="プロキシサーバを設定します。\n収集に影響しますのでよくわからない場合は設定しないでください。"
    if("Windows"==g_val.OS_VERSION):
        g_val.proxy_txt_rntry = tkinter.Entry(op_proxy,width=40)
    else:
        g_val.proxy_txt_rntry = tkinter.Entry(op_proxy,width=30)
    g_val.proxy_txt_rntry.place(x=10, y=70)

    text_proxy_f2=ttk.Label(op_proxy,anchor=tkinter.E,justify="left")
    text_proxy_f2.place(x=10, y=100)
    text_proxy_f2["text"]="記入例)127.0.0.1:9150"
    # ボタンの作成と配置
    button_p = ttk.Button(op_proxy,
                    text = 'チェック',
                    # クリック時にval()関数を呼ぶpy
                    #height = 50,
                    #width = 15,
                    
                    command=proxy_check
                    )
    if("Windows"==g_val.OS_VERSION):
        button_p.place(x=265, y=66.0,width=60,height=25)
    else:
        button_p.place(x=300, y=70.0,width=80,height=25)
    g_val.text_proxy_ck=ttk.Label(op_proxy,anchor=tkinter.E,justify="left")
    g_val.text_proxy_ck.place(x=270, y=95)
    #text_proxy_f2["text"]="無効です。\n別のプロキシを設定してください。"


    #############################################################################################################
    #############################################################################################################
    #ログ
    text_log_f=ttk.Label(op_logdl,anchor=tkinter.E,justify="left")
    text_log_f.place(x=10, y=10)

    if("Windows"==g_val.OS_VERSION):
        text_log_f["text"]="サポートに不具合の連絡をされる場合、こちらのログファイルをダウンロードしてお送りくいただく\nと問題解決が早くなる場合がございます"

    else:
        text_log_f["text"]="サポートに不具合の連絡をされる場合、こちらのログファイルをダウンロードしてお送り\nくいただくと問題解決が早くなる場合がございます"

    
    def log_buton():
        #log_file_name = g_val.path1+"\\..\\conf\\progress.txt"

        now = datetime.datetime.now()
        get_year=str(now.year)
        get_month = str(now.month)
        get_day   = str(now.day)

        if("Windows"==g_val.OS_VERSION):
            back_name = g_val.path1+"\\..\\out\\"+get_year+get_month+get_day+"_log_out.txt"
        else:
            back_name = g_val.path1+"/../out/"+get_year+get_month+get_day+"_log_out.txt"
        shutil.copy(g_val.log_tem_f, back_name)

        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            messagebox.showinfo('確認', 'ログ出力が完了しました。\noutフォルダを参照してください。\nfaile:'+back_name)
        else:
            messagebox.showinfo('Confirmination', 'Complete out the Log file.\noutRefer to folder \nfaile:'+back_name)
    button_log_ex = ttk.Button(op_logdl,
                    text = 'ダウンロード',
                    # クリック時にval()関数を呼ぶpy
                    command=log_buton,
                    #bg="#DDFFFF"
                    )
    button_log_ex.place(x=10, y=60,width=100,height=30)


    button_log_ex1 = ttk.Button(init_f,
                    text = '実行ログ',
                    # クリック時にval()関数を呼ぶpy
                    command=log_buton,
                    #bg="#DDFFFF"
                    )
    if("Windows"==g_val.OS_VERSION):
        button_log_ex1.place(x=300, y=250,width=70,height=30)
    else:
        button_log_ex1.place(x=400, y=225,width=70,height=30)

    #############################################################################################################
    def conf_log_init():
        if("Windows"==g_val.OS_VERSION):
            log_file_name = g_val.path1+"\\..\\conf\\"+g_val.language_get_value.split("(")[0]+"_progress.txt"
            back_name = g_val.path1+"\\..\\conf\\"+g_val.language_get_value.split("(")[0]+"_progress_bak.txt"
        else:
            log_file_name = g_val.path1+"/../conf/"+g_val.language_get_value.split("(")[0]+"_progress.txt"
            back_name = g_val.path1+"/../conf/"+g_val.language_get_value.split("(")[0]+"_progress_bak.txt"

        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            temp_log = [[["プロキシ","TEST_PROXY"]],#0
                        [["ゆらぎ","0"]],#1
                        [["オプションパスワード",""]],#2
                        [["カテゴリチェック",""]],#3
                        [["エリアチェック","",""]],#4
                        [["ドメインリスト","",]],#5
                        [["メールリスト","",]],#6
                        [["電話リスト","",]],#7
                        [["カテゴリツリー","","",""]],#8
                        [["カテゴリログ","-",]],#9
                        [["都道府県ログ","-",]],#10
                        [["市区町村ログ","-",]],#11
                        [["FAX(ベータ機能)",True,]],#12
                        [["平均評価","True",]],#13
                        [["口コミ","True",]],#14
                        [["営業時間(月)","True",]],#15
                        [["営業時間(火)","True",]],#16
                        [["営業時間(水)","True",]],#17
                        [["営業時間(木)","True",]],#18
                        [["営業時間(金)","True",]],#19
                        [["営業時間(土)","True",]],#20
                        [["営業時間(日)","True",]],#21
                        [["DWORD","",]],#22
                        [["DWORD_NUM","100",]],#23
                        [["jyoutyu_check","False",]],#jyoutyu_check#24
                        [["jyoutyu_end","0",]],#jyoutyu_end#25
                        [["OP_MODE","",]],#OP mode #26
                        [["CL_MODE","",]],#collect_user mode #27
                        [["DBG_MODE","",]],#dbg mode #28
                        [["FLEE_LI_MODE","",]],#freelicence  #29
                        [["LAN_MODE","",]],#lan  #30
                        [["URL_ROG","",]],#lan  #31
                        [["URL_COUNT","",]],#lan  #32
                        [["SEARCH_ARIA","False",]],#lan  #33#search 都道府県
                        [["SEARCH_MODE",g_val.mode_list[1],]],#lan  #34#search mode
                        ]
        else:
            temp_log = [[["Proxy","TEST_PROXY"]],#0
                        [["Swing","0"]],#1
                        [["Password",""]],#2
                        [["Category",""]],#3
                        [["Country","",""]],#4
                        [["Domain","",]],#5
                        [["Mail","",]],#6
                        [["Tell","",]],#7
                        [["Category tree","","",""]],#8
                        [["Category Log","-",]],#9
                        [["Country Log","-",]],#10
                        [["City Log","-",]],#11
                        [["FAX",True,]],#12
                        [["Average reviews","True",]],#13
                        [["All reviews","True",]],#14
                        [["Monday","True",]],#15
                        [["Tuesday","True",]],#16
                        [["Wednesday","True",]],#17
                        [["Thuersday","True",]],#18
                        [["Friday","True",]],#19
                        [["Satuerday","True",]],#20
                        [["Sunday","True",]],#21
                        [["DWORD",""]],#22
                        [["DWORD_NUM","100"]],#23
                        [["jyoutyu_check","False",]],#jyoutyu_check#24
                        [["jyoutyu_end","0",]],#jyoutyu_end#25
                        [["OP_MODE","",]],#OP mode #26
                        [["CL_MODE","",]],#collect_user mode #27
                        [["DBG_MODE","",]],#dbg mode #28
                        [["FLEE_LI_MODE","",]],#freelicence  #29
                        [["LAN_MODE","",]],#lan  #30
                        [["URL_ROG","",]],#lan  #31
                        [["URL_COUNT","",]],#lan  #32
                        [["SEARCH_ARIA","False",]],#lan  #33#search 都道府県
                        [["SEARCH_MODE",g_val.mode_list[1],]],#lan  #34#search mode
                        ]

        #エリアチェック　デフォルト
        temp_log[4]=g_val.default_eria
        temp_log[6]=g_val.default_bmail#デフォルトメール
        temp_log[22]=g_val.default_word
        

        #ログ書き込み
        if not os.path.isfile(log_file_name):
            with open(log_file_name, mode='w',encoding="utf_8_sig") as f:#,newline='\n'
                for temp_log_n in temp_log:
                    for temp_log_n0 in temp_log_n:
                        f.write(str(temp_log_n0) +"\n")

        shutil.copy(log_file_name, back_name)

        #初期値反映
        log_in_list = g_val.conf_log_txt()
        ini_n = 0
        for temp_log_n in temp_log:
            try:
                if(log_in_list[ini_n]):
                    temp=0
            except:
                log_in_list.append(temp_log_n)

            ini_n+=1

        log_kate=log_in_list[9][0][1]+"  "+log_in_list[10][0][1]+"  "+log_in_list[11][0][1]
        print(log_kate)
        g_val.get_imform["text"] = log_kate

        g_val.proxy_txt_rntry.insert(0,log_in_list[0][0][1])#プロキシ
        #print("ゆらぎ",log_in_list[1][0][1])
        if(log_in_list[1][0][1] !="-" and log_in_list[1][0][1] !=""):
            g_val.bl_yuragi.set (int(log_in_list[1][0][1]))#ゆらぎ

        #print(g_val.bl_yuragi.get())

        #op_ex_txt_rntry.insert(0,log_in_list[2][0][1])#パスワード→なし
        #print(log_in_list[3])
        for i in range(0,len(log_in_list[3])):#カテゴリ
            try:
                #if(i<=len(g_val.cate_box_all)):
                    #行追加
                g_val.cate_box_all[i][0].insert(tkinter.END, log_in_list[3][i][1])  

            except:
                traceback.print_exc()
                temp=0
        #エリアチェック
        for eria_n in log_in_list[4]:
            todouhuken_=eria_n[1]
            sikutyouson_= eria_n[2]
            #print(todouhuken_,sikutyouson_)
            if(todouhuken_ !="-" and todouhuken_ !=""):
                try:
                    g_val.tree.change_state(todouhuken_, "tristate")
                    g_val.tree.change_state(todouhuken_+"  "+sikutyouson_, "checked")
                except:
                    traceback.print_exc()
                    temp=0
        #カテツリー
        for eria_n in log_in_list[8]:
            dai_=eria_n[1]
            tyu_= eria_n[2]
            syou_= eria_n[3]
            #print(todouhuken_,sikutyouson_)
            if(dai_ !="-" and tyu_ !="" and syou_ !=""):
                try:
                    g_val.tree_kate.change_state(dai_, "tristate")
                    g_val.tree_kate.change_state(dai_+"  "+tyu_, "tristate")
                    g_val.tree_kate.change_state(dai_+"  "+tyu_+"  "+syou_, "checked")

                except:
                    #traceback.print_exc()
                    temp=0
        #ドメインリスト
        for i in range(0,len(log_in_list[5])):#カテゴリ
            try:
                if(i>1000):break
                if(i>=len(g_val.list_bdomain_bln)):
                    g_val.list_bdomain_bln.append("")

                    g_val.list_bdomain_bln[i] = tkinter.Entry(frame_domain,width=28)
                    g_val.list_bdomain_bln[i].place(x=10, y=(10+i*20))

                    if(50+i*20)>=300:
                        canvas_bdomomein["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        #frame_domain["height"]=(50+i*20)
                        canvas_bdomomein.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
                    
                g_val.list_bdomain_bln[i].insert(0,log_in_list[5][i][1])
            except:
                traceback.print_exc()
                temp=0
        #メールリスト
        print(len(log_in_list[6]))
        for i in range(0,len(log_in_list[6])):#dmail
            if(i>1000):break
            try:
                if(i>=len(g_val.list_bmail_bln)):
                    g_val.list_bmail_bln.append("")

                    g_val.list_bmail_bln[i] = tkinter.Entry(frame_dmail,width=28)
                    g_val.list_bmail_bln[i].place(x=10, y=(10+i*20))
                    #sleep(0.1)
                    if(50+i*20)>=300:
                        canvas_bmail["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_bmail.create_window((0,0),window=frame_dmail,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
                #print(i,log_in_list[6][i][1]) 
                g_val.list_bmail_bln[i].insert(0,log_in_list[6][i][1])
                #sleep(0.1)
            except:
                traceback.print_exc()
                sleep(10)
                temp=0

        #telllist
        for i in range(0,len(log_in_list[7])):#
            if(i>1000):break
            try:
                if(i>=len(g_val.list_btell_bln)):
                    g_val.list_btell_bln.append("")#

                    g_val.list_btell_bln[i] = tkinter.Entry(frame_btel,width=28)
                    g_val.list_btell_bln[i].place(x=10, y=(10+i*20))

                    if(50+i*20)>=300:
                        canvas_btel["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                        canvas_btel.create_window((0,0),window=frame_btel,anchor=tkinter.NW,width=200,height=(50+i*20))#canvas_kate.cget('width')) 
            
                g_val.list_btell_bln[i].insert(0,log_in_list[7][i][1])
            except:
                traceback.print_exc()
                temp=0
        
        if(log_in_list[12][0][1] !="-" and log_in_list[12][0][1] !=""):
            g_val.get_fax_bln.set (log_in_list[12][0][1])#12
        if(log_in_list[13][0][1] !="-" and log_in_list[13][0][1] !=""):
            g_val.get_hyouka_bln.set (log_in_list[13][0][1])#13
        if(log_in_list[14][0][1] !="-" and log_in_list[14][0][1] !=""):
            g_val.get_kutikomi_bln.set (log_in_list[14][0][1])#14
        if(log_in_list[15][0][1] !="-" and log_in_list[15][0][1] !=""):
            g_val.get_mon_bln.set (log_in_list[15][0][1])#15
        if(log_in_list[16][0][1] !="-" and log_in_list[16][0][1] !=""):
            g_val.get_tue_bln.set (log_in_list[16][0][1])#16
        if(log_in_list[17][0][1] !="-" and log_in_list[17][0][1] !=""):
            g_val.get_wed_bln.set (log_in_list[17][0][1])#17
        if(log_in_list[18][0][1] !="-" and log_in_list[18][0][1] !=""):
            g_val.get_thu_bln.set (log_in_list[18][0][1])#18
        if(log_in_list[19][0][1] !="-" and log_in_list[19][0][1] !=""):
            g_val.get_fri_bln.set (log_in_list[19][0][1])#19
        if(log_in_list[20][0][1] !="-" and log_in_list[20][0][1] !=""):
            g_val.get_sat_bln.set (log_in_list[20][0][1])#20
        if(log_in_list[21][0][1] !="-" and log_in_list[21][0][1] !=""):
            g_val.get_sun_bln.set (log_in_list[21][0][1])#21


        #ドメインリスト
        try:
            for i in range(0,len(log_in_list[22])):#カテゴリ
                try:
                    if(i>1000):break
                    if(i>=len(g_val.list_bword_bln)):
                        g_val.list_bword_bln.append("")

                        g_val.list_bword_bln[i] = tkinter.Entry(frame_domain,width=70)
                        g_val.list_bword_bln[i].place(x=10, y=(10+i*20))

                        if(50+i*20)>=300:
                            canvas_bdword["scrollregion"]=(0, 0, 50+i*20, 50+i*20)
                            #frame_domain["height"]=(50+i*20)
                            canvas_bdword.create_window((0,0),window=frame_domain,anchor=tkinter.NW,width=400,height=(50+i*20))#canvas_kate.cget('width')) 
                        
                    g_val.list_bword_bln[i].insert(0,log_in_list[22][i][1])
                except:
                    traceback.print_exc()
                    temp=0
        except:
            traceback.print_exc()
            temp=0
        try:
            g_val.ng_dword_rntry.insert(0,log_in_list[23][0][1])#プロキシ
            #print("ini",log_in_list)
        except:
            traceback.print_exc()
            temp=0
        try:
            g_val.bt_app_jyoutyu_.set(log_in_list[24][0][1])#12
            g_val.f_jyouty_end=(log_in_list[25][0][1])#12
        except:
            traceback.print_exc()
            temp=0

        try:
            g_val.url_log_his= log_in_list[31][0][1]
          
        except:
            traceback.print_exc()
            temp=0

        try:
            g_val.bt_genimu_eria.set(log_in_list[33][0][1])#33
        except:
            traceback.print_exc()
            temp=0



        
    ####################################################################################################
    ####################################################################################################
    
    def tyouhuku_conf_log_init():
        try:
            if("Windows"==g_val.OS_VERSION):
                re_list = g_val.path1+"\\..\\conf\\"#+r'*_progress.txt'
            else:
                re_list = g_val.path1+"/../conf/"#+r'*_progress.txt'
            #paths= os.listdir(re_list)
            paths = list(pathlib.Path(re_list).glob(r'*_progress.txt'))
            #paths.sort(key=os.path.getmtime)
            paths.sort(key=os.path.getmtime, reverse=True)

            try:
                # ソート結果の表示
                for file in paths:
                    print(f'{file.stat().st_mtime:.0f}  {file.name}')
                
                lan_file_name = paths[0].name.split("_progress")[0]
                print(lan_file_name)
                for lan_ist in g_val.Lnagage_list:
                    if( lan_file_name in lan_ist):
                        g_val.language_get_value = lan_ist
                        break
            except:
                pass
            print(g_val.language_get_value)
            #return
        
            if("Windows"==g_val.OS_VERSION):
                log_file_name = g_val.path1+"\\..\\conf\\"+g_val.language_get_value.split("(")[0]+"_progress.txt"
                back_name = g_val.path1+"\\..\\conf\\"+g_val.language_get_value.split("(")[0]+"_progress_bak.txt"
            else:
                log_file_name = g_val.path1+"/../conf/"+g_val.language_get_value.split("(")[0]+"_progress.txt"
                back_name = g_val.path1+"/../conf/"+g_val.language_get_value.split("(")[0]+"_progress_bak.txt"

            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                temp_log = [[["プロキシ","TEST_PROXY"]],#0
                            [["ゆらぎ","0"]],#1
                            [["オプションパスワード",""]],#2
                            [["カテゴリチェック",""]],#3
                            [["エリアチェック","",""]],#4
                            [["ドメインリスト","",]],#5
                            [["メールリスト","",]],#6
                            [["電話リスト","",]],#7
                            [["カテゴリツリー","","",""]],#8
                            [["カテゴリログ","-",]],#9
                            [["都道府県ログ","-",]],#10
                            [["市区町村ログ","-",]],#11
                            [["FAX(ベータ機能)",True,]],#12
                            [["平均評価","True",]],#13
                            [["口コミ","True",]],#14
                            [["営業時間(月)","True",]],#15
                            [["営業時間(火)","True",]],#16
                            [["営業時間(水)","True",]],#17
                            [["営業時間(木)","True",]],#18
                            [["営業時間(金)","True",]],#19
                            [["営業時間(土)","True",]],#20
                            [["営業時間(日)","True",]],#21
                            [["DWORD","",]],#22
                            [["DWORD_NUM","100",]],#23
                            [["jyoutyu_check","False",]],#jyoutyu_check#24
                            [["jyoutyu_end","0",]],#jyoutyu_end#25
                            [["OP_MODE","",]],#OP mode #26
                            [["CL_MODE","",]],#collect_user mode #27
                            [["DBG_MODE","",]],#dbg mode #28
                            [["FLEE_LI_MODE","",]],#freelicence  #29
                            [["LAN_MODE","",]],#lan  #30
                            [["URL_ROG","",]],#lan  #31
                            [["SEARCH_TURN","",]],#lan  #32#search turn
                            [["SEARCH_ARIA","False",]],#lan  #33#search 都道府県
                            [["SEARCH_MODE",g_val.mode_list[1],]],#lan  #34#search mode
                            ]
            else:
                temp_log = [[["Proxy","TEST_PROXY"]],#0
                            [["Swing","0"]],#1
                            [["Password",""]],#2
                            [["Category",""]],#3
                            [["Country","",""]],#4
                            [["Domain","",]],#5
                            [["Mail","",]],#6
                            [["Tell","",]],#7
                            [["Category tree","","",""]],#8
                            [["Category Log","-",]],#9
                            [["Country Log","-",]],#10
                            [["City Log","-",]],#11
                            [["FAX",True,]],#12
                            [["Average reviews","True",]],#13
                            [["All reviews","True",]],#14
                            [["Monday","True",]],#15
                            [["Tuesday","True",]],#16
                            [["Wednesday","True",]],#17
                            [["Thuersday","True",]],#18
                            [["Friday","True",]],#19
                            [["Satuerday","True",]],#20
                            [["Sunday","True",]],#21
                            [["DWORD",""]],#22
                            [["DWORD_NUM","100"]],#23
                            [["jyoutyu_check","False",]],#jyoutyu_check#24
                            [["jyoutyu_end","0",]],#jyoutyu_end#25
                            [["OP_MODE","",]],#OP mode #26
                            [["CL_MODE","",]],#collect_user mode #27
                            [["DBG_MODE","",]],#dbg mode #28
                            [["FLEE_LI_MODE","",]],#freelicence  #29
                            [["LAN_MODE","",]],#lan  #30
                            [["URL_ROG","",]],#lan  #31
                            [["SEARCH_TURN","",]],#lan  #32#search turn
                            [["SEARCH_ARIA","False",]],#lan  #33#search 都道府県
                            [["SEARCH_MODE",g_val.mode_list[1],]],#lan  #34#search mode
                            ]

            #エリアチェック　デフォルト
            temp_log[4]=g_val.default_eria
            temp_log[6]=g_val.default_bmail#デフォルトメール
            temp_log[22]=g_val.default_word
            
            #ログ書き込み
            if not os.path.isfile(log_file_name):
                with open(log_file_name, mode='w',encoding="utf_8_sig") as f:#,newline='\n'
                    for temp_log_n in temp_log:
                        for temp_log_n0 in temp_log_n:
                            f.write(str(temp_log_n0) +"\n")

            shutil.copy(log_file_name, back_name)

            #初期値反映
            log_in_list = g_val.conf_log_txt()
            ini_n = 0
            for temp_log_n in temp_log:
                try:
                    if(log_in_list[ini_n]):
                        temp=0
                except:
                    log_in_list.append(temp_log_n)

                ini_n+=1

            print("常駐チェック",log_in_list[24][0][1],":",log_in_list[25][0][1])
            
            #temp_log_w[24]=[["jyouyu_setti",bt_app_jyoutyu_.get()]]
            #temp_log_w[25]=[["jyoutyu_end",f_jyouty_end]]
            #temp_log_w[26]=[["mo",Op_ok]]#OP mode

            #temp_log_w[27]=[["cl",CL_INIT_]]#cl mode
            #temp_log_w[28]=[["db",dbg_]]#dbg mode
            #temp_log_w[29]=[["fl",Flag_free_licence]]#freelicence
            #temp_log_w[30]=[["lan",language_get_value]]#lan

            if(log_in_list[24][0][1] =="True"):# and log_in_list[25][0][1]==1):
                
                if(log_in_list[25][0][1]=="1"):
                    print("常駐発動")
                    g_val.Jyoutu_Mode_=1
                    g_val.data_log_write("常駐発動")
                    
                    g_val.Op_ok = int(log_in_list[26][0][1])#26 OP mode
                    g_val.CL_INIT_ = log_in_list[27][0][1]
                    g_val.dbg_ = int(log_in_list[28][0][1])
                    g_val.Flag_free_licence = log_in_list[29][0][1]
                    g_val.init_lang = log_in_list[30][0][1]
                    g_val.mode_get_value = log_in_list[34][0][1]
                    print("00::",log_in_list[26][0][1])
                    if(log_in_list[26][0][1] =="1"):#OP mode
                        print("OPMODE")
                        button_op_ex["text"] = "OK"
                        button_op_ex['bg'] = "#DDFFFF"
                        button_op_ex['state'] = "disable"
                        g_val.Op_ok=1
                        g_val.Flag_free_licence=1  
                        if(g_val.language_get_value==g_val.Lnagage_list[1]):
                            root.title('IZANAMI　営業リスト収集ツール【管理者】')
                        else:
                            root.title('IZANAMI　Sales listing tool【Adomin】')
                            
                    else:
                        if(1 == g_val.CL_INIT_):
                            button_op_ex["text"] = "OK"
                            button_op_ex['bg'] = "#DDFFFF"
                            #button_op_ex['state'] = "disable"
                            g_val.dbg_=0
                            g_val.login_ok = "collect_user"
                            #g_val.Op_ok=1
                            g_val.Flag_free_licence=1
                            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                                root.title('IZANAMI　営業リスト収集ツール【FREEDOM】')
                            else:
                                root.title('IZANAMI　Sales listing tool【FREEDOM】')

                        #DBG
                        if(g_val.dbg_==1):
                            button_op_ex["text"] = "OK"
                            button_op_ex['bg'] = "#DDFFFF"
                            #button_op_ex['state'] = "disable"
                            g_val.dbg_=1
                            #g_val.Op_ok=1
                            #g_val.Flag_free_licence=1
                            if(g_val.language_get_value==g_val.Lnagage_list[1]):
                                root.title('IZANAMI　営業リスト収集ツール【DEBUG】')
                            else:
                                root.title('IZANAMI　Sales listing tool【DEBUG】')
        except:
            traceback.print_exc()
            temp=0
    ####################################################################################################
    
    ####################################################################################################
    #HELP
    #
    text_help_v_f=ttk.Label(help_veision,anchor=tkinter.E,justify="left")
    text_help_v_f.place(x=10, y=10)
    text_help_v_f["text"]="IZANAMI APP \nVer "+g_val.SOFT_VERSION

    text_help_faq_f=ttk.Label(help_faq,anchor=tkinter.E,justify="left")
    text_help_faq_f.place(x=10, y=10)
    text_help_faq_f["text"]="よくある質問は、こちらをご覧ください。"

    def jump_to_link(url):
        webbrowser.open_new(url)
    text_help_faq_link=ttk.Label(help_faq,anchor=tkinter.E,justify="left",cursor="hand2")
    text_help_faq_link.place(x=10, y=30)
    text_help_faq_link["text"]="https://izanami.link/faqpage"
    text_help_faq_link.bind("<Button-1>", lambda e:jump_to_link("https://izanami.link/faqpage"))
    ##########################################################################################################
    g_val.get_fax_bln = tkinter.BooleanVar()
    check_get_fax = ttk.Checkbutton(
        get_item,
        text="FAX(外すとスピード上がります。)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_fax_bln,

    )
    check_get_fax.place(x=20, y=75)
    g_val.get_fax_bln.set(True)
    ##############################################
    g_val.get_hyouka_bln = tkinter.BooleanVar()
    check_get_hyouka = ttk.Checkbutton(
        get_item,
        text="平均評価数",
        #command=kate_sentaku_clr_,
        variable=g_val.get_hyouka_bln,

    )
    check_get_hyouka.place(x=20, y=100)
    g_val.get_hyouka_bln.set(True)
    ##############################################
    g_val.get_kutikomi_bln = tkinter.BooleanVar()
    check_get_kutikomi = ttk.Checkbutton(
        get_item,
        text="口コミ数",
        #command=kate_sentaku_clr_,
        variable=g_val.get_kutikomi_bln,

    )
    check_get_kutikomi.place(x=20, y=125)
    g_val.get_kutikomi_bln.set(True)
    ##############################################
    g_val.get_mon_bln = tkinter.BooleanVar()
    check_get_mon = ttk.Checkbutton(
        get_item,
        text="営業時間(月)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_mon_bln,

    )
    check_get_mon.place(x=20, y=150)
    g_val.get_mon_bln.set(True)
    ##############################################
    g_val.get_tue_bln = tkinter.BooleanVar()
    check_get_tue = ttk.Checkbutton(
        get_item,
        text="営業時間(火)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_tue_bln,

    )
    check_get_tue.place(x=20, y=175)
    g_val.get_tue_bln.set(True)
    ##############################################
    g_val.get_wed_bln = tkinter.BooleanVar()
    check_get_wed = ttk.Checkbutton(
        get_item,
        text="営業時間(水)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_wed_bln,

    )
    check_get_wed.place(x=20, y=200)
    g_val.get_wed_bln.set(True)
    ##############################################
    g_val.get_thu_bln = tkinter.BooleanVar()
    check_get_thu = ttk.Checkbutton(
        get_item,
        text="営業時間(木)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_thu_bln,

    )
    check_get_thu.place(x=20, y=225)
    g_val.get_thu_bln.set(True)
    ##############################################
    g_val.get_fri_bln = tkinter.BooleanVar()
    check_get_fri = ttk.Checkbutton(
        get_item,
        text="営業時間(金)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_fri_bln,

    )
    check_get_fri.place(x=20, y=250)
    g_val.get_fri_bln.set(True)
    ##############################################
    g_val.get_sat_bln = tkinter.BooleanVar()
    check_get_sat = ttk.Checkbutton(
        get_item,
        text="営業時間(土)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_sat_bln,

    )
    check_get_sat.place(x=20, y=275)
    g_val.get_sat_bln.set(True)
    ##############################################
    g_val.get_sun_bln = tkinter.BooleanVar()
    check_get_sun = ttk.Checkbutton(
        get_item,
        text="営業時間(日)",
        #command=kate_sentaku_clr_,
        variable=g_val.get_sun_bln,

    )
    check_get_sun.place(x=20, y=300)
    g_val.get_sun_bln.set(True)
    ##############################################

    text_kate_detail=ttk.Label(get_item,anchor=tkinter.E,justify="left")#font=("", "12", "bold")
    text_kate_detail.place(x=10, y=10)
    text_kate_detail["text"]="収集が不要な項目はチェックを外してください。\nチェックを外すことで収集スピードが多少改善する場合があります。"

    

    ##########################################################################################################
    #########################################################################################################################################
    #終了window
    def click_close():
        
        if(g_val.language_get_value==g_val.Lnagage_list[1]):

            if messagebox.askokcancel("Confirmation", "本当に閉じていいですか？\n"+"Are you sure to close?"):
                
                g_val.stop_=1
                g_val.stop_sys_=1
                #g_val.f_jyouty_end =0#開始1:停止0
                #g_val.Jyoutu_Mode_=0#取り下げ
                text_st_f["text"]="終了処理中。。。。"
                
                
        else:
            if messagebox.askokcancel("Confirmation", "本当に閉じていいですか？\n"+"Are you sure to close?"):

                g_val.stop_=1
                g_val.stop_sys_=1
                #g_val.f_jyouty_end =0#開始1:停止0
                #g_val.Jyoutu_Mode_=0#取り下げ
                text_st_f["text"]="End processing...."
                
    #########################################################################################
    #Languge
    def init_langage_():
        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.dai_kate_=g_val.dai_kate_J
            g_val.tyuu_kate_=g_val.tyuu_kate_J
            g_val.syou_kate_=g_val.syou_kate_J
        else:
            g_val.dai_kate_=g_val.dai_kate_e
            g_val.tyuu_kate_=g_val.tyuu_kate_e
            g_val.syou_kate_=g_val.syou_kate_e

        if(g_val.language_get_value==g_val.Lnagage_list[1]):
            g_val.todo_huken_=g_val.todo_huken_J
            g_val.sikutyouson_=g_val.sikutyouson_J
        elif(g_val.language_get_value==g_val.Lnagage_list[2]):
            g_val.todo_huken_=g_val_country.todo_huken_us
            g_val.sikutyouson_=g_val_country.sikutyouson_us
        elif(g_val.language_get_value==g_val.Lnagage_list[3]):
            g_val.todo_huken_=g_val_country.todo_huken_uK
            g_val.sikutyouson_=g_val_country.sikutyouson_uK
        elif(g_val.language_get_value==g_val.Lnagage_list[4]):
            g_val.todo_huken_=g_val_country.todo_huken_IE
            g_val.sikutyouson_=g_val_country.sikutyouson_IE
        elif(g_val.language_get_value==g_val.Lnagage_list[5]):
            g_val.todo_huken_=g_val_country.todo_huken_CA
            g_val.sikutyouson_=g_val_country.sikutyouson_CA
        elif(g_val.language_get_value==g_val.Lnagage_list[6]):
            g_val.todo_huken_=g_val_country.todo_huken_AU
            g_val.sikutyouson_=g_val_country.sikutyouson_AU
        elif(g_val.language_get_value==g_val.Lnagage_list[7]):
            g_val.todo_huken_=g_val_country.todo_huken_NZ
            g_val.sikutyouson_=g_val_country.sikutyouson_NZ
        elif(g_val.language_get_value==g_val.Lnagage_list[8]):
            g_val.todo_huken_=g_val_country.todo_huken_ZA
            g_val.sikutyouson_=g_val_country.sikutyouson_ZA

        #print(g_val.todo_huken_)
        #print(g_val.sikutyouson_)
        #sleep(100)
        cate_set()
        set_todohuken()


        if(g_val.mode_get_value==g_val.mode_list[1]):
            temp="開始:新規で収集を始めます。\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp+="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[2]):
            temp="開始:duda検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[3]):
            temp="開始:duda検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[4]):
            temp="開始:リクナビNEXT検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[5]):
            temp="開始:マイナビ検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[6]):
            temp="開始:就活会議検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[7]):
            temp="開始:エン転職検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[8]):
            temp="開始:タウンワーク検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"
        elif(g_val.mode_get_value==g_val.mode_list[9]):
            temp="開始:食べログク検索画面が表示されます。\n条件を入力して検索開始ボタンをクリックしてください。"
            temp +="\n\n終了:収集を中断・終了します。\n途中から開始:中断した状態から再開します。"#\n\n\n厳密収集：通常はカテゴリの設定をしても関係のない業種が収集されること\nがあります。厳密収集にチェックを入れるとカテゴリ名が同一の場合のみ収集\nしますが、収集できる件数が大幅に減少します。"
            temp +="\n\n\nメール収集をさらに強化：収集先を広げさらに調査します。収集数は向上\nしますが、全体的な収集速度は低下します。"


        text_st_f["text"]=temp
        
        if(g_val.language_get_value!=g_val.Lnagage_list[1]):

            #title
            if(g_val.Jyoutu_Mode_==0):
                root.title('IZANAMI　Sales listing tool')
            notebook.tab(tab_st, text="Start/End")
            notebook.tab(tab_cf, text="Listing setting")
            notebook.tab(tab_op, text="Option")
            notebook.tab(tab_help, text="Help")
            notebook_1_1.tab(cf_kategory, text="Category and progress")
            notebook_1_1.tab(cf_erea, text="Area")
            notebook_1_1.tab(cf_bl_list, text="Denial list")
            notebook_1_1.tab(cf_domain, text="Denial domain")
            notebook_1_1.add(cf_dword, text="Denial word")
            
            notebook_1_2.tab(op_tyouhuku, text="Remove the duplicated items")
            notebook_1_2.tab(op_yuragi, text="Swing")
            notebook_1_2.tab(op_proxy, text="Proxy")
            notebook_1_2.tab(get_item, text="Listing item")
            notebook_1_2.tab(op_logdl, text="Log DL")
            notebook_1_2.tab(op_ex, text="Expansion")
            notebook_1_3.tab(help_faq, text="FAQ")
            notebook_1_3.tab(help_veision, text="Version")

            #button.text.set("Updated Text")
                
            button["text"]="Start"
            button1["text"]="Pause"
            button2["text"]="Continue"
            #chk["text"]="Exact listing"
            chk0["text"]="Mail Exact listing"
            chk0_app["text"]="Resident app (measures against forced termination)" # 'アプリを常駐（強制終了対策）')
            chk0_todohuken["text"]="Serch without aria"
            #常駐
           
            # チェックボタン作成
            chk_tell["text"]='Phone No.'
            chk_mail["text"]='Email address'
            
            button_tyohuku["text"]='Reference'
            button_tyohuku_2["text"]='Execute (backup copy recommended)'
            button_op_ex["text"]='Send'

            check_eria["text"]="Select all"
            check_eria_clr["text"]="unselect all"
            check_eria_popular["text"]="Populous cities"
            check_kate0["text"]="Check all"

            check_clr_kate0["text"]="Uncheck all"
            button_domain["text"]='Add'
            button_bl["text"]='Add'
            button_bl0["text"]='Add'

            # ボタンの作成と配置
            button_p["text"]='Check'
            button_log_ex["text"]='Download'
            button_log_ex1["text"]='Log'

            check_get_fax["text"]="FAX (Listen speed will increase)"
            check_get_hyouka["text"]="Average reviews"
            check_get_kutikomi["text"]="All reviews"
            check_get_mon["text"]="Monday"
            check_get_tue["text"]="Tueseday"
            check_get_wed["text"]="Wednesday"
            check_get_thu["text"]="Thursday"
            check_get_fri["text"]="Friday"
            check_get_sat["text"]="Saturday"
            check_get_sun["text"]="Sunday"
            button_new_version["text"]='DownLoad',

            button_expire["text"]='Contract a paid license'
            button_free_paid["text"]='Contract a paid license'

            # ボタンの作成と配置


            #########text########################## 
            text_ini0["text"]="Waiting to be processed for launch."
            text_tyouhuku_["text"] = 'Integrate duplicated items into one. It will prioritize upper lines.'
            text_tyouhuku_f["text"]="Select a file"

            g_val.text_st_f1["text"]="Proxy setting : Invalid"
            g_val.window_log["text"]="Ready"

            text_op_ex_f["text"]="Input password"
            text_kate["text"]="Input keywords"
            text_kate0["text"]="Pick up categories"
            text_kate1["text"]="Now listing"

            g_val.get_imform.place(x=90, y=2.5)
            g_val.get_imform["width"]=40
            text_kate2["text"]="*Source is based on Google map."
            text_kate3["text"]="*Listing will start from the top to the bottom in the key word,\nand move to the top of checked category."
            text_bdomain_f["text"]="Input denial info.(up to 1000 items)\nEx.）izanami.link"
            text_bmail_f["text"]="Email address (up to 1000 items)\n*It is not collected if there in the below word. "
            text_btel_f["text"]="Phone numbers (No hyphen) \n(up to 1000 items)"
            text_bword_f["text"]="Input denial info.(up to 1000 items)\nEx.）denial\n*If there is the string before and after the email address, it is not collected."
            text_ng_dword_f["text"]="Reserch Num(befor and after)"
            text_ng_dword_f.place(x=220, y=15)

            yragi_txt ="Auto-listing has a higher risk that Google temporarily blocks the access.\n"
            yragi_txt +="Swing function will reduce the risk by moving like human.\n\n"
            yragi_txt +="Swing makes the listing speed slower but has a lower risk of being blocked.\n\n"
            yragi_txt +="Stop the system regularly regardless of ON or OFF.\n"
            yragi_txt +="We are not responsible for the case Google blocks the access."

            text_yuragi_f["text"]=yragi_txt
            text_proxy_f["text"]="Set a proxy server.\nYou can leave it blank if you are not sure as it will affect the listing."
            text_proxy_f2["text"]="Ex: 127.0.0.1:9150"
            text_log_f["text"]="Please download the the log here and sent it to a support team for bug report."
            text_kate_detail["text"]="Uncheck unnecessary items for listing.\nReducing list items may improve the listing speed."
            text_help_faq_f["text"]="See our website for FAQ."

            text_bmail0_f["text"]="Input denial info."
            temp="Start: Create a new listing.\nEnd: Stop listing.\nContinue: Restart listing where you left off."#n\n\nExact listing: It may include items not related to your categories.\nChecking in the Exact listing allows it to collect the exactly \nsame names of your categories. \nNote the number of listing items will decrease."
            temp +="\n\n\nEmail Exact listing:Collect email addresses strictly. \nCollection speed may decrease."
       
            text_st_f["text"]=temp

            text_ini_newversion["text"]="A new version is available. \n Current ver. is　"+g_val.SOFT_VERSION
            text_ini_expire["text"]="Your license has expired."
            #text_ini_free["text"]="You are using a free trial.\nListing is unlimited but only 2000 items can be output in csv data."

    #===========================
    def thread_st():
        global icon
        global root

        #-----------------------
        # メニュー
        #-----------------------
        image = Image.open(g_val.path1+'//IZ.ico')
        options_map = {'Show': lambda:[print('show_main_window'),root.after(0,root.deiconify)], 'Quit': lambda: root.after(1, botton1_clicked)} #変更 update
            
        items = []
        for option, callback in options_map.items():
                items.append(MenuItem(option, callback, default=True if option == 'Show' else False))

        menu = Menu(*items)
        
        #-----------------------
        # アイコン表示
        #-----------------------
        icon = pystray.Icon("test", image, title="IZNAMI", menu=menu)
        #icon=pystray.Icon("test", icon=None, "IZNAMI", menu)
        icon.run()


    root.protocol("WM_DELETE_WINDOW", click_close)
    thread_ini = threading.Thread(target=init_)
    thread_ini.start()

    thread_status = threading.Thread(target=status_wach_)
    thread_status.start()

    thread_status_v = threading.Thread(target=status_wach_v)
    thread_status_v.start()

    #thread_icon_v = threading.Thread(target=thread_st)
    #thread_icon_v.start()

    if(0):
        # スタートアップフォルダのパスを取得
        startup = winshell.startup()

        # ショートカットのパスを作成
        path = os.path.join(startup, "shortcut.lnk")

        # ショートカットを作成
        with winshell.shortcut(path) as link:
            link.path = g_val.path1+"\\IZANAMI.exe"
            link.description = "IZNAMI"
            # オプション：ショートカットアイコンを変更する
            # link.icon_location = "C:\\path\\to\\icon.ico"

    
except:
    #if(g_val.language_get_value==g_val.Lnagage_list[1]):
    #    text_ini1["text"]="初期化エラー"
    #else:
    #    text_ini1["text"]="Initialization error"

    traceback.print_exc()
    g_val.data_log_write(datetime.datetime.now())
    g_val.data_log_write(traceback.format_exc())
    g_val.err_message_w(100,traceback.print_exc())
    #-----------------------
   # Xボタンを押された時の処理
   #-----------------------
#root.protocol('WM_DELETE_WINDOW', lambda:root.withdraw())


root.mainloop()
sys.exit()