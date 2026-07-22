import select

from testit_python_commons.step import step

from locators import UsersAdminPageLocators
from pages.admin_pages.base_page import AdminBasePage


class AdminUsersPage(AdminBasePage):
    ENDPOINT = '/users'

    @step("Клик по кнопке 'Создать'")
    def _click_create_user_button(self):
        self.custom_click(selector=UsersAdminPageLocators.CREATE_USER_BTN)


    @step("Проверка: Должна быть вкладка 'Пользователи'")
    def should_be_users_page(self):
        self.check_url()
        self.elem_should_be_visible(UsersAdminPageLocators.CREATE_USER_BTN)


    @step("Cоздание пользователя")
    def create_user(self):
        self._click_create_user_button()