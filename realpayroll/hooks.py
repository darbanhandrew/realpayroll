from . import __version__ as app_version
#import frappe
app_name = "realpayroll"
app_title = "Real Agro Pay Roll System"
app_publisher = "Mohammad Darban Baran"
app_description = "Real Agro payroll system customized"
app_email = "darbanhandrew@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/realpayroll/css/realpayroll.css"
# app_include_js = "/assets/realpayroll/js/realpayroll.js"

# include js, css files in header of web template
# web_include_css = "/assets/realpayroll/css/realpayroll.css"
# web_include_js = "/assets/realpayroll/js/realpayroll.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "realpayroll/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "realpayroll.utils.jinja_methods",
#	"filters": "realpayroll.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "realpayroll.install.before_install"
# after_install = "realpayroll.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "realpayroll.uninstall.before_uninstall"
# after_uninstall = "realpayroll.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "realpayroll.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"realpayroll.tasks.all"
#	],
#	"daily": [
#		"realpayroll.tasks.daily"
#	],
#	"hourly": [
#		"realpayroll.tasks.hourly"
#	],
#	"weekly": [
#		"realpayroll.tasks.weekly"
#	],
#	"monthly": [
#		"realpayroll.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "realpayroll.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "realpayroll.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "realpayroll.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"realpayroll.auth.validate"
# ]


# create record in Employee Payroll Doctype for all the employees of a company after Company Payroll is created
doc_events = {
    "Company Payroll": {
        "after_insert": "realpayroll.crud_events.after_insert_company_payroll"
    },
    "Employee Payroll": {
        "before_save": "realpayroll.crud_events.before_save_employee_payroll"
    }
}
# after app install hooks
# after_install = "realpayroll.setup.after_install"
# load custom doctypes
# fixtures = [""]
