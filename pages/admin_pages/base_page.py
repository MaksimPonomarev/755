
from playwright.sync_api import expect
from testit_python_commons.step import step

from components.left_panel_component import LeftPanelComponent
from config import settings


class AdminBasePage:

    ENDPOINT = "/admin"
    def __init__(self, page):
        self.page = page
        self.left_panel = LeftPanelComponent(self)

    @step("Открытие страницы браузера и ожидание сети")
    def open(self, endpoint: str):
        self.page.goto(f"{settings.BASE_URL}{endpoint}", timeout=settings.timeout)
        self.wait_for_load_state()

    @step("Клик с ожиданием сети")
    def custom_click(self, selector: str):
        self.page.click(selector=selector)
        self.wait_for_load_state()

    @step("Проверка url")
    def check_url(self):
        expected_url = f"{settings.BASE_URL}{self.ENDPOINT}"
        expect(self.page).to_have_url(expected_url, timeout=settings.timeout)

    @step("Проверка: Элемент видимый на странице ")
    def elem_should_be_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible(timeout=settings.timeout)

    @step("Ожидание сети")
    def wait_for_load_state(self, state: str = "networkidle"):
        self.page.wait_for_load_state(state)

    @step("Клик с ожиданием 200 ответа")
    def click_and_wait_response(self, selector, url):
        """
        Кликает по элементу и ждет успешного ответа (200) от указанного URL.
        """
        with self.page.expect_response(url) as response_info:
            self.page.click(selector=selector)

        response = response_info.value
        if response.status != 200:
            raise AssertionError(f"Запрос к {url} завершился с ошибкой! Статус: {response.status}")

        return response

    @step("Проверка: Текст должен быть видимым")
    def check_text_by_selector(self, selector: str, text: str):
        locator = self.page.locator(selector).filter(has_text=text)
        expect(locator).to_be_visible(timeout=settings.timeout)
