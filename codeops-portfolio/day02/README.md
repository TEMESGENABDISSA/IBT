# Day 02 - Python Fundamentals & TeleBirr Projects

## 📌 Overview

This folder contains the Day 02 Python programming exercises from the CodeOps Module 1 training. The tasks focus on building a strong foundation in Python by practicing variables, conditional statements, loops, functions, dictionaries, and file handling.

The exercises are based on simple TeleBirr customer and transaction management scenarios to apply Python concepts to real-world problems.

---

## 📂 Project Structure

```
day02/
│
├── customer_report.py        # Customer tier classification program
├── transaction_report.py     # Transaction file processing program
├── transactions.txt          # Input transaction data
├── report.txt                # Generated transaction summary
├── practice.py               # Python fundamentals exercises
└── README.md                 # Project documentation
```

---

# 🚀 Projects

## 1. TeleBirr Customer Report

### File:

```
customer_report.py
```

### Description

A Python program that analyzes TeleBirr customer balances and assigns customers to different service tiers based on their account balance.

### Tier Classification

| Balance Range | Customer Tier |
| ------------- | ------------- |
| ≥ 1000 ETB    | Premium       |
| ≥ 500 ETB     | Standard      |
| < 500 ETB     | Basic         |

### Features

* Stores customer information using lists and tuples
* Uses a function with a return value to determine customer tiers
* Processes multiple customers using loops
* Generates a customer tier summary
* Uses conditional statements for decision making

### Example Output

```
Almaz: Premium (1500 ETB)
Dawit: Standard (700 ETB)
Tigist: Basic (200 ETB)

Summary:
Premium: 2
Standard: 1
Basic: 2
```

---

# 2. TeleBirr Transaction Report

### File:

```
transaction_report.py
```

### Description

A program that reads TeleBirr transaction records from a text file, calculates total spending per customer, and generates a sorted report.

### Input Format

The transaction file uses the format:

```
Customer_Name,Amount
```

Example:

```
Abebe,250.00
Kalkidan,120.50
```

### Features

* Reads transaction data from a file
* Processes data line by line
* Uses dictionaries to store customer totals
* Converts transaction values into numerical data
* Sorts customers by total spending
* Handles missing files using exception handling
* Generates a final summary report

### Generated Report

The program creates:

```
report.txt
```

Example:

```
Selam: 580.00
Kalkidan: 380.49
Abebe: 335.25
```

---

# 3. Python Practice Exercises

### File:

```
practice.py
```

This file contains Python exercises covering fundamental programming concepts.

## Topics Covered

### Temperature Checker

* User input
* `if / elif / else` conditions

### Receipt Generator

* `for` loops
* `range()`

### Even Number Generator

* Loops
* Modulo operator `%`

### Discount Calculator

* Functions
* Default parameters
* Return values

### Countdown Program

* `while` loops

---

# 🛠️ Requirements

Before running the programs, install:

* Python 3.x

Check Python installation:

```bash
python --version
```

---

# ▶️ Running the Programs

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd day02
```

Run customer report:

```bash
python customer_report.py
```

Run transaction report:

```bash
python transaction_report.py
```

Run practice exercises:

```bash
python practice.py
```

---

# 💡 Key Concepts Practiced

| Concept            | Usage                               |
| ------------------ | ----------------------------------- |
| Variables          | Store customer and transaction data |
| Lists & Tuples     | Manage collections of data          |
| Conditions         | Apply business rules                |
| Loops              | Process multiple records            |
| Functions          | Create reusable logic               |
| Dictionaries       | Store customer summaries            |
| File Handling      | Read and write files                |
| Exception Handling | Manage file errors                  |

---

# 🎯 Learning Outcomes

After completing this project, I gained practical experience in:

* Writing clean Python programs
* Creating reusable functions
* Applying programming logic using conditions and loops
* Processing structured data from files
* Using dictionaries for data aggregation
* Handling errors with exception handling
* Building small real-world Python applications

---

## 👨‍💻 Author

**Temesgen Abdissa**

Python Fundamentals Practice - CodeOps Module 1 Day 02
