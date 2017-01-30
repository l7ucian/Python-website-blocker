import time
from datetime import datetime as dt
temp_hosts_path = 'hosts'
hosts_path = 'C:/Windows/System32/drivers/etc/hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com','www.youtube.com']
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        with open(hosts_path, 'r+') as f:
            print('bad hours')
            content = f.read()
            for website in website_list:
                if website not in content:
                    f.write(redirect + 3*' '+website+'\n')
    else:
        print('Fun hours')
        with open(hosts_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
    time.sleep(5)
f.closed