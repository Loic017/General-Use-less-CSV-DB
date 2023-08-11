# General Use(less) CSV DB

A user friendly command line python program that setups local csv databases (aka sets up regular csv files that you can maintain on the command line).
Dbs arent secure, just for fun - or another note taking tool.

Pros:

-   Uses a prompt based system to guide the user through database creation, no need for long multiple line statements

Cons:

-   Doesnt have much real purpose

# To Do

-   [x] Create CSV table: Setup a new CSV file
-   [x] Create CSV headings: Set the headings for a created CSV
-   [x] Drop CSV table: Delete whole CSV table
-   [] Add heading: Add a heading to an existing CSV
-   [] Drop heading: Delete a heading from an existing CSV
-   [] Modify heading: Change a heading in an existing CSV
-   [] Connect to a CSV: Open a CSV table

    (Maybe ->)

-   [] CSV Pins: Add a pin to a CSV (?), Can only access csv with pin (Kind of useless since you can just open the csv file but why not)

# Setup

## Adding to Path

1. Install files (GUCDB.py & note.py) and put it into desired directory
2. Copy directory path
3. Go to start menu and search for environment variables
4. Select "edit environment variables"
5. In the "advanced" tab select "environment variables at the bottom
6. Select path in user variables and press edit
7. Press new on the opened window and paste in the directory path

## Using the script

1. Open command prompt
2. Enter "GUCDB.py" for a list of commands
3. Enter "GUCDB.py" with the command following it (e.g. GUCDB.py create)
