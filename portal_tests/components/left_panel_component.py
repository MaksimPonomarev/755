from locators import BasePageLocators


class LeftPanelComponent:
    def __init__(self, base_page):
        self.base_page = base_page


    def go_to_users(self):
        self.base_page.page.click(BasePageLocators.USERS_LINK)

    def go_to_roles(self):
        self.base_page.page.click(BasePageLocators.ROLES_LINK)