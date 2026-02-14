import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Load dataset and extract NO2 values.
    """
    df = pd.read_csv(file_path, encoding='latin1', low_memory=False)
    
    # Extract NO2 column (lowercase in dataset)
    x = df['no2'].dropna().values
    
    return x


def transform_feature(x, roll_number):
    """
    Apply roll-number-based non-linear transformation.
    z = x + ar * sin(br * x)
    """
    ar = 0.05 * (roll_number % 7)
    br = 0.3 * ((roll_number % 5) + 1)

    z = x + ar * np.sin(br * x)

    return z, ar, br


def estimate_parameters(z):
    """
    Estimate parameters of Gaussian-like PDF using MLE.
    """
    mu = np.mean(z)
    sigma2 = np.var(z)

    lambda_ = 1 / (2 * sigma2)
    c = 1 / np.sqrt(2 * np.pi * sigma2)

    return mu, sigma2, lambda_, c


def plot_pdf(z, mu, lambda_, c):
    """
    Plot histogram and learned PDF.
    """
    z_range = np.linspace(min(z), max(z), 500)
    pdf = c * np.exp(-lambda_ * (z_range - mu) ** 2)

    plt.figure(figsize=(8, 5))
    plt.hist(z, bins=50, density=True, alpha=0.6, label="Histogram of z")
    plt.plot(z_range, pdf, linewidth=2, label="Learned PDF")
    plt.title("Probability Density Function Estimation")
    plt.xlabel("Transformed Variable (z)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # 🔴 Enter your roll number here
    roll_number = 123  # Change this

    file_path = "data.csv"  # Change if filename is different

    # Step 1: Load Data
    x = load_data(file_path)

    # Step 2: Transform Feature
    z, ar, br = transform_feature(x, roll_number)

    print(f"ar = {ar}")
    print(f"br = {br}")

    # Step 3: Estimate PDF Parameters
    mu, sigma2, lambda_, c = estimate_parameters(z)

    print("\nEstimated Parameters:")
    print(f"Mean (mu): {mu}")
    print(f"Variance (sigma^2): {sigma2}")
    print(f"Lambda: {lambda_}")
    print(f"c: {c}")

    # Step 4: Plot
    plot_pdf(z, mu, lambda_, c)


if __name__ == "__main__":
    main()
