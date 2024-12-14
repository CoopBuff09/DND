import tkinter as tk
from tkinter import messagebox


class GUI(tk.Tk):
    def __init__(self):
        """
        Inherits all class info from tk class. 
        It configures a window that has radio buttons for
        class, race, level, and your familiar companion for 
        your character. Also makes a create button
        """
        super().__init__()
        self.title('DND')
        self.configure(background='tan4')
        self.minsize(600, 600)
        self.maxsize(600, 600)
        self.geometry("300x300+50+50")

        self.__dex: int = 0
        self.__strength: int = 0
        self.__constitution: int = 0
        self.__wisdom: int = 0
        self.__intelligence: int = 0
        self.__charisma: int = 0


        '''
        Creates label at the top and packs
        '''
        top = tk.Frame(self, pady=20, bg='darkgoldenrod1')
        welcome = tk.Label(top, text="Dungeons and Dragons Character Creator", bg='darkgoldenrod1')
        welcome.pack(pady=5)
        top.pack()
        '''
         Radio buttons for selecting a class. Creates and packs
        '''
        classes = tk.Frame(self, bg='tan4', pady=20)
        class_selection = tk.StringVar(value='Fighter')

        class_label = tk.Label(classes, text="Select a Class", bg='burlywood4')
        fighter = tk.Radiobutton(classes, text='Fighter', variable=class_selection, value='Fighter', bg='burlywood4')
        wizard = tk.Radiobutton(classes, text='Wizard', variable=class_selection, value='Wizard', bg='burlywood4')
        cleric = tk.Radiobutton(classes, text='Cleric', variable=class_selection, value='Cleric', bg='burlywood4')
        rogue = tk.Radiobutton(classes, text='Rouge', variable=class_selection, value='Rogue', bg='burlywood4')

        class_label.pack()
        fighter.pack(side='left')
        wizard.pack(side='left')
        cleric.pack(side='left')
        rogue.pack(side='left')
        classes.pack(side='top', padx=20, pady=2)

        """ 
        Radio buttons for selecting a race. Creates and packs.
        """
        races = tk.Frame(self, bg='burlywood4')
        race_selection = tk.StringVar(value='Human')

        race_label = tk.Label(races, text="Select a Race", bg='burlywood4')
        human = tk.Radiobutton(races, text='Human', variable=race_selection, value='Human', bg='burlywood4')
        orc = tk.Radiobutton(races, text='Orc', variable=race_selection, value='Orc', bg='burlywood4')
        goblin = tk.Radiobutton(races, text='Goblin', variable=race_selection, value='Goblin', bg='burlywood4')
        elf = tk.Radiobutton(races, text='Elf', variable=race_selection, value='Elf', bg='burlywood4')

        race_label.pack()
        human.pack(side='left')
        orc.pack(side='left')
        goblin.pack(side='left')
        elf.pack(side='left')
        races.pack(side='top', pady=20)
        '''
        Radio buttons for selecting a level. Creates and packs
        '''
        level = tk.Frame(self, pady=10, bg='burlywood4')
        level_selection = tk.StringVar(value='Lvl. 1')

        level_label = tk.Label(level, text="Select a Starting Level", bg='burlywood4')
        lvl_one = tk.Radiobutton(level, text='Lvl. 1', variable=level_selection, value='Lvl. 1', bg='burlywood4')
        level_three = tk.Radiobutton(level, text='Lvl. 3', variable=level_selection, value='Lvl. 3', bg='burlywood4')
        level_six = tk.Radiobutton(level, text='Lvl. 6', variable=level_selection, value='Lvl. 6', bg='burlywood4')
        level_elev = tk.Radiobutton(level, text='Lvl. 11', variable=level_selection, value='Lvl. 11', bg='burlywood4')

        level_label.pack()
        lvl_one.pack(side='left')
        level_three.pack(side='left')
        level_six.pack(side='left')
        level_elev.pack(side='left')
        level.pack(side='top', pady=20)
        '''
        Framework for familiar selection. Creates and packs
        '''
        familiar = tk.Frame(self, bg='burlywood4')
        familiar_selection = tk.StringVar(value='Toad')
        familiar_label = tk.Label(familiar, text='Choose a Familiar', bg='burlywood4')

        toad = tk.Radiobutton(familiar, text='Toad', variable=familiar_selection, value='Toad', bg='burlywood4')
        owl = tk.Radiobutton(familiar, text='Owl', variable=familiar_selection, value='Owl', bg='burlywood4')
        salamander = tk.Radiobutton(familiar, text='Salamander', variable=familiar_selection, value='Salamander', bg='burlywood4')
        ferret = tk.Radiobutton(familiar, text='Ferret', variable=familiar_selection, value='Ferret', bg='burlywood4')

        familiar_label.pack()
        toad.pack(side='left')
        owl.pack(side='left')
        salamander.pack(side='left')
        ferret.pack(side='left')
        familiar.pack(side='top', pady=20)
        '''
        creates frame for entry box and packs
        '''
        name_frame = tk.Frame(self, bg='burlywood4')
        name_label = tk.Label(name_frame, text="Choose Name:", bg='burlywood4')
        name_input = tk.Entry(name_frame, width=30)
        name_label.pack(pady=10)
        name_input.pack(pady=10)
        name_frame.pack(pady=20)

        '''
        Creates a create button
        '''
        generate_button = tk.Button(self, text='Create', command=lambda: [self.show_char(name_input.get(),class_selection.get(),race_selection.get(),level_selection.get(),familiar_selection.get(),self.__strength,self.__constitution,self.__wisdom,self.__intelligence,self.__dex,self.__charisma)])
        generate_button.pack(anchor='s')


   

    def show_char(self, name: str, class_choice: str, race_choice: str, lvl_choice: str, fam_choice: str,stren: int,con: int,wis: int,intel: int,dex:int,char:int) -> None:
        """
        This function handles what the create button does. It checks for entry box
        inputs to make sure there is no numbers and that it isn't blank.
        It then calculates the stats for your character dependent on what
        you choose for your characters level and class. lastly it creates a 
        message box that pops up all of your characters information and stores
        it to a .txt file unique to you characters name.
        """
        file_name: str = name.strip() + '.txt'

        if not name:
            messagebox.showerror("Error", "Stop!\nYou must choose a name for your adventurer!")
            return
    
        if not name.isalpha():  
            messagebox.showerror("Error", "Stop!\n What kind of name has numbers?\nTry again with only letters.")
            return
        
        if lvl_choice == 'Lvl. 1' and class_choice == 'Fighter':
            stren = 15
            con = 14
            dex = 13
            wis = 12
            intel = 10
            char = 8
        elif lvl_choice == 'Lvl. 3' and class_choice == 'Fighter':
            stren = 16
            con = 15
            dex = 13
            wis = 12
            intel = 10
            char = 8
        elif lvl_choice == 'Lvl. 6' and class_choice == 'Fighter':
            stren = 17
            con = 16
            dex = 14
            wis = 12
            intel = 10
            char = 8
        elif lvl_choice == 'Lvl. 11' and class_choice == 'Fighter':
            stren = 20
            con = 18
            dex = 14
            wis = 12
            intel = 10
            char = 8
        elif lvl_choice == 'Lvl. 1' and class_choice == 'Wizard':
            stren = 8
            con = 14
            dex = 13
            wis = 12
            intel = 15
            char = 10
        elif lvl_choice == 'Lvl. 3' and class_choice == 'Wizard':
            stren = 8
            con = 14
            dex = 13
            wis = 15
            intel = 16
            char = 10
        elif lvl_choice == 'Lvl. 6' and class_choice == 'Wizard':
            stren = 8
            con = 16
            dex = 13
            wis = 15
            intel = 17
            char = 10
        elif lvl_choice == 'Lvl. 11' and class_choice == 'Wizard':
            stren = 8
            con = 16
            dex = 13
            wis = 17
            intel = 20
            char = 10
        elif lvl_choice == 'Lvl. 1' and class_choice == 'Cleric':
            stren = 13
            con = 15
            dex = 10
            wis = 15
            intel = 8
            char = 12
        elif lvl_choice == 'Lvl. 3' and class_choice == 'Cleric':
            stren = 13
            con = 17
            dex = 10
            wis = 16
            intel = 8
            char = 12
        elif lvl_choice == 'Lvl. 6' and class_choice == 'Cleric':
            stren = 13
            con = 17
            dex = 10
            wis = 18
            intel = 8
            char = 12
        elif lvl_choice == 'Lvl. 11' and class_choice == 'Cleric':
            stren = 13
            con = 17
            dex = 10
            wis = 20
            intel = 8
            char = 12
        elif lvl_choice == 'Lvl. 1' and class_choice == 'Rogue':
            stren = 8
            con = 14
            dex = 15
            wis = 13
            intel = 12
            char = 10
        elif lvl_choice == 'Lvl. 3' and class_choice == 'Rogue':
            stren = 8
            con = 14
            dex = 17
            wis = 13
            intel = 12
            char = 11
        elif lvl_choice == 'Lvl. 6' and class_choice == 'Rogue':
            stren = 8
            con = 14
            dex = 18
            wis = 13
            intel = 12
            char = 11
        elif lvl_choice == 'Lvl. 11' and class_choice == 'Rogue':
            stren = 8
            con = 14
            dex = 20
            wis = 13
            intel = 12
            char = 11

        messagebox.showinfo("New Character", f"Your Name: {name}\nClass: {class_choice}\nRace: {race_choice}\nStarting Level: {lvl_choice}\nFamiliar: {fam_choice}\nStrength: {stren}\nDexterity: {dex}\nConstitution: {con}\nWisdom: {wis}\nIntelligence: {intel}\nCharisma: {char}")
        
        with open(file_name,'w') as file:
            file.write(f"Your Name: {name}\nClass: {class_choice}\nRace: {race_choice}\nStarting Level: {lvl_choice}\nFamiliar: {fam_choice}\nStrength: {stren}\nDexterity: {dex}\nConstitution: {con}\nWisdom: {wis}\nIntelligence: {intel}\nCharisma: {char}")
