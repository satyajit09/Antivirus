import WebDatabase
import AntiVirus

val = input("What would you like to do?\n 1. Check a file for viruses.\n 2. Check a directory for viruses.\n 3. Check and delete.\n 4. Check for virus using web database.\n 5. Get more info from web database.\n ")
path = input("enter file path : ")

if val == '1':
    print(AntiVirus.virus_checker(path))
elif val == '2':
    AntiVirus.virusScanner(path)
elif val == '3':
   AntiVirus.virusRemover(path)
elif val == '4':
    WebDatabase.virus_web_check('split.py')
else:
    WebDatabase.virus_info(path)
