Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter as tk
>>>
>>> # DEIN INTERPRETER-KERN
>>> def verarbeite_befehl(befehl, canvas, pacman):
...         teile = befehl.split("{")
...
>>>     # Richtung (dr) und Wert (iz) auslesen
>>>     if "dr" in teile:
  File "<python-input-5>", line 1
    if "dr" in teile:
IndentationError: unexpected indent
>>>         richtung = teile[teile.index("dr") + 1]
  File "<python-input-6>", line 1
    richtung = teile[teile.index("dr") + 1]
IndentationError: unexpected indent
>>>         pixel = int(teile[teile.index("iz") + 1], 16)
  File "<python-input-7>", line 1
    pixel = int(teile[teile.index("iz") + 1], 16)
IndentationError: unexpected indent
>>>
>>>         # Logik: 01=Hoch, 02=Runter, 03=Links, 04=Rechts
>>>         if richtung == "01": canvas.move(pacman, 0, -pixel)
  File "<python-input-10>", line 1
    if richtung == "01": canvas.move(pacman, 0, -pixel)
IndentationError: unexpected indent
>>>         if richtung == "02": canvas.move(pacman, 0, pixel)
  File "<python-input-11>", line 1
    if richtung == "02": canvas.move(pacman, 0, pixel)
IndentationError: unexpected indent
>>>         if richtung == "03": canvas.move(pacman, -pixel, 0)
  File "<python-input-12>", line 1
    if richtung == "03": canvas.move(pacman, -pixel, 0)
IndentationError: unexpected indent
>>>         if richtung == "04": canvas.move(pacman, pixel, 0)
  File "<python-input-13>", line 1
    if richtung == "04": canvas.move(pacman, pixel, 0)
IndentationError: unexpected indent
>>>
>>> # GRAFIK-FENSTER STARTEN
>>> root = tk.Tk()
>>> root.title("Pacman Hex-Flow Engine")
''
>>> canvas = tk.Canvas(root, width=400, height=400, bg="black")
>>> canvas.pack()
>>>
>>> # Pacman zeichnen (Gelber Kreis)
>>> pacman = canvas.create_oval(180, 180, 220, 220, fill="yellow")
>>>
>>> # TEST: Bewege Pacman mit DEINER Sprache (Rechts um 30 Pixel)
>>> # In einem echten Spiel würde das durch Tastendruck ausgelöst
>>> root.after(1000, lambda: verarbeite_befehl("dr{04{iz{1e", canvas, pacman))
'after#0'
>>>
>>> root.mainloop()
