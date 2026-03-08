Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...         canvas.delete("login_ui")
...         punktestand = lade_daten()
...         lade_map(canvas)
...         print(f"BOOT SUCCESS. SCORE: {punktestand}")
...     else:
...         messagebox.showerror("ERROR", "ZUGRIFF VERWEIGERT: L{0}")
...
... # Login-UI
... canvas.create_text(200, 150, text="IZ-FLOW OS: LOCKED", fill="red", font=("Courier", 14), tags="login_ui")
... pw_entry = tk.Entry(root, bg="black", fg="lime", insertbackground="white", justify="center")
... canvas.create_window(200, 200, window=pw_entry, tags="login_ui")
... root.bind('<Return>', login_logic)
...
... # Pacman
... pacman = canvas.create_oval(45, 45, 75, 75, fill="yellow")
...
... # --- 5. STEUERUNG (in{ky) ---
... def move(dx, dy):
...     if system_status == "RUN":
...         canvas.move(pacman, dx, dy)
...
... root.bind("<Up>", lambda e: move(0, -10))
... root.bind("<Down>", lambda e: move(0, 10))
... root.bind("<Left>", lambda e: move(-10, 0))
... root.bind("<Right>", lambda e: move(10, 0))
...
... # TERMINAL-SIMULATION (Tippe Befehle in die Konsole deines PCs)
... print("--- IZ-FLOW OS BOOT-TERMINAL BEREIT ---")
... root.mainloop()
...
