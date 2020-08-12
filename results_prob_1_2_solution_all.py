import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

problem_1 = [{'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'breadth_first_search', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 43, 'GOAL_TESTS': 56, 'STATES': 178}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'depth_first_graph_search', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 21, 'GOAL_TESTS': 22, 'STATES': 84}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'uniform_cost_search', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 60, 'GOAL_TESTS': 62, 'STATES': 240}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_unmet_goals', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 7, 'GOAL_TESTS': 9, 'STATES': 29}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_levelsum', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 6, 'GOAL_TESTS': 8, 'STATES': 28}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_maxlevel', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 6, 'GOAL_TESTS': 8, 'STATES': 24}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_setlevel', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 6, 'GOAL_TESTS': 8, 'STATES': 28}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'astar_search: h_unmet_goals', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 50, 'GOAL_TESTS': 52, 'STATES': 206}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'astar_search: h_pg_levelsum', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 28, 'GOAL_TESTS': 30, 'STATES': 122}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'astar_search: h_pg_maxlevel', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 43, 'GOAL_TESTS': 45, 'STATES': 180}, {'PROBLEM_NAME': 'Air Cargo Problem 1', 'SOLUTION_NAME': 'astar_search: h_pg_setlevel', 'ACTIONS_LENGTH': 20, 'EXPANSIONS': 33, 'GOAL_TESTS': 35, 'STATES': 138}, 
{'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'breadth_first_search', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 3343, 'GOAL_TESTS': 4609, 'STATES': 30503}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'depth_first_graph_search', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 624, 'GOAL_TESTS': 625, 'STATES': 5602}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'uniform_cost_search', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 5154, 'GOAL_TESTS': 5156, 'STATES': 46618}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_unmet_goals', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 17, 'GOAL_TESTS': 19, 'STATES': 170}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_levelsum', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 9, 'GOAL_TESTS': 11, 'STATES': 86}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_maxlevel', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 27, 'GOAL_TESTS': 29, 'STATES': 249}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'greedy_best_first_graph_search: h_pg_setlevel', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 9, 'GOAL_TESTS': 11, 'STATES': 84}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'astar_search: h_unmet_goals', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 2467, 'GOAL_TESTS': 2469, 'STATES': 22522}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'astar_search: h_pg_levelsum', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 357, 'GOAL_TESTS': 359, 'STATES': 3426}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'astar_search: h_pg_maxlevel', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 2887, 'GOAL_TESTS': 2889, 'STATES': 26594}, {'PROBLEM_NAME': 'Air Cargo Problem 2', 'SOLUTION_NAME': 'astar_search: h_pg_setlevel', 'ACTIONS_LENGTH': 72, 'EXPANSIONS': 1037, 'GOAL_TESTS': 1039, 'STATES': 9605}]

def return_subset(df: pd.DataFrame, col: str) -> pd.DataFrame:
    return df[["SOLUTION_NAME", col]]

def set_plot(x, y, x_label, y_label, title):
    pos = np.arange(len(x))
    fig, ax1 = plt.subplots()
    ax1.bar(x, y)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.set_title(title)
    ax1.tick_params(axis='x', direction='out', rotation=90)
    plt.show()

def main():
    df = pd.DataFrame(problem_1)
    subset_list = ["EXPANSIONS", "GOAL_TESTS", "STATES"]
    df1, df2 = df.loc[df["PROBLEM_NAME"] == "Air Cargo Problem 1"], df.loc[df["PROBLEM_NAME"] == "Air Cargo Problem 2"]

    df1_subset = {}
    df2_subset = {}

    for sub in subset_list:
        df1_subset[sub] = return_subset(df1, sub)

    for sub in df1_subset:
        current = df1_subset[sub]
        x, Y = current["SOLUTION_NAME"], current[sub]
        set_plot(x, Y, "SOLUTION", sub, f"{sub} by solution")


main()
