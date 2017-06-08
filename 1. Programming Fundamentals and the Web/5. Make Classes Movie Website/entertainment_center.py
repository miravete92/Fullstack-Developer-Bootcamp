import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

kill_bill = media.Movie("Kill Bill",
                     "An story of revenge and katanas",
                     "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                     "https://www.youtube.com/watch?v=ot6C1ZKyiME")

interstellar = media.Movie("Interstellar",
                     "A great space oddisey",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_martian = media.Movie("The Martian",
                     "An astronaut lost in Mars",
                     "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                     "https://www.youtube.com/watch?v=Ue4PCI0NamI")

inception = media.Movie("Inception",
                     "How to insert an idea on the subject's brain",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=66TuSJo4dZM")
#kill_bill.show_trailer()
movies = [toy_story,avatar,kill_bill,interstellar,the_martian,inception]
fresh_tomatoes.open_movies_page(movies)

