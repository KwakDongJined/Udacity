-- Table definitions for the tournament project.
-- Drop the database 'tournament' if it exists
DROP DATABASE IF EXISTS tournament;

-- Create the database 'tournament'
CREATE DATABASE tournament;

-- Connect to the database 'tournament'
\c tournament;

-- Create table 'players'
CREATE TABLE players (id SERIAL primary key, name TEXT);

-- Create table 'matches'
CREATE TABLE matches (id SERIAL primary key,
                      winner INTEGER REFERENCES players (id),
                      loser INTEGER REFERENCES players (id));


-- Create a view of standings (player rankings, names, matches)
CREATE VIEW standings AS
SELECT players.id, players.name,
(SELECT count(*) FROM matches WHERE players.id = matches.winner) AS wins,
(SELECT count(*) FROM matches WHERE players.id IN (winner, loser)) AS played
FROM players
ORDER BY wins DESC;
