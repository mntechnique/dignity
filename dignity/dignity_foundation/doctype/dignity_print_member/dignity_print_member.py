# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DignityPrintMember(Document):
	pass

@frappe.whitelist()
def get_member_details(membership_no):
	membership = frappe.get_doc("Dignity Membership",membership_no)
	return	membership.member_name,membership.membership_option,membership.membership_validity