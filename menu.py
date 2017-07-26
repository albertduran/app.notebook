import sys
from notebook import *


class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        '''Initialize basic menu.'''
        self.notebook = Notebook()
        self.choices = {
            1: self.show_notes,
            2: self.search_notes,
            3: self.add_note,
            4: self.modify_note,
            5: self.quit
        }

    def _note_exists(self, ident):
        '''Check if notes exists or not.'''
        for i in self.notebook.notes:
            if i.id == ident:
                return True
        return False

    def display_menu(self):
        print("""
        Notebook Menu

        1.Show all Notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit
        """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while(True):
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print ("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print ("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filtro = raw_input("Search for: ")
        notes = self.notebook.search(filtro)
        if notes:
            self.show_notes(notes)
        else:
            print("The word/s has not been found.")

    def add_note(self):
        memo = raw_input("Enter a memo: ")
        tags = raw_input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added")

    def modify_note(self):
        ident = input("Enter a note id: ")
        exist_id = self._note_exists(ident)
        if exist_id:
            memo = raw_input("Enter a memo: ")
            if memo:
                self.notebook.modify_memo(ident, memo)
            tags = raw_input("Enter tags: ")
            if tags:
                self.notebook.modify_tags(ident, tags)
        else:
            print("The note id has not been found.")

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
