# notes.py

import json
import os

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(note_text):
    notes = load_notes()
    note_id = len(notes) + 1
    notes[note_id] = note_text
    save_notes(notes)
    print("Not eklendi!")

def list_notes():
    notes = load_notes()
    if not notes:
        print("Henüz not yok.")
    for note_id, note_text in notes.items():
        print(f"{note_id}: {note_text}")

def delete_note(note_id):
    notes = load_notes()
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print("Not silindi!")
    else:
        print("Geçersiz not ID'si.")
