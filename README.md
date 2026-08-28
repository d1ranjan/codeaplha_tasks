AI Projects — Tasks 1, 2 & 4

A collection of three beginner-friendly Artificial Intelligence projects implemented in Python.
Projects
Task	Project	Main Technologies
Task 1	Language Translation Tool	Python, Tkinter, Deep Translator, gTTS, Pygame
Task 2	FAQ Chatbot	Python, Tkinter, Scikit-learn, TF-IDF, Cosine Similarity
Task 4	Object Detection & Tracking	Python, YOLO, OpenCV, ByteTrack
Task 1 — Language Translation Tool

A desktop translation application that allows users to enter text, select source and target languages, and obtain a translation.
Features

    Text input and translation

    Source and target language selection

    Multiple language support

    Copy translated text

    Text-to-speech

    Clear button

    Simple Tkinter GUI

Technologies

    Python

    Tkinter

    deep-translator

    gTTS

    pygame

Installation

pip install deep-translator gtts pygame

Run

python translation_tool.py

    Note: The deep-translator version does not require a Google Cloud API key or Google Cloud billing.

Task 2 — FAQ Chatbot

An NLP-based FAQ chatbot that finds the most relevant answer from a predefined FAQ knowledge base.
Features

    FAQ knowledge base

    Text preprocessing

    TF-IDF vectorization

    Cosine similarity

    Similarity score

    Unknown-question handling

    Chat history

    Enter-to-send

    Clear and Exit buttons

    Timestamped messages

Technologies

    Python

    Tkinter

    Scikit-learn

    TF-IDF

    Cosine Similarity

Installation

pip install scikit-learn

Run

python faq_chatbot.py

How It Works

User Question
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Most Similar FAQ
     ↓
Answer

Task 4 — Object Detection & Tracking

A real-time computer vision application using a pre-trained YOLO model to detect and track objects through a webcam.
Features

    Real-time object detection

    Webcam input

    Bounding boxes

    Object class labels

    Object tracking IDs

    ByteTrack tracking

    FPS counter

    Object counter

    Video recording

    Keyboard controls

Technologies

    Python

    Ultralytics YOLO

    OpenCV

    ByteTrack

Installation

pip install ultralytics opencv-python

Run

python object_detection_tracking.py

The YOLO model is downloaded automatically on first use.
Controls
Key	Action
Q	Quit
R	Start/stop recording

Recorded output is saved as:

tracked_output.mp4

How It Works

Webcam
   ↓
Video Frame
   ↓
YOLO Object Detection
   ↓
Bounding Boxes
   ↓
ByteTrack
   ↓
Tracking IDs
   ↓
Display / Recording

Project Structure

AI-Projects/
├── Task-1-Translation/
│   ├── translation_tool.py
│   └── README.md
│
├── Task-2-FAQ-Chatbot/
│   ├── faq_chatbot.py
│   └── README.md
│
└── Task-4-Object-Detection/
    ├── object_detection_tracking.py
    └── README.md

Purpose

These projects demonstrate practical applications of AI, Natural Language Processing, and Computer Vision using beginner-friendly Python implementations.
Author

Dipanshu Ranjan
