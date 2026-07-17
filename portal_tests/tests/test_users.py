


def test_add_user(admin_page, users_page):
    admin_page.open()
    admin_page.fill_and_submit_admin_login_form()
    admin_page.left_panel.go_to_users()
    users_page.should_be_users_page()



    pass