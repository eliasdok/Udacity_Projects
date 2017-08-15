import media
import fresh_tomatoes

#class instances
The_Godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "https://kek.gg/i/5rhdMt.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

Fight_club = media.Movie("Fight Club",
                         "An insomniac office worker,looking for a way to change his life.",
                         "https://kek.gg/i/KD3t_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

Boyhood = media.Movie("Boyhood",
                      "The life of Mason, from early childhood to his arrival at college.",
                      "https://kek.gg/i/6Dy3h3.jpg",
                      "https://www.youtube.com/watch?v=Y0oX0xiwOv8")

City_of_god = media.Movie("City of god",
                          "Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths.",
                          "https://kek.gg/i/5xr6wK.jpg",
                          "https://www.youtube.com/watch?v=dcUOO4Itgmw")

Scarface = media.Movie("Scarface",
                       "In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.",
                       "https://kek.gg/i/3tXwfV.jpg",
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

Redemption = media.Movie("Redemption",
                         "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                         "https://kek.gg/i/5gpmyF.jpg",
                         "https://www.youtube.com/watch?v=6hB3S9bIaco")


movies = [The_Godfather, Fight_club,Boyhood, City_of_god, Scarface, Redemption]

#open the movie list in the web browser
fresh_tomatoes.open_movies_page(movies)
