from locators import UsersAdminPageLocators
from pages.admin_pages.base_page import AdminBasePage


class AdminUsersPage(AdminBasePage):
    ENDPOINT = '/users'

    def should_be_users_page(self):
        self.check_url(endpoint=self.ENDPOINT)
        self.elem_should_be_visible(UsersAdminPageLocators.CREATE_USER_BTN)