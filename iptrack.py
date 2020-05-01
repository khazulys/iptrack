import json, requests, os
from time import sleep
from colorama import Style, Fore
a=Fore.GREEN
b=Fore.YELLOW
c=Fore.RED
d=Fore.BLUE
def logo():
	os.system('clear')
	print("""

      _____  ___  _____                _    
      \_   \/ _ \/__   \_ __ __ _  ___| | __
       / /\/ /_)/  / /\/ '__/ _` |/ __| |/ /
    /\/ /_/ ___/  / /  | | | (_| | (__|   < 
    \____/\/      \/   |_|  \__,_|\___|_|\_\\

	\033[4mTrack Location using IP Address\033[0m\n""")
                                        

def main():
	try:
		ipaddress=input("{}[√]ip address: {}".format(c,d))
		sleep(2)
		url="https://ipinfo.io/{}".format(ipaddress)
		request=requests.get(url)
		jsons=json.loads(request.text)
		print("\n{}[√]IP\t\t: {}{}".format(a,b,jsons['ip']))
		print("{}[√]City\t\t: {}{}".format(a,b,jsons['city']))
		print("{}[✓]Country\t: {}{}".format(a,b,jsons['country']))
		print("{}[√]Postcode\t: {}{}".format(a,b,jsons['postal']))
		print("{}[√]Timezone\t: {}{}".format(a,b,jsons['timezone']))
		print("{}[√]SimCard\t: {}{}".format(a,b, jsons['org']))
		print("{}[√]Location\t: {}{}".format(a,b,jsons['loc']))
		input("\n[FINISH] ")
		print(Style.RESET_ALL)
	except:
		exit()

if __name__=="__main__":
	logo();main()
