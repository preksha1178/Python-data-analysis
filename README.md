# Python-data-analysis
Online Shopping Data Analysis
Project Overview

This project analyzes an online shopping dataset to understand customer behavior, sales trends, and product performance. The analysis is performed using Python libraries to clean, process, and visualize the data.

The goal of this project is to demonstrate basic data analysis skills such as data loading, data processing, grouping, and visualization.

Technologies Used

Python

Pandas

NumPy

Matplotlib

Dataset Description

The dataset contains information about customer orders from an online store.

Columns in the dataset:

Column	Description
OrderID	Unique ID for each order
Customer	Name of the customer
Product	Product purchased
Category	Product category
Price	Price of the product
Quantity	Number of items purchased
Project Workflow
1 Data Loading

The dataset is loaded using Pandas from a CSV file.

2 Data Processing

Data is cleaned and a new column called Total Sales is created using:

Total = Price × Quantity

3 Data Analysis

The dataset is analyzed to find:

Total sales by category

Product performance

Sales distribution

4 Data Visualization

Graphs are generated to visualize insights using Matplotlib.

Examples of charts:

Category-wise sales bar chart

Product performance chart

Output Example

The project generates insights such as:

Which category has the highest sales

Which product generates the most revenue

Overall sales distribution

Project Structure
Online-Shopping-Data-Analysis
│
├── dataset.csv
├── analysis.py
└── README.md
How to Run the Project

Install required libraries

pip install pandas numpy matplotlib

Run the Python script

python analysis.py
Conclusion

This project demonstrates how Python can be used to analyze business data and extract meaningful insights. It helps in understanding customer purchasing patterns and sales trends.
