#data.seeding.py

import pandas as pd
import random
import os
import sys

# 1. تظبيط المسارات عشان الـ EXE
if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(script_dir, 'employee_data.csv')

# 2. استيراد ملفات المشروع
sys.path.insert(0, script_dir)
import database_config as dc
from analytics import get_salary_report, save_to_excel

# ==================== بداية الشغل ====================

print("بدء استيراد البيانات...")

# قراءة ملف الـ CSV
try:
    df = pd.read_csv(csv_path, usecols=['EmpID','FirstName','LastName','ADEmail','EmployeeStatus'])
    df = df[df['EmployeeStatus'] == 'Active']
    df = df.dropna(subset=['ADEmail'])

    df.rename(columns={
        'EmployeeStatus': 'Status',
        'ADEmail': 'Email'
    }, inplace=True)

    df['Email'] = df['Email'].str.lower().str.strip()
    df = df.drop_duplicates(subset=['EmpID'])
except FileNotFoundError:
    print(f"❌ خطأ: ملف البيانات مش موجود في المسار: {csv_path}")
    print("تأكد إن ملف employee_data.csv موجود جنب البرنامج.")
    input("اضغط Enter للخروج...")
    sys.exit()

# إدخال الموظفين
count = 0
for index, row in df.iterrows():
    # SQLite بيستخدم ? بدل %s
    sql = "INSERT OR IGNORE INTO employees (EmployeeID, FirstName, LastName, Email, Status) VALUES (?,?,?,?,?)"
    val = (row['EmpID'], row['FirstName'], row['LastName'], row['Email'], row['Status'])
    dc.cursor.execute(sql, val)
    if dc.cursor.rowcount:
        count += 1

dc.mydp.commit()
print(f"✅ تم إضافة {count} موظف جديد")

# إدخال السلف والجزاءات (Random Data)
n = ['Salary Advance', 'Health Insurance', 'Equipment Loan', 'Training Fees', 'Penalty']

for EmpID in df['EmpID']:
    sql = "INSERT OR IGNORE INTO financial_obligations (EmployeeID, Category, Amount, DueDate) VALUES (?,?,?,?)"
    category = random.choice(n)
    amount = random.randint(100, 5000)
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    duedate = f"2026-{month:02d}-{day:02d}"
    val = (EmpID, category, amount, duedate)
    dc.cursor.execute(sql, val)

dc.mydp.commit()
print("✅ تم تحديث السلف والجزاءات")

# تحديث الرواتب
for EmpID in df['EmpID']:
    sql = "UPDATE employees SET Salary=? WHERE EmployeeID=?"
    salary = random.randint(5000, 200000)
    val = (salary, EmpID)
    dc.cursor.execute(sql, val)

dc.mydp.commit()
print("✅ تم تحديث الرواتب")

# إنشاء التقرير
print("جاري إنشاء تقرير الرواتب...")
result = get_salary_report()
report_path = os.path.join(script_dir, "Final_Salary_Report.xlsx")
save_to_excel(result, report_path)

print("\n" + "="*60)
print("                تم بنجاح يا معلم! 💰🔥")
print(f"     التقرير جاهز باسم: Final_Salary_Report.xlsx")
print("="*60)

# ==================== إغلاق الاتصال (مهم جداً) ====================
try:
    dc.mydp.close()
    print("تم إغلاق قاعدة البيانات بأمان.")
except Exception as e:
    print(f"ملحوظة: {e}")

# ==================== تثبيت الشاشة للـ EXE ====================
try:
    input("\n                 اضغط Enter للخروج...")
except :
    os.system("pause >nul")