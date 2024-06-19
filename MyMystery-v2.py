import requests
import os
from colorama import Fore as F

def clear():
    if os.name == 'nt': 
        os.system('cls')  
    else:  
        os.system('clear')
def getresult(api_url):
    try:
        resp = requests.get(api_url)
        resp.raise_for_status() 
        data = resp.json()
        return data.get("result"), data.get("url")
    except requests.exceptions.RequestException as error:
        print(f"$ Erro na requisição: {error}")
    except ValueError:
        print("$ Erro ao decodificar o JSON")
    return None, None

clear()
banner='                                                                                                                                \n                ##############                    \n              ##################                  \n            ######          ######                \n            ####              ####                \n          ######                ####              \n          ####        MY         ####              \n          ####     MYSTERY.v2    ####              \n          ####                  ####                \n            ####              ####                \n            ######          ######                \n              ##################                  \n                  ##############                  \n                            ######                \n                              ######              \n                                ####              \n                                ######            \n                                  ######          \n                                    ####        '

print(banner)
print(f"                                        Web Version: {F.YELLOW}instantusername.com/{F.RESET}")

username = input(F.BLUE+F"[ {F.MAGENTA}? {F.BLUE}]{F.RESET} Username\n> ")

apis = {
    "Reddit": f"https://api.instantusername.com/c/reddit/{username}",
    "SnapChat": f"https://api.instantusername.com/c/snapchat/{username}",
    "Youtube": f"https://api.instantusername.com/c/youtube/{username}",
    "Twitch": f"https://api.instantusername.com/c/twitch/{username}",
    "Vimeo": f"https://api.instantusername.com/c/vimeo/{username}",
    "Rumble": f"https://api.instantusername.com/c/rumble/{username}",
    "DailyMotion": f"https://api.instantusername.com/c/dailymotion/{username}",
    "Slack": f"https://api.instantusername.com/c/slack/{username}",
    "Fiver": f"https://api.instantusername.com/c/fiverr/{username}",
    "Github": f"https://api.instantusername.com/c/github/{username}",
    "Gitlab": f"https://api.instantusername.com/c/gitlab/{username}",
    "Steam": f"https://api.instantusername.com/c/steamgroup/{username}",
    "XboxGamerTag": f"https://api.instantusername.com/c/xbox-gamertag/{username}",
    "Minecraft": f"https://api.instantusername.com/c/minecraft/{username}",
    "Lichess": f"https://api.instantusername.com/c/lichess/{username}",
    "Chess": f"https://api.instantusername.com/c/chess.com/{username}",
    "PlayStore": f"https://api.instantusername.com/c/google-playstore/{username}",
    "Roblox": f"https://api.instantusername.com/c/roblox/{username}",
    "Osu": f"https://api.instantusername.com/c/osu!/{username}",
    "Tetr.io": f"https://api.instantusername.com/c/tetr.io/{username}",
    "Dribbble": f"https://api.instantusername.com/c/dribbble/{username}",
    "Behance": f"https://api.instantusername.com/c/behance/{username}",
    "RedBubble": f"https://api.instantusername.com/c/redbubble/{username}",
    "ArtStation": f"https://api.instantusername.com/c/artstation/{username}",
    "LottieFiles": f"https://api.instantusername.com/c/lottiefiles/{username}",
    "Medium": f"https://api.instantusername.com/c/medium/{username}",
    "Wordpress": f"https://api.instantusername.com/c/wordpress/{username}",
    "Blogger": f"https://api.instantusername.com/c/blogger/{username}",
    "DevianArt": f"https://api.instantusername.com/c/deviantart/{username}",
    "Slides": f"https://api.instantusername.com/c/slides/{username}",
    "Spotify": f"https://api.instantusername.com/c/spotify/{username}",
    "SoundCloud": f"https://api.instantusername.com/c/soundcloud/{username}",
    "Genius (Artists)": f"https://api.instantusername.com/c/genius-(artists)/{username}",
    "Genius (Users)": f"https://api.instantusername.com/c/genius-(users)/{username}",
    "PromoDJ": f"https://api.instantusername.com/c/promodj/{username}",
    "Flickr": f"https://api.instantusername.com/c/flickr/{username}",
    "Unsplash": f"https://api.instantusername.com/c/unsplash/{username}",
    "VsCo": f"https://api.instantusername.com/c/vsco/{username}",
    "ReeSound": f"https://api.instantusername.com/c/freesound/{username}",
    "BandCamp": f"https://api.instantusername.com/c/bandcamp/{username}",
    "TrakTrain": f"https://api.instantusername.com/c/traktrain/{username}",
    "Telegram": f"https://api.instantusername.com/c/telegram/{username}",
    "Signal": f"https://api.instantusername.com/c/signal/{username}",
    "Kik": f"https://api.instantusername.com/c/kik/{username}",
    "Npm": f"https://api.instantusername.com/c/npm/{username}",
    "PyPi": f"https://api.instantusername.com/c/pypi/{username}",
    "RubyGems": f"https://api.instantusername.com/c/rubygems/{username}",
    "DockerHub": f"https://api.instantusername.com/c/docker-hub/{username}",
    "Replit": f"https://api.instantusername.com/c/replit.com/{username}",
    "CodeAcademy": f"https://api.instantusername.com/c/codecademy/{username}",
    "LeetCode": f"https://api.instantusername.com/c/leetcode/{username}",
    "HackerRank": f"https://api.instantusername.com/c/hackerrank/{username}",
    "CodePen": f"https://api.instantusername.com/c/codepen/{username}",
    "DevCommunity": f"https://api.instantusername.com/c/dev-community/{username}",
    "OpenSource": f"https://api.instantusername.com/c/opensource/{username}",
    "HackerOne": f"https://api.instantusername.com/c/hackerone/{username}",
    "HashOne": f"https://api.instantusername.com/c/hashnode/{username}",
    "GitBook": f"https://api.instantusername.com/c/gitbook/{username}",
    "Foostodon": f"https://api.instantusername.com/c/fosstodon/{username}",
    "Chaos": f"https://api.instantusername.com/c/chaos/{username}",
    "GeeksForGeeks": f"https://api.instantusername.com/c/geeksforgeeks/{username}",
    "Kaggle": f"https://api.instantusername.com/c/kaggle/{username}",

}
clear()
print(banner)
print(f"                                        Web Version: {F.YELLOW}instantusername.com/?q={username+F.RESET}\n")
print(f"[{F.YELLOW}Yandex{F.RESET}] https://yandex.com/search/?text='{username}'")
print(f"[{F.YELLOW}Google{F.RESET}] https://www.google.nl/search?q=inurl%3A{username}'")


print("\n------------- + SEARCHING + -------------\n")
for network, url in apis.items():
    status, resurl = getresult(url)
    if status is not None:
        if status == "taken":
            print(f"[{F.GREEN}Found{F.RESET}] {network} - {resurl}")
        else:
            pass
