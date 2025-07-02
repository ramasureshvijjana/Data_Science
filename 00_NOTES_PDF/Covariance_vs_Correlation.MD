# 📊 Covariance vs Correlation

---

## 🔹 Covariance

📌 **Definition**:  
Covariance measures how two variables change together.

📈 **Value Range**:  
Can be any real number (positive, negative, or zero).

🔍 **Interpretation**:
- ➕ **Positive**: Variables increase together  
- ➖ **Negative**: One increases while the other decreases  
- 0️⃣ **Zero**: No linear relationship

📐 **Units**:  
Depends on the units of the variables (e.g., `cm²`, `kg·m`, etc.)

🧮 **Formula**:  
```math
\text{Cov}(X, Y) = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
```
---

## 🔹 Correlation

📌 **Definition**:  
Correlation is the normalized form of covariance, showing the **strength and direction** of the linear relationship.

📏 **Value Range**:  
- ➕ `+1`: Perfect positive linear relationship  
- ➖ `-1`: Perfect negative linear relationship  
- 0️⃣ `0`: No linear relationship

📐 **Units**:  
Unitless (dimensionless)

⚖️ **Removes Scale Effect**:  
Makes it easier to compare relationships between different variable pairs.

🧮 **Formula**:  
```math
\text{Corr}(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}
```

Where:  
- σX = Standard deviation of X  
- σY = Standard deviation of Y

---

## 🔸 Summary Table

| 🧾 **Feature**     | 📉 **Covariance**                      | 📈 **Correlation**                            |
|--------------------|----------------------------------------|-----------------------------------------------|
| 🔍 Measures         | Direction of relationship              | Direction **and** strength of relationship    |
| 🔢 Range            | -∞ to +∞                               | -1 to +1                                       |
| 📐 Scale-sensitive  | ✅ Yes                                  | ❌ No (unitless)                               |
| 🎯 Use Case         | Intermediate step for correlation      | Easy comparison between variables             |
