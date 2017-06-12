import media
import fresh_tomatoes

# Create toy stort movie object
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# Create avatar movie object
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Create kill bill movie object
kill_bill = media.Movie("Kill Bill",
                     "An story of revenge and katanas",
                     "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                     "https://www.youtube.com/watch?v=ot6C1ZKyiME")

# Create interstellar movie object
interstellar = media.Movie("Interstellar",
                     "A great space oddisey",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Create the martian movie object
the_martian = media.Movie("The Martian",
                     "An astronaut lost in Mars",
                     "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                     "https://www.youtube.com/watch?v=Ue4PCI0NamI")

# Create inception movie object
inception = media.Movie("Inception",
                     "How to insert an idea on the subject's brain",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=66TuSJo4dZM")

# put all movie objects into an array
movies = [toy_story,avatar,kill_bill,interstellar,the_martian,inception]

# Create movie page and open in browser using fresh_tomatoes library
fresh_tomatoes.open_movies_page(movies)

