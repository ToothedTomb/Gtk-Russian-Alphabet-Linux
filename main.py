import gi
from gtts import gTTS
import os
import subprocess  # Use subprocess to ensure synchronous execution

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
    'Ш': import shutil

# Check if mpg123 is installed
if shutil.which("mpg123") is None:
    print("Error: mpg123 is not installed. Please install mpg123 to use this application.")
    exit(1)'Ш',
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
        self.set_resizable(False)  # Prevent window resizing

        grid = Gtk.Grid()
        self.add(grid)

        row, col = 0, 0
        for letter in key_map:
            button = Gtk.Button(label=letter)
            button.set_size_request(100, 100)  # Increase button size (width, height)
            
            # Set the font size of the button text
            button.get_style_context().add_class("big-font")

            button.connect("clicked", on_button_click, letter)
            grid.attach(button, col, row, 1, 1)
            col += 1
            if col > 7:  # Adjust for button layout
                col = 0
                row += 1

        # Adding custom CSS to set larger font size for buttons
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(b"""
        button.big-font {
            font-size: 90px;  /* Adjust the font size here */
            font-weight: bold;
        }
        """)
        Gtk.StyleContext.add_provider_for_screen(
            self.get_screen(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == "__main__":
    app = RussianAlphabetApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

