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
