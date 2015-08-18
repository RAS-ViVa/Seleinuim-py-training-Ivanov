class Film(object):

    def __init__(self, name='', year='', duration='', rating='', format="DVD"):
        self.name = name
        self.year = year
        self.duration = duration
        self.rating = rating
        self.format = format

    @ classmethod
    def random (NewFilm):
        from random import randint
        return NewFilm(name= (str(randint(0, 1000)) + " - test Film"),
                       year="1999",
                       duration="120",
                       rating="99")