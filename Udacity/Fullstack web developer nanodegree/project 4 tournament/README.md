## Project
Udacity-tournament is a simple database project completed for Udacity’s full-stack nano degree program. 
The project demonstrates the design and use of a PostgreSQL database to manage a swiss-system tournament, 
which is a non-elimination tournament system used in certain sport and game competitions.

This project was designed to teach student how to create and use database through the use of database schemes 
and how to manipulate the data inside the database. This project has two parts: defining the database schema 
(SQL table definitions) in tournament.sql, and writing code that will use it to track a Swiss tournament in tournament.py.

## FILES

project 4 tournament

├── tournament.py
├── tournament.sql
├── tournament_test.py
├── README.md

tournament.py - this file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program).

tournament.sql - this file is used to set up your database schema ( the table representation of your data structure).

tournament_test.py - this is a client program which will use your functions written in the tournament.py module.

## Tests

1. Open Terminal and browse to the vagrant folder
2. Type vagrant up
3. Type vagrant ssh
4. Type cd /vagrant/tournament
5. Type sql
6. copy the contents of tournament.sql and paste in to the terminal window
7. Type\q to quit out of PSQL
8. Run the tests
9. In the terminal type python tournament_test.py

## RESULTS

1. countPlayers() returns 0 after initial deletePalyers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
