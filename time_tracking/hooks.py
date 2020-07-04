# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "time_tracking"
app_title = "Time Tracking"
app_publisher = "Hardik Gadesha"
app_description = "App to Track Time of delivery"
app_icon = "octicon octicon-file-directory"
app_color = "#e6b800"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/time_tracking/css/time_tracking.css"
# app_include_js = "/assets/time_tracking/js/time_tracking.js"

# include js, css files in header of web template
# web_include_css = "/assets/time_tracking/css/time_tracking.css"
# web_include_js = "/assets/time_tracking/js/time_tracking.js"

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

# Website user home page (by function)
# get_website_user_home_page = "time_tracking.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "time_tracking.install.before_install"
# after_install = "time_tracking.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "time_tracking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"time_tracking.tasks.all"
# 	],
# 	"daily": [
# 		"time_tracking.tasks.daily"
# 	],
# 	"hourly": [
# 		"time_tracking.tasks.hourly"
# 	],
# 	"weekly": [
# 		"time_tracking.tasks.weekly"
# 	]
# 	"monthly": [
# 		"time_tracking.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "time_tracking.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "time_tracking.event.get_events"
# }

