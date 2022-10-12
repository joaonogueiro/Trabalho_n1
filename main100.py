#!/usr/bin/env python3

################## Library ###################
import argparse
from collections import namedtuple
from inspect import ArgSpec
import random
import string
from tracemalloc import start
from readchar import readkey
from termcolor import colored
from time import sleep, time, ctime
import time
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
        print('\nStarting...\n')
        sleep(1)
        return True

### Fuction to generate a random letter #####
def generate_letter():
    letter=random.choice(string.ascii_lowercase)
    return letter

### Fuction to generate a random letter #####
def key_press(result):
    s = generate_letter() 
    print('Type Letter ', colored((s), 'blue'))
    start_time = time.time()
    key = readkey()
    end_time = time.time()
    press_time = end_time - start_time
    result['inputs'].append(key)
    if key == s:
        print('You typed letter ', colored((key), 'green'))
    else:
        print('You typed letter ', colored((key), 'red'))
    print('The duration was: ' + str(press_time))   
    return result

############## Time mode #####################
def Time_mode():
    pass
    
############# Max Value mode #################
def Max_value_mode(result_dict):
    max_num=10
    for i in range(max_num):
        key_press(result_dict)
    return result_dict

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
        'test_duration': 0,
        'test_end': 0,
        'test_start': 0,
        'type_average_duration': 0,
        'type_hit_average_duration': 0,
        'type_miss_average_duration': 0}

    if start_test():

        result_dict['test_start'] = ctime()
        init_time = time.time()                 #seconds passed since 01/01/1970
        
        Max_value_mode(result_dict)

        result_dict['test_end'] = ctime()
        result_dict['test_duration'] = time.time() - init_time 

        print(colored(('\nThe test was finished\n'), 'blue'))
        print('The result:')
        pprint(result_dict)

if __name__ == '__main__':
    main() 