import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class helloword(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'D://Curso Selenium Platzi/chromedriver_win32/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')
        
    def test_visit_wikipedia(cls):
        cls.driver.get('https://www.wikipedia.org')
    
    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()
    

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output='reportes', report_name='hello-world-report'))