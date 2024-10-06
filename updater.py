import urllib.request, zipfile, os, requests


ver = requests.get('https://raw.githubusercontent.com/ThisIsDiver/RandomThunder/main/version.txt').text
ver_file = open('version.txt', 'r')
txt = ver_file.read()
ver_file.close()
if txt != ver:
    ver_file = open('version.txt','w')
    ver_file.write(ver)
    response = urllib.request.urlretrieve(
        'https://github.com/ThisIsDiver/RandomThunder/releases/download/RandomThunder002/RandomThunder.0.0.2.Reserve.zip',
        'RandomThunder.0.0.2.Reserve.zip')
    print(response)
    j = zipfile.ZipFile(response[0], 'r')
    files = j.namelist()
    j.extractall('text_extract')
    j.close()
    os.remove(response[0])