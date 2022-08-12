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


    # este metodo se encargara de acceder a los elementos para hacer la prueba del login fallando...
    def login_fail(self,username,password): # metodo para hacer prueba de fallo con el login

        self.driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(username) # USERNAME FIELD
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password) # PASSWORD FIELD
        self.driver.find_element(By.XPATH,"//*[@id='login-button']").click() # CLICKLOGIN
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button"))) # ESPERANDO EL MENSAJE DE LOGINERROR

        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/fail_login.png') #SC FAIL LOGIN

    # este metodo se encargara de acceder a los elementos para hacer la prueba del login exitosa...
    def log_succes(self,username,password): # metodo para hacer prueba del login correctamente

        self.driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(username) #USERNAME
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password) #PASSWORD
        self.driver.find_element(By.XPATH,"//*[@id='login-button']").click() #CLICK LOGIN


        time.sleep(3)

        # screenshot cuando es exitoso
        self.driver.save_screenshot('C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/Login_succes.png') #SC LOGIN SUCCES

    # este metodo se encargara de acceder a los elementos para hacer la prueba del checkout fallida...
    def checkout_fail(self, username,password):  # metodo para hacer prueba del login correctamente

        #logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        #esperando que cargue los prodcutos
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']")))
        #agregando producto a carrito
        self.driver.find_element(By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']").click()

        #dando click al carrito
        self.driver.find_element(By.ID, "shopping_cart_container").click()  # CLICK LOGOUT

        #dandole click al checkout
        self.driver.find_element(By.XPATH, "// *[ @ id = 'checkout']").click()

        #dandole click a continue
        self.driver.find_element(By.ID, "continue").click()

        #esperando el error
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'checkout_info_container'] / div / form / div[1] / div[4] / h3 / button")))
        #tirando sc cuando falla
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/checkout_fail.png')

    # este metodo se encargara de acceder a los elementos para hacer la prueba del checkout exitosa...
    def checkout_succes(self, username,password,first,last,zip):  # metodo para hacer prueba del login correctamente

        #logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        #esperando que cargue los prodcutos
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']")))
        #agregando producto a carrito
        self.driver.find_element(By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']").click()

        #dando click al carrito
        self.driver.find_element(By.ID, "shopping_cart_container").click()  # CLICK LOGOUT

        #dandole click al checkout
        self.driver.find_element(By.XPATH, "// *[ @ id = 'checkout']").click()

        #llenando formulario
        self.driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys(first)  # firtsname
        self.driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys(last)  # lastname
        self.driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys(zip)  # zip


        #dandole click a continue
        self.driver.find_element(By.ID, "continue").click()

        #dandole click a finish
        self.driver.find_element(By.ID, "finish").click()


        #esperando que muestre el mensaje exitoso
        self.wait.until(EC.presence_of_element_located((By.ID, "back-to-products")))

        #tirando sc cuando es exitoso
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/checkout_succes.png')

    # este metodo se encarga de probar que los productos cargan exitosamente....
    def products_succes(self,username,password):

        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        time.sleep(3)
        # tirando sc cuando es exitoso
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/products_succes.png')

    # este metodo se encarga de probar que los productos al cargar se muestran repetidas....
    def products_fail(self, username, password):
        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN
        time.sleep(3)
        # tirando sc cuando es fallido
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/products_fail.png')

    # este metodo se encarga de probar que el usuario no esta bloqueado
    def user_notblock(self,username,password):

        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        time.sleep(3)
        # tirando sc cuando es exitoso
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/usernotblock_succes.png')

    # este metodo se encarga de probar que el usuario esta bloqueado
    def user_block(self, username, password):
        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        time.sleep(3)
        # tirando sc cuando es exitoso
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/userblock_succes.png')

    # este metodo se encarga de probar que los productos al agregar son removidos correctamente.
    def remove_succes(self,username,password):

        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        # esperando que cargue los prodcutos
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']")))

        # agregando producto a carrito
        self.driver.find_element(By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']").click()

        # tirando sc cuando es exitoso agregar el producto
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/add_product_succes.png')

        #remove products
        self.driver.find_element(By.XPATH, "// *[ @ id = 'remove-sauce-labs-backpack']").click()

        # tirando sc cuando es fallido remover productos
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/remover_product_succes.png')

        # este metodo se encarga de probar que los productos al agregar no pueden ser removidos.

    # este metodo se encarga de probar que los productos al agregar no pueden ser removidos
    def remove_fail(self,username,password):

        # logeando
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)  # USERNAME
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)  # PASSWORD
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()  # CLICK LOGIN

        # esperando que cargue los prodcutos
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']")))

        # agregando producto a carrito
        self.driver.find_element(By.XPATH, "// *[ @ id = 'add-to-cart-sauce-labs-backpack']").click()

        # tirando sc cuando es exitoso agregar el producto
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/add_product_succes.png')

        #remove products
        self.driver.find_element(By.XPATH, "// *[ @ id = 'remove-sauce-labs-backpack']").click()

        # tirando sc cuando es fallido remover productos
        self.driver.save_screenshot(
            'C:/Users/zomal/PycharmProjects/pyTestSwagLabs/results/remover_product_fail.png')



