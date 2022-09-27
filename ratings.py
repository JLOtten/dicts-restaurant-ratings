ratings_file = open('scores.txt')

"""Restaurant rating lister."""

def create_dictionary(file):

    sorted_ratings = {}

    for line in file:
        line = line.strip()
        restaurant, score = line.split(":")
        sorted_ratings[restaurant] = int(score)
        
    return sorted_ratings

dictionary_created = create_dictionary(ratings_file)

def add_user_ratings():
    restaurant_name = input("Enter a restaurant name. ")
    restaurant_score = input("How would you rate it? ")
    dictionary_created[restaurant_name] = restaurant_score

def sort_ratings(file):
    
    dictionary_created

    for restaurant, score in sorted(file.items()):
        print(f"{restaurant}: {score}")

sort_ratings(dictionary_created)
        