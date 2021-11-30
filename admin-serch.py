import requests
import os
from colorama import Fore , init
import sys
from speedtest import Speedtest



init()
print(Fore.YELLOW + """                                                  `                                                  
                                            `/`  +-  ::                                             
                                         ..  +:`.+/`.+-  -                                          
                                          -:.+:/-/+.+/:--`                                          
                                           ./:so+so+s+-/                                            
                                            -+++++++++/`                                        
                     `````                  `..........                   `````                     
                         ``....-.-------::::------------::::-------.-....``                         
                                      `                               .                             
                             `--`  `..:.         `--. `-/```./`` ..-- .                             
                            `+... -:``/.         /-.. `:/.``-/.` o` ` +                             
                             --:/ -:../. .       .-:/` `/.` `/.` +    +                             
                             ````  ````  ``.....`````   ``   ``  `    `                             
                                                                                                    
                           ``````.....------------------------.....``````             v.1.0.0              
                     ````````````````````     sianor_sd               ````````````````````            
                                              `````````                               sianor tool
                      
                      
                      1 ) admin pannel finder  
                      2 )  speed test                                                  ## soon
                      3 ) send message in telegram to user by bot                      ## soon
                      """)      



search = [
    'robots.txt',
    'search/',
    'admin/',
    'login/',
    'sitemap.xml',
    'sitemap2.xml',
    'config.php',
    'wp-login.php',
    'log.txt',
    'update.php',
    'INSTALL.pgsql.txt',
    'user/login/',
    'INSTALL.txt',
    'profiles/',
    'scripts/',
    'LICENSE.txt',
    'CHANGELOG.txt',
    'themes/',
    'inculdes/',
    'misc/',
    'user/logout/',
    'user/register/',
    'cron.php',
    'filter/tips/',
    'comment/reply/',
    'xmlrpc.php',
    'modules/',
    'install.php',
    'MAINTAINERS.txt',
    'user/password/',
    'node/add/',
    'INSTALL.sqlite.txt',
    'UPGRADE.txt',
    'INSTALL.mysql.txt' ,
    'administrator/account.brf',
    'administrator.brf','acceso.brf',
    'admin_area/admin.html',
    'pages/admin/admin-login.brf',
    'admin/admin-login.brf',
    'admin-login.brf',
    'bb-admin/index.html',
    'bb-admin/login.html',
    'bb-admin/admin.html',
    'admin/home.html',
    'login.brf'
    ,'modelsearch/login.brf',
    'moderator.brf','moderator/login.brf',
    'moderator/admin.brf',
    'account.brf',
    'pages/admin/admin-login.html',
    'admin/admin-login.html',
    'admin-login.html',
    'controlpanel.brf',
    'admincontrol.brf',
    'modelsearch/admin.brf',
    'admincontrol/login.brf',
    'adm/admloginuser.brf','admloginuser.brf',
    'admin2.brf',
    'admin2/login.brf',
    'admin2/index.brf',
    'usuarios/login.brf',
    'adm/index.brf',
    'adm.brf',
    'affiliate.brf',
    'adm_auth.brf',
    'memberadmin.brf',
    'administratorlogin.brf',
    'cpanel',
    'cpanel.php',
    'cpanel.html',
]

url = input("Enter your URL: ")

for page in search:
    req = requests.get( "https://"+ url + "/" + page)
    if req.status_code == 200:
        print( Fore.GREEN + " [+] " + Fore.BLUE + "  page is ok " +url + "/"+ page )
    else:
        print( Fore.RED+ " [-]" + Fore.RED + " page is not ok " +url + "/" + page )
