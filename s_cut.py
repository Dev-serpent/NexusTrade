import os
import sys

def create_shortcut(target, shortcut_name, icon_path=None):
    try:
        import winshell
        from win32com.client import Dispatch
    except ImportError:
        print("Required modules not found. Please run: pip install pywin32 winshell")
        return

    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    if icon_path and os.path.exists(icon_path):
        shortcut.IconLocation = os.path.abspath(icon_path)
    else:
        shortcut.IconLocation = target  # fallback: use target's icon
    shortcut.save()
    print(f"Shortcut created at: {shortcut_path}")

if __name__ == "__main__":
    # Defaults: shortcut for launcher.bat
    shortcut_name = "NexusTrade Launcher"
    target = os.path.abspath("launcher.bat")
    icon_path = os.path.abspath("logo.ico")  # expects logo.ico in the same folder

    if len(sys.argv) > 1:
        target = os.path.abspath(sys.argv[1])
    if len(sys.argv) > 2:
        shortcut_name = sys.argv[2]
    if len(sys.argv) > 3:
        icon_path = os.path.abspath(sys.argv[3])

    create_shortcut(target, shortcut_name, icon_path)