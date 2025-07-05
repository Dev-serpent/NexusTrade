# How to Run NexusTrade AutoTyper

Welcome! Follow these steps to run the NexusTrade AutoTyper application:

---

## 1. Unzip the Files
- First, click the green **Code** button on GitHub, then choose **Download ZIP**.
- **Right-click** the ZIP file and select **Extract All**.
- Extract all files to a folder on your computer (e.g., your Desktop).

---

## 2. Install Python (if not already installed)
- Download Python from https://www.python.org/downloads/ (version 3.8 or newer recommended).
- You can also install Python from the Microsoft Store.
- During installation, **make sure to check the box that says "Add Python to PATH"**.
- Complete the installation.

---

## 3. Install Required Python Packages
- Open **Command Prompt** (press Win + R, type cmd, then hit Enter).
- Navigate to the folder where you unzipped the files. For example:
  cd Desktop\NexusTradeAutoTyper
- Install the required packages by running:
  pip install -r requirements.txt


---

## 4. Run the Application
- Double-click the setup.bat file to automatically create a desktop shortcut.
- To start the application:
  - Either double-click the desktop shortcut created, or
  - Double-click the launcher.bat file in the folder.

---

## 5. How to Use It
1. Enter the message you want to auto-send.
2. Set a timer interval in seconds (must be between 1 and 180).
3. Type the title of the target window (e.g., Untitled - Notepad, Discord, Google Chrome).
4. Select your F-key toggle from the dropdown (F1–F12).
5. Click into the target app window (e.g., Notepad).
6. Press the chosen F-key to start typing.
7. Press it again to stop.

---

## 6. Troubleshooting

- "No module named ..."
  Run:
    pip install -r requirements.txt

- "Python is not recognized"
  Ensure Python is installed and added to PATH.

- Not typing into the correct app
  Make sure the window title is accurate and currently visible.
  Try running the app as Administrator for full keyboard access.

- Need to debug?
  Open Command Prompt in the folder and run:
    python app.py

  Check the terminal for error messages.

---

You're all set — enjoy automating with NexusTrade AutoTyper!
