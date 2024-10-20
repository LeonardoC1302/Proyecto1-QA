from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
import os

class TestPlan(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_01_register_assistant(self):
        # Mismo flujo de inicio de sesión
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        # Navegación a Gestión de Asistentes
        assistants_button = self.driver.find_element(By.LINK_TEXT, "Equipo Guía")
        assistants_button.click()
        # Verificación URL
        self.assertIn("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)
        
        assistants_button = self.driver.find_element(By.LINK_TEXT, "Registrar Asistente")
        assistants_button.click()
        # Verificación URL
        self.assertIn("https://fonmala.nyc.dom.my.id/guias/register-asistente", self.driver.current_url)
        
        #Crear nuevo asistente
        #Completar formulario de asistente
        first_name_field = self.driver.find_element(By.ID, "name")
        last_name_field = self.driver.find_element(By.ID, "lastname")
        email_field = self.driver.find_element(By.ID, "email")
        phone_field = self.driver.find_element(By.ID, "phone")
        first_name_field.send_keys("Erika")
        last_name_field.send_keys("Cerdas")
        email_field.send_keys("ecerdasmejias04@gmail.com")
        phone_field.send_keys("84780342")

        # Registrar asistente
        submit_button = self.driver.find_element(By.CLASS_NAME, "create-student__form__submit")
        submit_button.click()

        # Verificación de la creación del asistente
        self.assertIn("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
