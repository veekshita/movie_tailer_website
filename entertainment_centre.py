import media
import fresh_tomatoes

# class instantiating section
life_of_pie = media.Movie("Life of pie",
                          "The story of a boy and his friend tiger",
                          "Rating:9/10",
                          "http://natasha-stojanovska.com/wp-content/uploads/2015/04/Life-Of-Pi.jpeg",
                          "https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "Rating:8/10",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "Rating:6/10",   
                     "http://resizing.flixster.com/7j4Uky7sPOl5jUPSL2JBIDjeCvk=/800x1200/v1.bTsxMTE3Njc5MjtqOzE3MTkxOzIwNDg7ODAwOzEyMDA",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

ZMND = media.Movie("Zindagi na milegi dubbara",
                   "A story on Life",
                   "Rating:9/10",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Zindaginamilegidobara.jpg/220px-Zindaginamilegidobara.jpg",
                   "https://www.youtube.com/watch?v=ifIBOKCfjVs")

Twilight = media.Movie("The twilight saga",
                       "love story between vampire and a human",
                       "Rating:7/10",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/twilight-2008/large_nlvPMLCdum7bkHKmDSMnNLGztmW.jpg",
                       "https://www.youtube.com/watch?v=edLB6YWZ-R4")

threeidiots = media.Movie("3 idiots",
                          "Life of engineers",
                          "Rating:9/10",
                          "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                          "https://www.youtube.com/watch?v=xvszmNXdM4w")

# appending movies into a list:
movies = [life_of_pie, toy_story, avatar, ZMND, Twilight, threeidiots]
# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)
