#Github Repo Link

#Sonam Yangki
#SWE
#02240364

#References
#Links that you referred while solving
#https://youtu.be/d-Eq6x1yssU?si=w5jbCKg7YckjwIk_
#https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjKvcnZmZeJAxV5Z0gAHR9vMVUYABAAGgJjZQ&co=1&ase=2&gclid=CjwKCAjw68K4BhAuEiwAylp3kgcuhGWynfII13ggjAgLNKp4ThBrscIH4uQnU5qrH7v5wmSuVY0wKRoCJnMQAvD_BwE&ei=i_IRZ_fNE7uE4-EP24_CsAc&ohost=www.google.com&cid=CAESVuD2liM-fE-6v2owk3ip6-uJU-x7DBYMFpem7RHAS9OkvHA05ze8XcBvnk3m77Qm6R60VqJICQqkRYl1Dvow0ipcGxeaowuCZpTiYU-W5s0o5BLcEcdR&sig=AOD64_2sFDB1tRL6FIyCXRQ140Rehc8Jjw&q&sqi=2&nis=4&adurl&ved=2ahUKEwi3v7nZmZeJAxU7wjgGHduHEHYQ0Qx6BAgSEAE

#the problem
#1. Dzongkha's unique characters complicated processing. 
#2. large dictionaries affected memory and lookup times.
#3. even the requests is install, firstly the out is correct. when i try second time it is not working.
#4. dictionary has many unwanted characters
#Solution
#1.Used utf-8 encoding for proper character handling. 
#2.Implemented a hash map for quick lookups and a cleaning algorithm to remove duplicates.


#check spelling
#import re

#def load_words_from_dictionary(file):
    #with open(file, 'r', encoding='utf-8') as f:
        #return set(f.read().splitlines())

#def ordinal(n):
    #return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

#def check_incorrect_words(text, dictionary):
    #with open(text, 'r', encoding='utf-8') as f:
        #for line_num, line in enumerate(f, start=1):
            #for pos, word in enumerate(re.findall(r'\S+', line), start=1):
                #if word not in dictionary:
                    #print(f"Line {line_num}, {ordinal(pos)} word '{word}' is incorrect.")

#if __name__ == "__main__":
    #check_incorrect_words('364.txt', load_words_from_dictionary('cleaned_dictionary.txt'))

