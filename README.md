# 💰 Payroll Management System (Lite)

A Python-based automated payroll system designed to process employee data, calculate financial obligations, and generate professional salary reports. This project demonstrates backend development skills, database management, and data automation.

## 🚀 Key Features
- **Database Integration:** Uses **SQLite** for reliable, serverless data storage.
- **Data Processing:** Automated cleaning and seeding of employee data from CSV files.
- **Financial Logic:** Calculates net salaries by processing complex SQL joins between employees and financial obligations (penalties, advances, etc.).
- **Automated Reporting:** Generates a professional **Excel (XLSX)** report with a single click using **Pandas**.
- **Portable:** Packaged into a standalone **EXE** for easy distribution.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, SQLite3, Openpyxl
- **Database:** SQLite
- **Deployment:** PyInstaller

## 📂 Project Structure
- `data_seeding.py`: The main entry point. Handles CSV importing, database seeding, and report triggers.
- `database_config.py`: Core database configuration and schema definition.
- `analytics.py`: Contains the business logic for calculating salaries and exporting to Excel.
- `employee_data.csv`: Sample dataset used for processing.

## 📊 How It Works
1. **Import:** The system reads active employee data from a CSV file.
2. **Seed:** It populates the SQLite database with employees and generates random financial records (for demo purposes).
3. **Calculate:** Runs an optimized SQL query to aggregate deductions and compute net salaries.
4. **Export:** Saves the final results into a formatted Excel file (`Final_Salary_Report.xlsx`).
