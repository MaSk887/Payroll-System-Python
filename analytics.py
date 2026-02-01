#analytics.py

import database_config as dc
import pandas as pd


def get_salary_report():
    # 1. جملة الـ SQL (صلحت الفاصلة المنقوطة وضفت الترتيب)
    sql = """ 
    SELECT 
        E.FirstName || ' ' || E.LastName as Emp_Name, 
        E.Salary, 
        COALESCE(SUM(F.Amount),0) as Deduction, 
        (E.Salary - COALESCE(SUM(F.Amount),0)) as FinalSalary  
    FROM employees E
    LEFT JOIN financial_obligations F ON E.EmployeeID = F.EmployeeID
    GROUP BY E.EmployeeID, E.FirstName, E.LastName, E.Salary
    ORDER BY FinalSalary DESC;
    """

    # 2. السحر هنا: Pandas بياخد جملة SQL والاتصال، ويرجع جدول جاهز
    # لاحظ إننا استخدمنا dc.mydp (اللي هو الاتصال نفسه) مش الـ cursor
    df = pd.read_sql_query(sql, dc.mydp)
    return df


def save_to_excel(df, filename):
    # 3. الدالة دي دلوقتي بتستلم DataFrame جاهز مش قائمة
    # فمش محتاجين نكتب pd.DataFrame() تاني ولا نكتب أسماء الأعمدة تاني

    df.index = df.index + 1
    df.index.name = '#'

    # الحفظ مباشرة
    df.to_excel(filename)
    print('done')