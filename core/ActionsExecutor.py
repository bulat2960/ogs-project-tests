import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import helpers.utils as utils

class ActionsExecutor:
    def __init__(self, action: ActionChains, width, height):
        self.is_stopped = True
        self.action = action
        self.width = width
        self.height = height

    def start(self):
        if not self.is_stopped:
            return
        
        self.is_stopped = False
    
    def stop(self):
        self.is_stopped = True

    def is_stopped(self):
        return self.is_stopped
    
    def get_functions(self): 
        return [self.click,
                self.multiclick,
                self.spacebar_pressing,
                self.esc_pressing,
                self.arrow_up_pressing,
                self.arrow_down_pressing]

    def click(self):
        while not self.is_stopped:
            x = utils.get_random_number(0, self.width - 1)
            y = utils.get_random_number(0, self.height - 1)

            self.action.move_by_offset(x, y).click().move_by_offset(-x, -y).perform()

            utils.sleep_for(1)
        
    def multiclick(self): 
        while not self.is_stopped:
            array_length = 5

            x = utils.get_random_numbers_array(0, 100, array_length)
            y = utils.get_random_numbers_array(0, 100, array_length)

            for i in range(array_length): 
                self.action.move_by_offset(x[i], y[i]).click().move_by_offset(-x[i], -y[i])
            self.action.perform()

            utils.sleep_for(1)

    def spacebar_pressing(self):
        while not self.is_stopped:
            self.action.send_keys(Keys.SPACE).perform()
            utils.sleep_random_interval(0, 3)

    def esc_pressing(self):
        while not self.is_stopped:
            self.action.send_keys(Keys.ESCAPE).perform()
            utils.sleep_for(30)
            
    def arrow_up_pressing(self):
        while not self.is_stopped:
            self.action.send_keys(Keys.ARROW_UP).perform()
            utils.sleep_random_interval(0, 10)

    def arrow_down_pressing(self):
        while not self.is_stopped:
            self.action.send_keys(Keys.ARROW_DOWN).perform()
            utils.sleep_random_interval(0, 10)