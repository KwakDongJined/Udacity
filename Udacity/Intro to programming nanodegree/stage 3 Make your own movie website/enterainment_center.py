import fresh_tomatoes
import media
'''This file is detailed information.
        Variables would be stored using movie class in media.py file'''

Old_Boy = media.Movie(
                    "Old Boy",
                    "After being kidnapped and imprisoned for fifteen years, \
                    Oh Dae-Su is released, only to find that \
                    he must find his captor in five days.",
                    "http://cfs5.tistory.com/upload_control/download.blog?fhandle=YmxvZzE2MzY3M0BmczUudGlzdG9yeS5jb206L2F0dGFjaC8wLzE3MDAwMDAwMDAwMy5qcGc%3D",  # noqa
                    "https://www.youtube.com/watch?v=I18wDlx6WzI"
                    )

The_Matrix = media.Movie(
                        "The Matrix",
                        "A computer hacker learns from mysterious rebels \
                        about the true nature of his reality and his role \
                        in the war against its controllers.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU"
                        )

Her = media.Movie(
                "Her",
                "A lonely writer develops an unlikely relationship \
                with an operating system designed to meet his every need.",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
                "https://www.youtube.com/watch?v=XsQqMwacZQw"
                )

Interstellar = media.Movie(
                        "Interstellar",
                        "A team of explorers travel through a wormhole in space\
                         in an attempt to ensure humanity's survival.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=3WzHXI5HizQ"
                        )

Transcendence = media.Movie(
                        "Transcendence",
                        "A scientist's drive for artificial intelligence, \
                        takes on dangerous implications when his consciousness \
                        is uploaded into one such program.",
                        "https://i.jeded.com/i/transcendence.29748.jpg",
                        "https://www.youtube.com/watch?v=VCTen3-B8GU"
                        )

A_Beautiful_Mind = media.Movie(
                            "A Beautiful mind",
                            "After John Nash, a brilliant but asocial mathematician, \
                            accepts secret work in cryptography, his life takes \
                            a turn for the nightmarish.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=aS_d0Ayjw4o"
                            )

movies = [Old_Boy, The_Matrix, Her, Interstellar, Transcendence, A_Beautiful_Mind]
'''Variables would be stored in movies list.'''
fresh_tomatoes.open_movies_page(movies)
'''it would open the outfile in the browser using input vales (movies)'''
