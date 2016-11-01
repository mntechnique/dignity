// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dignity Print Member', {
	refresh: function(frm, cdt, cdn) {
	}
});

frappe.ui.form.on("Dignity Print Member", {
	member_id1: function(frm, cdt, cdn) {
		var print_member = frappe.model.get_doc(cdt, cdn);
		if (print_member.member_id1) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_print_member.dignity_print_member.get_member_details",
				args: {
					membership_no: print_member.member_id1
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

frappe.ui.form.on("Dignity Print Member", {
	member_id2: function(frm, cdt, cdn) {
		var print_member = frappe.model.get_doc(cdt, cdn);
		if (print_member.member_id2) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_print_member.dignity_print_member.get_member_details",
				args: {
					membership_no: print_member.member_id2
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, ("member_name2"), r.message[0]);
					frappe.model.set_value(cdt, cdn, ("member_ship_option2"), r.message[1]);
					frappe.model.set_value(cdt, cdn, ("validity_2"), r.message[2]);
				}
			});

		} 
 	}
});

frappe.ui.form.on("Dignity Print Member", {
	member_id3: function(frm, cdt, cdn) {
		var print_member = frappe.model.get_doc(cdt, cdn);
		if (print_member.member_id3) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_print_member.dignity_print_member.get_member_details",
				args: {
					membership_no: print_member.member_id3
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, ("member_name3"), r.message[0]);
					frappe.model.set_value(cdt, cdn, ("member_ship_option3"), r.message[1]);
					frappe.model.set_value(cdt, cdn, ("validity_3"), r.message[2]);
				}
			});

		} 
 	}
});

frappe.ui.form.on("Dignity Print Member", {
	member_id4: function(frm, cdt, cdn) {
		var print_member = frappe.model.get_doc(cdt, cdn);
		if (print_member.member_id4) {
			frappe.call({
				method: "dignity.dignity_foundation.doctype.dignity_print_member.dignity_print_member.get_member_details",
				args: {
					membership_no: print_member.member_id4
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, ("member_name4"), r.message[0]);
					frappe.model.set_value(cdt, cdn, ("member_ship_option4"), r.message[1]);
					frappe.model.set_value(cdt, cdn, ("validity_4"), r.message[2]);
				}
			});

		} 
 	}
});