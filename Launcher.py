import webview
import threading
import time
import random

DEBUG_MODE = False

def switch_to_main():
    time.sleep(random.randint(7, 10))
    for w in webview.windows:
        if w.title == 'Open IDE':
            w.destroy()
        if w.title == 'OPEN IDE':
            w.show()

def main():
    window = webview.create_window(
        'OPEN IDE', 'Editor/Editor.html', width=785, height=515,
        resizable=False, fullscreen=False, frameless=False, text_select=True, hidden=True
    )
    splash = webview.create_window(
        'Open IDE', 'Editor/pages/Launching.html', width=450, height=400,
        resizable=False, fullscreen=False, frameless=True, text_select=True
    )
    print("made by syntaxMORG0 on GitHub")
    print("😄 What's up :D")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    threading.Thread(target=switch_to_main, daemon=True).start()
    webview.start(http_server=True, func=None, debug=DEBUG_MODE)

if __name__ == '__main__':
    main()
