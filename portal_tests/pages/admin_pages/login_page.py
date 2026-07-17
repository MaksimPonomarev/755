from locators import LoginAdminPageLocators
from pages.admin_pages.base_page import AdminBasePage


class AdminLoginPage(AdminBasePage):



    def fill_and_submit_admin_login_form(self):
        self.page.fill(LoginAdminPageLocators.ADMIN_LOGIN_INSERT_BTN, "admin@admin.com")
        self.page.fill(LoginAdminPageLocators.ADMIN_PASSWORD_INSERT_BTN, "admin@admin.com")
        self.page.click((LoginAdminPageLocators.SUBMIT_BTN))