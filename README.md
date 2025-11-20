# 🌍 Global Life Expectancy Data Analysis

## 📊 Overview

This project explores the relationship between **life expectancy** and several socioeconomic and health-related factors across **183 countries** from **2000 to 2015**. The dataset was sourced from the **World Health Organization (WHO)** via Kaggle, and includes variables such as GDP per capita, alcohol consumption, immunizations, healthcare expenditure, and years of schooling. 

The core question guiding this analysis is:

> **How should countries allocate their resources to best serve their citizens' health and prosperity?**

Our goal is to uncover patterns that can inform policymakers, researchers, and activists in improving global health outcomes.

---

## 📁 Project Structure

```bash
life-expectancy-analysis/
│
├── data/                          # Raw and cleaned CSV datasets
├── notebooks/                     # Jupyter Notebooks with EDA & visualizations
├── src/                           # Python scripts for cleaning, regression, plotting
├── outputs/                       # Generated figures and final visuals
├── README.md                      # Project overview and documentation
└── requirements.txt               # Python package dependencies
```

---

## 📦 Dataset Description

- **Source:** [Kaggle - Life Expectancy (WHO)](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- **Years Covered:** 2000–2015
- **Countries:** 183 (after filtering for missing data)
- **Observations:** 2,939 rows
- **Variables:** 22 including:
  - Life expectancy
  - GDP per capita
  - Health expenditure
  - Immunization rates
  - Alcohol consumption
  - BMI
  - Schooling
  - Status (developing vs developed)

---

## 🔍 Research Questions

1. **What is the relationship between GDP per capita and life expectancy in 2015?**
2. **How have changes in healthcare expenditure correlated with changes in life expectancy from 2000 to 2014?**
3. **Is there a significant relationship between years of schooling and life expectancy in 2015?**

---

## 🛠️ Methods

- **Python libraries used:** `pandas`, `matplotlib`, `statsmodels`
- **Statistical analysis:**
  - Linear regression
  - R² values to evaluate correlation strength
- **Visualizations:**
  - Color-coded scatter plots (developed vs. developing countries)
  - Comparative change analysis across time
- **Custom functions created to:**
  - Clean and organize country-level data
  - Compute percentage change across years
  - Visualize variable relationships

---

## 📈 Key Findings

### 1️⃣ GDP vs Life Expectancy
- **R² = 0.201** → Weak correlation
- High-income countries had higher life expectancy, but low-GDP countries varied widely, suggesting other key influencing factors.

### 2️⃣ Healthcare Expenditure Change vs Life Expectancy Change
- **Low direct correlation** found
- Even with massive increases in spending, some countries showed minimal improvement in life expectancy.
- Highlights the importance of **effective allocation** of resources rather than sheer spending.

### 3️⃣ Schooling vs Life Expectancy
- **R² = 0.67** → Strong correlation
- Especially evident in developing countries; increased education often linked with improved health outcomes.

---

## 📌 Limitations & Future Work

- **Omitted variable bias**: Not all key influencers (e.g., political stability, healthcare quality) were captured.
- **Data age**: Latest data is from 2015; excludes major events like COVID-19.
- **Next steps**:
  - Expand analysis with newer datasets
  - Break down "healthcare expenditure" into more detailed components
  - Explore machine learning models for improved prediction

---

## 📷 Visualizations

- **Figure 1:** Life Expectancy vs. GDP (2015)
- **Figure 2:** % Change in Healthcare Expenditure vs. % Change in Life Expectancy (2000–2014)
- **Figure 3:** Life Expectancy vs. Average Years of Schooling (2015)

---

## 📚 Citation

**Dataset:**  
Kumarra Jarshi, *Life Expectancy (WHO)*, 2017.  
🔗 https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who

---

## 🤝 Acknowledgments

This project was completed as part of a data analysis learning initiative. Special thanks to open data platforms and contributors who enable impactful, socially relevant research through accessible datasets.
