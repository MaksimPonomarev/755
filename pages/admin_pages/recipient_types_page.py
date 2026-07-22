from testit_python_commons.step import step

from locators import RecipientTypesLocators
from pages.admin_pages.base_page import AdminBasePage
from tools.faker import fake


class RecipientTypesAdminPage(AdminBasePage):

    ENDPOINT = "/recipient-types"

    @step("Проверка: открыта страница типов получателей")
    def should_be_recipient_types(self):
        self.check_url()
        self.elem_should_be_visible(selector=RecipientTypesLocators.CREATE_RECIPIENT_TYPE_BTN)

    @step("Создание Типа Получателей")
    def create_recipient_types(self):
        self.created_name = fake.random_name()
        self.custom_click(RecipientTypesLocators.CREATE_RECIPIENT_TYPE_BTN)
        self.page.locator(RecipientTypesLocators.NAME).fill(self.created_name)
        self.click_and_wait_response(selector=RecipientTypesLocators.CREATE_BTN, url="livewire/update")

    @step("Проверка: успешность создания Типа Получателя")
    def check_success_recipient_types_created(self):
        # изменить способ на сортировку по айди после правки 60511
        # self.custom_click(selector=RecipientTypesLocators.SORT_BY_ID_BTN)

        self.custom_click(selector=RecipientTypesLocators.SEARCH)
        self.page.fill(selector=RecipientTypesLocators.SEARCH, value=self.created_name)
        self.check_text_by_selector(selector=RecipientTypesLocators.ALL_LIST_ELEMENTS, text=self.created_name)

