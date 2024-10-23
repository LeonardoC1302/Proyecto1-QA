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

    def test_01__create_activity(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
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

        #Vemos el plan
        plan_button = self.driver.find_element(By.CLASS_NAME, "table__action--edit")
        plan_button.click()

        #Creamos actividad
        add_activity_button = self.driver.find_element(By.CLASS_NAME, "plan__add")
        add_activity_button.click()

        #Introducir datos de la actividad
        name_field = self.driver.find_element(By.NAME, "nombre")
        type_field = self.driver.find_element(By.NAME, "tipoId")
        modality_field = self.driver.find_element(By.NAME, "modalidad")
        realization_field = self.driver.find_element(By.NAME, "fecha")
        publication_field = self.driver.find_element(By.NAME, "fechaPublicacion")
        responsible_field = self.driver.find_element(By.NAME, "responsableId")
        description_field = self.driver.find_element(By.NAME, "descripcion")
        poster_field = self.driver.find_element(By.NAME, "afiche")

        name_field.send_keys("Actividad de Prueba ", time.strftime("%Y-%m-%d %H:%M:%S"))
        select_type = Select(type_field)
        select_type.select_by_index(1)
        modality_select = Select(modality_field)
        modality_select.select_by_index(1)
        # Publication date is tomorrow and realization date is the day after (mm/dd/yyyy)
        tomorrow = time.strftime("%m/%d/%Y", time.localtime(time.time() + 86400))
        after_tomorrow = time.strftime("%m/%d/%Y", time.localtime(time.time() + 172800))
        realization_field.send_keys(after_tomorrow)
        publication_field.send_keys(tomorrow)
        select_responsible = Select(responsible_field)
        select_responsible.select_by_index(1)
        description_field.send_keys("Actividad de prueba para testeo")

        # Subir afiche
        project_root = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(project_root, 'afiche.pdf')
        poster_field.send_keys(file_path)

        #Guardar actividad
        register_button = self.driver.find_element(By.CLASS_NAME, "add-activity__form__submit")
        register_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plan", self.driver.current_url)
        end = time.time()
        print("Tiempo de ejecucion - create_activity: ", end - start)

    def test_02__edit_activity(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
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

        #Vemos el plan
        plan_button = self.driver.find_element(By.CLASS_NAME, "table__action--edit")
        plan_button.click()

        #Vemos la actividad
        view_activity_button = self.driver.find_element(By.CLASS_NAME, "activityCard__view")
        view_activity_button.click()

        #Editamos actividad
        edit_activity_button = self.driver.find_element(By.CLASS_NAME, "activity__info__edit")
        edit_activity_button.click()

        #Modificamos el nombre de la actividad
        name_field = self.driver.find_element(By.NAME, "nombre")
        name_field.clear()
        name_field.send_keys("Actividad de Prueba [EDITADA]")

        #Guardar actividad
        register_button = self.driver.find_element(By.CLASS_NAME, "add-activity__form__submit")
        register_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plans/plan/activity", self.driver.current_url)
        end = time.time()
        print("Tiempo de ejecucion - edit_activity: ", end - start)

    def test_03_cancel_activity(self):
        start = time.time()
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
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

        #Vemos el plan
        plan_button = self.driver.find_element(By.CLASS_NAME, "table__action--edit")
        plan_button.click()

        #Vemos la actividad
        view_activity_button = self.driver.find_element(By.CLASS_NAME, "activityCard__view")
        view_activity_button.click()

        #Editamos actividad
        edit_activity_button = self.driver.find_element(By.CLASS_NAME, "activity__info__edit")
        edit_activity_button.click()

        #Cancelamos actividad
        status_field = self.driver.find_element(By.NAME, "estadoId")
        select_status = Select(status_field)
        select_status.select_by_index(1)

        #Ponemos la justificacion
        justification_field = self.driver.find_element(By.NAME, "justificacion")
        justification_field.send_keys("Actividad cancelada por testeo")

        #Guardar actividad
        register_button = self.driver.find_element(By.CLASS_NAME, "add-activity__form__submit")
        register_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plans/plan/activity", self.driver.current_url)
        end = time.time()
        print("Tiempo de ejecucion - cancel_activity: ", end - start)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
