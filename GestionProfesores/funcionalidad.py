import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized
from selenium.webdriver.support.ui import Select
import os
import random
import string
from time import sleep

def generate_unique_email(first_name, last_name):
    # Convert names to lowercase and remove spaces
    first = first_name.lower().replace(" ", "")
    last = last_name.lower().replace(" ", "")
    
    # Generate a random string of 3 digits
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    # Generate a random string of 2 letters
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
    
    # Combine everything to create a unique email
    email = f"{first}.{last}{random_digits}{random_letters}@gmail.com"
    
    return email
#Pruebas Funcionales Dinámicas:
class GestionProfesores(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")
    
    def test_login(self):
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

        button = self.driver.find_element(By.XPATH, "//a[@href='/professors/register' and @class='professors_actions__register']")
        button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors/register", self.driver.current_url)
        
        users = [
            ("Emma", "Rodriguez"),
            ("Liam", "Chang"),
            ("Sophia", "Patel"),
            ("Noah", "Kim"),
            ("Olivia", "Singh")
        ]


        first_name, last_name = random.choice(users)

        email = generate_unique_email(first_name, last_name)

        # selecionar campus
        select_element = self.driver.find_element(By.ID, "campus")
        select = Select(select_element)
        select.select_by_index(1)
        selected_option = select.first_selected_option
        print(f"Selected campus: {selected_option.text}")

        # Ingresar datos del profesor        
        name = self.driver.find_element(By.ID, "name")
        name.clear()
        name.send_keys(first_name)

        lastname = self.driver.find_element(By.ID, "lastname")
        lastname.clear()
        lastname.send_keys(last_name)

        email_field = self.driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(email)

        office_phone = ''.join(random.choices(string.digits, k=8))
        mobile_phone = ''.join(random.choices(string.digits, k=8))

        officephone = self.driver.find_element(By.ID, "office-phone")
        officephone.clear()
        officephone.send_keys(office_phone)

        phone = self.driver.find_element(By.ID, "phone")
        phone.clear()
        phone.send_keys(mobile_phone)

        # ingresar img
        img = self.driver.find_element(By.ID, "imagen")
        project_root = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(project_root, 'daniel.jpg')
        img.send_keys(file_path)

        #registar
        button = self.driver.find_element(By.XPATH, "//input[@class='create-student__form__submit' and @type='submit' and @value='Registrar']")
        button.click()

        print(f"Registered user: {first_name} {last_name} with email {email}")
        
        self.assertIn("https://fonmala.nyc.dom.my.id/professors", self.driver.current_url)


    

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
