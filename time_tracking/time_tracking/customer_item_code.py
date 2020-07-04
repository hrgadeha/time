from __future__ import unicode_literals
import frappe, erpnext
import frappe.defaults
from frappe.utils import cint, flt, fmt_money
from frappe import _, msgprint, throw

@frappe.whitelist()
def getCustomerItemCode(item,customer):
	customer_item_code = frappe.db.sql("select icd.ref_code from `tabItem Customer Detail` icd where icd.parent = '{0}' and icd.customer_name = '{1}';".format(item,customer),as_dict = True)
	code = customer_item_code[0]
	return code
