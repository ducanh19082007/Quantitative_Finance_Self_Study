import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from IPython.display import display
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class Agent:
    def __init__(self, epoch: int = 0):
        self.epoch = epoch

    @staticmethod
    def visualization(file_name: str):
        """Plot and save all numeric columns from CSV"""

        # === Build safe file path ===
        csv_path = Path(__file__).resolve().parent.parent / "csv_dataset" / file_name
        if not csv_path.exists():
            raise FileNotFoundError(f"File not found: {csv_path}")

        # === Load data ===
        df = pd.read_csv(csv_path)
        display(df.head())

        # Clean column names
        df.columns = df.columns.str.strip()

        # === Output folder ===
        output_folder = Path(__file__).parent / f"{file_name}_plots"
        output_folder.mkdir(parents=True, exist_ok=True)

        # === Plot all numeric columns ===
        for col in df.columns:
            if not np.issubdtype(df[col].dtype, np.number):
                continue

            plt.figure(figsize=(10, 5))
            plt.plot(df[col])
            plt.title(f"{col} Over Time")
            plt.xlabel("Index")
            plt.ylabel(col)

            output_path = output_folder / f"{col}.png"
            plt.savefig(output_path, dpi=300, bbox_inches="tight")
            plt.show()
            plt.close()

    @staticmethod
    def convert_to_csv(input_file: str, output_name: str):
        """
        Converts non-CSV files into CSV and saves to csv_dataset.
        Currently supports Excel (.xlsx).
        """
        input_path = Path(input_file)

        if not input_path.exists():
            raise FileNotFoundError(f"File not found: {input_path}")

        output_folder = Path(__file__).resolve().parent.parent / "csv_dataset"
        output_folder.mkdir(parents=True, exist_ok=True)

        if input_path.suffix in [".xlsx", ".xls"]:
            df = pd.read_excel(input_path)
        else:
            raise ValueError("Unsupported file type for conversion")

        output_path = output_folder / f"{output_name}.csv"
        df.to_csv(output_path, index=False)

        print(f"Saved CSV to: {output_path}")

    @staticmethod
    def pca_conversion(file_name: str, n_components: int = 2):
        """Run PCA and generate plots + dataset"""

        # === Load CSV ===
        csv_path = Path(__file__).resolve().parent.parent / "csv_dataset" / file_name
        if not csv_path.exists():
            raise FileNotFoundError(f"File not found: {csv_path}")

        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()

        # === Extract numeric data (skip first column like Date) ===
        df_num = df.iloc[:, 1:]

        # === PCA Pipeline ===
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("pca", PCA(n_components=n_components))
        ])

        principal_comps = pipeline.fit_transform(df_num)

        pca_df = pd.DataFrame(
            principal_comps,
            columns=[f"PC{i+1}" for i in range(n_components)]
        )

        display(pca_df.head())

        # === Save PCA CSV ===
        dataset_folder = Path(__file__).parent / f"{file_name}_PCA_Dataset"
        dataset_folder.mkdir(parents=True, exist_ok=True)

        pca_csv_path = dataset_folder / f"{file_name}_PCA.csv"
        pca_df.to_csv(pca_csv_path, index=False)

        # === Plot folder ===
        plot_folder = Path(__file__).parent / f"{file_name}_plots"
        plot_folder.mkdir(parents=True, exist_ok=True)

        # --- Scatter + KDE plot ---
        plt.figure(figsize=(10, 6))
        sns.kdeplot(
            x=pca_df["PC1"],
            y=pca_df["PC2"],
            fill=True,
            cmap="Blues",
            thresh=0.05,
            levels=15
        )
        sns.scatterplot(
            x="PC1",
            y="PC2",
            data=pca_df,
            s=40
        )

        plt.title("PCA Scatter + Density")

        scatter_path = plot_folder / f"{file_name}_PCA_scatter.png"
        plt.savefig(scatter_path, dpi=300, bbox_inches="tight")
        plt.close()

        # --- PC1 Line Plot ---
        plt.figure(figsize=(12, 5))
        sns.lineplot(data=pca_df["PC1"], label="PC1")
        plt.axhline(pca_df["PC1"].mean(), linestyle="--", label="Mean")
        plt.axhline(pca_df["PC1"].max(), linestyle=":", label="Max")
        plt.axhline(pca_df["PC1"].min(), linestyle=":", label="Min")

        plt.title("PC1 Over Time")
        plt.xlabel("Index")
        plt.ylabel("PC1 Value")
        plt.legend()

        line_path = plot_folder / f"{file_name}_PC1_line.png"
        plt.savefig(line_path, dpi=300, bbox_inches="tight")
        plt.show()
        plt.close()

    def agent_in_action(self):
        """Agent execution placeholder"""
        pass


if __name__ == "__main__":
    Agent.visualization("TSLA.csv")
    Agent.pca_conversion("TSLA.csv", 2)
