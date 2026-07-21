import testit


@testit.externalId("successful_creation_user_with_all_fields")
@testit.workItemIds(10609)
@testit.displayName("Успешное создание пользователя со всеми заполненными полями")
def test_successful_creation_user_with_all_fields(admin_page, users_page):
    admin_page.open_and_register_admin_panel()
    admin_page.left_panel.go_to_users()
    users_page.should_be_users_page()
    users_page.create_user()




