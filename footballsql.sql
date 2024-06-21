DROP TABLE IF EXISTS PLAYER_GAME;
DROP TABLE IF EXISTS COACH_GAME;
DROP TABLE IF EXISTS PLAYER_SEASON;
DROP TABLE IF EXISTS COACH_SEASON;
DROP TABLE IF EXISTS PLAYER;
DROP TABLE IF EXISTS COACH;
DROP TABLE IF EXISTS GAME;
DROP TABLE IF EXISTS SEASON;


CREATE TABLE SEASON (
    season_id INTEGER PRIMARY KEY,
    begin TEXT NOT NULL,
    end TEXT NOT NULL
);

INSERT INTO SEASON (season_id, begin, end) 
VALUES (1, '2024-06-01', '2024-12-31');

CREATE TABLE COACH (
    coach_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address_street TEXT,
    address_city TEXT,
    address_postcode TEXT,
    yrs_experience INTEGER
);

INSERT INTO COACH (coach_id, name, address_street, address_city, address_postcode, yrs_experience) 
VALUES (1, 'Jack Waller', '123 Road Name', 'London', 'A1 B23', 10);


CREATE TABLE PLAYER (
    player_id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    name TEXT NOT NULL,
    shots INTEGER,
    hits INTEGER,
    steals INTEGER,
    rebounds INTEGER,
    blocks INTEGER,
    coach_id INTEGER,
    FOREIGN KEY (coach_id) REFERENCES COACH(coach_id)
);

INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (1, 12, 'Jasper Doge', 50, 300, 50, 200, 100, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (2, 12, 'George Fluffy', 40, 600, 60, 250, 150, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (3, 12, 'Luigi Little', 70, 360, 40, 180, 80, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (4, 12, 'Max Maxington', 20, 100, 25, 120, 40, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (5, 12, 'Chip Munk', 50, 200, 25, 160, 120, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (6, 12, 'Simon Mannington', 60, 340, 120, 210, 50, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (7, 12, 'Pepe Desilva', 23, 300, 30, 140, 20, 1);
INSERT INTO PLAYER (player_id, number, name, shots, hits, steals, rebounds, blocks, coach_id) 
VALUES (8, 12, 'Brad Chadington', 100, 500, 100, 300, 200, 1);

CREATE TABLE GAME (
    game_id INTEGER PRIMARY KEY,
    home TEXT NOT NULL,
    away TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    location_street TEXT,
    location_city TEXT,
    location_postcode TEXT,
    season_id INTEGER,
    FOREIGN KEY (season_id) REFERENCES SEASON(season_id)
);

INSERT INTO GAME (game_id, home, away, date, time, location_street, location_city, location_postcode, season_id) 
VALUES (1, 'Red Team', 'Blue Team', '2024-06-21', '19:00', '456 Arena Dr', 'London', 'A1 C41', 1);
INSERT INTO GAME (game_id, home, away, date, time, location_street, location_city, location_postcode, season_id) 
VALUES (2, 'Yellow Team', 'Red Team', '2024-06-02', '13:00', '123 Stadium St', 'Birmingham', 'B2 D52', 1);
INSERT INTO GAME (game_id, home, away, date, time, location_street, location_city, location_postcode, season_id) 
VALUES (3, 'Red Team', 'Green Team', '2024-06-10', '15:00', '456 Arena Dr', 'London', 'A1 C41', 1);
INSERT INTO GAME (game_id, home, away, date, time, location_street, location_city, location_postcode, season_id) 
VALUES (4, 'Purple Team', 'Red Team', '2024-06-15', '19:00', '789 Pitch Lane', 'Manchester', 'M3 D63', 1);

CREATE TABLE COACH_GAME (
    coach_id INTEGER,
    game_id INTEGER,
    PRIMARY KEY (coach_id, game_id),
    FOREIGN KEY (coach_id) REFERENCES COACH(coach_id),
    FOREIGN KEY (game_id) REFERENCES GAME(game_id)
);

CREATE TABLE COACH_SEASON (
    coach_id INTEGER,
    season_id INTEGER,
    PRIMARY KEY (coach_id, season_id),
    FOREIGN KEY (coach_id) REFERENCES COACH(coach_id),
    FOREIGN KEY (season_id) REFERENCES SEASON(season_id)
);

CREATE TABLE PLAYER_SEASON (
    player_id INTEGER,
    season_id INTEGER,
    PRIMARY KEY (player_id, season_id),
    FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
    FOREIGN KEY (season_id) REFERENCES SEASON(season_id)
);

CREATE TABLE PLAYER_GAME (
    player_id INTEGER,
    game_id INTEGER,
    PRIMARY KEY (player_id, game_id),
    FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
    FOREIGN KEY (game_id) REFERENCES GAME(game_id)
);

INSERT INTO COACH_GAME (coach_id, game_id) VALUES (1, 1);
INSERT INTO COACH_SEASON (coach_id, season_id) VALUES (1, 1);
INSERT INTO PLAYER_SEASON (player_id, season_id) VALUES (1, 1);
INSERT INTO PLAYER_GAME (player_id, game_id) VALUES (1, 1);

SELECT g.game_id, g.home, g.away FROM player p JOIN PLAYER_GAME pg ON p.player_id = pg.player_id
JOIN GAME g ON pg.game_id = g.game_id
WHERE p.player_id = 1;