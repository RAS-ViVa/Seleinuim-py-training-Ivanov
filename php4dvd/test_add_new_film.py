from model.user import User
from model.film import Film
#from selenium_fixture import app


def test_add_new_film(app):
    app.login(User.Admin())
    assert app.is_logged_in()

    before = app.sum_films_collection()
#    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    app.add_new_film(Film.random())
    after = app.sum_films_collection()
    assert (after-before) == 1
    app.logout()
    app.ensure_logout
