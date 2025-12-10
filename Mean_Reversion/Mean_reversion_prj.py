import yfinance
import pandas as pd
import numpy as np
from pathlib import Path
from IPython.display import display
import matplotlib.pyplot as plt
from typing import List, Tuple


class Mean_Reversion:
    def data_local_retrieve(self, file_name: str) -> pd.DataFrame:
        csv_path = Path(__file__).resolve().parent.parent / "csv_dataset" / file_name
        
        if not csv_path.exists():
            raise FileNotFoundError(f"Input path not found: {file_name}")

        dataframe_csv = pd.read_csv(csv_path)
        dataframe_csv.columns = dataframe_csv.columns.str.strip()
        display(dataframe_csv)
        return dataframe_csv

    def __init__(self, file_name):
        self.csv_dataset = self.data_local_retrieve(file_name)

    @staticmethod
    def data_yfinance_retrieve():
        pass

    def Basic_Mean_Reversion_(self, prices: List[float],
                              init_value = 100, 
                             buy_threshold: float = 1, 
                             sell_threshold: float = 1, 
                             trading_cost: float = 0.0
                            ) -> Tuple[List[float], float, List[float]]:
        """
        Basic mean-reversion strategy using Z-score.

        Args:
            prices: List of historical prices.
            buy_threshold: Z-score threshold to trigger buy.
            sell_threshold: Z-score threshold to trigger sell.
            trading_cost: Fractional cost per trade.

        Returns:
            profits: List of profit/loss per time step.
            total_profit: Sum of profits.
            capital_curve: Cumulative capital over time.
        """

        prices_array = np.array(prices)
        n = len(prices)
        profits = []
        capital_curve = [init_value]  # Start capital
        position_prev = 0
        capital_prev = 1.0

        cumulative_sum = 0.0
        cumulative_sq_diff = 0.0

        for t in range(n):
            P_t = prices[t]
            cumulative_sum += P_t
            mean_t = cumulative_sum / (t + 1)

            if t == 0:
                std_t = 0
            else:
                cumulative_sq_diff += (P_t - mean_t) ** 2
                std_t = np.sqrt(cumulative_sq_diff / (t + 1))

            # Calculate Z-score
            Z_t = 0 if std_t == 0 else (P_t - mean_t) / std_t

            # Decision: 1 = Buy, -1 = Sell, 0 = Hold
            if Z_t < -buy_threshold:
                position = 1
            elif Z_t > sell_threshold:
                position = -1
            else:
                position = 0

            # Profit calculation
            if t == 0:
                profit = 0
            else:
                price_change = P_t - prices_array[t-1]
                profit = position_prev * price_change - trading_cost * abs(position_prev - position)
            
            profits.append(profit)

            # Update capital
            capital_prev = capital_prev * (1 + profit / (prices_array[t-1] if t > 0 else P_t))
            capital_curve.append(capital_prev)

            # Update previous position
            position_prev = position

        total_profit = sum(profits)
        return profits, total_profit, capital_curve


    def run_and_plot_strategy(self, price_column: str, save_plot: bool = False, plot_file: str = "mean_reversion_plot.png"):
            """Run the mean-reversion strategy and plot profits."""
            prices = self.csv_dataset[price_column].values.tolist()

            profits, total_profit, capital_curve = self.Basic_Mean_Reversion_(prices)

            # Add results to DataFrame
            self.csv_dataset["MeanRev_Profit"] = profits
            self.csv_dataset["CumProfit"] = self.csv_dataset["MeanRev_Profit"].cumsum()
            self.csv_dataset["Capital"] = capital_curve[:-1]

            # Print first 20 rows
            print("\n=== Strategy Profits (first 20 rows) ===")
            print(self.csv_dataset[["MeanRev_Profit", "CumProfit", "Capital"]].head(20))
            print("Total profit:", total_profit)

            # Plotting
            fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

            axes[0].plot(self.csv_dataset[price_column], color="blue")
            axes[0].set_title(f"{price_column} Price")

            axes[1].plot(self.csv_dataset["MeanRev_Profit"], color="orange")
            axes[1].set_title("Mean Reversion Profit per Step")

            axes[2].plot(self.csv_dataset["CumProfit"], color="green")
            axes[2].set_title("Cumulative Profit")

            plt.tight_layout()
            if save_plot:
                plt.savefig(plot_file, dpi=300)
                print(f"Plot saved as {plot_file}")
            plt.show()
            plt.close()


if __name__ == "__main__":
    FILE_NAME = "TSLA.csv"
    PRICE_COLUMN = "Close"

    bot = Mean_Reversion(FILE_NAME)
    bot.run_and_plot_strategy(PRICE_COLUMN)