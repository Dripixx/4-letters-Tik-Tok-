import string
import random
import time
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook
from TikTokApi import TikTokApi


api = TikTokApi()

def random_letter():
    lower_upper_alphabet = string.ascii_letters
    return random.choice(lower_upper_alphabet)
    
def random_username(lettercount):
    username = ""
    for i in range(lettercount):
        username += random_letter()
    return username


def main():
    print(Fore.MAGENTA + '''
Your name
''')
    while 1:
        username = "4Letterstiktok"
        webhook_url = ""
        
        random_lettercount = random.randint(1,2)
        if random_lettercount == 1:     
            username = random_username(4)
            webhook_url = ""
        else:
            username = random_username(4)
            webhook_url = ""
            
        try:       
            api.getUserObject(username)
            print(Fore.GREEN + '[AVAIBLE] ' + Fore.White + username)
            webhook = DiscordWebhook(url=webhook_url, content="Avaible | " + username)
            webhook.execute()
        except:
            webhook = DiscordWebhook(url=webhook_url, content="Taken | " + username)
            webhook.execute()
            print(Fore.RED + "[TAKEN] " + Fore.WHITE + username)
            time.sleep(2)    


main()
