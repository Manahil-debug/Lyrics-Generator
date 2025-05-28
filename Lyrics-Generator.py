import tkinter as tk
import pyttsx3
import threading
import random
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Sample lyric lines pool
sample_lines = [
    "Your flame breathes in warm silence",
    "The lost dust burns",
    "Let the heart fall so still",
    "Only the silent star knows",
    "In the soft sky, I rise",
    "In the deep light, I fade",
    "Your wind shines in cold silence",
    "Only the bright dream knows",
    "In the deep dream, I rise",
    "The lost heart shines",
    "Only the bright star knows",
    "Let the dream breathe so lost",
    "A warm flame will glow",
    "Let the heart drift so lost"
]

# Function to speak aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to generate lyrics
def generate_lyrics():
    mood = mood_entry.get().strip()
    lines = lines_entry.get().strip()

    if not mood or not lines:
        lyrics_display.config(text="Please fill in both fields.")
        return

    try:
        num_lines = int(lines)
    except ValueError:
        lyrics_display.config(text="Please enter a valid number for lines.")
        return

    lyrics_display.config(text="Generating lyrics...")

    def process():
        time.sleep(1)  # Simulated delay
        selected_lines = random.choices(sample_lines, k=num_lines)
        title = f"♣     {mood.capitalize()} Whispers     ♣\n\n"
        result = title + "\n".join(selected_lines)
        lyrics_display.config(text=result)

        # Read aloud if checkbox selected
        if read_aloud_var.get():
            speak("\n".join(selected_lines))

    threading.Thread(target=process).start()

# GUI setup
root = tk.Tk()
root.title("Lyrics Generator")
root.geometry("600x600")
root.configure(bg="#d3d3d3")

# Mood input
tk.Label(root, text="Type Mood:", bg="#d3d3d3").pack()
mood_entry = tk.Entry(root)
mood_entry.pack()

# Number of lines input
tk.Label(root, text="Number of lines:", bg="#d3d3d3").pack()
lines_entry = tk.Entry(root)
lines_entry.pack()

# Checkbox for read aloud
read_aloud_var = tk.BooleanVar()
tk.Checkbutton(root, text="Read Aloud?", variable=read_aloud_var, bg="#d3d3d3").pack()

# Checkbox for dark mode
dark_mode_var = tk.BooleanVar()

def toggle_dark_mode():
    if dark_mode_var.get():
        root.configure(bg="#2e2e2e")  # dark background
        # update widget colors to dark mode
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Checkbutton)):
                widget.configure(bg="#2e2e2e", fg="white")
            elif isinstance(widget, tk.Entry):
                widget.configure(bg="#4b4b4b", fg="white", insertbackground="white")
            elif isinstance(widget, tk.Button):
                widget.configure(bg="#555555", fg="white", activebackground="#777777")
        lyrics_display.configure(bg="#1e1e1e", fg="white")
    else:
        root.configure(bg="#d3d3d3")  # original light background
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Checkbutton)):
                widget.configure(bg="#d3d3d3", fg="black")
            elif isinstance(widget, tk.Entry):
                widget.configure(bg="white", fg="black", insertbackground="black")
            elif isinstance(widget, tk.Button):
                widget.configure(bg="SystemButtonFace", fg="black", activebackground="SystemButtonFace")
        lyrics_display.configure(bg="white", fg="black")

tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode, bg="#d3d3d3").pack()

# Generate button
tk.Button(root, text="Generate Lyrics", command=generate_lyrics).pack(pady=10)

# Lyrics display label
lyrics_display = tk.Label(
    root,
    text="",
    bg="white",
    width=70,
    height=20,
    justify="left",
    anchor="nw",
    wraplength=550,
    font=("Helvetica", 12)
)
lyrics_display.pack(pady=20)

root.mainloop()
