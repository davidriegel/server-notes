import sys
import json
import time
import os

class printColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def now() -> str:
    return time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    
def createNote(title: str, note: str):
    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
    data = json.load(json_data)
    json_data.close()
    
    for existing_note in data['notes']:
        if existing_note['title'] == title:
            return print(f"{printColors.FAIL}Note already exists{printColors.ENDC}")
    
    data['notes'].append({
        'createdAt': now(),
        'updatedAt': now(),
        'title': title,
        'note': note
    })
    
    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'), 'w')
    json.dump(data, json_data)
    json_data.close()
    
    return print(f"{printColors.OKGREEN}Note created{printColors.ENDC}")

def removeNote(title: str):
    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
    data = json.load(json_data)
    json_data.close()
    
    for existing_note in data['notes']:
        if existing_note['title'] == title:
            data['notes'].remove(existing_note)
            json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'), 'w')
            json.dump(data, json_data)
            json_data.close()
            
            return print(f"{printColors.OKGREEN}Note removed{printColors.ENDC}")
    
    return print(f"{printColors.FAIL}Note not found{printColors.ENDC}")
    

def showNote(title: str):
    if title == '':
        return showAllNotes()

    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
    data = json.load(json_data)
    json_data.close()
    
    for note in data['notes']:
        if note['title'] == title:
            return print(f"{printColors.BOLD}{printColors.HEADER}Showing note: {printColors.UNDERLINE}{title}{printColors.ENDC}\n{printColors.OKCYAN}Created at: {note['createdAt']}{printColors.ENDC}\n{printColors.WARNING}Last update: {note['updatedAt']}{printColors.ENDC}\n\n{printColors.OKGREEN}{note['note']}{printColors.ENDC}")
        
    return print(f"{printColors.FAIL}Note not found{printColors.ENDC}")

        
def showAllNotes():
    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
    data = json.load(json_data)
    json_data.close()
        
    notes = f"{printColors.BOLD}{printColors.HEADER}Showing all notes:{printColors.ENDC}\n\n"
    if len(data['notes']) == 0:
        return print(f"{printColors.FAIL}No notes found{printColors.ENDC}")
    
    for note in data['notes']:
        notes += f"{printColors.OKGREEN}Title:{printColors.ENDC} {printColors.UNDERLINE}{note['title']}{printColors.ENDC}\n"
        
    return print(notes)

def updateNote(title: str, note: str):
    json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
    data = json.load(json_data)
    json_data.close()
    
    for existing_note in data['notes']:
        if existing_note['title'] == title:
            existing_note['note'] = note
            existing_note['updatedAt'] = now()
            json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'), 'w')
            json.dump(data, json_data)
            json_data.close()
            
            return print(f"{printColors.OKGREEN}Note updated{printColors.ENDC}")
    
    return print(f"{printColors.FAIL}Note not found{printColors.ENDC}")

def showHelpMenu():
    return print(f"{printColors.HEADER}{printColors.UNDERLINE}{printColors.BOLD}This project is only here to take notes or quick thoughts from the CMD for later :){printColors.ENDC}\n{printColors.BOLD}I may add a UI at a later date{printColors.ENDC}\n\n{printColors.OKCYAN}py notes.py help {printColors.ENDC}| Shows you this menu.\n{printColors.OKCYAN}py add <title> <note> {printColors.ENDC}| Create a new note\n{printColors.OKCYAN}py remove <title> {printColors.ENDC}| Delete notes\n{printColors.OKCYAN}py show {printColors.ENDC}| Overview of all notes\n{printColors.OKCYAN}py show <title> {printColors.ENDC}| Show note information{printColors.ENDC}")

if __name__ == '__main__':
    try:
        json_data = open(os.path.join(os.path.dirname(__file__), 'notes.json'))
        json_data.close()
    except FileNotFoundError:
        createJSON = open(os.path.join(os.path.dirname(__file__), 'notes.json'), 'w')
        createJSON.write('{"notes": []}')
        createJSON.close()
    
    if len(sys.argv) < 2:
        print('Usage: py notes.py <help|add|remove|show|update> <title> <optional:note>')
        sys.exit(1)
        
    action = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else ''
    note = sys.argv[3] if len(sys.argv) > 3 else ''
    
    if action in ["add", "update"] and len(sys.argv) < 4:
        print('Usage: py notes.py <add|update> <title> <note>')
        sys.exit(1)
    
    if len(title) > 25:
        print('Title must be less than 25 characters')
        sys.exit(1)
    
    if action == 'add':
        createNote(title=title, note=note)
    elif action == 'remove':
        removeNote(title=title)
    elif action == 'show':
        showNote(title=title)
    elif action == 'update':
        updateNote(title=title, note=note)
    elif action == 'help':
        showHelpMenu()
    else:
        print('Unknown action: ' + action)
        sys.exit(1)
    
    sys.exit(0)
