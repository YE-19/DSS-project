# DSS Project: Decision Making Under Uncertainty

This project implements the five classic approaches for **Decision Making under Uncertainty** using **Python**.  
The core objective is to provide a flexible tool capable of analyzing any arbitrary **Payoff Matrix** provided by the user.

---

## 1. Project Overview

### Feature Overview

| Feature            | Details                                                  |
|-------------------|----------------------------------------------------------|
| Technique          | Decision Making under Uncertainty (DSS)                 |
| Programming Lang.  | Python 3.x                                               |
| Core Library       | NumPy (for matrix operations)                            |
| Code Structure     | Object-Oriented Programming (OOP) using `DecisionMaker` class |

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

| Method                   | Criterion       | Team Assigned  | Implementation Focus (The Logic)                        |
|--------------------------|-----------------|----------------|---------------------------------------------------------|
| maximax_approach()       | Optimistic      | 3 & 4            | Find the Maximum of the row Maximums                  |
| maximin_approach()       | Pessimistic     | 5 & 6            | Find the Maximum of the row Minimums                  |
| hurwicz_approach(alpha)  | Realism         | 7 & 8             | Apply the formula: (α × Max) + ((1 − α) × Min)       |
| regret_approach()        | Minimax Regret  | 9 & 10       | Calculate Regret Matrix → Find row Max → Find overall Min |
| laplace_approach()       | Equal Likelihood| 11         | Calculate the Mean (Average) of each row → Find overall Max |

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



 
