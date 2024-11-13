import gi
from gtts import gTTS
import os
import subprocess  # Use subprocess to ensure synchronous execution
from gi.repository import Pango
# GTK version requirement
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Function for handling button clicks
def on_button_click(widget, letter):
    if letter:  # Check if the letter is not silent
        print(f"Speaking: {letter}")
        # Create the TTS object with Russian language
        tts = gTTS(text=letter, lang='ru')
        # Save the speech to a temporary file
        tts.save("letter.mp3")
        # Play the speech using mpg123 synchronously
        subprocess.run(["mpg123", "letter.mp3"])

# Mapping of Russian letters and their corresponding pronunciation
key_map = {
    'А': 'А',
    'Б': 'Б',
    'В': 'В',
    'Г': 'Г',
    'Д': 'Д',
    'Е': 'Е',
    'Ё': 'Ё',
    'Ж': 'Ж',
    'З': 'З',
    'И': 'И',
    'Й': 'Й',
    'К': 'К',
    'Л': 'Л',
    'М': 'М',
    'Н': 'Н',
    'О': 'О',
    'П': 'П',
    'Р': 'Р',
    'С': 'С',
    'Т': 'Т',
    'У': 'У',
    'Ф': 'Ф',
    'Х': 'Х',
    'Ц': 'Ц',
    'Ч': 'Ч',
    'Ш': 'Ш',
    'Щ': 'Щ',
    'Ъ': '',  # Silent hard sign
    'Ы': 'Ы',
    'Ь': '',  # Silent soft sign
    'Э': 'Э',
    'Ю': 'Ю',
    'Я': 'Я'
}

# Main GTK application class
class RussianAlphabetApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gtk - Russian Alphabet!")
        self.set_border_width(10)
        self.set_resizable(False)

        grid = Gtk.Grid()
        self.add(grid)

        row, col = 0, 0
        max_cols = 8  # Adjust this value to fit all letters evenly

        for letter in key_map:
            button = Gtk.Button(label=letter)
            button.set_size_request(50, 50)  # Set button size
            button.modify_font(Pango.FontDescription("50"))  # Set font size directly on the button
            button.connect("clicked", on_button_click, letter)
            grid.attach(button, col, row, 1, 1)
            col += 1
            if col >= max_cols:  # Move to the next row when reaching max columns
                col = 0
                row += 1

if __name__ == "__main__":
    app = RussianAlphabetApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

