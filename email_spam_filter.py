import tkinter as tk
from tkinter import messagebox
import re


spam_words = ["win", "free", "cash", "prize", "lottery", "urgent", "buy now", "click here", "money", "credit"]


def calculate_spam_probability(email_text):
    words = re.findall(r'\b\w+\b', email_text.lower())
    spam_count = sum(1 for word in words if word in spam_words)
    total_words = len(words)

  
    probability = spam_count / total_words if total_words > 0 else 0
    return probability


def check_spam():
    email_text = email_entry.get("1.0", tk.END)
    probability = calculate_spam_probability(email_text)
    
    if probability > 0.3:  
        result = "SPAM ❌ (Spam Probability: {:.2f})".format(probability)
    else:
        result = "HAM ✅ (Spam Probability: {:.2f})".format(probability)
    
    messagebox.showinfo("Result", result)


root = tk.Tk()
root.title("Email Spam Filter (DAA Mini Project)")
root.geometry("600x400")
root.config(bg="lightblue")

title_label = tk.Label(root, text="Email Spam Filter using DAA", font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=20)

email_entry = tk.Text(root, height=10, width=60, font=("Arial", 12))
email_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Spam", command=check_spam, font=("Arial", 14), bg="green", fg="white")
check_button.pack(pady=10)

root.mainloop()
