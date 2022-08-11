import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from MainStuff.main_page import Mainpage

class TestSearh():
    @pytest.fixture
    def Test_inicialP(self):
        # options to add as arguments
        from selenium.webdriver.chrome.options import Options
        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")

        # chrome to stay open
        option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.wait = WebDriverWait(self.driver,10)




        self.page = Mainpage(self.driver,self.wait)
        self.page.ir_pagina_busc()

    def test_url(self,Test_inicialP):
        self.page.chek_url("https://youtube.com")

    def test_login_fail(self,Test_inicialP):
        self.page.login_fail('asdasdasd','asdasdasdasd')

    def test_login_succes(self,Test_inicialP):
        self.page.log_succes('standard_user','secret_sauce')

    def test_checkout_fail(self,Test_inicialP):
        self.page.checkout_fail('standard_user','secret_sauce')

    def test_checkout_succes(self,Test_inicialP):
        self.page.checkout_succes('standard_user','secret_sauce','jonathan','montero','12345')

    def test_product_succes(self,Test_inicialP):
        self.page.products_succes('standard_user','secret_sauce')

    def test_product_fail(self,Test_inicialP):
        self.page.products_fail('problem_user','secret_sauce')