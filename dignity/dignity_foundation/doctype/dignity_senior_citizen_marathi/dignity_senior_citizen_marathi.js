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
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_card_series",
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
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_card_series",
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
				method: "dignity.dignity_foundation.doctype.dignity_senior_citizen.dignity_senior_citizen.get_card_series",
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