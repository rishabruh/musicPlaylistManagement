import mysql.connector as sql

db = sql.connect(host="pop-os", user="rishabh", passwd='', database="proj")
pointer = db.cursor()
crit=''
keyword=''

def addSong():
    global db
    global pointer
    Track = str(input("Enter song name: "))
    Artist = input("Enter artist's name: ")
    Album = input("Enter album name: ")
    query = (
        f"INSERT INTO playlist (Track,Artist,Album) VALUES('{Track}','{Artist}','{Album}');"
    )
    pointer.execute(query)
    out = pointer.fetchall()
    for x in out:
        print(out)
    confirm = input("Confirm these changes?[y\n] ")
    if confirm.lower() == "y":
        db.commit()
    else:
        db.rollback()


def search():
    askCriteria = input(
        """What do you want for search with?
[1]By Track
[2]By Artist
[3]By Album
>
    """
    )
    if askCriteria == "1":
        crit = "Track"
    elif askCriteria == "2":
        crit = "Artist"
    elif askCriteria == "3":
        crit = "Album"
    keyword = input(f"Enter {crit} keyword: ")
    return crit
    return keyword


def searchSong(crit,keyword):
    global db
    global pointer
    try:
        query = f"SELECT * FROM playlist WHERE {crit}={keyword};"
        pointer.execute(query)
    except:
        print("Error!")
    out = pointer.fetchall()
    for x in out:
        print(out)
    db.commit()


def removeSong(crit, keyword):
    global db
    global pointer
    query = f"DELETE FROM playlist WHERE {crit}={keyword};"
    pointer.execute(query)
    out = pointer.fetchall()
    for x in out:
        print(out)
    confirm = input("Confirm these changes?[y\n] ")
    if confirm.lower() == "y":
        db.commit()
    else:
        db.rollback()


def displayPlaylist():
    global db
    global pointer
    query='SELECT * FROM playlist;'
    pointer.execute(query)
    out=pointer.fetchall()
    for x in out:
        print(out)

def updatePlaylist(crit,keyword):
    global pointer
    global db
    askrefkey=input('''What do you want to change?
[1]By Track
[2]By Artist
[3]By Album
> ''')
    if askrefkey == "1":
        refkey = "Track"
    elif askrefkey == "2":
        refkey = "Artist"
    elif askrefkey == "3":
        refkey = "Album"
    refval=input(f"Which {refkey} to look for? ")
    keyword = input(f"Enter {crit} keyword: ")
    query=f'UPDATE playlist SET {crit}={keyword} WHERE {refkey}={refval};'
    pointer.execute(query)
    out=pointer.fetchall()
    for x in out:
        print(out)

while True:
    print(
        """Music Playlist Sim Thingy 2000:
[1]Add Song
[2]Delete Song
[3]Display Playlist
[4]Update Playlist
[5]Search Song
[6]Exit"""
    )
    userChoice = input("Enter a choice:\n>")
    if userChoice == "6":
        db.close()
        exit()
    elif userChoice == "1":
        addSong()
        print('\n ==================== \n')
    elif userChoice == "2":
        search()
        removeSong(crit, keyword)
        print('\n ==================== \n')        
    elif userChoice=='3':
        displayPlaylist()
        print('\n ==================== \n')
    elif userChoice=='4':
        search()
        updatePlaylist(crit,keyword)
        print('\n ==================== \n')
    elif userChoice=='5':
        search()
        searchSong(crit,keyword)
        print('\n ==================== \n')
