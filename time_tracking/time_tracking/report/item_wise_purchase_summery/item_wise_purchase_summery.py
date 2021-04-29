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
        return [_("Supplier") + ":Data:180",
		_("Item Code") + ":Data:120",
		_("Item Name") + ":Data:200",
		_("Average Rate") + ":Currency:140",
		_("Average Discount") + ":Percent:140"]

def get_data(conditions,filters):
	oem = frappe.db.sql("""select
			so.supplier_name,
			soi.item_code,
			soi.item_name,
			avg(soi.rate),
			avg(soi.discount_percentage)
			from `tabPurchase Order` so,
			`tabPurchase Order Item` soi where so.docstatus = 1 
			and so.name = soi.parent 
			%s group by soi.item_code, so.supplier;"""%conditions, filters, as_list=1)

	return oem

def get_conditions(filters):
	conditions = ""
	if filters.get("supplier"):
		conditions += " and so.supplier = %(supplier)s"
	if filters.get("item_code"):
		conditions += " and soi.item_code = %(item_code)s"
	return conditions, filters
