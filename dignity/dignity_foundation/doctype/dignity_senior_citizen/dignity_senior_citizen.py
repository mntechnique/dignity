# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.utils
from frappe.model.document import Document

class DignitySeniorCitizen(Document):
	def validate(self):
		if self.age < 60 or not self.age:
			frappe.throw(_("Age should be more than 60 for Senior Citizen"))


@frappe.whitelist()
def get_tahsildar(state,city,centre):
	conditions=""
	if state and city and centre:
		filters = {}
		filters["state"]= state
		filters["city"] = city
		filters["centre"] = centre
		print filters
		if state:
			conditions += " and parent = %(state)s"
		if city:
			conditions += " and tahsildar_city = %(city)s"
		if centre:
			conditions += " and tahsildar_centre = %(centre)s"
		tahsildar = frappe.db.sql("""select tahsildar_no,tahsildar_series from `tabDignity Tahsildar Master` where 1=1 %s""" % (conditions,),filters)
	return tahsildar[0][0],tahsildar[0][1]