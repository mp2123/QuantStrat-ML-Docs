# Options Volatility Tracker & Backtesting Framework

> **Status:** Active Research & Development  
> **Privacy Note:** The private research/backtesting code, Charles Schwab API OAuth handlers, database reset scripts, and experimental strategy research and local model artifacts are stored in a local, private Git repository to protect credential security and keep runtime state private. This repository serves as a **public documentation shell** to highlight the architecture and workflow.

## Project Overview

A Python-based backtesting and options analytics research project designed to process historical market data, evaluate options pricing metrics, and study quantitative analytics and backtesting concepts.

### Key Capabilities

- **Backtesting Engine:** Built a custom Python backtesting framework supporting transaction costs, walk-forward validation, and strict no-look-ahead controls to prevent data leakage during model training.
- **Volatility Analytics:** Developed an options analytics module to compare implied vs. realized volatility, calculate Black-Scholes Greeks, visualize volatility skew, and estimate expected market moves using synthetic/public data inputs.
- **Risk-Adjusted Performance:** Automated calculation of key portfolio metrics including Sharpe/Sortino ratios, maximum drawdowns, and VaR/CVaR against benchmark comparisons.
- **Database Architecture:** Manages historical tick data and pre-computed features using a local SQL data warehouse.

## Tech Stack

- **Languages:** Python
- **Data Engineering:** SQL, pandas, NumPy
- **Machine Learning:** scikit-learn (Gradient Boosting, regression modeling)
- **Analytics:** Statistical Data Analysis, Cross-Validation, Backtesting, Risk Analytics

## Sanitized Code Excerpts

Select non-sensitive files and architectural components (such as DataFrame schemas and feature engineering definitions) are provided in the `examples/sanitized-code-excerpts/` directory to demonstrate data structures without exposing proprietary strategy implementations.
