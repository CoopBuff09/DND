import tkinter as tk
from tkinter import messagebox


class GUI(tk.Tk):

    class_final = ''
    race_final = ''
    level_final = ''
    familiar_final = ''

    def __init__(self):
        super().__init__()
        self.title('DND')
        self.configure(background='tan4')
        self.minsize(600, 600)
        self.maxsize(600, 600)
        self.geometry("300x300+50+50")

        # Creates label at the top
        top = tk.Frame(self, pady=20, bg='darkgoldenrod1')
        welcome = tk.Label(top, text="Dungeons and Dragons Character Creator", bg='darkgoldenrod1')
        welcome.pack(pady=5)
        top.pack()

        # Radio buttons for selecting a class
        classes = tk.Frame(self, bg='tan4', pady=20)
        class_selection = tk.StringVar(value=1)

        class_label = tk.Label(classes, text="Select a Class", bg='burlywood4')
        fighter = tk.Radiobutton(classes, text='Fighter', variable=class_selection, value=1, bg='burlywood4')
        wizard = tk.Radiobutton(classes, text='Wizard', variable=class_selection, value=2, bg='burlywood4')
        cleric = tk.Radiobutton(classes, text='Cleric', variable=class_selection, value=3, bg='burlywood4')
        rogue = tk.Radiobutton(classes, text='Rouge', variable=class_selection, value=4, bg='burlywood4')

        class_label.pack()
        fighter.pack(side='left')
        wizard.pack(side='left')
        cleric.pack(side='left')
        rogue.pack(side='left')
        classes.pack(side='top', padx=20, pady=2)

        # Radio buttons for selecting a race
        races = tk.Frame(self, bg='burlywood4')
        race_selection = tk.StringVar(value=1)

        race_label = tk.Label(races, text="Select a Race", bg='burlywood4')
        human = tk.Radiobutton(races, text='Human', variable=race_selection, value=1, bg='burlywood4')
        orc = tk.Radiobutton(races, text='Orc', variable=race_selection, value=2, bg='burlywood4')
        goblin = tk.Radiobutton(races, text='Goblin', variable=race_selection, value=3, bg='burlywood4')
        elf = tk.Radiobutton(races, text='Elf', variable=race_selection, value=4, bg='burlywood4')

        race_label.pack()
        human.pack(side='left')
        orc.pack(side='left')
        goblin.pack(side='left')
        elf.pack(side='left')
        races.pack(side='top', pady=2)

        # Radio buttons for selecting a level
        level = tk.Frame(self, pady=10, bg='burlywood4')
        level_selection = tk.StringVar(value=1)

        level_label = tk.Label(level, text="Select a Starting Level", bg='burlywood4')
        lvl_one = tk.Radiobutton(level, text='Lvl. 1', variable=level_selection, value=1, bg='burlywood4')
        level_three = tk.Radiobutton(level, text='Lvl. 3', variable=level_selection, value=2, bg='burlywood4')
        level_six = tk.Radiobutton(level, text='Lvl. 6', variable=level_selection, value=3, bg='burlywood4')
        level_elev = tk.Radiobutton(level, text='Lvl. 11', variable=level_selection, value=4, bg='burlywood4')

        level_label.pack()
        lvl_one.pack(side='left')
        level_three.pack(side='left')
        level_six.pack(side='left')
        level_elev.pack(side='left')
        level.pack(side='top', pady=2)

        # Framework for familiar selection
        familiar = tk.Frame(self, bg='burlywood4')
        familiar_selection = tk.StringVar(value=1)
        familiar_label = tk.Label(familiar, text='Choose a Familiar', bg='burlywood4')

        toad = tk.Radiobutton(familiar, text='Toad', variable=familiar_selection, value=1, bg='burlywood4')
        owl = tk.Radiobutton(familiar, text='Owl', variable=familiar_selection, value=2, bg='burlywood4')
        salamander = tk.Radiobutton(familiar, text='Salamander', variable=familiar_selection, value=3, bg='burlywood4')
        ferret = tk.Radiobutton(familiar, text='Ferret', variable=familiar_selection, value=4, bg='burlywood4')

        familiar_label.pack()
        toad.pack(side='left')
        owl.pack(side='left')
        salamander.pack(side='left')
        ferret.pack(side='left')
        familiar.pack(side='top', pady=2)

        # Input for name
        name_frame = tk.Frame(self, bg='burlywood4')
        name_label = tk.Label(name_frame, text="Choose Name:", bg='burlywood4')
        name_input = tk.Entry(name_frame, width=30)
        name_label.pack(pady=10)
        name_input.pack(pady=10)
        name_frame.pack()

        # Create button
        generate_button = tk.Button(self, text='Create', command=lambda: [self.find_class(class_selection.get(),self.class_final),self.show_char(name_input.get(),class_selection.get(),race_selection.get())])
        generate_button.pack(anchor='s')


    def find_class(self,class_value,class_final):
        
        if class_value ==1:
            class_final = 'Fighter'
        elif class_value ==2:
            class_final = 'Wizard'
        elif class_value ==3:
            class_final = 'Cleric'
        else:
            class_final = 'Rouge'

    def show_char(self, name, class_choice, race_choice):
        if class_choice == 1:
            class_choice = 'Fighter'
        messagebox.showinfo("New Character", f"Your Name: {name}\nClass: {class_choice}\nRace: {race_choice}")









# class Character:
#     def __init__(self,stren=10,dex=10,con=10,intel=10,wis=10,char=10):
#         self.stren = stren
#         self.dex = dex
#         self.con = con
#         self.intel = intel
#         self.wis = wis
#         self.char = char
#         self.speed = 30
        
#     def return_stats(self):
#         return f'Strength {self.stren} Dexterity: {self.dex} Constition: {self.con} Intelligence {self.intel} Wisdom: {self.wis} Charisma: {self.char}'
    
    



# class Orc(Character):
#     def __init__(self):
#         super().__init__(stren=14, con=12)
#         self.race = 'Orc'

# class Elf(Character):
#     def __init__(self):
#         super().__init__(dex=12, char= 14)    
#         self.race = 'Elf'

# class Goblin(Character):
#     def __init__(self):
#         super().__init__(dex=12, con=11)
#         self.race = 'Elf'

# class Human(Character):
#     def __init__(self):
#         super().__init__(stren=11,dex=11,con=11,intel=11,wis=11,char=11)
#         self.race = 'Human'

# human = Human()
# orc = Orc()
# elf = Elf()
# goblin = Goblin()

# print(human.return_stats())
# print(human.race)
