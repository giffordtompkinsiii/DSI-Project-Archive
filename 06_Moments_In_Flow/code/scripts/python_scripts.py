import os
from PIL import Image
   

def remove_corrupted_images(root_directory='.'):
    '''
    Walks through 

    '''
    for (root,_,files) in os.walk(root_directory, topdown=False):
        for file in files:
            if os.path.splitext('.')[-1] ==  'jpg':
                try:
                    img_path = os.path.join(root,file)
                    img = Image.open(img_path)
                    img.verify()
                except(IOError, SyntaxError):
                    corrupted_file_name = os.path.join(root,'corrupted_images',file)
                    os.rename(img_path, corrupted_file_name)
        print(f'Completed inspection of {root}')