
# !!! ATTENTION !!!
# !!! ATTENTION !!!
# !!! ATTENTION !!!
# !!! ATTENTION !!!
# !!! ATTENTION !!!

# This code is very bad, and i understand this.
# Please, do NOT USE this code.
# Thank You.


from lib2to3.pgen2 import driver
import os
import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime,date
import winsound
import calendar
import time
import pyautogui

def current_time() :
    now = datetime.now()
    return str(now.strftime("%H:%M:%S"))

def current_date() :
    today = date.today()
    return str(today.strftime("%Y-%m-%d"))

def normalize_links(links) :
    links = links.split(' ')
    return ' '.join(links).split()


def beep() :
    winsound.Beep(500, 1000)
    time.sleep(0.5)
    winsound.Beep(500, 1000)
    time.sleep(0.5)
    winsound.Beep(500, 1000)

def log(message) :
#    _log = open(os.path.realpath(os.path.dirname(__file__)) + '\\' + '_LOG.txt','a')
#    _log.write('[' + current_time() + '] ' + message)
#    _log.close()
    pass

save_path = os.path.realpath(os.path.dirname(__file__)) + '\\' + current_date()

if not os.path.exists(save_path) :
    os.mkdir(save_path)


class MainWindows(BaseWidget):

    def __init__(self):
        super(MainWindows,self).__init__('VK Auto Poster. v1.0')

        self._login  = ControlText('Лоігн')
        self._pass = ControlText('Пароль')
        self._comment   = ControlText('Коментар')
        self._links   = ControlText('Посилання')
        self._button     = ControlButton('Запустити коментування')

        self._button.value = self.__buttonAction

 
    def __buttonAction(self):

        #log('Логін: ' + self._login.value)        
        #log('Пароль: ' + self._pass.value)
        #log('Коментар: ' + self._comment.value)
        #log('Записи: ' + self._links.value)
        
        chrome_options = webdriver.ChromeOptions(); 
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        driver = webdriver.Chrome(options=chrome_options);  
        driver.maximize_window()
        driver.get("https://vk.com/")
        
        # На головній сторінці вводимо логін і натискаємо на кнопку входу
        while True :
            try :
                driver.find_element(By.CLASS_NAME, "VkIdForm__header")
                break 
            except :
                continue

        while True :
            try :
                login = driver.find_element(By.ID, "index_email")
                login.send_keys(str(self._login.value))
                login.send_keys(Keys.ENTER)
                break
            except :
                continue


        # Вводимо пароль та натискаємо на авторизацію
        while True :
            try :
                password = driver.find_element(By.NAME, "password")
                password.send_keys(str(self._pass.value))
                password.send_keys(Keys.ENTER)
                break
            except :
                continue    



        # Очікуємо авторизації сторінки
        while True :
            try :
                driver.find_element(By.ID, "post_field")
                post_link = str(self._links.value)
                post_link = post_link.replace("https://vk.com","https://m.vk.com")
                post_link = normalize_links(post_link)
                break
            except :  
                continue

        for ol in post_link :
        
            driver.get(ol)

            try :
                textfield = driver.find_element(By.ID, "reply_field_text")
            except :
                beep()
                print('Запис ' + ol + ' видалено')
                continue

            textfield.send_keys(str(self._comment.value))
            send_button = driver.find_element(By.ID, "nc_submit")
            send_button.click()

            time.sleep(3)

            #Перевірити чи акаунт заблокований
            try :
                textfield = driver.find_element(By.ID, "reply_field_text")
                check_text = textfield.get_attribute('value')

                if str(check_text) == str(self._comment.value) :
                    print("Акаунт заблокований!")
                    beep()
                    break
            except :
                pass

            #Перевірити чи є капча
            try :
                capcha = driver.find_element(By.CLASS_NAME, "captcha_form")
                print('Captcha!!')
                beep()
                time.sleep(60)
            except :
                pass 

             

            #like_reaction = driver.find_element(By.CLASS_NAME, "ReactionImage__animationContainer")
            #like_reaction.click()

            current_GMT = time.gmtime()
            ts = calendar.timegm(current_GMT)
            screenshot = pyautogui.screenshot(save_path + '\image'+str(ts)+'.png')

            time.sleep(1)

        driver.close()

       

#Execute the application
if __name__ == "__main__": pyforms.start_app( MainWindows )
