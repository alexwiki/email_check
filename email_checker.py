import re
import json
import os
from zenlog import log

def main():

    check_json('/json_data/MOCK_DATA.json')
    #simple_manual_check()
def check_json(file):

    with open('./json_data/MOCK_DATA.json','r') as f:
        data=json.load(f)
        for line in data:
            print(line)
            log.warning("candidate e-mail: "+line["email"])
            try: 
                re.match(".+?@\w.+?\.\w{2,3}",line["email"])
                log.info("RegEx matched")
            except:
                log.error("Failed to match regEx: "+str(line))   

def simple_manual_check():    
    emails={"Alex":"alex@mail.com","Kostas":"kostas@mail.com","Fake":"fake@mail.c"}
    
    for key in emails:
        try: 
            re.match(".+?@\w.+?\.\w{2,3}",key)
            log.info("RegEx matched")
        except:
            log.error("Failed to match regEx: "+str(key))   


main()
