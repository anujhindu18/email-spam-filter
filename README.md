# Email Spam Filter Using Python

## Project Overview

The Email Spam Filter is a Machine Learning project developed using Python to classify emails or text messages as **Spam** or **Not Spam (Ham)**.

The project uses Natural Language Processing (NLP) techniques to process text and a machine learning algorithm to identify spam messages based on patterns learned from a labeled dataset.

The main objective is to reduce unwanted messages and demonstrate how machine learning can solve a real-world text classification problem.

## Objectives

- Build a machine learning model to detect spam messages.
- Clean and preprocess email or message text.
- Convert text into numerical features using TF-IDF.
- Train and evaluate a classification model.
- Predict whether a new message is spam or legitimate.
- Understand the practical applications of NLP and machine learning.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn
- **NLP Technique:** Text preprocessing and TF-IDF Vectorization
- **Machine Learning Algorithm:** Multinomial Naive Bayes
- **Development Environment:** Jupyter Notebook, Google Colab, or VS Code
- **Dataset Format:** CSV

## Project Workflow

1. **Data Collection:** Load a labeled dataset containing spam and legitimate messages.
2. **Data Cleaning:** Remove missing values and duplicate records.
3. **Text Preprocessing:** Normalize text and prepare it for feature extraction.
4. **Feature Extraction:** Convert text into numerical features using TF-IDF.
5. **Data Splitting:** Divide the dataset into training and testing sets.
6. **Model Training:** Train a Multinomial Naive Bayes classifier.
7. **Model Evaluation:** Measure accuracy, precision, recall, and F1-score.
8. **Spam Prediction:** Classify new messages as Spam or Not Spam.

## Project Structure

```text
Email-Spam-Filter/
│
├── data/
│   └── spam.csv
│
├── notebooks/
│   └── email_spam_filter.ipynb
│
├── models/
│   └── spam_classifier.pkl
│
├── src/
│   └── train_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

Note: This is a suggested structure. The actual files may differ depending on your implementation.

## Dataset

The project requires a labeled dataset containing messages and their corresponding categories.

Example:

| Message | Label |
|---|---|
| Congratulations! You have won a free prize. | Spam |
| Hi, are we meeting tomorrow? | Ham |
| Claim your reward now by clicking this link. | Spam |
| Please send me the project report. | Ham |

A commonly used dataset for this project is the **SMS Spam Collection Dataset**, which contains labeled spam and legitimate SMS messages. It can be used as a starting point for building a text spam classifier.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Email-Spam-Filter.git
cd Email-Spam-Filter
```

Replace `your-username` with your GitHub username and use your actual repository URL.

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Create a `requirements.txt` file containing:

```text
pandas
numpy
scikit-learn
jupyter
```

Install the packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Project

If the project is implemented in Jupyter Notebook, run:

```bash
jupyter notebook
