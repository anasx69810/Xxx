# Modules

import            os
from os           import system
import            typing
from typing       import Union, List
import            tkinter.messagebox
import            tls_client # Could Make It More HQ By Adding A Different Library But Then Again It's Open Source So IDGAF
import            ab5 # Good Library For Some Decent UI - Use It                                                        |
from ab5          import vgratient #                                                                                    |
import            colorama #                                                                                            |
from colorama     import Fore # Me Personally I Prefer rich HOWEVER It's Open Source So - - - - - - - - - - - - - - - - -
import            webbrowser
import            random
import            string
import            sys

# Funcs

def installmodules() -> None: # Can You Use subprocess For This? Yes ~ Am I Going To Use It For A More Friendly User Interface? Fuck No.
    try:
        import tls_client
        import ab5
        import colorama

    except ModuleNotFoundError:
        system('pip install tls_client')
        system('pip install ab5')
        system('pip install colorama')

def set_title(title : str) -> None: 
    system("title " + title)

def clear() -> None:
    system("cls" if os.name == "nt" else "clear") # clear If On Mac

def loadtokens(filename : str) -> List[str]:
    try:
        with open(filename, "r") as file:
            tokens = file.readlines()
            return [token.strip() for token in tokens if token.strip()]
        
    except FileNotFoundError: # NOT Adding Output Printing To This LMFAO ~ Add It Your Self If You Want
        # print("Where's The Fucking File You Dumbass?")
        return []

def getthatmsg() -> None:
    tkinter.messagebox.showinfo("READ ME", "I Asked On My Server What Tool Would Like To Have Access To [For Free] And A Lot Of Yall Wanted This. Decided To Make This Open Source [It Is A SHIT Tool TBH, IDK Why You Would Want It] - Enjoy")
    tkinter.messagebox.showinfo("READ ME", "Developed By Lovely [Bro Do I Even Wanna Take Credits For This Shit? LOL :sob:] + Skids Will Probably Delete This Line OR Rebrand It!")
    
# UI

whatisthisui : str = '''

                                            ╔═╗┌┬┐┌┐ ┌─┐┌┬┐┌─┐
                                            ╠═╣│││├┴┐├┤  │││ │
                                            ╩ ╩┴ ┴└─┘└─┘─┴┘└─┘

                                            1 ⋆ ɢᴇɴᴇʀᴀᴛᴇ ᴛᴏᴋᴇɴꜱ
                                            2 ⋆ ᴄʜᴇᴄᴋ ᴛᴏᴋᴇɴꜱ
                                            3 ⋆ ꜱᴜʀᴘʀɪꜱᴇ

'''

def bnr() -> None:
    start_color=[0, 0, 255]
    end_color=[255, 255, 255]

    print(vgratient(whatisthisui,start_color,end_color))

whatisthisui2 : str = '''

                                            ╔═╗┌┬┐┌┐ ┌─┐┌┬┐┌─┐
                                            ╠═╣│││├┴┐├┤  │││ │
                                            ╩ ╩┴ ┴└─┘└─┘─┴┘└─┘
                                        
'''

def banner() -> None:
    start_color=[0, 0, 255]
    end_color=[255, 255, 255]

    print(vgratient(whatisthisui2,start_color,end_color))

# Colors

b : str = Fore.BLUE
s : str = Fore.LIGHTBLACK_EX
g : str = Fore.LIGHTGREEN_EX
r : str = Fore.LIGHTRED_EX

def sadlyes() -> None:
    clear()

    banner()

    amount   : int = int(input(f"                                            {s}Enter Amount To Generate{s} {b}>{b} {s}").strip())

    # filename : str = input(f"                                            {s}Enter The File Location Of Where Everything Is Going To Be Saved{s} {b}[{b} {s}Drag The File To Your Terminal{s} {b}{b}] {s}").strip() ~ This Is Optional, But If You Want To Use This You Need To Enter The Same File For Token Checking
    
    with open("tokens.txt", "w") as f:
        for _ in range(amount):
            l1              : str = "MTI" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(23))
            l2              : str = "".join(random.choice(string.ascii_letters + string.digits + '_-')  for _ in range(6))
            l3              : str = "".join(random.choice(string.ascii_letters + string.digits + '_-')  for _ in range(38))
            rndmstringfinal : str = f"{l1}.{l2}.{l3}"
            print(f"                                            {s}Token{s} {b}|{b} {s}{rndmstringfinal}{s} {b}|{b}")

            f.write(rndmstringfinal + "\n")

    exit = input(f"                                            {s}Press{s} {b}[{b} {s}ENTER{s} {b}]{b} {s}To Go Back. . .{s}")
    exit = main()

def checker() -> None:
    clear()

    banner()

    session = tls_client.Session() # Could I Improve This? Yes! ~ Is This An Open Source Code? Yes ~ So Is There A Point? Nah

    tokens = loadtokens("tokens.txt") 

    with open("output/valid.txt", "a") as vf, open("output/locked.txt", "a") as lf, open("output/invalid.txt", "a") as invf:

        for token in tokens:
            headers = {
                "Authorization" : token 
                # "Accept" : 
                # "Accept-Encoding" :
                # "User-Agent" :
            }

            # Aren't These The Most SHIT Headers You've Ever Seen? YES! You Thought I Was Gonna At Least Add A UA. . .So Did I! But Guess WHAT? It's An Open Source Code!
            # You Really Thought You Were About To Get Good Quality Headers On This Shit, Didn't You

            try:
                rr = session.get('https://discord.com/api/v9/users/@me/library', headers=headers)

                if rr.status_code == 200:
                    print(f"            {g}Valid Token{g} {b}|{b} {s}{token[:45]}{s} {b}|{b} {s}200")
                    vf.write(token + "\n")
                    sys.stdout.flush() # Is The Printing That Fast That It Needs stdout.flush? Nah ~ Am I Adding It? Yes 
                
                elif rr.status_code == 401:
                    print(f"            {r}Invalid Token{r} {b}|{b} {s}{token}{s} {b}|{b} {s}400")
                    invf.write(token + "\n")
                    sys.stdout.flush()

                elif "You need to verify your account in order to perform this action." in rr.text:
                    print(f"            {r}Locked Token{r} {b}|{b} {s}{token}{s} {b}|{b} {s}400")
                    lf.write(token + "\n")
                    sys.stdout.flush()

                else:
                    print(f"            {r}Error On Token{r} {b}|{b} {s}{token}{s} {b}|{b} {s}{r.status_code} {b}~{b} {r.text}")
                    sys.stdout.flush()

            except Exception as e:
                print(f"            {r}Error{r} {b}|{b} {s}{str(e)}")
                sys.stdout.flush()

    exit = input(f"            {s}Press{s} {b}[{b} {s}ENTER{s} {b}]{b} {s}To Go Back. . .{s}")
    exit = main()

def selfpromo() -> None:
    yt : str = "https://www.youtube.com/@ambedotools"
    dc : str = "https://discord.gg/2hYjPvR8Eh"

    webbrowser.open_new_tab(yt)
    webbrowser.open_new_tab(dc)
    main()

# Main Func

def main() -> None:
    clear()

    set_title('Whatever The Fuck This Is. . .Welcome! Why The Fuck Are You Using A String Gen?')

    bnr()

    usernamea = os.getlogin()

    choice : Union[str,int] = input(f"                                            {s}Is This{s} {b}[{b} {s}{usernamea}{s} {b}]{b} {s}? ").strip()

    if choice == "1" : sadlyes()

    elif choice == "2" : checker()

    elif choice == "3" : selfpromo()

    else : main()


if __name__ == '__main__':
    installmodules()

    getthatmsg()

    main()
