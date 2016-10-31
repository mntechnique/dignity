// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dignity Print Member', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Dignity Print Member', {
	member_id1: function(frm, cdt, cdn) {
		var print_member = frappe.model.get_doc(cdt, cdn);
		if (print_member.member_id1) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_print_member.dignity_print_member.get_member_datails",
				args: {
					membership_no: member_id1
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, ("member_name1"), r.message[0]);
					frappe.model.set_value(cdt, cdn, ("member_ship_option1"), r.message[1]);
					frappe.model.set_value(cdt, cdn, ("validity_1"), r.message[2]);
				}
			});

		} 
 	}
});