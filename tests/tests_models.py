import webbrowser
import selenium

from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver

from homePage.models import Employer


class ModelTestCase(TestCase):
    def test_employer_creation(self):
        employer = Employer.objects.create(name="UnitTestName UnitTestName UnitTestName", e_mail="UnitTestE-Mail",
                                           organization="UnitTestOrganization")
        employer.save()
        self.assertEquals(employer.name, "UnitTestName UnitTestName UnitTestName")

    def test_create_employer_in_real_db(self):
        employer = Employer.objects.create(name="UnitTestName2 UnitTestName2 UnitTestName2", e_mail="UnitTestE-Mail2",
                                           organization="UnitTestOrganization2")


browser = webdriver.Edge()
browser.get("http://127.0.0.1:8000/admin/homePage/employer/")
browser.find_element("By.class", "addlink").click()
