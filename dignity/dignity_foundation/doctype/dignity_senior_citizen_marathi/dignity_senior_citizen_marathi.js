// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dignity Senior Citizen Marathi', {
	refresh: function(frm) {
	}
});

frappe.ui.form.on("Dignity Senior Citizen Marathi", {
	tahsildar_centre: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen_marathi.dignity_senior_citizen_marathi.get_card_series_marathi",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "new_series_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "card_number", r.message[1]);
				}
			});
		}
 	},
	tahsildar_city: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen_marathi.dignity_senior_citizen_marathi.get_card_series_marathi",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "new_series_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "card_number", r.message[1]);
				}
			});
		}
 	},
	tahsildar_state: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.tahsildar_centre)
		{			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen_marathi.dignity_senior_citizen_marathi.get_card_series_marathi",
				args: {
					state: frm.doc.tahsildar_state,
					city: frm.doc.tahsildar_city,
					centre: frm.doc.tahsildar_centre
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "new_series_no", r.message[0]);
					frappe.model.set_value(cdt, cdn, "card_number", r.message[1]);
				}
			});
		}
 	},
	card_series_start: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.card_series_start)
		{ 
			var cardnumber = senior_citizen.card_series_start + senior_citizen.new_series_no;
			frappe.model.set_value(cdt,cdn,"card_number",cardnumber);
		}
 	},
	new_series_no: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.new_series_no)
		{ 
			var cardnumber = senior_citizen.card_series_start + senior_citizen.new_series_no;
			frappe.model.set_value(cdt,cdn,"card_number",cardnumber);
		}
 	}
});

frappe.ui.form.on("Dignity Senior Citizen Marathi", {
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

frappe.ui.form.on("Dignity Senior Citizen Marathi", {
	year: function(frm, cdt, cdn) {
		var senior_citizen = frappe.model.get_doc(cdt, cdn);
		if (senior_citizen.year) {
			var today = frappe.datetime.get_today();
			var current_year = today.toString().substring(0,4);
			var years_diff = current_year-senior_citizen.year;
			frappe.model.set_value(cdt,cdn,"age",years_diff);
		} else {
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
 	}
});