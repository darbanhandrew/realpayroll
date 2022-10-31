import frappe


# def after_install():
#     # define a new doctype called Company Payroll which has the following fields:
#     # Company
#     # Payroll Period with Month and Year
#     # Calculation Formula
#     # Tax

#     # The calculation formula is a text field where the user can enter a formula to calculate the salary of the employee. The formula can be a simple addition or subtraction of the basic salary or it can be a complex formula with multiple conditions. For example, the formula can be:
#     #basic_salary + (basic_salary * 0.1) - (basic_salary * 0.05) + (basic_salary * 0.02) - (basic_salary * 0.01)

#     # The tax field is a percentage field where the user can enter the tax percentage for the company. For example, the tax percentage can be 10% or 20% or 30% or 40% or 50%.
#     # The user can create multiple Company Payroll records for the same company and the same payroll period. For example, the user can create a Company Payroll record for the month of January 2019 and the calculation formula can be:
#     #basic_salary + (basic_salary * 0.1) - (basic_salary * 0.05) + (basic_salary * 0.02) - (basic_salary * 0.01)

#     company_doctype = "Company Payroll"
#     company_docfields = [
#         {
#             "fieldname": "company",
#             "fieldtype": "Link",
#             "label": "Company",
#             "options": "Company",
#             "reqd": 1
#         },
#         {
#             "fieldname": "payroll_period",
#             "fieldtype": "Date",
#             "label": "Payroll Period",
#             "reqd": 1
#         },
#         {
#             "fieldname": "calculation_formula",
#             "fieldtype": "Text",
#             "label": "Calculation Formula",
#             "reqd": 1
#         },
#         {
#             "fieldname": "tax",
#             "fieldtype": "Percent",
#             "label": "Tax",
#             "reqd": 1
#         }
#     ]

#     # define a new doctype
#     employee_doctype = "Employee Payrolls"
#     # add a new field
#     employee_docfields = [
#         {
#             "fieldname": "employee",
#             "fieldtype": "Link",
#             "label": "Employee",
#             "options": "Employee",
#             "reqd": 1
#         },
#         # link the employee doctype to the company doctype
#         {
#             "fieldname": "company_payroll",
#             "fieldtype": "Link",
#             "label": "Company Payroll",
#             "options": company_doctype,
#             "reqd": 1
#         },
#         {
#             "fieldname": "month",
#             "fieldtype": "Select",
#             "label": "Month",
#             "options": "January\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember",
#             "reqd": 1
#         },
#         {
#             "fieldname": "year",
#             "fieldtype": "Int",
#             "label": "Year",
#             "reqd": 1
#         },
#         {
#             "fieldname": "basic_salary",
#             "fieldtype": "Currency",
#             "label": "Basic Salary",
#             "reqd": 1
#         },
#         # add a set of fields for all the days in a month (1-31)
#         {
#             "fieldname": "day_1",
#             "fieldtype": "Currency",
#             "label": "Day 1"
#         },
#         {
#             "fieldname": "day_2",
#             "fieldtype": "Currency",
#             "label": "Day 2"
#         },
#         {
#             "fieldname": "day_3",
#             "fieldtype": "Currency",
#             "label": "Day 3"
#         },
#         {
#             "fieldname": "day_4",
#             "fieldtype": "Currency",
#             "label": "Day 4"
#         },
#         {
#             "fieldname": "day_5",
#             "fieldtype": "Currency",
#             "label": "Day 5"
#         },
#         {
#             "fieldname": "day_6",
#             "fieldtype": "Currency",
#             "label": "Day 6"
#         },
#         {
#             "fieldname": "day_7",
#             "fieldtype": "Currency",
#             "label": "Day 7"
#         },
#         {
#             "fieldname": "day_8",
#             "fieldtype": "Currency",
#             "label": "Day 8"
#         },
#         {
#             "fieldname": "day_9",
#             "fieldtype": "Currency",
#             "label": "Day 9"
#         },
#         {
#             "fieldname": "day_10",
#             "fieldtype": "Currency",
#             "label": "Day 10"
#         },
#         {
#             "fieldname": "day_11",
#             "fieldtype": "Currency",
#             "label": "Day 11"
#         },
#         {
#             "fieldname": "day_12",
#             "fieldtype": "Currency",
#             "label": "Day 12"
#         },
#         {
#             "fieldname": "day_13",
#             "fieldtype": "Currency",
#             "label": "Day 13"
#         },
#         {
#             "fieldname": "day_14",
#             "fieldtype": "Currency",
#             "label": "Day 14"
#         },
#         {
#             "fieldname": "day_15",
#             "fieldtype": "Currency",
#             "label": "Day 15"
#         },
#         {
#             "fieldname": "day_16",
#             "fieldtype": "Currency",
#             "label": "Day 16"
#         },
#         {
#             "fieldname": "day_17",
#             "fieldtype": "Currency",
#             "label": "Day 17"
#         },
#         {
#             "fieldname": "day_18",
#             "fieldtype": "Currency",
#             "label": "Day 18"
#         },
#         {
#             "fieldname": "day_19",
#             "fieldtype": "Currency",
#             "label": "Day 19"
#         },
#         {
#             "fieldname": "day_20",
#             "fieldtype": "Currency",
#             "label": "Day 20"
#         },
#         {
#             "fieldname": "day_21",
#             "fieldtype": "Currency",
#             "label": "Day 21"
#         },
#         {
#             "fieldname": "day_22",
#             "fieldtype": "Currency",
#             "label": "Day 22"
#         },
#         {
#             "fieldname": "day_23",
#             "fieldtype": "Currency",
#             "label": "Day 23"
#         },
#         {
#             "fieldname": "day_24",
#             "fieldtype": "Currency",
#             "label": "Day 24"
#         },
#         {
#             "fieldname": "day_25",
#             "fieldtype": "Currency",
#             "label": "Day 25"
#         },
#         {
#             "fieldname": "day_26",
#             "fieldtype": "Currency",
#             "label": "Day 26"
#         },
#         {
#             "fieldname": "day_27",
#             "fieldtype": "Currency",
#             "label": "Day 27"
#         },
#         {
#             "fieldname": "day_28",
#             "fieldtype": "Currency",
#             "label": "Day 28"
#         },
#         {
#             "fieldname": "day_29",
#             "fieldtype": "Currency",
#             "label": "Day 29"
#         },
#         {
#             "fieldname": "day_30",
#             "fieldtype": "Currency",
#             "label": "Day 30"
#         },
#         {
#             "fieldname": "day_31",
#             "fieldtype": "Currency",
#             "label": "Day 31"
#         },
#         {
#             "fieldname": "total_days",
#             "fieldtype": "Int",
#             "label": "Total Days"
#         },
#         {
#             "fieldname": "total_salary",
#             "fieldtype": "Currency",
#             "label": "Total Salary"
#         },
#         {
#             "fieldname": "total_hours",
#             "fieldtype": "Int",
#             "label": "Total Hours"
#         },
#         {
#             "fieldname": "total_overtime",
#             "fieldtype": "Int",
#             "label": "Total Overtime"
#         },
#         {
#             "fieldname": "total_overtime_amount",
#             "fieldtype": "Currency",
#             "label": "Total Overtime Amount"
#         },
#         {
#             "fieldname": "total_deductions",
#             "fieldtype": "Currency",
#             "label": "Total Deductions"
#         },
#         {
#             "fieldname": "total_tax",
#             "fieldtype": "Currency",
#             "label": "Total Tax"
#         },
#         {
#             "fieldname": "total_net_salary",
#             "fieldtype": "Currency",
#             "label": "Total Net Salary"
#         },
#         {
#             "fieldname": "total_cash",
#             "fieldtype": "Currency",
#             "label": "Total Cash"
#         },
#         {
#             "fieldname": "total_bank",
#             "fieldtype": "Currency",
#             "label": "Total Bank"
#         },

#     ]
#     # register the custom doctypes
#     # check if the doctype exists
#     if not frappe.db.exists("DocType", company_doctype) and not frappe.db.exists("DocType", employee_doctype):
#         frappe.get_doc({
#             "doctype": "DocType",
#             "module": "Real Agro Pay Roll System",
#             "fields": company_docfields,
#             "name": company_doctype,
#             #give permission to all

#         }).insert()

#         frappe.get_doc({
#             "doctype": "DocType",
#             "module": "Real Agro Pay Roll System",
#             "fields": employee_docfields,
#             "name": employee_doctype,
#         }).insert()
