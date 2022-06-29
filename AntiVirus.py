import hashlib
import os

#Global Variables
virusHashes = list(open('virusHash.txt','r').read().split('\n'))

def md5_hash(path):
    try:
        with open(path,"rb") as f:
            bytes = f.read()
            md5hash = hashlib.md5(bytes).hexdigest()
            f.close()
        return md5hash
    except:
        return 0
    

def virus_checker(pathOfFile):

    global virusHashes

    virusHash = md5_hash(pathOfFile)

    for i in virusHashes:
        if i == virusHash:
            print(pathOfFile+" contains malware")
            return 1
    return 0

virusPath = []

def virusScanner(path):

    dir_list = list()

    for(dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    for i in dir_list:
        print(i)
        if virus_checker(i) != 0:
            virusPath.append(i)

def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
