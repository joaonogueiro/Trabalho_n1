#!/usr/bin/env python3

################## Library ###################
import argparse
from ast import If
from collections import namedtuple
import random
import string
from readchar import readkey
from termcolor import colored
from time import sleep, time, ctime
import time
from pprint import pprint

##############################################

###### Variable input from type tuble ########
Input = namedtuple('Input', ['requested', 'received', 'duration'])  # complex = namedtuble('complex', ['r','i'])


######### Fuction to start the test ##########
def start_test():
    print('Press any key to start the test')
    print(colored(('    Press space to finish'), 'red'))

    K = (ord(readkey()))  # K -> character pressed to initialize the test

    if K == 32:  # 32 -> space bar in ascii
        K = ('Space bar')
        print('Terminating the test...')
        sleep(1)
        exit()  # when space bar is pressed the program ends
    else:
        print('\nStarting...\n')
        sleep(1)
        return True


### Fuction to generate a random letter and read the press key####
def key_press(result):
    rand_letter = random.choice(string.ascii_lowercase)
    print('Type Letter ', colored((rand_letter), 'blue'))

    start_time = time.time()

    key = readkey()

    end_time = time.time()
    duration = end_time - start_time

    if key == ' ':  # 32 -> space bar in ascii
        print('Terminating the test...')
        sleep(1)
        pretty_print(result)
        exit()

    if key == rand_letter:
        print('You typed letter ', colored((key), 'green'))
        result['number_of_hits'] += 1
    else:
        print('You typed letter ', colored((key), 'red'))

    press_result = Input(rand_letter, key, duration)

    result['inputs'].append(press_result)

    result['number_of_types'] += 1

    result['test_duration'] += duration

    return result

############## Time mode #####################
def timeMode(t, result_dict):
    while result_dict['test_duration'] < t:
        key_press(result_dict)
    return result_dict


############# Max Value mode #################
def Max_value_mode(max_num, result_dict):
    for i in range(max_num):
        key_press(result_dict)
    return result_dict

def pretty_print(result):
    result['test_end'] = ctime()

    result['type_average_duration'] = (result['test_duration'])/(result['number_of_types'])
    
    if result['number_of_types']==0:
        result['type_miss_average_duration'] = 99999999999999
    else:
        result['type_miss_average_duration'] = (result['test_duration'])/(result['number_of_hits'])

    if result['number_of_hits'] == 0:
        result['type_hit_average_duration'] = 99999999999999
    else:
        result['type_hit_average_duration'] = (result['test_duration'])/(result['number_of_hits'])

    result['type_miss_average_duration'] = (result['test_duration'])/((result['number_of_types'])-(result['number_of_hits']))

    print(colored(('\nThe test was finished\n'), 'blue'))
    print('The result:')
    pprint(result)

################## main #######################
def main():
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm', '--use_time_mode', action='store_true',
                        help='Max number of secs for time mode or maximum number os inputs for number of inputs mode.')
    parser.add_argument('-mv', '--max_value', type=int, required=True,
                        help='Max number of seconds for time mode or maximum number os inputs for number inputs mode.')
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
        init_time = time.time()
        result_dict = timeMode(args['max_value'], result_dict)
    else:
        print('Test Mode: Max Value - ' + str(args['max_value']) + ' responses')
        start_test()
        result_dict['test_start'] = ctime()
        init_time = time.time()
        result_dict = Max_value_mode(args['max_value'], result_dict)

    pretty_print(result_dict)

if __name__ == '__main__':
    main()