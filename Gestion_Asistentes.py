from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time


class TestAsistente(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_01_register_assistant(self):
        # Mismo flujo de inicio de sesión
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
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
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)
        
        assistants_button = self.driver.find_element(By.LINK_TEXT, "Registrar Asistente")
        assistants_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias/register-asistente", self.driver.current_url)
        time.sleep(3)
        
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
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)

    def test_02_register_assistant_missing_email(self):
        # Mismo flujo de inicio de sesión
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
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
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)
        
        assistants_button = self.driver.find_element(By.LINK_TEXT, "Registrar Asistente")
        assistants_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias/register-asistente", self.driver.current_url)
        time.sleep(3)
        
        # Crear nuevo asistente con el campo de correo vacío
        first_name_field = self.driver.find_element(By.ID, "name")
        last_name_field = self.driver.find_element(By.ID, "lastname")
        phone_field = self.driver.find_element(By.ID, "phone")
        first_name_field.send_keys("Erika")
        last_name_field.send_keys("Cerdas")
        phone_field.send_keys("84780342")
        
        # Dejar el campo de email vacío
        email_field = self.driver.find_element(By.ID, "email")
        email_field.clear()

        # Intentar registrar asistente
        submit_button = self.driver.find_element(By.CLASS_NAME, "create-student__form__submit")
        submit_button.click()

        # Verificación de mensajes de error
        error_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert--error') and contains(text(), 'El correo es obligatorio')]")
        self.assertTrue(error_message.is_displayed())
        
        # Verificar que la URL no cambió debido al error
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias/register-asistente", self.driver.current_url)

    def test_03_asignar_asistente(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        assistants_button = self.driver.find_element(By.LINK_TEXT, "Equipo Guía")
        assistants_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)
        
        assistants_button = self.driver.find_element(By.LINK_TEXT, "Asignar Asistente Administrativo por Campus")
        assistants_button.click()
        # Verificación URL
        self.assertEqual("https://fonmala.nyc.dom.my.id/guias/asignar/asistente", self.driver.current_url)

        campus_button = self.driver.find_element(By.ID, "campus")
        campus_button.click()

        campus = self.driver.find_element(By.XPATH, "//option[@value='1']")
        campus.click()

        asistente_button = self.driver.find_element(By.ID, "asistente")
        asistente_button.click()

        asistente = self.driver.find_element(By.XPATH, "//option[text() = 'Erika Cerdas']")
        asistente.click()

        time.sleep(3)

        asignar_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        asignar_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
