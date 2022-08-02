# чтение с базы
import json

def take_from_base(path = 'phone_numbers.json'):
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
    return data

def rewrite_base(dictionary,path = 'phone_numbers.json'):
    with open(path, 'w') as outfile:
        json.dump(dictionary, outfile,indent=2)
        outfile.close()