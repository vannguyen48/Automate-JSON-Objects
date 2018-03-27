#!/usr/bin/env python3
import argparse
import json

sc_dict = {}

class StoreCreds(argparse.Action):
     def __init__(self, option_strings, dest, nargs=None, **kwargs):
         self._nargs = nargs
         super(StoreCreds, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
     def __call__(self, parser, namespace, values, option_string=None):
         for kv in values:
             k,v = kv.split("=")
             sc_dict[k] = v
         setattr(namespace, self.dest, sc_dict)

def loadjson():
    """
    Load current credential JSON file, retrieve current credential data

    """
    with open('servercred.json') as jsoncred:
        hastext = jsoncred.read(1)
        if not hastext: # if text is empty, then returns empty dictionarty
            data = {}
        else:
            data = json.load(open('servercred.json'))
    return data

def processinput(dict):
    """
    Processes input from the command line and append to credential file

    Args:
        dict: dictionary containing existing server credentials, or an empty dictionary if there is no credential

    """
    parser = argparse.ArgumentParser(description = 'Gather server credentials and append to json cred file')
    parser.add_argument("--name", type = str)
    parser.add_argument("--key_pairs", dest="sc_dict", action=StoreCreds, nargs="+", metavar="KEY=VAL")
    args = parser.parse_args()
    dict[args.name] = sc_dict
    with open ('servercred.json', 'w') as fp:
        json.dump(dict, fp, indent = 4)
        fp.close()


def main():
    """
    Performs a main check

    """
    dict = loadjson()
    processinput(dict)

if __name__ == '__main__':
    """
    Performs a main check

    """
    main()
