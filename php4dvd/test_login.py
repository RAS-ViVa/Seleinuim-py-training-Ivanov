from model.user import User
#from selenium_fixture import app


def test_login_with_valid_credentials(app):
#    app.ensure_logout()
#    assert app.is_logged_in()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()
