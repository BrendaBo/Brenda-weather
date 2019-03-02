from time import sleep
import os, shutil
usb_path = '/Volumes/'
content = os.listdir(usb_path) 
while True:
    new_content = os.listdir(usb_path)
    if new_content != content:
        print('检测到U盘')
        break
    sleep(3)
    print('aa')
for item in new_content:
    if item not in content:
        shutil.copytree(os.path.join(usb_path,item),'usb_copy')
        content.append(item)