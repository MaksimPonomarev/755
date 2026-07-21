from testit_python_commons.step import step

from locators import BasePageLocators


class LeftPanelComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    @step("Переход на вкладку 'Пользователи'")
    def go_to_users(self):
        self.base_page.custom_click(BasePageLocators.USERS_LINK)

    @step("Переход на вкладку 'Роли'")
    def go_to_roles(self):
        self.base_page.custom_click(BasePageLocators.ROLES_LINK)

    @step("Переход на вкладку 'Типы Получателей'")
    def go_to_recipient_types(self):
        self.base_page.custom_click(BasePageLocators.RECIPIENT_TYPES_LINK)
