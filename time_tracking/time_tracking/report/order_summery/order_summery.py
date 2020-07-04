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
		_("Sales Order") + ":Link/Sales Order:150",
		_("Order Date") + ":Date:100",
		_("Tentative Date") + ":Date:130",
		_("Customer PO") + ":Data:120",
                _("PO Date") + ":Date:100",
		_("Item Code") + ":Link/Item:200",
		_("Customer Code") + ":Data:200",
		_("Order Qty") + ":Float:150",
		_("Deliverd Qty") + ":Float:150",
		_("Pending Qty") + ":Float:150"]

def get_data(conditions,filters):
	oem = frappe.db.sql("""select so.customer_name,so.name,so.transaction_date,soi.tentative_date,so.po_no,so.po_date,soi.item_code,
			soi.customer_item_code,soi.qty,soi.delivered_qty, (soi.qty - soi.delivered_qty) from `tabSales Order` so, 
			`tabSales Order Item` soi where so.docstatus = 1 and so.name = soi.parent 
			%s;"""%conditions, filters, as_list=1)

	return oem

def get_conditions(filters):
	conditions = ""
	if filters.get("customer"):
		conditions += " and so.customer = %(customer)s"

	if filters.get("po_no"):
		conditions += " and so.po_no = %(po_no)s"

	return conditions, filters

