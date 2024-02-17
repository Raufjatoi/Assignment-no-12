# 9. Song Organizer:
#  Develop a program that stores song titles, artists, and genres in a dictionary. Include functions to 
# sort by different criteria (title, artist, genre) and search for specific songs
dm = []

while True:
    song_t = input('Enter song Title: ')
    artist = input('Enter artist name: ')
    genre = input('Enter genre name: ')
    
    song_entry = {'song_name': song_t, 'Artist_name': artist, 'genre': genre}
    dm.append(song_entry)
    
    print(dm)
    
    search = input("What do you want to search: A/S/G :: ").upper()
    
    if search == 'A':
        a = input('Enter artist: ')
        found = False
        for song in dm:
            if song['Artist_name'].lower() == a.lower():
                found = True
                break
        if found:
            print('Song found')
        else:
            print('Song not found')
            
    elif search == 'S':
        s = input('Enter song: ')
        found = False
        for song in dm:
            if song['song_name'].lower() == s.lower():
                found = True
                break
        if found:
            print('Song found')
        else:
            print('Song not found')
            
    elif search == 'G':
        g = input('Enter genre: ')
        found = False
        for song in dm:
            if song['genre'].lower() == g.lower():
                found = True
                break
        if found:
            print('Song found')
        else:
            print('Song not found')
            
    else:
        print('Invalid input')
        
    cont = input('Enter "q" to quit, or anything else to continue: ').lower()
    if cont == 'q':
        break


