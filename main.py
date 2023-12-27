from selenium import webdriver
from selenium.webdriver import ActionChains

from core.ActionsExecutor import ActionsExecutor
from core.ThreadPool import ThreadPool
from core.LoginForm import LoginForm

def authorize(get_link):
    link = get_link()
    driver.get(link)

def start():
    actions_executor.start()
    thread_pool.init_pool() 

def stop(): 
    actions_executor.stop()

driver = webdriver.Chrome()
driver.set_window_size(1500, 1000)

width = driver.execute_script("return window.innerWidth")
height = driver.execute_script("return window.innerHeight")

action = ActionChains(driver, 0)

actions_executor = ActionsExecutor(action, width, height)
functions = actions_executor.get_functions()

thread_pool = ThreadPool(functions)

login_form = LoginForm(authorize,
                       start,
                       stop)

login_form.run()

