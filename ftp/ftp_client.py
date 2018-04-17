import ssh_client
import errno
import os
from datetime import datetime
from ftplib import FTP

#base_dir = '/data1/nelson/data'

def establishConnection():
    ftp = FTP('')
    ftp.connect('192.168.147.128',9000)
    ftp.login()
    ftp.cwd('users') 
    ftp.retrlines('LIST')
    return ftp

def createNewUserDir(user):
    ftp = establishConnection()
    ftp.mkd(user)
    ftp.cwd(user)
    ftp.mkd('raw')
    ftp.mkd('tophat')
    ftp.quit()

def uploadFile(user, path, name):
    ftp = establishConnection()
    file_name = user + "/raw/" + name
    ftp.storbinary('STOR '+file_name, open(path, 'rb'))
    ftp.quit()

def downloadFile(user, path, name):
    ftp = establishConnection()
    local_file = open(name, 'wb')
    file_path = user + "/" + path
    ftp.retrbinary('RETR '+file_path, local_file.write, 1024)
    ftp.quit()
    local_file.close()

def listFiles(user, path):
    ftp = establishConnection()
    dir_path = user + "/" + path
    ftp.cwd(dir_path)
    files = []
    try:
        files = ftp.nlst()
    except(ftplib.error_perm, resp):
        if str(resp) == "550 No files found":
            print("No files in this directory")
        else:
            raise
    for f in files:
        print(f)
    ftp.quit()
    return files

def createSpecificDir(user, folder):
    ftp = establishConnection()
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    ftp.cwd(user)
    ftp.cwd(folder)
    ftp.mkd(current_time)
    ftp.quit()
    return current_time
    
#createNewUserDir('test01')
#uploadFile('test01', 'example2.fai', 'example2.fai')
#downloadFile('test01', 'raw/example2.fai', 'example3.fa')
#listFiles('test01', 'raw')
#createSpecificDir('test01', 'tophat')
#ssh_client.send_command("docker run ei11051/tophat")
