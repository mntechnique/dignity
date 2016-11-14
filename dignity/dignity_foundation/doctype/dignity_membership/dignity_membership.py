# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate
from frappe.model.document import Document

class DignityMembership(Document):
	def validate(self):
		if getdate(self.membership_date) > getdate(self.membership_validity):
			frappe.throw(_("Membership Date cannot be greater than membership expiry date"))
		tahsildar = frappe.db.sql("""select name from `tabDignity Membership` where membership_no = %s and membership_validity = %s""",(self.membership_no,self.membership_validity))
		if tahsildar:
			cur_doc_name = tahsildar[0][0]
			if cur_doc_name: 
				if cur_doc_name == self.name:
					pass
				else:
					frappe.throw(_("Membership ID already exists with same expiry date. Please change expiry date of renewal accordingly."))