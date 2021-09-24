import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Analysis:

    def __init__(self, dataset):
        self.dataset = dataset
        self.efficiency_column = pd.Series(dtype="object")
        self.most_efficient_player = 0
        self.least_efficient_player = 0
        self.optimal_row = pd.Series(dtype="object")
        self.least_optimal_row = pd.Series(dtype="object")
        self.efficient_dataset = self.obtain_efficiency()

    def __str__(self):
        return str(self.dataset)

    def obtain_efficiency(self):
        self.efficiency_column = self.dataset["pts"] / self.dataset["min"]
        self.dataset["Efficiency"] = self.efficiency_column
        return self.dataset

    def find_efficient_player(self):
        self.most_efficient_player = max(
            self.obtain_efficiency()["Efficiency"])

        self.optimal_row = self.dataset.loc[df['Efficiency']
                                            == self.most_efficient_player]

        print("\nFinding most efficient player: ")

        return self.optimal_row

    def find_least_efficient_player(self):
        self.least_efficient_player = min(
            self.obtain_efficiency()["Efficiency"])

        self.least_optimal_row = self.dataset.loc[df['Efficiency']
                                                  == self.least_efficient_player]

        print("\nFinding least efficient player: ")

        return self.least_optimal_row

    def plotting_efficiency(self):
        plt.figure(figsize=(10, 7))
        plt.scatter(self.efficient_dataset["gp"],
                    self.efficient_dataset["Efficiency"])
        plt.title("Efficiency vs. Games Played")
        plt.xlabel("Games Played")
        plt.ylabel("Efficiency (Pts. per min played)")
        plt.show()

    def efficiency_distribution(self):

        plotting_data = self.efficient_dataset["Efficiency"]
        binwidth = 0.02

        plt.figure(figsize=(10, 7))
        plt.hist(x=plotting_data,
                 bins=np.arange(min(plotting_data), max(
                     plotting_data) + binwidth, binwidth),
                 density=False)
        plt.title("Distribution of Player Efficiency")
        plt.xlabel("Efficiency of Player (Pts. per min played)")
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    df = pd.read_csv("nba-players.csv")
    analysing_players = Analysis(df)
    print(analysing_players.find_efficient_player())
    print(analysing_players.plotting_efficiency())
    print(analysing_players.efficiency_distribution())
