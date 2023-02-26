import unittest
#from pyunitreport import HTMLTestRunner
from selenium import webdriver

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self = webdriver.Chrome(executable_path=r'D://Curso Selenium Platzi/chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)
    
       
    def test_search_test_field(self):
        search_field = self.driver.find_element_by_id("search")
        
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
        
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
        
        
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))
        
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')
    
    def tearDown(self):
           self.driver.quit()
          

if __name__=="__main__":
    unittest.main(verbosity=2)