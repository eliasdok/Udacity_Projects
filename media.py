import webbrowser

        #We use this class Movie to store information of a movie
class Movie:   
        def __init__(self, movie_title, storyline, movie_image, trailer_youtube):
        #Instance variables of class movie
           self.title = movie_title
           self.storyline = storyline
           self.movie_image_url = movie_image
           self.trailer_youtube_url = trailer_youtube

        #Instance method (play the trailer in the web browser)
        def show_trailer(self):
           webbrowser.open(self.trailer_youtube_url)
           
        

