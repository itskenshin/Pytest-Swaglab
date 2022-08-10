import time

from selenium.webdriver.support import expected_conditions as EC
from MainStuff.base import Base

from selenium.webdriver.common.by import By
class Mainpage(Base):
    # metodo constructor cuando creamos objeto de esta clase va inicializar con los siguiente atri
    def __init__(self,driver,wait):
        self.url = 'https://www.saucedemo.com/' # url de la pagina

        super().__init__(driver, wait) # llamando el metodo init de la clase padre

    def ir_pagina_busc(self):
        self.ir_pagina(self.url) # aqui estoy iendo a la pagina que le pasamos


    def chek_url(self,url):
        assert self.give_url() == url # si la url que le pasamos es igual a la url true si no tira error..


    def login_fail(self,username,password): # metodo para hacer prueba de fallo con el login

        self.driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(username) # USERNAME FIELD
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password) # PASSWORD FIELD
        self.driver.find_element(By.XPATH,"//*[@id='login-button']").click() # CLICKLOGIN
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button"))) # ESPERANDO EL MENSAJE DE LOGINERROR

        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/fail_login.png') #SC FAIL LOGIN


    def log_succes(self,username,password): # metodo para hacer prueba del login correctamente
        #TIRANDO SC A LA PAGINA PRINCIPAL
        self.driver.save_screenshot('resultados/main_page.png')

        self.driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(username) #USERNAME
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password) #PASSWORD
        self.driver.find_element(By.XPATH,"//*[@id='login-button']").click() #CLICK LOGIN

        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/Login_succes.png') #SC LOGIN SUCCES

        self.driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']").click()  # CLICK ICON MENU
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/MENU_ICCON.png')  # SC menuicon

        self.wait.until(EC.presence_of_element_located((By.ID,"logout_sidebar_link" ))) # ESPERANDO EL LOGOUT BUTTOM

        self.driver.find_element(By.ID,"logout_sidebar_link").click()  # CLICK LOGOUT

        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/logout_succes.png')  # SC logout


