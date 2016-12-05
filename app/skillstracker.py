"""CLI skillstracker to track campers learning progress
Usage:
    skillstracker.py add <skill> 
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

if ARGS['viewall']:    
    #implement view all added skills

if ARGS['view']:
    #implement view specific status here
    #status is ARGS['learnt'] or ARGS['pending']

if ARGS['progress']:
    #display percentage learnt