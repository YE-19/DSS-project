import numpy as np

class DecisionMaker:
    """
    Class to implement the five approaches of Decision Making under Uncertainty.
    """
    
    def __init__(self, matrix, alternatives=None, states=None):
        self.matrix = np.array(matrix) 
        
        if self.matrix.size == 0:
            raise ValueError("The payoff matrix cannot be empty.")
        
        rows, cols = self.matrix.shape
        self.alternatives = alternatives if alternatives is not None else [f"Alternative {i+1}" for i in range(rows)]
        self.states = states if states is not None else [f"State {i+1}" for i in range(cols)]
        
        print(f"✅ DecisionMaker Class initialized with {rows} Alternatives and {cols} States.")

    # ----------------------------------------------------
    # 2. Decision Methods (Modified to show VALUES)
    # ----------------------------------------------------
    
    def maximax_approach(self):
        # 1. Find max of each row
        max_values = np.max(self.matrix, axis=1)
        # 2. Find the best index
        best_index = np.argmax(max_values)
        # 3. Get the value
        best_value = max_values[best_index]
        
        return f"{self.alternatives[best_index]} (Max Payoff: {best_value})"

    def maximin_approach(self):
        # 1. Find min of each row
        min_values = np.min(self.matrix, axis=1)
        # 2. Find the best index (Max of mins)
        best_index = np.argmax(min_values)
        # 3. Get the value
        best_value = min_values[best_index]
        
        return f"{self.alternatives[best_index]} (Guaranteed Min Payoff: {best_value})"

    def hurwicz_approach(self, alpha=0.5):
        max_values = np.max(self.matrix, axis=1)
        min_values = np.min(self.matrix, axis=1)
        hurwicz_scores = alpha * max_values + (1 - alpha) * min_values
        
        best_index = np.argmax(hurwicz_scores)
        best_value = hurwicz_scores[best_index]
        
        return f"{self.alternatives[best_index]} (Score: {best_value:.2f})"

    def regret_approach(self):
        # 1. Regret Matrix
        col_maxes = np.max(self.matrix, axis=0)
        regret_matrix = col_maxes - self.matrix
        
        # 2. Max Regret per row
        max_regrets = np.max(regret_matrix, axis=1)
        
        # 3. Min of Max Regrets
        best_index = np.argmin(max_regrets)
        best_value = max_regrets[best_index]
        
        return f"{self.alternatives[best_index]} (Max Regret: {best_value})"

    def laplace_approach(self):
        means = np.mean(self.matrix, axis=1)
        best_index = np.argmax(means)
        best_value = means[best_index]
        
        return f"{self.alternatives[best_index]} (Average Value: {best_value:.2f})"
    
    # ----------------------------------------------------
    # 3. Output Method
    # ----------------------------------------------------
    def display_results(self, hurwicz_alpha=0.6):
        print("\n--- Final Decision Results (Under Uncertainty) ---")
        
        maximax_d = self.maximax_approach()
        maximin_d = self.maximin_approach()
        hurwicz_d = self.hurwicz_approach(hurwicz_alpha)
        regret_d = self.regret_approach()
        laplace_d = self.laplace_approach()
        
        print(f"1. Maximax (Optimistic):      {maximax_d}")
        print(f"2. Maximin (Pessimistic):     {maximin_d}")
        print(f"3. Hurwicz (Alpha={hurwicz_alpha}):    {hurwicz_d}")
        print(f"4. Minimax Regret:            {regret_d}")
        print(f"5. Laplace (Equal Likelihood):{laplace_d}")


# ----------------------------------------------------
# 4. Interactive Mode Functions
# ----------------------------------------------------

def get_matrix_input():
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
            
            if len(row) == 0:
                print("Empty input. Please enter numbers.")
                continue

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
    payoff_matrix = get_matrix_input()
    
    if not payoff_matrix:
        print("Exiting due to empty matrix.")
        return

    try:
        dss_problem = DecisionMaker(matrix=payoff_matrix)
    except Exception as e:
        print(f"Error initializing DecisionMaker: {e}")
        return

    while True:
        print("\n--- METHOD SELECTION ---")
        print("1: Maximax (Optimistic)")
        print("2: Maximin (Pessimistic)")
        print("3: Hurwicz (Realism)")
        print("4: Minimax Regret")
        print("5: Laplace (Equal Likelihood)")
        print("6: Show All Results")
        print("7: Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
        
        try:
            choice = int(choice)
            result_message = ""
            
            if choice == 1:
                result_message = dss_problem.maximax_approach()
            elif choice == 2:
                result_message = dss_problem.maximin_approach()
            elif choice == 3:
                try:
                    alpha_input = input("Enter Hurwicz Alpha (0 to 1) [Default 0.5]: ")
                    alpha = float(alpha_input) if alpha_input.strip() else 0.5
                    if 0 <= alpha <= 1:
                        result_message = dss_problem.hurwicz_approach(alpha=alpha)
                    else:
                        print("Alpha must be between 0 and 1.")
                        continue
                except ValueError:
                    print("Invalid Alpha input.")
                    continue
            elif choice == 4:
                result_message = dss_problem.regret_approach()
            elif choice == 5:
                result_message = dss_problem.laplace_approach()
            elif choice == 6:
                dss_problem.display_results(hurwicz_alpha=0.6)
                continue
            else:
                print("Invalid choice.")
                continue

            print("\n--- RESULT ---")
            print(result_message)
            
        except ValueError:
            print("Invalid input.")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    run_interactive_mode()