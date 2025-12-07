import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import csv
from IPython.display import display
from pathlib import Path
import os

class Agent:
    def __init__(self, epoch):
        self.epoch = epoch

    @staticmethod
    def visualization_(file_name: str):
        # Build path to CSV
        path = Path(__file__).parent / "csv_dataset" / file_name

        # Read CSV
        df = pd.read_csv(path)

        # Display first 5 rows
        display(df.head(5))

        # Plot the 'Close' 
        df.columns = df.columns.str.strip()
        if "Close" in df.columns:
            plt.figure(figsize=(10, 5))
            plt.plot(df["Close"], label="Close Price")
            plt.title("TSLA Close Price")
            plt.xlabel("Index")
            plt.ylabel("Price")
            plt.legend()
            plt.show()
        else:
            print("No 'Close' column found in CSV.")
            
    @staticmethod
    def change_to_csv(other_file_name: str) -> pd.DataFrame:
        '''this will chance other file but csv into csv itself, and put into the folder csv_dataset'''
    
    @staticmethod
    def PCA_convertion(file_name:str, n_components: int = 2) -> pd.DataFrame:
        from sklearn.decomposition import PCA
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import Pipeline
        
        path = Path(__file__).parent / "csv_dataset" / file_name
        
        df = pd.read_csv(path)
        
        df.columns = df.columns.str.strip()
        
        df_num = df.iloc[:, 1:]
        
        pipeline_ = Pipeline([
            ("scaler", StandardScaler()),
            ("PCA", PCA(n_components=n_components))
        ])
        
        principal_com = pipeline_.fit_transform(df_num)
        
        pca_df = pd.DataFrame(
            principal_com, columns=[f"PC{i+1}" for i in range(n_components)],
        )
        
        display(pca_df.head())
        
        OUTPUT_FOLDER = Path(__file__).parent /  f"{file_name}_PCA_Dataset"
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        output_path = os.path.join(OUTPUT_FOLDER, f"{file_name}_PCA_implemented.csv")
        pca_df.to_csv(output_path, index = False)
        
        import seaborn as sns

        # Assume pca_df is your PCA DataFrame with PC1 and PC2
        # For demonstration, let's say we have:
        # pca_df = pd.DataFrame(principal_components, columns=["PC1", "PC2"])
        import seaborn as sns

        OUTPUT_FOLDER = Path(__file__).parent / f"{file_name}_plot"
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        plt.figure(figsize=(10, 6))
        sns.kdeplot(
            x=pca_df["PC1"], 
            y=pca_df["PC2"], 
            fill=True,
            cmap="Blues", 
            thresh=0.05,
            levels=15,
            alpha=0.5
        )
        sns.scatterplot(
            x="PC1", 
            y="PC2", 
            data=pca_df, 
            color="red", 
            s=40, 
            alpha=0.6
        )
        plt.title("PCA of Stock Data: Scatter + Density")

        # Save first figure BEFORE showing
        output_path_1 = os.path.join(OUTPUT_FOLDER, f"{file_name}_PCA_scatter.png")
        plt.savefig(output_path_1, dpi=300, bbox_inches="tight")
        plt.show()
        plt.close()  # close to avoid overlap

        # 2️⃣ Line plot for PC1 over time
        plt.figure(figsize=(12, 5))
        sns.lineplot(data=pca_df["PC1"], label="PC1", color="blue")
        plt.axhline(pca_df["PC1"].mean(), color="green", linestyle="--", label="Mean")
        plt.axhline(pca_df["PC1"].max(), color="red", linestyle=":", label="Max")
        plt.axhline(pca_df["PC1"].min(), color="orange", linestyle=":", label="Min")
        plt.title("PC1 Evolution Over Time with Min/Max/Mean")
        plt.xlabel("Index")
        plt.ylabel("PC1 Value")
        plt.legend()

        # Save second figure BEFORE showing
        output_path_2 = os.path.join(OUTPUT_FOLDER, f"{file_name}_PC1_line.png")
        plt.savefig(output_path_2, dpi=300, bbox_inches="tight")
        plt.show()
        plt.close()

        print("\nExplained variance ratio:")
        #print(pipeline_.named_steps["pca"].explained_variance_ratio_)

        


if __name__ == "__main__":
    Agent.visualization_("TSLA.csv")
    Agent.PCA_convertion("TSLA.csv", 2)
