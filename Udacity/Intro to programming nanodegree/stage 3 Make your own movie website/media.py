import webbrowser

class Movie():
    '''This file provides a way to store movie information
    which is movie title, storyline, poster image, trailer url. '''

    def __init__(self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        ''' __init__ is the constructor for a class.
        Each parameter would be stored in variables on the stack.'''
