#Here we will be accessing a football database using sqlite3 and python - we will be able to add, delete, update and view the database using the CLI.

import sqlite3
from tabulate import tabulate

#Ask the user, based on the following databases, COACH, PLAYER, GAME or SEASON if they'd like to select option 1 to interact with the databases or option 2 to do a custom query.
print("Would you like to interact with the databases or do a custom query? 1. Interact with databases, 2. Custom query")
choice = input("Enter choice: ")
while choice != "1" and choice != "2":
    print("Invalid choice, please enter a valid choice")
    choice = input("Enter choice: ")

#If user picks option 2, ask the user to enter a query and execute the query using sqlite3 and use try catch to throw an error if the syntax is incorrect. Then ask the user if they'd like to do another query. If yes, repeat and if not, exit the program.
if choice == "2":
   #while loop to keep asking the user for queries until they decide to exit the program
   while True:
        query = input("Enter query: ").upper()
        conn = sqlite3.connect('football.db')
        c = conn.cursor()
        #try catch to throw an error if the syntax is incorrect
        try:
            c.execute(query)
            print(tabulate(c.fetchall(), headers=[i[0] for i in c.description]))
        except sqlite3.Error as e:
            print(e)
        conn.close()
        another_query = input("Would you like to do another query? Y/N: ").upper()
        while another_query != "Y" and another_query != "N":
            print("Invalid choice, please enter a valid choice")
            another_query = input("Would you like to do another query? Y/N: ").upper()
        if another_query == "N":
            print("Programme will now exit")
            exit()

#ask user which table they'd like to interact with, either COACH, PLAYER, GAME or SEASON based on user input. Convert to uppercase
if choice == "1":
    print("Which table would you like to interact with? COACH, PLAYER, GAME or SEASON")
    table = input("Enter table: ").upper()
    while table != "COACH" and table != "PLAYER" and table != "GAME" and table != "SEASON":
        print("Invalid table, please enter a valid table")
        table = input("Enter table: ").upper()

#Based on the table chosen, ask thhe user what they would like to do with the table - view, add, delete or update
print("What would you like to do with the table? 1. View, 2. Add, 3. Delete, 4. Update")
option = input("Enter option: ")
while option != "1" and option != "2" and option != "3" and option != "4":
    print("Invalid option, please enter a valid option")
    option = input("Enter option: ")

#if user picks coach table and view - the following code will run.
if table == "COACH" and option == "1":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT * FROM COACH")
    print(c.fetchall())
    conn.close()

#if user picks coach table and add - the following code will run asking for user input to add a new coach and the following data coach_id, name, address_street, address_city, address_postcode, yrs_experience.
if table == "COACH" and option == "2":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    coach_id = input("Enter new coach ID: ")
    #while loop to check if coach_id already exists in the database
    while c.execute("SELECT * FROM COACH WHERE coach_id = ?", (coach_id,)).fetchall():
        print("Coach ID already exists, please enter a new coach ID")
        coach_id = input("Enter new coach ID: ")
    name = input("Enter full name: ")
    address_street = input("Enter registered address street: ")
    address_city = input("Enter registered address city: ")
    address_postcode = input("Enter registered address postal code: ")
    yrs_experience = input("Enter experience amount in YEARS: ")
    c.execute("INSERT INTO COACH VALUES (?, ?, ?, ?, ?, ?)", (coach_id, name, address_street, address_city, address_postcode, yrs_experience))
    print("Coach added successfully - application will now exit")
    conn.commit()
    conn.close()

#if user picks coach table and delete - the following code will run asking for user input to delete a coach based on coach_id given.
if table == "COACH" and option == "3":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    coach_id = input("Enter the ID of the coach information you would like to delete: ")
    confirm_delete = input("Are you sure you want to delete this coach? Y/N: ").upper()
    while confirm_delete != "Y" and confirm_delete != "N":
        print("Invalid choice, please enter a valid choice")
        confirm_delete = input("Are you sure you want to delete this coach? Y/N: ").upper()
    if confirm_delete == "Y":
        c.execute("DELETE FROM COACH WHERE coach_id = ?", (coach_id,))
        conn.commit()
        print("Coach deleted successfully - application will now exit")
    elif confirm_delete == "N":
        print("Coach not deleted - programme will now exit")
        exit()
    conn.close()

#if user picks coach table and update - the following code will run asking for user input to update a coach based on coach_id given.
if table == "COACH" and option == "4":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    coach_id = input("Enter the ID of the coach you would like to change the information of: ")
    name = input("Enter full anem: ")
    address_street = input("Enter registered address street: ")
    address_city = input("Enter registered address city: ")
    address_postcode = input("Enter registered address postal code: ")
    yrs_experience = input("Enter experience amount in YEARS: ")
    c.execute("UPDATE COACH SET name = ?, address_street = ?, address_city = ?, address_postcode = ?, yrs_experience = ? WHERE coach_id = ?", (name, address_street, address_city, address_postcode, yrs_experience, coach_id))
    conn.commit()
    conn.close()

#if user picks player table and view - the following code will run
if table == "PLAYER" and option == "1":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT * FROM PLAYER")
    print(c.fetchall())
    conn.close()

#if user picks player table and add - the following code will run asking for user input to add a new player and the following data player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id.
if table == "PLAYER" and option == "2":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    player_id = input("Enter new player ID: ")
    #while loop to check if player_id already exists in the database
    while c.execute("SELECT * FROM PLAYER WHERE player_id = ?", (player_id,)).fetchall():
        print("Player ID already exists, please enter a new player ID")
        player_id = input("Enter new player ID: ")
    number = input("Enter player number: ")
    name = input("Enter full name: ")
    shots = input("Enter amount of shots: ")
    hits = input("Enter amount of hits: ")
    steals = input("Enter amount of steals: ")
    rebounds = input("Enter amount of rebounds: ")
    blocks = input("Enter amount of blocks: ")
    coach_id = input("Enter coach ID: ")
    c.execute("INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id))
    conn.commit()
    conn.close()

#if user picks player table and delete - the following code will run asking for user input to delete a player based on player_id given and adding a confirm delete message with a Y/N option.
if table == "PLAYER" and option == "3":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    player_id = input("Enter player_id: ")
    confirm_delete = input("Are you sure you want to delete this player? Y/N: ").upper()
    while confirm_delete != "Y" and confirm_delete != "N":
        print("Invalid choice, please enter a valid choice")
        confirm_delete = input("Are you sure you want to delete this player? Y/N: ").upper()
    if confirm_delete == "Y":
        c.execute("DELETE FROM PLAYER WHERE player_id = ?", (player_id,))
        conn.commit()
    elif confirm_delete == "N":
        print("Player not deleted - programme will now exit")
        exit()
    conn.close()

#if user picks player table and update - the following code will run asking for user input to update a player based on player_id given.
if table == "PLAYER" and option == "4":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    player_id = input("Enter player_id: ")
    number = input("Enter player number: ")
    name = input("Enter full name: ")
    shots = input("Enter amount of shots: ")
    hits = input("Enter amount of hits: ")
    steals = input("Enter amount of steals: ")
    rebounds = input("Enter amount of rebounds: ")
    blocks = input("Enter amount of blocks: ")
    coach_id = input("Enter coach ID: ")
    c.execute("UPDATE PLAYER SET number = ?, name = ?, shots = ?, hits = ?, steals = ?, rebounds = ?, blocks = ?, coach_id = ? WHERE player_id = ?", (number, name, shots, hits, steals, rebounds, blocks, coach_id, player_id))
    conn.commit()
    conn.close()

#if user picks game table and view - the following code will run
if table == "GAME" and option == "1":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT * FROM GAME")
    print(c.fetchall())
    conn.close()

#if user picks game table and add - the following code will run asking for user input to add a new game and the following data game_id, home, away, date, time, location_street, location_city, location_postcode, season_id.
if table == "GAME" and option == "2":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    game_id = input("Enter new game ID: ")
    #while loop to check if game_id already exists in the database
    while c.execute("SELECT * FROM GAME WHERE game_id = ?", (game_id,)).fetchall():
        print("Game ID already exists, please enter a new game ID")
        game_id = input("Enter new game ID: ")
    home = input("Enter home team: ")
    away = input("Enter away team: ")
    date = input("Enter date of game: ")
    time = input("Enter time of game: ")
    location_street = input("Enter location street: ")
    location_city = input("Enter location city: ")
    location_postcode = input("Enter location postal code: ")
    season_id = input("Enter season ID: ")
    c.execute("INSERT INTO GAME VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (game_id, home, away, date, time, location_street, location_city, location_postcode, season_id))
    conn.commit()
    conn.close()

#if user picks game table and delete - the following code will run asking for user input to delete a game based on game_id given and adding a confirm delete message with a Y/N option.
if table == "GAME" and option == "3":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    game_id = input("Enter game_id: ")
    confirm_delete = input("Are you sure you want to delete this game? Y/N: ").upper()
    while confirm_delete != "Y" and confirm_delete != "N":
        print("Invalid choice, please enter a valid choice")
        confirm_delete = input("Are you sure you want to delete this game? Y/N: ").upper()
    if confirm_delete == "Y":
        c.execute("DELETE FROM GAME WHERE game_id = ?", (game_id,))
        conn.commit()
    elif confirm_delete == "N":
        print("Game not deleted - programme will now exit")
        exit()
    conn.close()

#if user picks game table and update - the following code will run asking for user input to update a game based on game_id given.
if table == "GAME" and option == "4":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    game_id = input("Enter game_id: ")
    home = input("Enter home team: ")
    away = input("Enter away team: ")
    date = input("Enter date of game: ")
    time = input("Enter time of game: ")
    location_street = input("Enter location street: ")
    location_city = input("Enter location city: ")
    location_postcode = input("Enter location postal code: ")
    season_id = input("Enter season ID: ")
    c.execute("UPDATE GAME SET home = ?, away = ?, date = ?, time = ?, location_street = ?, location_city = ?, location_postcode = ?, season_id = ? WHERE game_id = ?", (home, away, date, time, location_street, location_city, location_postcode, season_id, game_id))
    conn.commit()
    conn.close()

#if user picks season table and view - the following code will run
if table == "SEASON" and option == "1":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT * FROM SEASON")
    print(c.fetchall())
    conn.close()

#if user picks season table and add - the following code will run asking for user input to add a new season and the following data season_id, begin, end.
if table == "SEASON" and option == "2":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    season_id = input("Enter new season ID: ")
    #while loop to check if season_id already exists in the database
    while c.execute("SELECT * FROM SEASON WHERE season_id = ?", (season_id,)).fetchall():
        print("Season ID already exists, please enter a new season ID")
        season_id = input("Enter new season ID: ")
    begin = input("Enter season start date: ")
    end = input("Enter season end date: ")
    c.execute("INSERT INTO SEASON VALUES (?, ?, ?)", (season_id, begin, end))
    conn.commit()
    conn.close()

#if user picks season table and delete - the following code will run asking for user input to delete a season based on season_id given and adding a confirm delete message with a Y/N option.
if table == "SEASON" and option == "3":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    season_id = input("Enter season_id: ")
    confirm_delete = input("Are you sure you want to delete this season? Y/N: ").upper()
    while confirm_delete != "Y" and confirm_delete != "N":
        print("Invalid choice, please enter a valid choice")
        confirm_delete = input("Are you sure you want to delete this season? Y/N: ").upper()
    if confirm_delete == "Y":
        c.execute("DELETE FROM SEASON WHERE season_id = ?", (season_id,))
        conn.commit()
    elif confirm_delete == "N":
        print("Season not deleted - programme will now exit")
        exit()
    conn.close()

#if user picks season table and update - the following code will run asking for user input to update a season based on season_id given.
if table == "SEASON" and option == "4":
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    season_id = input("Enter season_id: ")
    begin = input("Enter season start date: ")
    end = input("Enter season end date: ")
    c.execute("UPDATE SEASON SET begin = ?, end = ? WHERE season_id = ?", (begin, end, season_id))
    conn.commit()
    conn.close()

#Programme will now exit
print("Programme will now exit")
exit()



    