import numpy as np

class DecisionMaker:
    """
    Class to implement the five approaches of Decision Making under Uncertainty.
    It manages the payoff matrix and provides the methods for each decision criterion.
    """
    
    # ----------------------------------------------------
    # 1. Constructor: Initialization and Data Setup
    # (Completed by Leader)
    # ----------------------------------------------------
    def __init__(self, matrix, alternatives=None, states=None):
        """
        Initializes the DecisionMaker with the payoff matrix and labels.
        :param matrix: List of lists representing the Payoff Matrix (Outcomes).
        :param alternatives: List of strings for the alternative actions (Rows).
        :param states: List of strings for the states of nature (Columns).
        """
        
        # Convert the input list of lists into a NumPy array for efficient calculation.
        self.matrix = np.array(matrix) 
        
        # Check if the matrix is empty.
        if self.matrix.size == 0:
            raise ValueError("The payoff matrix cannot be empty.")
        
        # Determine the number of rows (alternatives) and columns (states).
        rows, cols = self.matrix.shape
        
        # Define alternative names, using default names if none are provided.
        self.alternatives = alternatives if alternatives is not None else [f"Alternative {i+1}" for i in range(rows)]
        
        # Define state names, using default names if none are provided.
        self.states = states if states is not None else [f"State {i+1}" for i in range(cols)]
        
        print(f"✅ DecisionMaker Class initialized with {rows} Alternatives and {cols} States.")

    # ----------------------------------------------------
    # 2. Decision Methods (To be implemented by the team)
    # ----------------------------------------------------
    
    def maximax_approach(self):
        # ----------------------------------------------------------------------
        # TO BE IMPLEMENTED BY TEAM MEMBERS (Maximax / Optimistic Criterion)
        # This method should:
        # 1. Find the maximum payoff for each alternative (row).
        # 2. Select the alternative that yields the overall maximum payoff.
        # 3. Use self.matrix and np.max(..., axis=1).
        # ----------------------------------------------------------------------
        return "Not Implemented Yet: Maximax Logic"

    def maximin_approach(self):
        # ----------------------------------------------------------------------
        # TO BE IMPLEMENTED BY TEAM MEMBERS (Maximin / Pessimistic Criterion)
        # This method should:
        # 1. Find the minimum payoff for each alternative (row).
        # 2. Select the alternative that yields the maximum of these minimum payoffs.
        # 3. Use self.matrix and np.min(..., axis=1).
        # ----------------------------------------------------------------------
        return "Not Implemented Yet: Maximin Logic"

    def hurwicz_approach(self, alpha=0.5):
        # ----------------------------------------------------------------------
        # TO BE IMPLEMENTED BY TEAM MEMBERS (Hurwicz / Criterion of Realism)
        # This method should:
        # 1. Calculate Value = (alpha * Max Payoff) + ((1 - alpha) * Min Payoff) for each row.
        # 2. Select the alternative with the highest calculated Value.
        # 3. The 'alpha' parameter is passed when called from the interactive mode.
        # ----------------------------------------------------------------------
        return f"Not Implemented Yet: Hurwicz Logic (alpha={alpha})"

    def regret_approach(self):
        # ----------------------------------------------------------------------
        # TO BE IMPLEMENTED BY TEAM MEMBERS (Minimax Regret Criterion)
        # This method should:
        # 1. Calculate the Regret Matrix: Regret = Max Payoff in state - Actual Payoff.
        # 2. Find the maximum Regret for each alternative (row).
        # 3. Select the alternative that minimizes this maximum regret.
        # ----------------------------------------------------------------------
        return "Not Implemented Yet: Minimax Regret Logic"

    def laplace_approach(self):
        # ----------------------------------------------------------------------
        # TO BE IMPLEMENTED BY TEAM MEMBERS (Laplace / Equal Likelihood Criterion)
        # This method should:
        # 1. Calculate the average payoff (mean) for each alternative (row).
        # 2. Select the alternative that yields the highest average payoff.
        # 3. Use self.matrix and np.mean(..., axis=1).
        # ----------------------------------------------------------------------
        return "Not Implemented Yet: Laplace Logic"
    
    # ----------------------------------------------------
    # 3. Output Method
    # (Completed by Leader)
    # ----------------------------------------------------
    def display_results(self, hurwicz_alpha=0.6):
        """Calls all decision methods and prints the results."""
        
        print("\n--- Final Decision Results (Under Uncertainty) ---")
        
        # Call the five approaches.
        maximax_d = self.maximax_approach()
        maximin_d = self.maximin_approach()
        hurwicz_d = self.hurwicz_approach(hurwicz_alpha)
        regret_d = self.regret_approach()
        laplace_d = self.laplace_approach()
        
        # Display the results.
        print(f"1. Maximax (Optimistic): {maximax_d}")
        print(f"2. Maximin (Pessimistic): {maximin_d}")
        print(f"3. Hurwicz (Realism, alpha={hurwicz_alpha}): {hurwicz_d}")
        print(f"4. Minimax Regret: {regret_d}")
        print(f"5. Laplace (Equal Likelihood): {laplace_d}")


# ----------------------------------------------------
# 4. Interactive Mode Functions
# (Completed by Leader)
# ----------------------------------------------------

def get_matrix_input():
    """Helper function to get the payoff matrix from the user."""
    print("\n--- MATRIX INPUT ---")
    print("Enter the payoff matrix row by row, with values separated by spaces.")
    print("Example (3 states): 3000 1500 -500")
    
    matrix = []
    first_row_len = 0
    while True:
        try:
            row_input = input(f"Enter Alternative {len(matrix) + 1} values (or 'done' to finish): ")
            if row_input.lower() == 'done':
                if len(matrix) == 0:
                    print("Matrix cannot be empty. Please enter values.")
                    continue
                break
                
            row = [float(x.strip()) for x in row_input.split()]
            
            if len(matrix) == 0:
                first_row_len = len(row)
            elif len(row) != first_row_len:
                print(f"Error: All alternatives must have {first_row_len} states. Please re-enter Alternative {len(matrix) + 1}.")
                continue
            
            matrix.append(row)
            
        except ValueError:
            print("Invalid input. Please enter numbers only (e.g., 100 50).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
            
    return matrix


def run_interactive_mode():
    """Runs the main DSS analysis in interactive mode."""
    
    # 1. Get the Payoff Matrix from the user
    payoff_matrix = get_matrix_input()
    
    if not payoff_matrix:
        print("Exiting due to empty matrix.")
        return

    # 2. Initialize the Decision Maker Class
    try:
        dss_problem = DecisionMaker(matrix=payoff_matrix)
    except Exception as e:
        print(f"Error initializing DecisionMaker: {e}")
        return

    # 3. Get the user's choice of method
    while True:
        print("\n--- METHOD SELECTION ---")
        print("Select a Decision Approach:")
        print("1: Maximax (Optimistic)")
        print("2: Maximin (Pessimistic)")
        print("3: Hurwicz (Realism)")
        print("4: Minimax Regret")
        print("5: Laplace (Equal Likelihood)")
        print("6: Show All Results")
        print("7: Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Exiting Decision Support System. Goodbye!")
            break
        
        try:
            choice = int(choice)
            result_message = ""
            
            if choice == 1:
                result_message = f"Maximax Decision: {dss_problem.maximax_approach()}"
            elif choice == 2:
                result_message = f"Maximin Decision: {dss_problem.maximin_approach()}"
            elif choice == 3:
                # Prompt for Alpha only if Hurwicz is selected
                alpha_input = input("Enter Hurwicz Alpha (coefficient of optimism, 0 to 1): ")
                alpha = float(alpha_input)
                if 0 <= alpha <= 1:
                    result_message = f"Hurwicz Decision (Alpha={alpha}): {dss_problem.hurwicz_approach(alpha=alpha)}"
                else:
                    print("Alpha must be between 0 and 1. Please try again.")
                    continue
            elif choice == 4:
                result_message = f"Minimax Regret Decision: {dss_problem.regret_approach()}"
            elif choice == 5:
                result_message = f"Laplace Decision: {dss_problem.laplace_approach()}"
            elif choice == 6:
                # Show all results (using default alpha 0.6)
                dss_problem.display_results(hurwicz_alpha=0.6)
                continue
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
                continue

            print("\n--- ANALYSIS RESULT ---")
            print(result_message)
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred during analysis: {e}")
            break


# ----------------------------------------------------
# 5. Execution Block
# ----------------------------------------------------
if __name__ == "__main__":
    # RUN THE INTERACTIVE MODE
    run_interactive_mode()