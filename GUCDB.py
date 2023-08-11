from note import Note
import csv
import os

def setup():
    if not os.path.exists("CLINotes.csv"):
        with open("CLINotes.csv", "w") as csvfile:
            fieldnames = ['ID', 'Title', 'Note', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("Success! Setup complete.")
    else:
        print("CLINotes has already been setup.")

def getCSVLen():
    with open("CLINotes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        csvLen = 0
        for row in reader:
            csvLen += 1
        return csvLen

def getNewID():
        with open("CLINotes.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            csvLen = getCSVLen()
            rowCount = 0
            for row in reader:
                rowCount += 1
                if rowCount == csvLen:
                    return int(row['ID']) + 1
            return 0

def create():
    note = Note.createNote()
    newId = getNewID()
    with open("CLINotes.csv", "a") as csvfile:
        fieldnames = ['ID', 'Title', 'Note', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'ID': newId, 'Title': note.title, 'Note': note.note, 'Date': note.date})
    print("Note Created")

def displayNotes():
    with open("CLINotes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("ID: " + row['ID'])
            print("Title: " + row['Title'])
            print("")

def displayNote():
    noteId = input("Enter note ID")
    with open("CLINotes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ID'] == noteId:
                print("Title: " + row['Title'])
                print("Content: " + row['Content'])
                print("Date: " + row['Date'])
                print("")
                return
    print("Note not found.")

def editNoteTitle():
    noteId = input("Enter note ID")
    newTitle = input("Enter new title")
    with open("CLINotes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ID'] == noteId:
                row['Title'] = newTitle
                print("Title changed.")
                return
    print("Note not found.")


def main():
    print("Welcome to CLINotes!")
    print("              ")
    print("Commands:")
    print("> setup - Setup CLI notes")
    print("> create - Create a note")
    print("> editNoteTitle - Edit a note title")
    print("> displayNotes - Display all notes")
    print("> displayNote - Display a note")

if __name__ == '__main__':
    main()
