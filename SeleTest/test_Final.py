import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from MainStuff.main_page import Mainpage

class TestSearh():

    @pytest.fixture
    def Test_inicialP(self):

        #******************* configuraciones de selenium *******************

        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")


        option.add_experimental_option("detach", True) # chrome to stay open

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.wait = WebDriverWait(self.driver,10)

        # ****************************************************************************************************

        self.page = Mainpage(self.driver,self.wait)
        self.page.ir_pagina_busc()

    #################### TESTS ######################

    ###### puebas url ##############################

    def test_url(self,Test_inicialP):
        self.page.chek_url("https://youtube.com")

    #################### Login tests ########################

    def test_login_fail(self,Test_inicialP):
        self.page.login_fail('asdasdasd','asdasdasdasd')

    def test_login_succes(self,Test_inicialP):
        self.page.log_succes('standard_user','secret_sauce')

    ###################### checkout products tests ###########

    def test_checkout_fail(self,Test_inicialP):
        self.page.checkout_fail('standard_user','secret_sauce')

    def test_checkout_succes(self,Test_inicialP):
        self.page.checkout_succes('standard_user','secret_sauce','jonathan','montero','12345')

##################### products test###########################

    def test_product_succes(self,Test_inicialP):
        self.page.products_succes('standard_user','secret_sauce')

    def test_product_fail(self,Test_inicialP):
        self.page.products_fail('problem_user','secret_sauce')

################### block users tests #########################

    def test_user_not_block(self,Test_inicialP):
        self.page.user_notblock('standard_user','secret_sauce')

    def test_user_block(self,Test_inicialP):
        self.page.user_block('locked_out_user','secret_sauce')

########################remove producst tests#######################

    def test_remove_product_succes(self,Test_inicialP):
        self.page.remove_succes("standard_user","secret_sauce")

    def test_remove_product_fail(self,Test_inicialP):
        self.page.remove_fail("problem_user","secret_sauce")