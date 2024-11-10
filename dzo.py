import requests

url = 'https://csf101-server-cap1.onrender.com/get/input/364'
txt_file= requests.get(url)

with open('364.txt', 'wb')as file:
    data = file.write(txt_file.content)

print('Download 364.txt')