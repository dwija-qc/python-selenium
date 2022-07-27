import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class tugas(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("dwi31") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("dwi31@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("dwi123")   # isi password
        time.sleep(1)
        browser.find_element(By.XPATH, '//button[text()="Daftar sekarang"]').click() # klik tombol daftar
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"__next").text


        self.assertIn('Selamat', response_data)

    def test_a_login_success(self):
         
         # steps
         browser = self.browser
         browser.get("https://myappventure.herokuapp.com/login")
         time.sleep(3)
         browser.find_element(By.NAME,"email").send_keys("dwi31@gmail.com")
         time.sleep(1)
         browser.find_element(By.NAME,"password").send_keys("dwi123")
         time.sleep(1)
         browser.find_element(By.TAG_NAME,"button").click()

         browser.find_element(By.XPATH, '//button[text()="Masuk"]').click()
         time.sleep(1)

         response_data = browser.find_element(By.ID,"__next")

         self.assertIn('Anda', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()