import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "http://www.movieposterdb.com/posters/05_06/1995/0114709/l_22446_0114709_f380546e.jpg",
                        "https://www.youtube.com/watch?v=c3986gGp3Qs")


avatar = media.Movie("Avatar",
                     "A marine on the planet",
                     "http://www.movieposterdb.com/posters/10_08/2009/499549/l_499549_43475538.jpg",
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I")


pursuit = media.Movie("The Pursuit of Happyness",
                      "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional endeavor",
                      "http://www.movieposterdb.com/posters/07_12/2006/454921/l_454921_9d11428d.jpg",
                      "https://www.youtube.com/watch?v=SIZKoak6gp8")


shawshank = media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency",
                        "http://www.movieposterdb.com/posters/11_08/1994/111161/l_111161_e9ccda65.jpg",
                        "https://www.youtube.com/watch?v=RLw6hBFJ8bk")

forestgump = media.Movie("Forest Gump",
                         "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him",
                         "http://www.movieposterdb.com/posters/06_02/1994/0109830/l_94169_0109830_27bf435e.jpg",
                         "https://www.youtube.com/watch?v=EtYNngO7eq4")

thegodfather = media.Movie("The Godfather",
                           "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son",
                           "http://www.movieposterdb.com/posters/11_05/1972/68646/l_68646_87a25cbd.jpg",
                           "https://www.youtube.com/watch?v=vdQi6Ebjm8c")


movies = [toy_story, avatar, pursuit, shawshank, forestgump, thegodfather]

fresh_tomatoes.open_movies_page(movies)
