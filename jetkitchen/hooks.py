from . import __version__ as app_version

app_name = "jetkitchen"
app_title = "Jet Kitchen"
app_publisher = "Logedosoft Business Solution"
app_description = "Industrial kitchen manufacturing"
app_email = "info@logedosoft.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jetkitchen/css/jetkitchen.css"
# app_include_js = "/assets/jetkitchen/js/jetkitchen.js"

# include js, css files in header of web template
# web_include_css = "/assets/jetkitchen/css/jetkitchen.css"
# web_include_js = "/assets/jetkitchen/js/jetkitchen.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jetkitchen/public/scss/website"

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
#	"methods": "jetkitchen.utils.jinja_methods",
#	"filters": "jetkitchen.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jetkitchen.install.before_install"
# after_install = "jetkitchen.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jetkitchen.uninstall.before_uninstall"
# after_uninstall = "jetkitchen.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jetkitchen.notifications.get_notification_config"

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
override_doctype_class = {
	"Request for Quotation": "jetkitchen.overrides.request_for_quatation.CustomRFQ"
}

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
#		"jetkitchen.tasks.all"
#	],
#	"daily": [
#		"jetkitchen.tasks.daily"
#	],
#	"hourly": [
#		"jetkitchen.tasks.hourly"
#	],
#	"weekly": [
#		"jetkitchen.tasks.weekly"
#	],
#	"monthly": [
#		"jetkitchen.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "jetkitchen.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "jetkitchen.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "jetkitchen.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


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
#	"jetkitchen.auth.validate"
# ]
