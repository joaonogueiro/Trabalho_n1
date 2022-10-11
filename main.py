#!/usr/bin/env python3

################## Library ###################
import argparse
from collections import namedtuple
from inspect import ArgSpec
import random
from readchar import readkey
from termcolor import colored
from time import sleep, time, ctime
from pprint import pprint
##############################################

###### Variable input from type tuble ########
Input = namedtuple('Input', ['requested', 'received', 'duration']) #complex = namedtuble('complex', ['r','i'])


######### Fuction to start the test ##########
def start_test():

    print('Press any key to start the test')
    print(colored(('    Press space to finish'), 'red'))

    K = (ord(readkey())) #K -> character pressed to initialize the test

    if K == 32:  #32 -> space bar in ascii
        K = ('Space bar')
        print('Terminating the test...')
        sleep(1)
        exit() #when space bar is pressed the program ends
    else:
        print('Starting...')
        sleep(1)
        return True

### Fuction to generate a random letter #####
def generate_letter():
    lett = chr(random.randint(ord('a'), ord('z')))
    return lett

### Fuction to generate a random letter #####
def key_press():
    s = generate_letter() 
    print('Type Letter ', colored((s), 'blue'))
    key = readkey()
    if key == s:
        print('You typed letter ', colored((key), 'green'))
    else:
        print('You typed letter ', colored((key), 'red'))
        
############## Time mode #####################
def Time_mode():
    pass
    
############# Max Value mode #################
def Max_value_mode():
    max_num=10
    for i in range(0, max_num):
        key_press()
    return True

############# Show the result #################
def Show_result(result_dict):
    pprint(result_dict)

################## main #######################
def main():
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm', '--use_time_mode', type = int, required = True, help='Max number of secs for time mode or maximum number os inputs for number of inputs mode.')
    parser.add_argument('-mv MAX_VALUE', '--max_value MAX_VALUE',type = int, required = True, help='Max number of seconds for time mode or maximum number os inputs for number inputs mode.')
   # args = parser.parse_args()

    result_dict = {
        'inputs': [],
        'number_of_hits': 0,
        'number_of_types': 0,
        'type_average_duration': 0,
        'type_hit_average_duration': 0,
        'type_miss_average_duration': 0}

    if start_test():
        Max_value_mode()

if __name__ == '__main__':
    main() 