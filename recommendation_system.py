movies = {
    "action": ["KGF", "Pushpa", "Salaar"],
    "comedy": ["Jathi Ratnalu", "F2", "MAD"],
    "romance": ["Hi Nanna", "Sita Ramam", "Love Story"]
}

genre = input("Enter genre (action/comedy/romance): ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Genre not found")
