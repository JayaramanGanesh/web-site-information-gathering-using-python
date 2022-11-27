import os
import re
import platform
import whois
import requests 
from bs4 import BeautifulSoup
from pywebcopy import save_webpage
from socket import *

print(
   '''\033[31m
                ___.     .__        _____      
__  _  __ ____\_ |__   |__| _____/ ________  
\ \/ \/ _/ __ \| __ \  |  |/    \   __/  _ \ 
 \     /\  ___/| \_\ \ |  |   |  |  |(  <_> )
  \/\_/  \___  |___  / |__|___|  |__| \____/ 
             \/    \/          \/          
             '\033[0m'  
   '''
)
print('========================================')
print('\n')
print('\033[92m1.web domain information gathering')
print('2.web site sub domain scanning')
print('3.web site link extracking')
print('4.web site source code download')
print('5.open port scanning \033[0m')
print('\n')
print('========================================')
print('\n')


weblink = str(input('please given the web site :'))
selectid = input('which one you have select if you choose above mention the value :')

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'



if selectid == '1':
        domain = whois.whois(weblink)
        print('whois domain')
        print('------------')
        print(color.GREEN + "[+] Registrar Name: " + color.STOP, domain.registrar)
        print(color.GREEN + "[+] Organisation: " + color.STOP, domain.org)
        print(color.GREEN + "[+] City: " + color.STOP, domain.city)
        print(color.GREEN + "[+] State: " + color.STOP, domain.state)
        print(color.GREEN + "[+] Country: " + color.STOP, domain.country)
        print(color.GREEN + "[+] ZipCode: " + color.STOP, domain.zipcode)
        print(color.GREEN + "[+] Whois Server: " + color.STOP, domain.whois_server)
        print(color.GREEN + "[+] Name Servers: " + color.STOP)
        print(color.GREEN + "[+] Referral url " + color.STOP, domain.referral_url)
        print(color.GREEN + "[+] Updated time  " + color.STOP, domain.updated_date)
        print(color.GREEN + "[+] Expiration date " + color.STOP,domain.expiration_date)
        print(color.GREEN + "[+] status " + color.STOP, domain.status)
        print(color.GREEN + "[+] Registrant postal code " + color.STOP, domain.registrant_postal_code)
        print(color.GREEN + "[+] Dnssec" + color.STOP, domain.dnssec) 
        print(color.GREEN + "[+] Domain register address " + color.STOP, domain.address)
        print(color.GREEN + "[+] Domain Register company email address " + color.STOP, domain.emails)
     

elif selectid == '2':
        print('sub domain scainning the site :'+ color.BLUE + weblink + color.STOP )
        print('------------------------------------------------------------------------------')
        print('\n')
        txt = open('subtxt.txt', 'r').readlines()
        for i in txt:
          sub_website = i.strip() + "." + weblink
          try:
             r = requests.get("https://"+sub_website)
             print( "[+] " +color.RED + sub_website + color.STOP +color.GREEN + '  status code ' + color.STOP ,r.status_code)
          except:
             pass
         

elif selectid == '3':
           print(color.BLUE ,'web site links extracting ....',color.STOP)
           print('------------------------------')
           print('\n')
           grab = requests.get('https://' + weblink)
           soup = BeautifulSoup(grab.text, 'html.parser')
           for link in soup.find_all("a"):
               linkss = link.get('href') 
               print('[+]'+ linkss +color.RED +'status code '+color.STOP ,link.status_code)


elif selectid == '4':
         print(color.BLUE,'web site source code downloading',color.STOP)
         print('---------------------------------------------')
         print('\n')
         project = {'project_name': 'site folder'}
         path = input('please set folder path for downloading files :')
         print(color.BLUE ,'web site downloading start...............',color.STOP)
         try:
            save_webpage( url=weblink,project_folder= path,**project)
         except:
            print(color.RED,'web site source code cannot downloading are such files are downloading please theck the folder ',color.STOP)
            pass


elif selectid == '5':
         print(color.BLUE,'open port scanner....',color.STOP)     
         print('----------------------------------')
         print('\n')
         print('web port scanner take long time ur given value based so waiting for final result....')
         resp = input(' GIVEN UPPER VALUE TYPE YES/NO :')
         if resp == 'YES':
            target = weblink
            ip = gethostbyname(target)
            print(color.GREEN,'starting scaning the host ',color.STOP,':',color.BLUE,ip,color.STOP)
            for i in range(1000,9999):
                 s= socket(AF_INET,SOCK_STREAM)
                 connect = s.connect_ex((ip,i))
                 if (connect == 0):
                    print(color.BLUE,'port %d : open'%(i,))
                 s.close
            else :
                exit()

