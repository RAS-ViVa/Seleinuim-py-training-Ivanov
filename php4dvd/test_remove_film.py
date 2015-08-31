from model.user import User
from model.film import Film
import logging


def test_remove_film(app):
    app.login(User.Admin())
    assert app.is_logged_in()
    before = app.sum_films_collection()
#    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    app.remove_film()
    after = app.sum_films_collection()
    assert (before - after) == 1
    app.logout()
    app.ensure_logout

