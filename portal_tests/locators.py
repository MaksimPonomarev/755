from config import settings


class BasePageLocators:
    USERS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/users"]'
    ROLES_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/shield/roles"]'
    LICENSEES_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/licenses"]'
    PRODUCTS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/products"]'
    SUBSCRIPTIONS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/subscriptions"]'
    ORGANIZATIONS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/oranizations/organizations"]'
    GROUPS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/recipient-types"]'
    TAGS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/release-tags"]'
    RELEASES_INK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/releases"]'
    SYSLOG_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/syslogs"]'
    DOWNLOAD_LOGS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/download-logs"]'




class UsersAdminPageLocators:
    CREATE_USER_BTN = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/admin/users/create"]'





class LoginAdminPageLocators:
    ADMIN_LOGIN_INSERT_BTN = '#form\.login'
    ADMIN_PASSWORD_INSERT_BTN = '#form\.password'
    SUBMIT_BTN = 'button[type="submit"]'


