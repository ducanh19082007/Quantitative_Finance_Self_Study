import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split

class Regression:
    def Linear_Regression(self, X_train, y_train, X_test):
        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import Pipeline

        # Build pipeline
        Lig_Reg_Pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("LinearRegression", LinearRegression(
                fit_intercept=True,
                positive=True
            )),
        ])

        # Reshape for sklearn (2D)
        X_train = X_train[:, np.newaxis]
        X_test = X_test[:, np.newaxis]

        Lig_Reg_Pipeline.fit(X_train, y_train)

        y_predict = Lig_Reg_Pipeline.predict(X_test)

        Lig_Reg = Lig_Reg_Pipeline.named_steps["LinearRegression"]

        intercept_predict = Lig_Reg.intercept_
        weight = Lig_Reg.coef_

        return y_predict, weight, intercept_predict
    
    def Polynomial_Regression(self, X_train, y_train, X_test):
        """Polynomial Regression: later"""

    def Put_graph_into_folder(self, folder_name, file_name, X_train, y_train, X_test, y_pred):
        # Create folder INSIDE the current script's directory
        base_dir = Path(__file__).parent
        folder_path = base_dir / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        # Final output path (inside that folder)
        output_path = folder_path / f"{file_name}_regression.png"

        # Plot training data
        plt.figure()
        plt.scatter(X_train, y_train, label="Training Data")

        # True line
        y_real = 3 * X_test + 1
        plt.plot(X_test, y_real, label="True Line (y = 3x + 1)", linestyle="--", color="green")

        # Model prediction line
        plt.plot(X_test, y_pred, label="Model Prediction", color="red")

        plt.legend()

        # Save correctly
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.show()
        plt.close()

        print(f"Saved graph to: {output_path}")


    @staticmethod
    def Linear_Reg_main():
        rng = np.random.RandomState(16)

        # Training data
        X_train = 10 * rng.rand(90)
        y_train = 3 * X_train + 1 + 3.5978*rng.randn(90)

        # Test data
        X_test = np.linspace(0, 10, 100)

        # Create model
        model = Regression()

        # Train + Predict
        y_pred, weights, intercept = model.Linear_Regression(X_train, y_train, X_test)

        print(f"Learned weight (slope): {weights}")
        print(f"Learned intercept (bias): {intercept}")

        # Plot + Save
        model.Put_graph_into_folder("plots", "linear_regression", X_train, y_train, X_test, y_pred)

if __name__ == "__main__":
    Regression.Linear_Reg_main()
