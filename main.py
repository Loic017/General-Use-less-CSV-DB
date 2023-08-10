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
    

def create():
    note = Note.createNote()
    newId = 0
    with open("CLINotes.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        csvLen = sum(1 for row in reader)
        rowCount = 0
        for row in reader:
            if rowCount == csvLen:
                newId = int(row['ID']) + 1

    with open("CLINotes.csv", "a") as csvfile:
        fieldnames = ['ID', 'Title', 'Content', 'Date']
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
    setup()
    create()

if __name__ == '__main__':
    main()

