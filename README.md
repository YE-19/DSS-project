# DSS Project: Decision Making Under Uncertainty

This project implements the five classic approaches for **Decision Making under Uncertainty** using **Python**.  
The core objective is to provide a flexible tool capable of analyzing any arbitrary **Payoff Matrix** provided by the user.

---

## 1. Project Overview

### Feature Overview

| Feature           | Details                                                       |
| ----------------- | ------------------------------------------------------------- |
| Technique         | Decision Making under Uncertainty (DSS)                       |
| Programming Lang. | Python 3.x                                                    |
| Core Library      | NumPy (for matrix operations)                                 |
| Code Structure    | Object-Oriented Programming (OOP) using `DecisionMaker` class |

---

## 2. Setup and Prerequisites

### A. Environment Setup

To run this project, you must install the required library.

Install NumPy using the terminal:

```bash
pip install numpy
```

### B. Execution

Navigate to the folder:  
In your VS Code Terminal, ensure you are inside the directory that contains **decision_maker.py**.

Run the script using Python:

```bash
python decision_maker.py
```

---

---

## 3. Interactive Execution Guide

The program runs in an interactive mode, guiding the user through data input and analysis.

### Step 1: Matrix Input (Data Entry)

The program will prompt you to enter the **Payoff Matrix** row by row.

**Rule:** Enter numeric values (integers or decimals) separated by spaces.

**Example Input** (for a matrix with 3 states/columns):

```text
Enter Alternative 1 values (or 'done' to finish): 3000 1500 -500
Enter Alternative 2 values (or 'done' to finish): 2000 2000 1000
Enter Alternative 3 values (or 'done' to finish): done
```

### Step 2: Method Selection (Analysis)

After successful matrix initialization, you will be prompted to choose the analysis method:

```text
--- METHOD SELECTION ---

Select a Decision Approach:
1: Maximax (Optimistic)
# ... (Other options)
7: Exit

Enter your choice (1-7):
```

Note for Hurwicz (Option 3): If you choose 3, the program will prompt you for the Alpha ($\alpha$) value (Coefficient of Optimism) between 0 and 1.

---

## 4. Code Structure and Team Tasks

The core logic of the project resides in the `DecisionMaker` class.  
Your team's task is to implement the logic inside the five placeholder methods.

### Team Tasks for Each Method

| Method                  | Criterion        | Team Assigned | Implementation Focus (The Logic)                            |
| ----------------------- | ---------------- | ------------- | ----------------------------------------------------------- |
| maximax_approach()      | Optimistic       | 3 & 4         | Find the Maximum of the row Maximums                        |
| maximin_approach()      | Pessimistic      | 5 & 6         | Find the Maximum of the row Minimums                        |
| hurwicz_approach(alpha) | Realism          | 7 & 8         | Apply the formula: (α × Max) + ((1 − α) × Min)              |
| regret_approach()       | Minimax Regret   | 9 & 10        | Calculate Regret Matrix → Find row Max → Find overall Min   |
| laplace_approach()      | Equal Likelihood | 11            | Calculate the Mean (Average) of each row → Find overall Max |

### Execution Responsibility

- All methods must use `self.matrix` for calculations.
- All methods must return the **name of the optimal alternative** (e.g., `'Alternative 1'`).

---

## 5. Implementation Guidelines

Adhering to these guidelines is crucial for successful code merging and project delivery.

### ✔ Do Not Modify Structure

DO NOT change the following methods as they form the backbone of the project:

- `__init__`
- `display_results`
- Interactive mode functions: `get_matrix_input`, `run_interactive_mode`

### ✔ Use NumPy

Leverage NumPy functions for all matrix operations:

- `np.max`, `np.min`, `np.mean`, `np.where`

Avoid writing manual loops where a NumPy function exists.

### ✔ Strict Return Type

Ensure your function returns a **string** representing the decision.  
Example:

```python
return self.alternatives[index]
```

### Mandatory Documentation

For the Word Report, each team must include:

1. **The Algorithm** – step-by-step logic used.
2. **A Manual Solution** – showing the calculation for your assigned method based on the sample matrix.
3. **The Code Snippet** – of your implemented method.

---

## 6. NumPy: Why It's Essential for DSS

The entire project structure, including the `DecisionMaker` class, relies heavily on the **NumPy (Numerical Python)** library.

NumPy is crucial because it provides high-performance data structures called **arrays**, which make matrix operations (the core of Decision Support Systems) fast and efficient.

### Avoid Loops

NumPy allows you to perform complex calculations (like finding the maximum value in an entire row) with a single function call, replacing verbose and error-prone **for loops**.

### The Regret Matrix

Calculating the **Minimax Regret matrix** is nearly impossible without NumPy's ability to subtract an array from a scalar or another array directly.

---

## 7. Setup: Installing the Library

Before running the project, every team member must install **NumPy** into their Python environment.

**Command:** Open your VS Code Terminal or Command Prompt and execute:

```bash
pip install numpy
```

---

## 8. 🎯 How to Use NumPy in Each Decision Model

The `__init__` method already converts the user's input matrix into a **NumPy array** stored as `self.matrix`.

Your team members must use specific **NumPy functions** to implement their assigned logic for each decision model.

### NumPy Functions for Each Decision Approach

| Decision Approach          | NumPy Function(s) to Use                        | Core Logic (The Calculation)                                                                                                                                                            |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximax (Optimistic)       | `np.max(..., axis=1)` and `np.max()`            | Find the maximum value in each row, then find the single largest value among those maximums.                                                                                            |
| Maximin (Pessimistic)      | `np.min(..., axis=1)` and `np.max()`            | Find the minimum value in each row, then find the single largest value among those minimums.                                                                                            |
| Hurwicz (Realism)          | `np.max()`, `np.min()`, and basic arithmetic    | Use the formula: (α × Max Payoff) + ((1 − α) × Min Payoff).                                                                                                                             |
| Laplace (Equal Likelihood) | `np.mean(..., axis=1)` and `np.max()`           | Calculate the average (mean) payoff for each alternative.                                                                                                                               |
| Minimax Regret             | `np.max(..., axis=0)` and `np.min(..., axis=1)` | Crucial Step: Calculate the Regret Matrix: `Regret = np.max(self.matrix, axis=0) - self.matrix`. Then find the maximum regret per alternative and select the minimum of those maximums. |

---

## Finding the Final Decision Index

Once the optimal value (e.g., the Maximin value) is found, the `np.where()` function is used to locate the index of the row that produced that value.  
This allows the function to return the **Alternative's name**.

**Python Example: Finding the index of the Maximin Decision**

```python
# Example: Finding the index of the Maximin Decision
max_of_min_payoffs = np.max(min_of_rows)
decision_index = np.where(min_of_rows == max_of_min_payoffs)[0][0]
return self.alternatives[decision_index]
```
