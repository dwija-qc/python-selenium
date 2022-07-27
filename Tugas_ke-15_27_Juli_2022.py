import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class tugas(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #1 Register Sucess (Positive)
    def test_a_success_register(self): 
        # steps
        browser = self.browser 
        browser.get("https://myappventure.herokuapp.com/registration") 
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("dwi55") 
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("dwi55@gmail.com") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("dwi123") 
        time.sleep(1)
        browser.find_element(By.XPATH, '//button[text()="Daftar sekarang"]').click() 
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"p.mt-12.pb-3.max-w-md.font-semibold.text-center").text

        self.assertEquals(response_data,'Selamat! Akun anda berhasil dibuat')

    #2 Register Existing (Negative)
    def test_b_register_existing(self): 

        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration")
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("dwi50") 
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("dwi50@gmail.com")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("dwi123")
        time.sleep(1)
        browser.find_element(By.XPATH, '//button[text()="Daftar sekarang"]').click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"p.px-1.leading-5").text


        self.assertEquals(response_data,'Email atau username sudah terdaftar')

    #3 Register null password (Negative)
    def test_c_register_null_password(self): 

        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration")
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("dwi88") 
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("dwi88@gmail.com")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH, '//button[text()="Daftar sekarang"]').click() 
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"div.flex.items-center.justify-start.text-xs.text-white.font-light").text


        self.assertEquals(response_data,'diperlukan kata sandi')

    #4 Login Success (Positive)
    def test_d_login_success(self):
         
         # steps
         browser = self.browser
         browser.get("https://myappventure.herokuapp.com/login")
         time.sleep(3)
         browser.find_element(By.NAME,"email").send_keys("dwi50@gmail.com")
         time.sleep(1)
         browser.find_element(By.NAME,"password").send_keys("dwi123")
         time.sleep(1)
         browser.find_element(By.XPATH, '//button[text()="Masuk"]').click()
         time.sleep(8)

         response_data = browser.find_element(By.CSS_SELECTOR,"div.flex.justify-center.text-center.text-shadow-xl").text

         self.assertEqual(response_data,'Mulai Petualanganmu')

    
    #5 Login wrong email (Negative)
    def test_e_login_wrong_email(self):
         
         # steps
         browser = self.browser
         browser.get("https://myappventure.herokuapp.com/login")
         time.sleep(3)
         browser.find_element(By.NAME,"email").send_keys("dwi99@gmail.com")
         time.sleep(1)
         browser.find_element(By.NAME,"password").send_keys("dwi123")
         time.sleep(1)
         browser.find_element(By.XPATH, '//button[text()="Masuk"]').click()
         time.sleep(5)

         response_data = browser.find_element(By.CSS_SELECTOR,"p.px-1.leading-5").text

         self.assertIn('Alamat email atau kata sandi', response_data)

    #6 Login Wrong Password (Negative)
    def test_f_login_wrong_password(self):
         
         # steps
         browser = self.browser
         browser.get("https://myappventure.herokuapp.com/login")
         time.sleep(3)
         browser.find_element(By.NAME,"email").send_keys("dwi50@gmail.com")
         time.sleep(1)
         browser.find_element(By.NAME,"password").send_keys("dwi1231")
         time.sleep(1)
         browser.find_element(By.XPATH, '//button[text()="Masuk"]').click()
         time.sleep(5)

         response_data = browser.find_element(By.CSS_SELECTOR,"p.px-1.leading-5").text

         self.assertIn('Kata Sandi Salah', response_data)

    #7 Login Null Password (Negative)
    def test_g_login_pasword_null(self):
         
         # steps
         browser = self.browser
         browser.get("https://myappventure.herokuapp.com/login")
         time.sleep(3)
         browser.find_element(By.NAME,"email").send_keys("dwi50@gmail.com")
         time.sleep(1)
         browser.find_element(By.NAME,"password").send_keys("")
         time.sleep(1)
         browser.find_element(By.XPATH, '//button[text()="Masuk"]').click()
         time.sleep(5)

         response_data = browser.find_element(By.CSS_SELECTOR,"div.flex.items-center.justify-start.text-xs.text-white.font-light").text

         self.assertIn('diperlukan kata sandi', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()