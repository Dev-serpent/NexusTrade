import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import keyboard

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NexusTrade AutoTyper")

        # Message input
        tk.Label(root, text="Message:").grid(row=0, column=0, sticky="e")
        self.message_var = tk.StringVar()
        tk.Entry(root, textvariable=self.message_var, width=40).grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # Timer input
        tk.Label(root, text="Timer (secs, 1-180):").grid(row=1, column=0, sticky="e")
        self.timer_var = tk.StringVar()
        tk.Entry(root, textvariable=self.timer_var, width=10).grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # F-key selector
        tk.Label(root, text="Toggle Key:").grid(row=2, column=0, sticky="e")
        self.fkey_var = tk.StringVar(value="F8")
        fkeys = [f"F{i}" for i in range(1, 13)]
        ttk.Combobox(root, textvariable=self.fkey_var, values=fkeys, width=5, state="readonly").grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(root, text="(Press this key to Start/Stop)").grid(row=2, column=2, sticky="w")

        # Status label
        self.status_var = tk.StringVar(value="Status: Stopped")
        tk.Label(root, textvariable=self.status_var, fg="blue").grid(row=3, column=0, columnspan=3, pady=5)

        # Instruction
        tk.Label(root, text="Click anywhere in this app window before using the toggle key.").grid(row=4, column=0, columnspan=3, pady=2)

        # Control variables
        self.running = False
        self.thread = None

        # Keyboard hook in background
        self.fkey_listener_thread = threading.Thread(target=self.fkey_listener, daemon=True)
        self.fkey_listener_thread.start()

    def fkey_listener(self):
        while True:
            fkey = self.fkey_var.get()
            try:
                keyboard.wait(fkey.lower())
                self.toggle_run()
                while keyboard.is_pressed(fkey.lower()):
                    time.sleep(0.1)
            except Exception:
                pass

    def toggle_run(self):
        if not self.running:
            # Validate inputs
            message = self.message_var.get()
            try:
                timer = int(self.timer_var.get())
                if timer < 1 or timer > 180:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Input Error", "Timer must be an integer between 1 and 180.")
                return

            if not message:
                messagebox.showerror("Input Error", "Message field cannot be empty.")
                return

            self.running = True
            self.status_var.set(f"Status: Running (press {self.fkey_var.get()} to Stop)")
            self.thread = threading.Thread(target=self.type_loop, daemon=True)
            self.thread.start()
        else:
            self.running = False
            self.status_var.set("Status: Stopped")

    def type_loop(self):
        timer = int(self.timer_var.get())
        message = self.message_var.get()
        while self.running:
            # Simulate rapid typing and Enter
            self.simulate_typing_and_enter(message)
            for _ in range(timer * 10):  # Check every 0.1s to allow faster stop
                if not self.running:
                    break
                time.sleep(0.1)

    def simulate_typing_and_enter(self, message):
        self.root.focus_force()
        self.root.after(0, lambda: self.clear_and_type(message))

    def clear_and_type(self, message):
        entry = self.root.winfo_children()[1]  # message input Entry
        entry.delete(0, tk.END)
        entry.insert(0, message)
        entry.event_generate('<Return>')  # Simulate Enter key event on Entry

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()