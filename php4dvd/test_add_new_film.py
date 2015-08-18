from model.user import User
from model.film import Film
#from selenium_fixture import app


def test_add_new_film(app):
    app.login(User.Admin())
    assert app.is_logged_in()

    before = app.sum_films_collection() #первоначальное кол-во фильмов в коллекции
#    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    app.add_new_film(Film.random()) #добавляем новый фильм с произвольным названием

    after = app.sum_films_collection() #определяем новое кол-во фильмов в коллекции
    assert (after-before) == 1 #проверяем, что добавился один фильм
    app.logout()