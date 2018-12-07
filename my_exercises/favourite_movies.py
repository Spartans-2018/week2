class Movies:
    """
    Make a class of your favorite movie or tv show
    When the class is instantiated I want to have the following instance variables
        self.cast, self.characters, self.release, self.genre
    I also want to be able to use the following methods
        .get_cast will return me a list of cast members real names
        .get_characters will return me a list of the characters in the movie
        .get_release will return me the release date of that movie
        .get_genre will return the genres this movie belongs to   """

    def __init__(self, cast='Bradley Cooper', characters='the guy', release='2000', genre='comedy'):
        self.cast = cast
        self.characters = characters
        self.release = release
        self.genre = genre

    def get_cast(self):
        return self.cast
    
    def get_characters(self):
        return self.characters

    def get_genre(self):
        return self.genre
    
    def get_release(self):
        print(self)
        return self.release

my_favmovies = Movies(cast=["Russel Crowe", "Oliver Reed"], characters=["Maximus", "Ceasar"],genre=["May 1, 2000"], release=["Action"] )
my_favtvshows = Movies("Olivia", "Kalisi", "2017", "Action, Fantasy")
# print(my_favmovies.get_cast())
# print(my_favmovies.get_characters())
# print(my_favmovies.get_genre())
# print(my_favmovies.get_release())
# print(my_favmovies)  # refering the object hexadecimal location of the object
# print(my_favtvshows)

my_favseries = Movies()   # this instance will use default parameters
print(my_favseries.get_cast())