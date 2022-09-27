ratings_file = open('scores.txt')
"""Restaurant rating lister."""

def create_dictionary(file):
    """Reads scores file and returns a dictionary"""

    restaurant_scores = {}

    for line in file:
        line = line.strip()
        restaurant, score = line.split(":")
        restaurant_scores[restaurant] = int(score)
        
    return restaurant_scores

    #dictionary_created = create_dictionary(ratings_file)

def add_user_ratings(ratings):
    """Add a user restaurant and rating."""
    restaurant_name = input("Enter a restaurant name. ")
    restaurant_rating = input("How would you rate it? ")
    ratings[restaurant_name] = restaurant_rating

def sort_ratings(file):
    """Print out restaurants and ratings sorted by alphabetical order."""
    
    dictionary_created

    for restaurant, score in sorted(file.items()):
        print(f"Restaurant: {restaurant}, Rating: {score}")


dictionary_created = create_dictionary(ratings_file)

add_user_ratings(dictionary_created)

sort_ratings(dictionary_created)  