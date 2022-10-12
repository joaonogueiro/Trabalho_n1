#!/usr/bin/env python3

################## Library ###################
import argparse
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

######### Fuction that stops the test when space is pressed  ##########
def stop_test(key, result):
    K = ord(key) #K -> character pressed to initialize the test
    if K == 32:  #32 -> space bar in ascii
        K = ('Space bar')
        print(colored('\n   Interrupted Test\n', 'red'))
        result['test_end'] = ctime()
        pprint(result)
        exit()
    else:
        return True

######### Fuction to start the test ##########
def start_test():

    print('Press any key to start the test')
    print(colored(('    Press space to finish'), 'red'))

    K = (ord(readkey())) #K -> character pressed to initialize the test

    if K == 32:  #32 -> space bar in ascii
        K = ('Space bar')
        print('Terminating the test...')
        sleep(1)
        exit()
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

    while stop_test(key, result):
        
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
def timeMode(t, result_dict):
    init_time = time.time()
    while result_dict['test_duration'] < t:
        key_press(result_dict)
        result_dict['test_duration'] = time.time() - init_time
        print(result_dict['test_duration'])
    return result_dict

############# Max Value mode #################
def Max_value_mode(max_num, result_dict):
    init_time = time.time()  
    for i in range(max_num):
        key_press(result_dict)
        result_dict['test_duration'] = time.time() - init_time
    return result_dict

################## main #######################
def main():
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm', '--use_time_mode', action = 'store_true', help = 'Max number of secs for time mode or maximum number os inputs for number of inputs mode.')
    parser.add_argument('-mv', '--max_value',type = int, required = True, help='Max number of seconds for time mode or maximum number os inputs for number inputs mode.')
    args = vars(parser.parse_args())

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
    
    if args['use_time_mode']:
        print('Test Mode: Time mode - ' + str(args['max_value']) + 'seconds')
        start_test() 
        result_dict['test_start'] = ctime()
        result_dict = timeMode(args['max_value'], result_dict)
    else:
        print('Time mode: Off. Test Mode: Max Value - ' + str(args['max_value']) + ' responses')
        start_test()
        result_dict['test_start'] = ctime()
        result_dict = Max_value_mode(args['max_value'], result_dict)
       
    result_dict['test_end'] = ctime() 

    print(colored(('\nThe test was finished\n'), 'blue'))
    print('The result:')
    pprint(result_dict)

if __name__ == '__main__':
    main() 