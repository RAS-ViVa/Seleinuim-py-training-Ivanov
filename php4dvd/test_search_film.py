'''
from model.user import User
from model.film import Film
from selenium.webdriver.common.keys import Keys
import logging


def test_search_film(app):
#    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    app.login(User.Admin())
    assert app.is_logged_in()
    beforeCollectionFilms = app.sum_films_collection()
    wich_FilmSearch =app.film_name()
    app.clear_search_field()

    app.search_film(wich_FilmSearch)


    FilmSearched=app.film_name()
    afterCollectionFilms = app.sum_films_collection()

    assert beforeCollectionFilms > afterCollectionFilms
    assert wich_FilmSearch == FilmSearched
    app.logout()
'''