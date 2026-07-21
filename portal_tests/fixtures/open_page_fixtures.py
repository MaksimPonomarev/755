import pytest

from pages.admin_pages.login_page import AdminLoginPage
from pages.admin_pages.recipient_types_page import RecipientTypesAdminPage

from pages.admin_pages.users_page import AdminUsersPage


@pytest.fixture
def admin_page(page):
    return AdminLoginPage(page)

@pytest.fixture
def users_page(page):
    return AdminUsersPage(page)

@pytest.fixture
def recipient_types_page(page):
    return RecipientTypesAdminPage(page)