import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class GestionProfesores(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")
    
    def test_login(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Ingresar a la página de login
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

        # Ingresar credenciales
        email = self.driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys("admin@admin.com")

        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("admin")

        # Presiona el botón de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".form__submit")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id", self.driver.current_url)

        # Acceder a la pagina de profesores
        login_button = self.driver.find_element(By.LINK_TEXT, "Profesores")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors", self.driver.current_url)



        self.driver.find_element(By.XPATH, "//a[@href='/professors/coordinator' and @class='professors_actions__coordinator']").click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors/coordinator", self.driver.current_url)

        button = self.driver.find_element(By.CLASS_NAME, 'coordinator__form__label--radio')
        button.click()

        sleep(2)

        coordinador_button = self.driver.find_element(By.XPATH, '//label[.//input[@type="radio" and @class="coordinator__form__radio" and @value="12"]]')
        coordinador_button.click()

        submit_button = self.driver.find_element(By.CLASS_NAME, 'coordinator__form__submit')
        submit_button.click()



        self.assertIn("https://fonmala.nyc.dom.my.id/professors", self.driver.current_url)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
