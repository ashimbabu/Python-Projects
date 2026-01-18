print("===== Music Library Playlist Recommender =====")

music_library = []

while True:
    print("\n1. Add Song")
    print("2. View Library")
    print("3. Create Playlist by Genre")
    print("4. Recommend Songs by Mood")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Song title: ")
        artist = input("Artist name: ")
        genre = input("Genre (pop/rock/jazz/classical/other): ")
        duration = float(input("Duration (minutes): "))

        song = {
            "title": title,
            "artist": artist,
            "genre": genre.lower(),
            "duration": duration
        }

        music_library.append(song)
        print("Song added successfully!")

    elif choice == "2":
        if not music_library:
            print("Music library is empty.")
        else:
            print("\nTitle\tArtist\tGenre\tDuration")
            for s in music_library:
                print(f"{s['title']}\t{s['artist']}\t{s['genre']}\t{s['duration']}")

    elif choice == "3":
        g = input("Enter genre: ").lower()
        print(f"\nPlaylist ({g.upper()}):")
        found = False
        for s in music_library:
            if s["genre"] == g:
                print(f"- {s['title']} by {s['artist']}")
                found = True
        if not found:
            print("No songs found for this genre.")

    elif choice == "4":
        mood = input("Enter mood (happy/sad/relax/energetic): ").lower()
        print("\nRecommended Songs:")

        for s in music_library:
            if mood == "happy" and s["genre"] in ["pop", "dance"]:
                print(f"- {s['title']}")
            elif mood == "sad" and s["genre"] in ["classical", "jazz"]:
                print(f"- {s['title']}")
            elif mood == "energetic" and s["genre"] in ["rock"]:
                print(f"- {s['title']}")
            elif mood == "relax" and s["genre"] in ["jazz", "classical"]:
                print(f"- {s['title']}")

    elif choice == "5":
        print("Exiting Music App. Goodbye!")
        break

    else:
        print("Invalid choice.")
