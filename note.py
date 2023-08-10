import datetime

class Note:
    def __init__(self, title, note, date):
        self.title = title
        self.note = note
        self.date = date

    def __str__(self):
        return f"{self.title} // {self.note} // Written: {self.date}"
    
    def getTitle(self):
        return self.title
    
    def getText(self):
        return self.note
    
    def getDate(self):
        return self.date
    
    def setTitle(self, title):
        self.title = title

    def setText(self, note):
        self.note = note
    
    @classmethod
    def createNote(cls):
        print("Enter a title for your note")
        title = input(">> ")
        print("Enter your note")
        note = input(">> ")
        date = datetime.datetime.now()
        return cls(title, note, date)
