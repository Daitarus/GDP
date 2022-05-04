from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
    
    
def upload_dir(dir_path=''):
    
    try:
        drive = GoogleDrive(gauth)
        
        for file_name in os.listdir(dir_path):
        
            my_file = drive.CreateFile({'title': f'{file_name}'})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()
            
            print(f'File {file_name} was uploaded!')
            
        return 'Success!'
    except Exception as _ex:
        return 'Error! Maybe the path is wrong!'
    
    
def main():
    dir_path=input('Enter dir path: ')
    print(upload_dir(dir_path))
    
    
if __name__ =='__main__':
    main()