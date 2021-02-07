// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Wise Purchase Summery"] = {
	"filters": [
		{
            			"fieldname": "supplier",
            			"label": __("Supplier"),
            			"fieldtype": "Link",
				"options": "Supplier"
        	}
	]
};
