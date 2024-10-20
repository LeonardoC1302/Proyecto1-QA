from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
import os

class TestActividades(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_01_filter_student(self):
        # Navegación a inicio de sesión
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        # Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Iniciar sesión
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()


        # Navegación a Gestión de Estudiantes
        students_button = self.driver.find_element(By.LINK_TEXT, "Estudiantes")
        students_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/students", self.driver.current_url)

        # Filtrar estudiante por Apellido
        search_button = self.driver.find_element(By.ID, "apellidos")
        search_button.click()
        
        # Verificar que los estudiantes están ordenados por apellido
        student_last_names = self.driver.find_elements(By.XPATH, "//td[2]")  
        last_names = [el.text for el in student_last_names]
        time.sleep(2)

        # Verificar si la lista está ordenada por apellido
        self.assertEqual(last_names, sorted(last_names), "Los estudiantes no están ordenados por apellido correctamente")
    
    def test_02_filter_student(self):
        # Navegación a inicio de sesión
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        # Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Iniciar sesión
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()


        # Navegación a Gestión de Estudiantes
        students_button = self.driver.find_element(By.LINK_TEXT, "Estudiantes")
        students_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/students", self.driver.current_url)

        # Filtrar estudiante por Carnet
        search_button = self.driver.find_element(By.ID, "carnet")
        search_button.click()
        
        # Verificar que los estudiantes están ordenados por carnet
        student_carnet = self.driver.find_elements(By.XPATH, "//td[3]")  
        carnets = [el.text for el in student_carnet]
        time.sleep(2)

        # Verificar si la lista está ordenada por apellido
        self.assertEqual(carnets, sorted(carnets), "Los estudiantes no están ordenados por carnet correctamente")
            
        
    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()


