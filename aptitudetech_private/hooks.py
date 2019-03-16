# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aptitudetech_private"
app_title = "Aptitudetech Private"
app_publisher = "Aptitudetech"
app_description = "Private app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@aptitudetech.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aptitudetech_private/css/aptitudetech_private.css"
# app_include_js = "/assets/aptitudetech_private/js/aptitudetech_private.js"

# include js, css files in header of web template
# web_include_css = "/assets/aptitudetech_private/css/aptitudetech_private.css"
# web_include_js = "/assets/aptitudetech_private/js/aptitudetech_private.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aptitudetech_private.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aptitudetech_private.install.before_install"
# after_install = "aptitudetech_private.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aptitudetech_private.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

#permission_query_conditions = {
# 	"Issue": "aptitudetech_private.permissions.get_issue_permissions_query_conditions",
#}

#has_permission = {
#	"Issue": "aptitudetech_private.permissions.has_permission_to_issue",
#}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
#	"Task": {
#		"onload": "aptitudetech_private.events.on_issue_onload"
#	}
	"Issue": {
		"validate" : "aptitudetech_private.events.on_issue_validate"
	}
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"aptitudetech_private.tasks.all"
# 	],
#	"cron": {
 	"18 * * * *": [
 		"aptitudetech_private.tasks.daily"
	]
#	}
#	"cron": {
#	 	"18 * * * *": [
#	 		"aptitudetech_private.tasks.daily"
 #		]
#	}
# 	"daily": [
# 		"aptitudetech_private.tasks.daily"
# 	],
# 	"hourly": [
# 		"aptitudetech_private.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aptitudetech_private.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aptitudetech_private.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "aptitudetech_private.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
#override_whitelisted_methods = {
#	"frappe.desk.doctype.kanban_board.kanban_board.update_doc": "aptitudetech_private.events.kanban_update_doc"
#}

fixtures = [
{
	"dt": "Custom Field",
	"filters": {
        	"name": ["in", [
        	        "Project Task-end_time",
             		"Project Task-start_time",
             		"Issue-column_break_28",
             		"Issue-kanban_status",
             		"Issue-approved_work_end_time",
             		"Issue-approved_work_start_time",
             		"Issue-reported_work_end_time",
             		"Issue-reported_work_start_time",
             		"Issue-captured_end_working_time",
             		"Issue-captured_start_working_time",
             		"Issue-captured_assigned_time",
             		"Issue-captured_incoming_time",
             		"Issue-captured_times",
             		"Issue-active_tickets",
             		"Issue-other_links",
             		"Issue-other_references",
             		"Issue-services_html",
             		"Issue-to_do",
             		"Issue-tickets_links",
             		"Issue-tickets_html",
             		"Task-issue",
             		"Issue-related_project",
             		"Issue-tasks",
             		"Issue-ticket_type",
         	]]
    	}
},
{
	'dt': 'Workflow State',
    	"filters": {
        	"name": ["in", [
        		"Approved",
        	        "To Approve",
             		"Rejected",
         	]]
    	}
},
{
	'dt': 'Workflow Action',
    	"filters": {
        	"name": ["in", [
             		"Approve",
             		"Reject",
         	]]
    	}
},
{
	'dt': 'Workflow',
        "filters": {
    		"name": ["in", [
        	     "Simplified Time Sheet Approval",
         	]]
    	}

},
]
