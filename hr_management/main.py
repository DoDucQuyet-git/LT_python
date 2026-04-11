import tkinter as tk
from controllers.hr_controller import HRController
from views.main_view import MainView

if __name__ == "__main__":
    root = tk.Tk()
    controller = HRController()
    app = MainView(root, controller)
    root.mainloop()
