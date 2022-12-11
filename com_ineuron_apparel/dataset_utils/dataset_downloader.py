import gdown
from zipfile import ZipFile

# Original Link :- https://drive.google.com/file/d/14QoqoZQLYnUmZgYblmFZ2u2eHo9yv2aA/view?usp=sharing
url = 'https://drive.google.com/uc?id=14QoqoZQLYnUmZgYblmFZ2u2eHo9yv2aA'
output = 'Fire_smoke.zip'

gdown.download(url, output, quiet=False)

# specifying the zip file name
file_name = output

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
