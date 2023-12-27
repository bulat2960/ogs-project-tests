import time
import random

def sleep_for(seconds):
    time.sleep(seconds)

def sleep_random_interval(min, max):
    time.sleep(random.randint(min, max)) 

def get_random_number(min, max):
    return random.randint(min, max)

def get_random_numbers_array(min, max, size):
    return [get_random_number(min, max) for i in range(size)]