import re
from zenlog import log

def main():

    emails={"Alex":"alex@mail.com","Kostas":"kostas@mail.com"}

    for key in emails:
        try: 
            re.match(".+?@\w.+?\.\w.+",key)
            log.info("RegEx matched")
        except:
            log.error("Failed to match regEx: "+str(key))   


main()
