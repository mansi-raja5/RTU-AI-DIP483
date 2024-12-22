# Shopping Intent Classifier

This project implements a machine learning classifier to predict whether a user intends to make a purchase during their session on an online shopping website. The classifier uses a k-nearest neighbors algorithm to make predictions based on user behavior data.

## Files

### `shopping.py`
- The main program file that contains the following functions:
  - `load_data`: Reads and processes input data from a CSV file.
  - `train_model`: Trains a k-nearest neighbors classifier using the provided evidence and labels.
  - `evaluate`: Computes the sensitivity (true positive rate) and specificity (true negative rate) of the model.
  - `main`: The entry point of the program, which handles data loading, model training, predictions, and evaluation.

### `shopping.csv`
- The dataset file containing user session data. Each row represents a session and includes features such as the number of pages visited, duration on pages, bounce rates, and whether the session resulted in a purchase.

### `README.md`
- Documentation for the project, including setup instructions and details about the implementation.

## Prerequisites
- Python 3.7 or higher
- Required Python packages:
  - `scikit-learn`

Install the necessary dependencies by running:
```bash
pip install scikit-learn
```

### `How to Run`
- Ensure all files (shopping.py and shopping.csv) are in the same directory.
- Run the program using the following command:
```bash
python shopping.py shopping.csv
```
- The program will output:
- The number of correct and incorrect predictions.
- The sensitivity (true positive rate) and specificity (true negative rate) of the classifier.
![image](https://github.com/user-attachments/assets/b80764e9-f87b-4de2-9aba-51a9b2b23361)
