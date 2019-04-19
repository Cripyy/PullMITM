import os
import time

print('This script removes old MITM script, and then downloads the new updated one from GitHub\n\n')

print('Checking if there is a MITM folder in Documents')
if os.path.isdir('/root/Documents/MITM'):
    if True:
        print('The file exists')
        delete_folder = input('\nDo you want to delete the old file?[y/n] ')
        if delete_folder == 'y' or '':
            os.system('sudo rm -r /root/Documents/MITM')
            if os.path.isdir('/root/Documents/MITM-old'):
                if True:
                    os.system('sudo rm -r /root/Documents/MITM-old')
        else:
            os.system('sudo mv /root/Documents/MITM /root/Documents/MITM-old')

print('\nStarting download in 2 seconds and placing the folder in Documents')
time.sleep(2)

os.system('sudo git clone https://github.com/Cripyy/MITM /root/Documents/MITM')
print('\n\nDownload complete, stopping script')
