import testit



@testit.externalId("test_create_recipient_types")
@testit.workItemIds(10676)
@testit.displayName("Создание Тип Получателя")
def test_create_recipient_types(admin_page, recipient_types_page):
    admin_page.open_and_register_admin_panel()
    admin_page.left_panel.go_to_recipient_types()
    recipient_types_page.should_be_recipient_types()
    recipient_types_page.create_recipient_types()
    recipient_types_page.check_success_recipient_types_created()