import tkinter as tk
from tkinter import messagebox




def create_button():
    create_window = tk.Toplevel(root)
    create_window.title("New Window")
    create_window
    tk.Label(create_window, text="This is a new window").pack()



root = tk.Tk()
root.title('DND')
root.configure(background='tan4')
root.minsize(600,600)
root.maxsize(600,600)
root.geometry("300x300+50+50")

    

    #creates label at the top
top = tk.Frame(pady=20,bg='darkgoldenrod1')
welcome = tk.Label(top,text="Dungeons and Dragons Character Creator",bg='darkgoldenrod1')
welcome.pack(pady=5)
top.pack()
    
    
    #Radio buttons for selecting a class
classes = tk.Frame(root,bg='tan4',pady=20)
class_selection = tk.StringVar(value = 0)

class_label = tk.Label(classes, text = "Select a Class",bg='burlywood4')
fighter = tk.Radiobutton(classes, text = 'Fighter', variable = class_selection, value = 1,bg='burlywood4')
wizard = tk.Radiobutton(classes, text = 'Wizard', variable = class_selection, value = 2,bg='burlywood4')
cleric = tk.Radiobutton(classes, text = 'Cleric', variable = class_selection, value = 3,bg='burlywood4')
rogue = tk.Radiobutton(classes, text = 'Rouge', variable = class_selection, value = 4,bg='burlywood4')

class_label.pack()
fighter.pack(side='left')
wizard.pack(side='left')
cleric.pack(side='left')
rogue.pack(side='left')
classes.pack(side='top',padx=20,pady=2)

    #Radio buttons for selecting a race
races = tk.Frame(root,bg='burlywood4')
race_selection = tk.StringVar(value = 0)

race_label = tk.Label(races, text = "Select a Race",bg='burlywood4')
human = tk.Radiobutton(races, text = 'Human', variable = race_selection, value = 1,bg ='burlywood4')
orc = tk.Radiobutton(races, text = 'Orc', variable = race_selection, value = 2,bg='burlywood4')
goblin = tk.Radiobutton(races, text = 'Goblin', variable = race_selection, value = 3,bg='burlywood4')
elf = tk.Radiobutton(races, text = 'Elf', variable = race_selection, value = 4,bg='burlywood4')

race_label.pack()
human.pack(side='left')
orc.pack(side='left')
goblin.pack(side='left')
elf.pack(side='left')
races.pack(side='top',pady=2)

    #Radio buttons for selecting a level
level = tk.Frame(root,pady=10,bg='burlywood4')
level_selection = tk.StringVar(value = 0)

level_label = tk.Label(level, text = "Select a Starting Level",bg='burlywood4')
lvl_one = tk.Radiobutton(level, text = 'Lvl. 1', variable = level_selection, value = 1,bg='burlywood4')
level_three = tk.Radiobutton(level, text = 'Lvl. 3', variable = level_selection, value = 2,bg='burlywood4')
level_six = tk.Radiobutton(level, text = 'Lvl. 6', variable = level_selection, value = 3,bg='burlywood4')
level_elev = tk.Radiobutton(level, text = 'Lvl. 11', variable = level_selection, value = 4,bg='burlywood4')

level_label.pack()
lvl_one.pack(side='left')
level_three.pack(side='left')
level_six.pack(side='left')
level_elev.pack(side='left')
level.pack(side='top',pady=2)

    #framework for familoiar selection
familiar = tk.Frame(root,bg='burlywood4')
familiar_selection = tk.StringVar(value=0)
familiar_label = tk.Label(familiar, text='Choose a subclass',bg='burlywood4')
familiar_label.pack(side='left')
familiar.pack(side='top')

    #creates create button
generate_button = tk.Button(root,text='Create',command =create_button)
generate_button.pack(anchor='s')

   

root.mainloop()




