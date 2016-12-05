"""CLI skillstracker to track campers learning progress
Usage:
    skillstracker.py add [<skill>...] 
    skillstracker.py viewall 
    skillstracker.py setstatus <skill>
    skillstracker.py view <status>
    skillstracker.py progress
    skillstracker.py (-h | --help)

Arguments
    <command>
    <skill>  Name of the skill to be added/modified
    <status> Status of skills: learnt or pending

Options:
   -h --help    Show this screen
"""
from docopt import docopt
import requests
from termcolor import colored


if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')

if ARGS['add']:
    #implement add function here
    #skill name is ARGS['skill']
    if ARGS['<skill>']:
        for skill in ARGS['<skill>']:
            print skill
    pass

if ARGS['viewall']:    
    #implement view all added skills
    pass

if ARGS['view']:
    #implement view specific status here
    #status is ARGS['learnt'] or ARGS['pending']
    #pass
    
    RES = requests.get(API_URL)
    if RES.status_code == 200:
        print colored('Getting all values...', 'green')
        for post in RES.json():
            if post["status"] == ARGS["<status>"]: # To check status Learn or Pending
                print post["skill"] + "\t|\t" + post["status"]
    else:
        print colored('Error: There was a problem ' \
            'processing your request', 'red')

if ARGS['progress']:
    #display percentage learnt
    pass
