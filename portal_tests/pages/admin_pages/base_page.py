
from playwright.sync_api import expect

from components.left_panel_component import LeftPanelComponent
from config import settings


class AdminBasePage:

    ENDPOINT = "/admin"
    def __init__(self, page):
        self.page = page
        self.left_panel = LeftPanelComponent(self)

    def open(self):
        self.page.goto(f"{settings.BASE_URL}+{self.ENDPOINT}")


    def check_url(self, endpoint: str):
        expected_url = f"{settings.BASE_URL}{self.ENDPOINT}"
        expect(self.page).to_have_url(expected_url)

    def elem_should_be_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()