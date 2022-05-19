import uuid,random,string,os,ctypes,json
try:
    import requests
    from colorama import Fore
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
    import requests
    from colorama import Fore

redline = Fore.RED+"─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
inputed  = Fore.LIGHTWHITE_EX+"["+ Fore.BLUE+           ">"+Fore.LIGHTWHITE_EX+"] "
sended   = Fore.LIGHTWHITE_EX+"["+ Fore.LIGHTGREEN_EX+          "*"+Fore.LIGHTWHITE_EX+"] "
question = Fore.LIGHTWHITE_EX+"["+ Fore.LIGHTMAGENTA_EX+"?"+Fore.LIGHTWHITE_EX+"] "
annowns  = Fore.LIGHTWHITE_EX+"["+ Fore.LIGHTRED_EX+           "!"+Fore.LIGHTWHITE_EX+"] "
msgFromProg = Fore.LIGHTWHITE_EX+"["+Fore.LIGHTYELLOW_EX+"~"+Fore.LIGHTWHITE_EX+"] "
infohash = Fore.LIGHTWHITE_EX+"["+Fore.LIGHTBLUE_EX+"#"+Fore.LIGHTWHITE_EX+"] "
added = Fore.LIGHTWHITE_EX+"["+Fore.GREEN+"+"+Fore.LIGHTWHITE_EX+"] "

ppp = '{'
ppp1 = '}'

ctypes.windll.kernel32.SetConsoleTitleW('#Reset-Sender - By @hmzoa - V1.0')
os.system('mode con: cols=129 lines=22')
logohere = f"""
           {Fore.LIGHTMAGENTA_EX}   ██╗ ██╗ ██████╗ ███████╗███████╗███████╗████████╗   ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
             ████████╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝   ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
             ╚██╔═██╔╝██████╔╝█████╗  ███████╗█████╗     ██║█████╗███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
             ████████╗██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║╚════╝╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
             ╚██╔═██╔╝██║  ██║███████╗███████║███████╗   ██║      ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
              ╚═╝ ╚═╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝      ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                {Fore.LIGHTBLACK_EX}instagram password reset by - @HMZOA
{Fore.RED}─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────                                                                                """




def main():
    print(logohere)

    target = input(f'{inputed}Target without({Fore.LIGHTCYAN_EX}@{Fore.LIGHTWHITE_EX}) < {Fore.LIGHTGREEN_EX}user {Fore.LIGHTWHITE_EX}or {Fore.LIGHTGREEN_EX}email{Fore.LIGHTWHITE_EX} > : ')
    print('\n'+redline)



    if "@" in target:
        usem = "user_email"
    else:
        usem = "username"

    data = {
        "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
        usem: target,
        "guid": uuid.uuid4(),
        "device_id": uuid.uuid4()
    }

    head = {
        "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)"
    }

    req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data)

    if "obfuscated_email" in req.text:
        responsjson = json.loads(req.text)
        print(f"{question}Obfuscated Email {responsjson['obfuscated_email']}")
        print(f'{infohash}Here Is the request respons from {Fore.LIGHTMAGENTA_EX}instagram{Fore.LIGHTWHITE_EX} :\n{Fore.LIGHTYELLOW_EX+req.text}\n{redline}')

        print(f'\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()
        exit(42069072)

    elif req.status_code == 404:
        print(f'\n{annowns}Password Reset Request Fail , There is no user such as {Fore.LIGHTRED_EX}@{target+Fore.LIGHTWHITE_EX}')
        print(f'{infohash}Here Is the request respons from {Fore.LIGHTMAGENTA_EX}instagram{Fore.LIGHTWHITE_EX} : {Fore.LIGHTRED_EX}{ppp}"message":"No users found","status":"fail"{ppp1}{Fore.LIGHTWHITE_EX}\n\n{redline}')

        print(f'\n\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()
        exit(42069072)

    elif "Please wait a few minutes before you try again" in req.text:
        print(f'\n{annowns}Password Reset Request Fail , Please wait a few minutes before you try again ,Rate Limit reached . ')
        print(f'{infohash}Here Is the request respons from {Fore.LIGHTMAGENTA_EX}instagram{Fore.LIGHTWHITE_EX} : \n{Fore.LIGHTYELLOW_EX+req.text+Fore.LIGHTWHITE_EX}\n\n{redline}')

        print(f'\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()
        exit(42069072)
        
    elif "Sorry, we can't send you a link to reset your password. Please contact Instagram for help." in req.text:
        
        print(f"\n{annowns}Password Reset Request Fail , maybe it's an abandoned account . ")
        print(f'{infohash}Here Is the request respons from {Fore.LIGHTMAGENTA_EX}instagram{Fore.LIGHTWHITE_EX} : \n{Fore.LIGHTYELLOW_EX+req.text+Fore.LIGHTWHITE_EX}\n\n{redline}')

        print(f'\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()
        exit(42069072)
    else:
        responsjson = json.loads(req.text)
        print(f"{sended}Reset Successfully Sended , check your email .")
        
        print(f'{infohash}Here Is the request respons from {Fore.LIGHTMAGENTA_EX}instagram{Fore.LIGHTWHITE_EX} : \n{Fore.LIGHTYELLOW_EX+req.text+Fore.LIGHTWHITE_EX}\n\n{redline}')

        
        print(f'\n\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()
        exit(42069072)

if __name__ == '__main__':
    main()
