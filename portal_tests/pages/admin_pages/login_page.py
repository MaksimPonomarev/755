from locators import LoginAdminPageLocators
from pages.admin_pages.base_page import AdminBasePage
from testit_python_commons.step import step


class AdminLoginPage(AdminBasePage):

    ENDPOINT = "/login"

    @step("Ввод кредов и нажатие кнопки 'Войти'")
    def fill_and_submit_admin_login_form(self):
        self.page.fill(LoginAdminPageLocators.ADMIN_LOGIN_INSERT_BTN, "admin@admin.com")
        self.page.fill(LoginAdminPageLocators.ADMIN_PASSWORD_INSERT_BTN, "admin@admin.com")
        self.custom_click(LoginAdminPageLocators.SUBMIT_BTN)

    @step("Открыть страницу и авторизоваться в админке")
    def open_and_register_admin_panel(self):
        self.open(endpoint=self.ENDPOINT)
        self.fill_and_submit_admin_login_form()