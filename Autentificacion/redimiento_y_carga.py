import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized
from threading import Thread


# Prueba de Rendimiento y Carga
class PruebaCargaLogin(unittest.TestCase):

    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    @parameterized.expand([
        ("admin@admin.com", "admin"),
        ("user1@example.com", "password1"),
        ("user2@example.com", "password2"),
        # Puedes añadir más combinaciones de email y password aquí
    ])
    def test_login(self, email, password):
        try:
            # Ingresar a la página de login
            login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
            login_button.click()
            self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

            # Ingresar credenciales
            email_field = self.driver.find_element(By.ID, "email")
            email_field.send_keys(email)

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(password)

            # Presionar el botón de login
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".form__submit")
            login_button.click()

            # Verificar si el login fue exitoso
            self.assertIn("https://fonmala.nyc.dom.my.id", self.driver.current_url)

        finally:
            # No cerrar el navegador aquí
            pass

    # Función para ejecutar múltiples hilos
    def ejecutar_prueba(self):
        threads = []
        # Lista de diferentes credenciales para cada hilo (puedes ajustarla)
        credenciales = [
            ("admin@admin.com", "admin"),
            ("user1@example.com", "password1"),
            ("user2@example.com", "password2"),
            ("admin@admin.com", "admin"),
            ("user1@example.com", "password1"),
            ("user2@example.com", "password2")
        ]
        
        for email, password in credenciales:
            t = Thread(target=self.test_login, args=(email, password))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

    def tearDown(self):
        # Cerrar el navegador al final de todas las pruebas
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

