Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...     for r_idx, reihe in enumerate(map_daten):
...         for c_idx, kachel in enumerate(reihe):
...             if kachel == 1:
...                 canvas.create_rectangle(c_idx*40, r_idx*40, c_idx*40+40, r_idx*40+40, fill="blue", tags="bk")
...
...     # Pacman (sy{iz{pm)
...     global pacman
...     pacman = canvas.create_oval(45, 45, 75, 75, fill="yellow")
...     print("IZ-FLOW OS: SYSTEM L{1}")
...
... # GRAFIK-SETUP
... root = tk.Tk()
... root.title("IZ-FLOW OS - SECURITY SHELL")
... canvas = tk.Canvas(root, width=400, height=400, bg="black")
... canvas.pack()
...
... # START-UI (sy{pw)
... t1 = canvas.create_text(200, 100, text="SYSTEM LOCKED", fill="red", font=("Courier", 18))
... t2 = canvas.create_text(200, 140, text="GIB HEX-CODE EIN (A1):", fill="white", font=("Courier", 10))
... pw_input = tk.Entry(root, bg="black", fg="lime", insertbackground="white", justify="center")
... pw_window = canvas.create_window(200, 180, window=pw_input)
...
... root.bind('<Return>', lambda e: check_pw(e, pw_input, canvas, [t1, t2, pw_window]))
...
... # Steuerung (in{ky)
... root.bind("<Right>", lambda e: canvas.move(pacman, 40, 0) if system_status == "BOOTING" else None)
... root.bind("<Left>", lambda e: canvas.move(pacman, -40, 0) if system_status == "BOOTING" else None)
...
... root.mainloop()
...
ZUGRIFF VERWEIGERT: L{0}
IZ-FLOW OS: SYSTEM L{1}
