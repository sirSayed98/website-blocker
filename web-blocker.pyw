import time
from datetime import datetime as dt

host_temp="hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
website_list = ['www.facebook.com', 'facebook.com']
redirect="127.0.0.1"
start_time =3
end_time = 20

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("Working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+ website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
