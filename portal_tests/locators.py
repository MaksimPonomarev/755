from config import settings


class LoginAdminPageLocators:
    ADMIN_LOGIN_INSERT_BTN = '#form\.login'
    ADMIN_PASSWORD_INSERT_BTN = '#form\.password'
    SUBMIT_BTN = 'button[type="submit"]'



class BasePageLocators:
    USERS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/users"]'
    ROLES_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/shield/roles"]'
    LICENSEES_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/licenses"]'
    PRODUCTS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/products"]'
    SUBSCRIPTIONS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/subscriptions"]'
    ORGANIZATIONS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/oranizations/organizations"]'
    RECIPIENT_TYPES_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/recipient-types"]'
    TAGS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/release-tags"]'
    RELEASES_INK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/releases"]'
    SYSLOG_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/syslogs"]'
    DOWNLOAD_LOGS_LINK = f'li .fi-sidebar-item a[href="{settings.BASE_URL}/download-logs"]'

    CREATE_RESOURCE_BTN = "[id='key-bindings-1']"



class UsersAdminPageLocators:
    CREATE_USER_BTN = f'a[href="{settings.BASE_URL}/users/create"]'


class CreateUserAdminPageLocators:
    FIO = "[id='form.fio']"
    LOGIN = "[id='form.login']"
    PASSWORD = "[id='form.password']"
    ORGANIZATION = "[id='form.organization_id']"
    ROLE = "div[x-data*='form.roles']"


class OrganizationsAdminPageLocators:
    CREATE_ORGANIZATIONS_BTN = f'a[href="{settings.BASE_URL}//oranizations/organizations/create"]'
    

class CreateOrganizationAdminPageLocators:
    NAME = "[id='form.name']"
    TYPE = "[id='form.type']"
    INN = "[id='form.inn']"
    RECIPIENT_TYPE = "div[x-data*='form.recipient_type_id']"
    PARENT_ORGANIZATION = "div[x-data*='form.parent_organization_id']"


class RecipientTypesLocators:
    CREATE_RECIPIENT_TYPE_BTN = r'[wire\:click="mountAction(\'create\')"]'
    NAME = "[id='mountedActionSchema0.name']"
    CREATE_BTN = "[x-data='filamentFormButton'][type='submit']"

    ALL_LIST_ELEMENTS = "tr[wire\\:key*='table.records']"
    SORT_BY_ID_BTN = r"[wire\:click='sortTable(\'id\')']"

    SEARCH = "[wire\\:key*='tableSearch.field.input']"