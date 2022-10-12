#!/usr/bin/env python3

################## Library ###################
import argparse
from ast import If
from collections import namedtuple
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

### Fuction to generate a random letter and read the press key####
def key_press(result):
        
    rand_letter=random.choice(string.ascii_lowercase)
    print('Type Letter ', colored((rand_letter), 'blue'))

    start_time = time.time()

    key = readkey()

    end_time = time.time()
    duration = end_time - start_time

    press_result=Input(rand_letter, key, duration)
    result['inputs'].append(press_result)

    result['number_of_hits'] +=1

    if key == rand_letter:
        print('You typed letter ', colored((key), 'green'))
        result['number_of_types'] += 1
    else:
        print('You typed letter ', colored((key), 'red'))
    
    return result

############## Time mode #####################
def timeMode(result_dict):
    t = 10
    if result_dict['test_start']-time.time() != t:
        key_press(result_dict)
    return result_dict

############# Max Value mode #################
def Max_value_mode(result_dict):
    print(result_dict['test_start'])
    max_num=10
    for i in range(max_num):
        key_press(result_dict)
    return result_dict

################## main #######################
def main():
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm', '--use_time_mode', action = 'store_true', help = 'Max number of secs for time mode or maximum number os inputs for number of inputs mode.')
    parser.add_argument('-mv MAX_VALUE', '--max_value MAX_VALUE',type = int, required = True, help='Max number of seconds for time mode or maximum number os inputs for number inputs mode.')
    #args = parser.parse_args()

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
        
        #if arg['use_time_mode']:
        #    print('Test Mode: Time mode ' + str(args['max_number]) + 'seconds)
        #     result_dict=timeMode(args['max_number'], result_dict) 
        #else:
         #    print('Test Mode: Time mode ' + str(args['max_number]) + 'seconds)
         #    result_dict=Max_value_mode(args['max_number'], result_dict) 

        timeMode(result_dict)
        #Max_value_mode(result_dict)

        result_dict['test_end'] = ctime()
        result_dict['test_duration'] = time.time() - init_time 

        print(colored(('\nThe test was finished\n'), 'blue'))
        print('The result:')
        pprint(result_dict)

if __name__ == '__main__':
    main() 