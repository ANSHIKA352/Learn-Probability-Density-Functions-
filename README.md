
## Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model

---

## 📌 Project Overview

This project aims to learn the parameters of a Probability Density Function (PDF) after applying a roll-number-based non-linear transformation to real-world environmental data.

The dataset used contains air quality measurements across various Indian cities. The feature selected for analysis is **NO₂ (Nitrogen Dioxide)** concentration.

The objective is to:
1. Apply a roll-number-parameterized non-linear transformation.
2. Estimate parameters of a Gaussian-like probability density function.

---

## 📊 Dataset Information

- **Dataset:** India Air Quality Data  
- **Source:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data  
- **Feature Used:** `no2`

---

## 🔹 Step 1: Non-Linear Transformation

Each NO₂ value \( x \) is transformed using:

\[
z = x + a_r \sin(b_r x)
\]

Where:

- \( a_r = 0.05 \times (r \bmod 7) \)
- \( b_r = 0.3 \times ((r \bmod 5) + 1) \)
- \( r \) = University Roll Number
- mod = remainder operation

This transformation introduces controlled non-linearity dependent on the roll number.

---

## 🔹 Step 2: Learning the Probability Density Function

We estimate parameters of the following Gaussian-like PDF:

\[
\hat{p}(z) = c \cdot e^{-\lambda (z - \mu)^2}
\]

### Parameter Estimation Method

Maximum Likelihood Estimation (MLE) is used to estimate:

- **μ (Mean)** = Mean of transformed values  
- **σ² (Variance)** = Variance of transformed values  

From variance:

- \( \lambda = \frac{1}{2\sigma^2} \)
- \( c = \frac{1}{\sqrt{2\pi\sigma^2}} \)

---

## 📈 Output

- Histogram of transformed variable \( z \)
- Learned probability density function plotted over histogram
- Estimated values of μ, λ, and c

---

## 🛠 Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Google Colab  

---

## 📚 Concepts Demonstrated

- Non-linear feature transformation  
- Gaussian distribution modeling  
- Probability Density Function estimation  
- Maximum Likelihood Estimation (MLE)  
- Data preprocessing and visualization  

---

## 🚀 Learning Outcome

This project demonstrates practical implementation of statistical modeling and probability density estimation using real-world environmental data.

---

## 📂 Repository Structure

```
│── assignment.ipynb
│── main.py
│── README.md
```


University: Your University Name  

