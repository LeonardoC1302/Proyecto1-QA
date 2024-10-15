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

    def test_01__comment_activity(self):
        # Navegacion a inicion de sesion
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        #Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")

        username_field.send_keys("ecerdas@itcr.ac.cr")
        password_field.send_keys("admin")

        #Check de login 
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        #Navegacion a gestion de planes
        plans_button = self.driver.find_element(By.LINK_TEXT, "Planes")
        plans_button.click()

        #Vemos el plan
        plan_button = self.driver.find_element(By.CLASS_NAME, "table__action--edit")
        plan_button.click()

        #Vemos la actividad
        view_activity_button = self.driver.find_element(By.CLASS_NAME, "activityCard__view")
        view_activity_button.click()

        #Comentamos actividad
        comment_button = self.driver.find_element(By.CLASS_NAME, "activity__main__comment")
        comment_button.click()

        #Introducir comentario
        comment_field = self.driver.find_element(By.NAME, "contenido")
        comment_field.send_keys("Comentario de prueba")

        #Guardar comentario
        submit_button = self.driver.find_element(By.CLASS_NAME, "comment-form__submit")
        submit_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plans/plan/activity", self.driver.current_url)

    def test_02_comment_comment(self):
        # Navegacion a inicion de sesion
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        #Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")

        username_field.send_keys("ecerdas@itcr.ac.cr")
        password_field.send_keys("admin")

        #Check de login 
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        #Navegacion a gestion de planes
        plans_button = self.driver.find_element(By.LINK_TEXT, "Planes")
        plans_button.click()

        #Vemos el plan
        plan_button = self.driver.find_element(By.CLASS_NAME, "table__action--edit")
        plan_button.click()

        #Vemos la actividad
        view_activity_button = self.driver.find_element(By.CLASS_NAME, "activityCard__view")
        view_activity_button.click()

        #Comentamos el comentario
        comment_button = self.driver.find_element(By.CLASS_NAME, "comment__comment")
        comment_button.click()

        #Introducir comentario
        comment_field = self.driver.find_element(By.NAME, "contenido")
        comment_field.send_keys("Respuesta de prueba")

        #Guardar comentario
        submit_button = self.driver.find_element(By.CLASS_NAME, "comment-form__submit")
        submit_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plans/plan/activity", self.driver.current_url)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
