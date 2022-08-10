class Base:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait


    def ir_pagina(self,url):
        self.driver.get(url)
        self.url = self


    def give_url(self):
        return self.driver.current_url
