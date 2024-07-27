import os
import json
import requests

banner = '''
\033[1;91m
\033[1;97m
\033[41;1m AEDOTRIS \033[00;1m
'''
os.system('clear')
print(banner)

username = input('\033[1;97m[\033[1;91m×\033[1;97m] Username: ')
password = input('\033[1;97m[\033[1;91m×\033[1;97m] Password: ')

url = 'https://b-api.facebook.com/method/auth.login'
params = {
    'access_token': '237759909591655|0f140aabedfb65ac27a739ed1a2263b1',
    'format': 'json',
    'sdk_version': '2',
    'email': username,
    'locale': 'en_US',
    'password': password,
    'sdk': 'ios',
    'generate_session_cookies': '1',
    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'
}

response = requests.get(url, params=params)
cak = response.json()

print("\n\033[1;97m[\033[1;91m×\033[1;97m]  \033[1;92m")
print(json.dumps(cak, indent=4))
print("\033[1;97m")

if "session_key" in cak:
    print("\n\033[1;97m[\033[1;91m×\033[1;97m] Your Access Token: \033[1;92m")
    print(cak["access_token"])
    print("\033[1;97m")
    with open("token.txt", 'a') as token_file:
        token_file.write(cak["access_token"] + '\n')
else:
    print("\n\033[1;97m[\033[1;91m×\033[1;97m] Login Failed !")
    print(" ")
