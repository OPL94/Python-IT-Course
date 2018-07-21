jb_movies = {
    "Roger Moore": " Live and Let Die",
    "Sean Connery": "From Russia With Love",
    "Pierce Brosnan": "Die Another Day",
    "Daniel Craig": "Skyfall"
}

count = 0

print("Try and name 4 actors who have played James Bond.")

for x in range(1,5):
    answer = input("Attempt %d - Name an actor: " %(x))

    if answer.title() in jb_movies:
        print("Well done: %s was Bond in %s." % (answer.title(), jb_movies[answer.title()]))
        count += 1
    else:
        print("Sorry. %s hasn't played Bond as far as I know." % (answer.title()))

print("You got %d out of 4." % (count))
