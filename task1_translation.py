import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame


languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur"
}


def translate_text():

    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    source = source_language.get()
    target = target_language.get()

    if source == target:

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, text)

        return

    try:

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            translated
        )

    except Exception as e:

        messagebox.showerror(
            "Translation Error",
            f"Unable to translate.\n\n{e}"
        )


def copy_text():

    translated = output_text.get(
        "1.0",
        tk.END
    ).strip()

    if not translated:

        messagebox.showwarning(
            "Warning",
            "There is no translated text."
        )

        return

    root.clipboard_clear()

    root.clipboard_append(
        translated
    )

    root.update()

    messagebox.showinfo(
        "Copied",
        "Translated text copied!"
    )


def speak_text():

    translated = output_text.get(
        "1.0",
        tk.END
    ).strip()

    if not translated:

        messagebox.showwarning(
            "Warning",
            "Translate something first."
        )

        return

    target_code = languages[
        target_language.get()
    ]

    try:

        
        speech = gTTS(
            text=translated,
            lang=target_code
        )

        filename = "translated_voice.mp3"

        speech.save(filename)

        
        pygame.mixer.init()

        pygame.mixer.music.load(
            filename
        )

        pygame.mixer.music.play()

    except Exception as e:

        messagebox.showerror(
            "Speech Error",
            f"Unable to generate speech.\n\n{e}"
        )


def clear_text():

    input_text.delete(
        "1.0",
        tk.END
    )

    output_text.delete(
        "1.0",
        tk.END
    )


root = tk.Tk()

root.title(
    "AI Language Translation Tool"
)

root.geometry(
    "800x650"
)

root.resizable(
    False,
    False
)


title = tk.Label(
    root,
    text="AI Language Translation Tool",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)



language_frame = tk.Frame(root)

language_frame.pack(pady=10)

tk.Label(
    language_frame,
    text="Source Language:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10
)


source_language = ttk.Combobox(
    language_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)

source_language.set("English")

source_language.grid(
    row=0,
    column=1,
    padx=10
)


tk.Label(
    language_frame,
    text="Target Language:",
    font=("Arial", 12)
).grid(
    row=0,
    column=2,
    padx=10
)


target_language = ttk.Combobox(
    language_frame,
    values=list(languages.keys()),
    state="readonly",
    width=15
)

target_language.set("Hindi")

target_language.grid(
    row=0,
    column=3,
    padx=10
)




tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 13, "bold")
).pack(
    anchor="w",
    padx=50
)


input_text = tk.Text(
    root,
    height=7,
    width=80,
    font=("Arial", 12)
)

input_text.pack(
    pady=5
)




tk.Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold"),
    width=15,
    height=2
).pack(
    pady=10
)




tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 13, "bold")
).pack(
    anchor="w",
    padx=50
)


output_text = tk.Text(
    root,
    height=7,
    width=80,
    font=("Arial", 12)
)

output_text.pack(
    pady=5
)




button_frame = tk.Frame(root)

button_frame.pack(
    pady=15
)



tk.Button(
    button_frame,
    text="Copy",
    command=copy_text,
    width=12
).grid(
    row=0,
    column=0,
    padx=5
)



tk.Button(
    button_frame,
    text="Speak",
    command=speak_text,
    width=12
).grid(
    row=0,
    column=1,
    padx=5
)




tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=12
).grid(
    row=0,
    column=2,
    padx=5
)



root.mainloop()