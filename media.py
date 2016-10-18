import webbrowser

class Movie():
    """ ... this is the class documentation docstring ...
    its movie class 
    """
    def __init__(self, movie_title, movie_rating, movie_storyline, poster_image,
                 trailer_youtube):
        """ ... this is the constructor method docstring ...
        its a function which takes input whenever init is calledand create memory
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ show_trailer() docstring...
        this opens webbrowser for trailer
        """
        webbrowser.open(self.trailer_youtube_url)
            
            
