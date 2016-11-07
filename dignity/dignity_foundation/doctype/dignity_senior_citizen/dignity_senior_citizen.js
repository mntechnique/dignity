// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dignity Senior Citizen', {
	refresh: function(frm) {
	}
});

frappe.ui.form.on("Dignity Senior Citizen", {
	tahsildar_centre: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_tahsildar",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "tahsildar_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "naming_series", r.message[1]);
				}
			});
		}
 	},
	tahsildar_city: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_tahsildar",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "tahsildar_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "naming_series", r.message[1]);
				}
			});
		}
 	},
	tahsildar_state: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_tahsildar",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "tahsildar_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "naming_series", r.message[1]);
				}
			});
		}
 	}
});

frappe.ui.form.on("Dignity Senior Citizen", {
	date_of_birth: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.date_of_birth) {
			var today = frappe.datetime.get_today();
			var date_of_birth = senior_citizen.date_of_birth;
			year = senior_citizen.date_of_birth.toString().substring(0,4);
			var days_diff = frappe.datetime.get_day_diff(today,senior_citizen.date_of_birth);
			age = Math.round(days_diff/365);
			frappe.model.set_value(cdt,cdn,"age",age);
			frappe.model.set_value(cdt,cdn,"year",year);
		} 
 	}
});

frappe.ui.form.on("Dignity Senior Citizen", {
	year: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.year) {
			var today = frappe.datetime.get_today();
			var current_year = today.toString().substring(0,4);
			var years_diff = current_year-senior_citizen.year;
			frappe.model.set_value(cdt,cdn,"age",years_diff);
		} 
 	}
});