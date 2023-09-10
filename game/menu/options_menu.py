from tkinter import *
#from PIL import ImageTk, Image
import opening_menu_reformed

class OptionsMenu:
    def __init__(self):
        self.options_root = Tk()
        self.options_root.title("Game setup")
        self.options_root.geometry("600x600")

        self.text_size = StringVar()
        self.text_size_options = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
                           36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
        self.text_size.set(40)

        self.text_type = StringVar()
        self.text_type.set("Arial-Black")
        self.text_type_options = ["Arial-Black", "Roboto", "Open Sans", "Monteserrat", "Lato", "Roboto Mono", "Oswald",
                          "Raleway", "Ubuntu", "Phudu"]
    def collect_values(self):
        font_selected = self.text_type.get()
        text_size_selected = self.text_size.get()
        self.options_root.destroy()
        menu = opening_menu_reformed.OpeningMenu(font_selected, text_size_selected)
        menu.main_menu()

    def main(self):
        font_options = OptionMenu(self.options_root, self.text_type, *self.text_type_options)
        font_options.pack(pady=20)

        text_size_options = OptionMenu(self.options_root, self.text_size, *self.text_size_options)
        text_size_options.pack(pady=20)

        font_button = Button(self.options_root, text="choose your font and text size", command=self.collect_values)
        font_button.pack(pady=10)

        self.options_root.mainloop()
"""option = OptionsMenu()
option.main()"""