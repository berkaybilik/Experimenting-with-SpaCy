import spacy
nlp = spacy.load('en_core_web_md')

def recommend_movie(given_movie_description):
    """
    Gets a movie description and recommends a movie based on the given description.

    Further Details:
    Reads movies from the file movies.txt which contains a movie and its description in each line like: 'Movie X: watch this, it is cool'. 
    Compares each movie from the file to the given movie description using SpaCy's 'similarity' function to a similarity score for each comparison.
    Returns the movie name with the higest similarity score.
    """

    # Read the file movies.txt 
    with open("movies.txt") as movies_file:
        movies_list = [movie.strip() for movie in movies_file]

    nlp_movie = nlp(given_movie_description)

    best_fit_and_score = ("", 0)
    for movie_from_list in movies_list:


        movie_name, movie_description = movie_from_list.split(":")

        nlp_movie_description_from_list = nlp(movie_description)

        similarity_score = nlp_movie.similarity(nlp_movie_description_from_list) #Gets a similarity score for all movies in movie.txt

        if similarity_score > best_fit_and_score[1]:
            best_fit_and_score = (movie_name, similarity_score)

    return best_fit_and_score[0]



watched_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(recommend_movie(watched_movie))
    
