import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import keyboard
import pyautogui

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NexusTrade AutoTyper")

        # Message input
        ttk.Label(root, text="Message:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.message_entry = ttk.Entry(root, width=40)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        # Timer input
        ttk.Label(root, text="Timer (secs):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.timer_entry = ttk.Entry(root, width=10)
        self.timer_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # F-key toggle selection
        ttk.Label(root, text="Toggle Key:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.fkey_var = tk.StringVar()
        fkeys = [f"F{i}" for i in range(1, 13)]
        self.fkey_combo = ttk.Combobox(root, textvariable=self.fkey_var, values=fkeys, state="readonly", width=10)
        self.fkey_combo.current(0)
        self.fkey_combo.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Status label
        self.status_label = ttk.Label(root, text="Press selected F-key to start/stop", foreground="blue")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Internal state
        self.running = False
        self.listener_thread = threading.Thread(target=self.listen_toggle_key, daemon=True)
        self.listener_thread.start()

    def listen_toggle_key(self):
        while True:
            selected_key = self.fkey_var.get().lower()
            if selected_key:
                keyboard.wait(selected_key)
                self.toggle_run()

    def toggle_run(self):
        self.running = not self.running
        if self.running:
            self.status_label.config(text="AutoTyper Running... (Press key to stop)", foreground="green")
            self.root.iconify()
            self.start_typing()
        else:
            self.status_label.config(text="Stopped. Press selected F-key to start", foreground="red")

    def start_typing(self):
        def run():
            try:
                timer = int(self.timer_entry.get())
                if not (1 <= timer <= 180):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Timer", "Timer must be an integer between 1 and 180.")
                self.running = False
                self.status_label.config(text="Invalid input. Restart.", foreground="red")
                return

            message = self.message_entry.get().strip()
            if not message:
                messagebox.showerror("Missing Input", "Message cannot be empty.")
                self.running = False
                return

            while self.running:
                self.simulate_typing_and_enter(message)
                time.sleep(timer)

        threading.Thread(target=run, daemon=True).start()

    def simulate_typing_and_enter(self, message):
        try:
            pyautogui.write(message, interval=0)
            pyautogui.press('enter')
        except Exception as e:
            self.running = False
            self.status_label.config(text="Error: " + str(e), foreground="red")
            messagebox.showerror("Typing Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
