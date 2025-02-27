# 🧾 Data Sweeper

**A Streamlit-Powered CSV/Excel Converter with Built-in Data Cleaning**  
Transform files between formats while ensuring data quality through automated cleaning and visualization.

## ✨ Features

- **Dual Format Conversion**  
  Convert CSV ↔ Excel seamlessly while preserving data integrity
- **Smart Data Cleaning**  
  - Remove duplicate rows with 1 click  
  - Auto-fill missing numeric values using column averages
- **Encoding Flexibility**  
  Supports UTF-8, Latin1, ISO-8859-1, CP1252 encodings for CSVs
- **Column Control**  
  Selectively choose columns to process/export
- **Instant Visualizations**  
  Auto-generated bar/line charts for numeric columns
- **Error Diagnostics**  
  Clear troubleshooting guides for common file issues

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-FF4B4B?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas)
![Openpyxl](https://img.shields.io/badge/Openpyxl-3.1%2B-green)

## 🚀 Installation & Usage

### Requirements
```bash
pip install streamlit pandas openpyxl altair
```

# Quick Start

## Clone repository:
```bash
git clone https://github.com/your-username/data-sweeper.git
cd data-sweeper
```
## Launch app:
```bash
streamlit run app.py
```

# Workflow
Upload CSV/XLSX files via drag-and-drop

- **Clean Data using 1-click tools**
- -**Select Columns to keep in final output**
- **Visualize numeric trends with auto-charts**
- **Convert & Download in desired format**

# 🚨 Troubleshooting Guide

## Common Fixes:
```bash
# Fix missing dependencies
pip install --force-reinstall openpyxl pandas

# Resolve encoding errors
pip install charset-normalizer==3.3.2

# Fix visualization issues
pip install --upgrade jsonschema referencing
```
# 🤝 Contributing

## Fork the repository
## Create feature branch:
```bash
git checkout -b feature/your-feature
```
## Commit changes:
```bash
git commit -m 'Add awesome feature'
```
## Push to branch:
```bash
git push origin feature/your-feature
```
## Open a Pull Request

# 📜 License
© 2025 Zuhaib Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
