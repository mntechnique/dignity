# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DignityPrintMember(Document):
	def validate(self):
		if not self.member_id1:
			self.member_name1 = ""
			self.member_ship_option1 = ""
			self.validity_1 = ""
		if not self.member_id2:
			self.member_name2 = ""
			self.member_ship_option2 = ""
			self.validity_2 = ""
		if not self.member_id3:
			self.member_name3 = ""
			self.member_ship_option3 = ""
			self.validity_3 = ""
		if not self.member_id4:
			self.member_name4 = ""
			self.member_ship_option4 = ""
			self.validity_4 = ""

@frappe.whitelist()
def get_member_details(membership_no):
	membership = frappe.get_doc("Dignity Membership",membership_no)
	return	membership.member_name,membership.membership_option,membership.membership_validity