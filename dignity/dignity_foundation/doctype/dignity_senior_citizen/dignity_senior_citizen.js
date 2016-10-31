// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dignity Senior Citizen', {
	refresh: function(frm) {
	}
});

/*frappe.ui.form.on("Dignity Senior Citizen", {
	date_of_birth: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.date_of_birth) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_age",
				args: {
					docname: frm.doc.name
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "age", r.message);
				}
			});

		} 
 	}
});*/

frappe.ui.form.on("Dignity Senior Citizen", {
	date_of_birth: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.date_of_birth) {
			var today = frappe.datetime.get_today();
			var days_diff = frappe.datetime.get_day_diff(today,senior_citizen.date_of_birth);
			age = Math.round(days_diff/365);
			frappe.model.set_value(cdt,cdn,"age",age)
		} 
 	}
});