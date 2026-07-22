from testit_python_commons.step import step

from locators import OrganizationsAdminPageLocators, CreateOrganizationAdminPageLocators
from pages.admin_pages.base_page import AdminBasePage
from tools.faker import Fake, fake


class OrganizationsAdminPage(AdminBasePage):

    @step("Клик по кнопке 'Создать'")
    def _start_creation_organization(self):
        self.custom_click(selector=OrganizationsAdminPageLocators.CREATE_ORGANIZATIONS_BTN)


    def _fill_and_submit_form_create_organization(self):
        self.page.fill(CreateOrganizationAdminPageLocators.NAME, value=fake.random_name())

    def create_organization(self):
