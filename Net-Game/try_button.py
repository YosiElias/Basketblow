import tkinter as tk
label = tk.Label(text='Instead of the space button,  Blow!\nIf you want back to menu please click on \'esc\'', font=('Times','30'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+{}+{}".format(150, 550))
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()