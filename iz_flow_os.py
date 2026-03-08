Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...
... canvas = tk.Canvas(root, width=400, height=400, bg="black")
... canvas.pack()
...
... # Login-UI (sy{pw)
... t1 = canvas.create_text(200, 150, text="SYSTEM LOCKED", fill="red", font=("Courier", 16))
... t2 = canvas.create_text(200, 180, text="GIB HEX-CODE EIN (A1):", fill="white", font=("Courier", 10))
... pw_entry = tk.Entry(root, bg="black", fg="lime", insertbackground="white", justify="center")
... pw_window = canvas.create_window(200, 220, window=pw_entry)
...
... # Pacman & Geister (syp) - erst nach Login voll aktiv
... pacman = canvas.create_oval(180, 300, 210, 330, fill="yellow")
...
... # --- STEUERUNG (in{ky) ---
... root.bind('<Return>', lambda e: login_check(e, pw_entry, canvas, [t1, t2, pw_window]))
...
... # Bewegung nach dem Login
... def move(r):
...     if system_status == "RUN":
...         verarbeite_befehl(f"dr{{{r}}}{{iz{{14", canvas, pacman)
...
... root.bind("<Up>", lambda e: move("01"))
... root.bind("<Down>", lambda e: move("02"))
... root.bind("<Left>", lambda e: move("03"))
... root.bind("<Right>", lambda e: move("04"))
...
... # --- WICHTIG: Das Fenster offen halten ---
... print("SYSTEM READY. WARTE AUF BOOT...")
... root.mainloop()
...
