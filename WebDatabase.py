import requests
import hashlib
from colorama import Fore

apikey = "Put your VirusTotal api key here"

def virus_web_check(pathOfFile):

    with open(pathOfFile,"rb") as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()
        #sha256hash = "52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c"
        f.close()
        query = {'apikey':{apikey}, 'resource':{sha256hash}}
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=query)
        obj = response.json()

        if 'positives' in obj:
            print(Fore.MAGENTA + 'This file contins the virus '+Fore.LIGHTRED_EX + obj['scans']['Kaspersky']['result'] + Fore.RESET)
        else:
            print(Fore.LIGHTGREEN_EX + 'This file is safe' + Fore.RESET)

def virus_info(pathOfFile):

    with open(pathOfFile,"rb") as f:
        bytes = f.read()
        #sha256hash = hashlib.sha256(bytes).hexdigest()
        sha256hash = "52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c"
        f.close()
        query = {'apikey':{apikey}, 'resource':{sha256hash}}
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=query)
        obj = response.json()

        print(Fore.CYAN + 'total : ' + Fore.LIGHTGREEN_EX+ str(obj['total']) + Fore.RESET)
        print(Fore.CYAN + 'positives : ' + Fore.LIGHTRED_EX +str(obj['positives']) + Fore.RESET)

        if 'positives' in obj:
            for pair in obj['scans'].items():
                if pair[1]['detected'] == True:
                    print(Fore.LIGHTBLUE_EX + pair[0] + ' : ' +  Fore.LIGHTYELLOW_EX + pair[1]['result'] + Fore.RESET)

        else:
            print(Fore.LIGHTGREEN_EX + 'This file is safe' + Fore.RESET)
        
