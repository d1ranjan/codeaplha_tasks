import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




faqs = [
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial Intelligence (AI) is the field of creating machines and software that can perform tasks that normally require human intelligence."
    },

    {
        "question": "What is machine learning?",
        "answer": "Machine Learning (ML) is a branch of AI in which computers learn patterns from data and use those patterns to make predictions or decisions."
    },

    {
        "question": "What is deep learning?",
        "answer": "Deep Learning is a type of machine learning that uses artificial neural networks with multiple layers to learn complex patterns."
    },

    {
        "question": "What is Python?",
        "answer": "Python is a high-level programming language commonly used for software development, data science, artificial intelligence, machine learning and automation."
    },

    {
        "question": "What is NLP?",
        "answer": "NLP stands for Natural Language Processing. It is a branch of AI that allows computers to process and understand human language."
    },

    {
        "question": "What is a chatbot?",
        "answer": "A chatbot is a software application that communicates with users through text or speech."
    },

    {
        "question": "What is an API?",
        "answer": "API stands for Application Programming Interface. It allows different software applications to communicate with each other."
    },

    {
        "question": "What is a neural network?",
        "answer": "A neural network is a machine learning model inspired by the human brain. It consists of interconnected nodes called neurons."
    },

    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning is a machine learning method where a model learns from labelled training data."
    },

    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning is a machine learning method that discovers patterns or structures in data without labelled answers."
    },

    {
        "question": "What is generative AI?",
        "answer": "Generative AI is a type of artificial intelligence that can create new content such as text, images, audio, video and code."
    },

    {
        "question": "What is a dataset?",
        "answer": "A dataset is a collection of data used for analysis, machine learning or other computational tasks."
    },

    {
        "question": "What is computer vision?",
        "answer": "Computer vision is a branch of AI that enables computers to understand and analyze images and videos."
    },

    {
        "question": "What is an algorithm?",
        "answer": "An algorithm is a step-by-step procedure used to solve a problem or perform a particular task."
    },

    {
        "question": "What is training data?",
        "answer": "Training data is the data used to teach a machine learning model to recognize patterns and make predictions."
    }
]



def preprocess(text):

    text = text.lower()

  
    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

   
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text




questions = [
    faq["question"]
    for faq in faqs
]


processed_questions = [
    preprocess(question)
    for question in questions
]



vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)




def get_answer(user_question):

    processed_question = preprocess(
        user_question
    )

    if not processed_question:

        return (
            "Please enter a question.",
            0
        )

   
    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    
    best_index = similarity_scores.argmax()

    best_score = similarity_scores[
        0
    ][best_index]

    
    if best_score < 0.15:

        return (
            "Sorry, I could not find a relevant "
            "answer in my FAQ database. Try something else.",
            best_score
        )

    answer = faqs[
        best_index
    ]["answer"]

    return answer, best_score



def get_time():

    return datetime.now().strftime(
        "%H:%M"
    )

def send_message(event=None):

    question = input_box.get().strip()

    if not question:
        return

    
    current_time = get_time()


    chat_area.config(
        state=tk.NORMAL
    )

    
    chat_area.insert(
        tk.END,
        f"You [{current_time}]:\n",
        "user_name"
    )

    chat_area.insert(
        tk.END,
        f"{question}\n\n",
        "user_message"
    )


    answer, score = get_answer(
        question
    )


    chat_area.insert(
        tk.END,
        f"Bot [{current_time}]:\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        f"{answer}\n",
        "bot_message"
    )

    
    chat_area.insert(
        tk.END,
        f"Similarity Score: {score:.2f}\n\n",
        "score"
    )

    
    chat_area.config(
        state=tk.DISABLED
    )

    
    input_box.delete(
        0,
        tk.END
    )

    
    chat_area.see(
        tk.END
    )




def clear_chat():

    chat_area.config(
        state=tk.NORMAL
    )

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.insert(
        tk.END,
        "Bot:\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        "Hello! I am your FAQ chatbot.\n"
        "Ask me about AI, ML, Python, NLP or "
        "computer vision.\n\n",
        "bot_message"
    )

    chat_area.config(
        state=tk.DISABLED
    )




def exit_program():

    root.destroy()




root = tk.Tk()

root.title(
    "AI FAQ Chatbot"
)

root.geometry(
    "800x700"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#f2f2f2"
)



title = tk.Label(
    root,
    text="AI FAQ Chatbot",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)

title.pack(
    pady=(15, 5)
)


subtitle = tk.Label(
    root,
    text="NLP • TF-IDF • Cosine Similarity",
    font=("Arial", 11),
    bg="#f2f2f2"
)

subtitle.pack(
    pady=(0, 10)
)




chat_area = scrolledtext.ScrolledText(
    root,
    width=85,
    height=27,
    font=("Arial", 11),
    wrap=tk.WORD
)

chat_area.pack(
    padx=20,
    pady=10
)




chat_area.tag_config(
    "user_name",
    font=("Arial", 11, "bold")
)

chat_area.tag_config(
    "user_message",
    font=("Arial", 11)
)

chat_area.tag_config(
    "bot_name",
    font=("Arial", 11, "bold")
)

chat_area.tag_config(
    "bot_message",
    font=("Arial", 11)
)

chat_area.tag_config(
    "score",
    font=("Arial", 9)
)



chat_area.insert(
    tk.END,
    "Bot:\n",
    "bot_name"
)

chat_area.insert(
    tk.END,
    "Hello! I am your FAQ chatbot.\n"
    "Ask me about AI, ML, Python, NLP or "
    "computer vision.\n\n",
    "bot_message"
)

chat_area.config(
    state=tk.DISABLED
)



input_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)

input_frame.pack(
    fill=tk.X,
    padx=20,
    pady=5
)


input_box = tk.Entry(
    input_frame,
    font=("Arial", 13)
)

input_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=8
)



send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    font=("Arial", 11, "bold"),
    width=10
)

send_button.pack(
    side=tk.RIGHT,
    padx=5
)




control_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)

control_frame.pack(
    pady=10
)



tk.Button(
    control_frame,
    text="Clear Chat",
    command=clear_chat,
    width=15
).grid(
    row=0,
    column=0,
    padx=5
)




tk.Button(
    control_frame,
    text="Exit",
    command=exit_program,
    width=15
).grid(
    row=0,
    column=1,
    padx=5
)




input_box.bind(
    "<Return>",
    send_message
)



root.mainloop()