import frappe


def after_insert_company_payroll(doc, method=None):
    # create a employee payroll record for each employee in the company for that month and year
    # get all employees in the company
    employees = frappe.get_all(
        "Employee", filters={"company": doc.company}, fields=["name", "first_name", "last_name", "оклад", "designation", "department"])
    for employee in employees:
        # create a employee payroll record for each employee in the company for that month and year
        # create a doc of payroll.real_agro_pay_roll_system.emp
        employee_payroll = frappe.get_doc({
            'doctype': 'Employee Payroll',
        })
        employee_payroll.employee = employee.name
        employee_payroll.first_name = employee.first_name
        employee_payroll.last_name = employee.last_name
        # get month from the date field in doc.payroll_period
        employee_payroll.designition = employee.designition
        employee_payroll.department = employee.department
        employee_payroll.period_date = doc.payroll_period
        employee_payroll.company = doc.company
        if employee.оклад:
            employee_payroll.basic_salary = float(
                employee.оклад.replace(" ", ""))
        else:
            employee_payroll.basic_salary = 0.0
        employee_payroll.day_1 = 0.0
        employee_payroll.day_2 = 0.0
        employee_payroll.day_3 = 0.0
        employee_payroll.day_4 = 0.0
        employee_payroll.day_5 = 0.0
        employee_payroll.day_6 = 0.0
        employee_payroll.day_7 = 0.0
        employee_payroll.day_8 = 0.0
        employee_payroll.day_9 = 0.0
        employee_payroll.day_10 = 0.0
        employee_payroll.day_11 = 0.0
        employee_payroll.day_12 = 0.0
        employee_payroll.day_13 = 0.0
        employee_payroll.day_14 = 0.0
        employee_payroll.day_15 = 0.0
        employee_payroll.day_16 = 0.0
        employee_payroll.day_17 = 0.0
        employee_payroll.day_18 = 0.0
        employee_payroll.day_19 = 0.0
        employee_payroll.day_20 = 0.0
        employee_payroll.day_21 = 0.0
        employee_payroll.day_22 = 0.0
        employee_payroll.day_23 = 0.0
        employee_payroll.day_24 = 0.0
        employee_payroll.day_25 = 0.0
        employee_payroll.day_26 = 0.0
        employee_payroll.day_27 = 0.0
        employee_payroll.day_28 = 0.0
        employee_payroll.day_29 = 0.0
        employee_payroll.day_30 = 0.0
        employee_payroll.day_31 = 0.0
        employee_payroll.total_hours = 0.0
        employee_payroll.total_salary = 0.0
        employee_payroll.total_overtime_amount = 0.0
        employee_payroll.total_deductions = 0.0
        employee_payroll.total_tax = 0.0
        employee_payroll.total_net_salary = 0.0
        employee_payroll.total_bank = 0.0
        employee_payroll.total_cash = 0.0
        employee_payroll.tax_on_workers = 0.0
        employee_payroll.tax_on_salary_for_credit = 0.0
        employee_payroll.tax_on_salary = 0.0
        employee_payroll.save()
        frappe.db.commit()


def before_save_employee_payroll(doc, method=None):
    doc.total_hours = doc.day_1 + doc.day_2 + doc.day_3 + doc.day_4 + doc.day_5 + doc.day_6 + doc.day_7 + doc.day_8 + doc.day_9 + doc.day_10 + doc.day_11 + doc.day_12 + doc.day_13 + doc.day_14 + doc.day_15 + \
        doc.day_16 + doc.day_17 + doc.day_18 + doc.day_19 + doc.day_20 + doc.day_21 + doc.day_22 + doc.day_23 + \
        doc.day_24 + doc.day_25 + doc.day_26 + doc.day_27 + \
        doc.day_28 + doc.day_29 + doc.day_30 + doc.day_31
    doc.total_tax = doc.tax_on_workers + \
        doc.tax_on_salary_for_credit + doc.tax_on_salary
    doc.total_salary = doc.total_hours * doc.basic_salary
    doc.total_net_salary = doc.total_salary + doc.total_overtime_amount - \
        doc.total_deductions - doc.total_tax
    doc.total_bank = 0.7 * doc.total_net_salary
    doc.total_cash = 0.3 * doc.total_net_salary
    return doc
