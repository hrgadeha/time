# Copyright (c) 2013, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
        conditions, filters = get_conditions(filters)
        columns = get_column()
        data = get_data(conditions,filters)
        return columns,data

def get_column():
        return [_("Customer") + ":Data:180",
		_("Item Code") + ":Data:120",
		_("Item Name") + ":Data:200",
		_("Customer Code") + ":Data:120",
		_("Average Rate") + ":Currency:140",
		_("Average Discount") + ":Percent:140"]

def get_data(conditions,filters):
	oem = frappe.db.sql("""select
				so.customer_name,
				soi.item_code,
				soi.item_name,
				soi.customer_item_code,
				avg(soi.rate),
				avg(soi.discount_percentage)
				from `tabSales Order` so,
				`tabSales Order Item` soi 
			where so.docstatus = 1 and so.name = soi.parent %s
			group by soi.item_code, so.customer;"""%conditions, filters, as_list=1)

	return oem

def get_conditions(filters):
	conditions = ""
	if filters.get("customer"):
		conditions += " and so.customer = %(customer)s"

	if filters.get("item_code"):
		conditions += " and soi.item_code = %(item_code)s"

	return conditions, filters
