import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep

os.system("xdg-open https://wa.link/7v2bxa")
time.sleep(1)
os.system('clear')
logo =("""\x1b[1;36m      
        
 ___      ___   __    ___            __      _____  ___   
|"  \    /"  | |" \  |"  |          /""\    (\"   \|"  \  
 \   \  //   | ||  | ||  |         /    \   |.\\   \    | 
 /\\  \/.    | |:  | |:  |        /' /\  \  |: \.   \\  | 
|: \.        | |.  |  \  |___    //  __'  \ |.  \    \. | 
|.  \    /:  | /\  |\( \_|:  \  /   /  \\  \|    \    \ | 
|___|\__/|___|(__\_|_)\_______)(___/    \___)\___|\____\) 
                                                          
                                                                                                                                      
                        \033[1;91m\033[m ;41m\033[1;33m\033[1;35m\033[1;37mBɽ͢oʞɘ͡ŋ-Pʌ͜͡ɽɗʜ͢ʌŋ Cʜ͜͡ʌɭtɘ'Rʌ͜͡ʜɘ͢ŋgɘ-Kʌ͢͡ʆıɭɘ'Mɘ͜͡ɽə-\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
              \033[1;91m\033[1;41m\033[1;33m\033[1;35m\033[1;37mBʌ͜͡ɢʌıɽ'Bʜ͜͡ı-Yʌʜ͢͡ʌŋ Eʞ-Sıtʌ͜͡ɽ̆ʌ'Too͡ʈ-Jʌ͜͡ƞɘ'Sə-Aʌ͜͡sɱ͢͡ʌŋ-Sʋ͜͡ƞʌ-Nʌ͜͡ʜı'Hoʈ͜͡ʌ\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
╔═════════════════════════════════════════════════════════════════════════════════════╗
║  \033[1;31mN4M3       : MILAN                                                                                      ║
║  \033[1;32mRULL3X     : MILAN HELPING ZONE                                                                         ║
║  \033[1;32mFORM 🏠    : DHARAN                                                                                     ║ 
║  \033[1;34mBR9ND      : MULTI POST                                                                                 ║
║  \033[1;37mGitHub     : MILAN INSIDE                                                                               ║
║  \033[1;32mWH9TS9P    : +9779704612289                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
\x1b[1;32m 𝗠𝗨𝗟𝗧𝗬 𝗧𝗢𝗞𝗘𝗡 𝗣𝗢𝗦𝗧 𝗧𝗢𝗢𝗟 𝗘𝗡𝗝𝗢𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘
\033[1;30m 𝗠𝗨𝗟𝗧𝗬 𝗣𝗢𝗦𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗧𝗦 𝗧𝗢𝗢𝗟 """ )
# Print the logo
print(Fore. CYAN + logo +  Style.RESET_ALL)
# Start time

print("\033[92mSTART TIM3 :", time.strftime("%Y-%m-%d %H:%M:%S"))  



# Login System

os.system('espeak -a 300 "OFSAN CHUNE                     ONE                     YA                     TWO                     YA                     ZERO"')
# Prompt Password 
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    mmm = requests.get('https://pastebin.com/raw/DxLQsVfs').text

    if mmm not in password:
        print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗘𝗥𝗗➜ ')
        sys.exit()
        
pas()

# Prompt for token file
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input("\033[1;32m ➜ KITNE POST ME TOOL LAGANA HA WO NUMBER DALO"))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Define the user IDs and message files
user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣0𝗦𝗧 𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥➜ ")
    print('\x1b[1;32m\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗔𝗦𝗦𝗚𝗘 𝗙𝗜𝗟𝗘➜  ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    user_messages[user_id] = message_file




# Prompt for delay time in messages
delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 /𝗧𝗜𝗠𝗘 (in seconds) 𝗙𝗢𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦 : "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Prompt for delay before repeating the process
repeat_delay = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥  𝗗𝗘𝗟𝗔𝗬/𝗧𝗜𝗠𝗘 (in seconds) 𝗕𝗘𝗙𝗢𝗥𝗘 𝗥𝗘𝗣𝗘𝗔𝗧𝗜𝗡𝗚 𝗧𝗛𝗘  𝗣𝗥𝗢𝗖𝗘𝗦𝗦 : "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Get profile name using an access token
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

# Function to send a message to a user's inbox conversation using an access token
def send_message(access_token, user_id, message):
    url = "https://graph.facebook.com/v15.0/{}/comments".format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Referer': 'https://www.facebook.com/',
        'Authorization': f'Bearer {access_token}'
    }
    data = {'message': hater_name + ' ' + message}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'\033[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>\n \033[1;32m[{current_time}] {Fore.WHITE} 𝗬𝗢𝗨𝗥 𝗖𝗠𝗠𝗘𝗡𝗧 𝗦𝗘𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬➜𝗧𝗔𝗥𝗚𝗘𝗧 𝗜𝗗 {user_id}: \033[1;32m{hater_name + message}\n\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        return True
    else:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'\x1b[1;33m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>\n\x1b[1;32m[{current_time}] \x1b[1;31mError sending comment to user ID {user_id}: \x1b[1;31m{hater_name + message}\n \x1b[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'\x1b[1;31m[{current_time}] Response content: \x1b[1;31m{response.content.decode()}')
        return False

# Main loop to send messages
while True:
    total_successful_messages = 0
    total_unsuccessful_messages = 0

    # Iterate over the access tokens
    for i, access_token in enumerate(access_tokens):
        try:
            # Login using the access token and get the profile name
            profile_name = get_profile_name(access_token)
            if not profile_name:
                continue

            profile_number = i + 1
            access_token_id = access_token[:4] + '********'

            # Print the profile information
            print(f'\x1b[1;37mPROFILE➜{profile_number} (ID➜ {access_token_id})➜ {profile_name}')
            print('\x1b[1;37m<<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>>')

            # Iterate over the user IDs and messages
            for user_id, message_file in user_messages.items():
            	
                # Read messages from the message file for the current user ID
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()

                # Shuffle the messages for the current user
                
                # Get the hater name for the current user ID
                hater_name = haters_name[user_id]


                # Get the messages count for the current user
                messages_count = len(messages)

                # Get the current message index for the user ID
                message_index = i % messages_count

                # Get the message for the current index
                message = messages[message_index]

                if send_message(access_token, user_id, message):
                    total_successful_messages += 1
                else:
                    total_unsuccessful_messages+= 1

                time.sleep(delay_time)  # Delay between each message
            # Print Facebook ID, message, and current date/time after message is sent
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;32m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 𝗜𝗗 ➜: {user_id}')
            print('\x1b[1;36m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
            print('\x1b[1;32m𝗡𝗘𝗫𝗧 𝗜𝗗 𝗥𝗘𝗔𝗗𝗬 𝗧𝗢 𝗦𝗘𝗡𝗗 𝗖𝗢𝗠𝗠𝗘𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠 𝗡𝗔𝗠 𝗧𝗢 𝗬𝗪𝗔𝗗 𝗛𝗢𝗚𝗔 𝗬𝗔 𝗕𝗛𝗨𝗟 𝗚𝗔𝗬𝗔 ' )  
            print('\x1b[1;33m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;31m[{current_time}] Internet disconnected. Reconnecting in 10 seconds...{Style.RESET_ALL}')
            time.sleep(10)

        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;31m[{current_time}] An error occurred:➜ {str(e)}{Style.RESET_ALL}')
            continue

    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    print('\x1b[1;34mAll comments sent. Waiting before repeating the process...')
    print('\x1b[1;36m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    time.sleep(delay_time)  # Delay before repeating the process
