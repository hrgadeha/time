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
		_("Item Code") + ":Link/Item:200",
		_("Average Rate") + ":Currency:180",
		_("Average Discount") + ":Percent:180",
		_("Order Qty") + ":Float:150",
		_("Received Qty") + ":Float:150",
		_("In Transit Qty") + ":Float:150"]

def get_data(conditions,filters):
	oem = frappe.db.sql("""select so.supplier_name,soi.item_code,
			avg(soi.rate),avg(soi.discount_percentage),sum(soi.qty),sum(soi.received_qty),(sum(soi.qty) - sum(soi.received_qty)) 
			from `tabPurchase Order` so,
			`tabPurchase Order Item` soi where so.docstatus = 1 and so.name = soi.parent %s 
			group by soi.item_code;"""%conditions, filters, as_list=1)

	return oem

def get_conditions(filters):
	conditions = ""
	if filters.get("supplier"):
		conditions += " and so.supplier = %(supplier)s"

	return conditions, filters
