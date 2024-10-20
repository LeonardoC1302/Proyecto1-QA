from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class TestPlan(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_01__create_plan(self):
        start = time.time()
        # Navegacion a inicion de sesion
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        #Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")

        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        #Check de login 
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        #Navegacion a gestion de planes
        plans_button = self.driver.find_element(By.LINK_TEXT, "Planes")
        plans_button.click()

        #Creacion de plan
        create_button = self.driver.find_element(By.CLASS_NAME, "plans__actions__create")
        create_button.click()

        #Introducir datos del plan
        name_field = self.driver.find_element(By.NAME, "nombre")
        description_field = self.driver.find_element(By.NAME, "descripcion")

        name_field.send_keys("Plan de Prueba ", time.strftime("%Y-%m-%d %H:%M:%S"))
        description_field.send_keys("Plan de prueba para testeo")

        #Guardar plan
        submit_button = self.driver.find_element(By.CLASS_NAME, "create-plan__form__submit")
        submit_button.click()
        
        self.assertIn("https://fonmala.nyc.dom.my.id/plans", self.driver.current_url)
        end = time.time()
        print("Tiempo de ejecucion - create_plan: ", end - start)

    def test_02__delete_plan(self):
        start = time.time()
        # Navegacion a inicion de sesion
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        #Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")

        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        #Check de login 
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        #Navegacion a gestion de planes
        plans_button = self.driver.find_element(By.LINK_TEXT, "Planes")
        plans_button.click()

        #Borrar plan
        delete_button = self.driver.find_element(By.CLASS_NAME, "table__action--delete")
        delete_button.click()

        end = time.time()
        print("Tiempo de ejecucion - delete_plan: ", end - start)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
