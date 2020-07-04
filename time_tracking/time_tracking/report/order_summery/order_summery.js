// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Order Summery"] = {
	"filters": [
		{
            			"fieldname": "customer",
            			"label": __("Customer"),
            			"fieldtype": "Link",
				"options": "Customer"
        	},
		{
            			"fieldname": "po_no",
            			"label": __("Customer PO"),
            			"fieldtype": "Data"
        	}
	]
};
