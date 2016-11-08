# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.utils
from frappe.utils import flt, cstr
from frappe.model.document import Document

class DignitySeniorCitizen(Document):
	def validate(self):
		if self.age < 60 or not self.age:
			frappe.throw(_("Age should be more than 60 for Senior Citizen"))
		if not self.tahsildar_state or not self.tahsildar_city or not self.tahsildar_centre:
			frappe.throw(_("State, City and Card Center are mandatory fields"))
		if not self.tahsildar_state or not self.tahsildar_city or not self.tahsildar_name:
				frappe.throw(_("State, City and Tahsildar Name are mandatory fields"))
		#Check Card Center Combination
		if self.tahsildar_state and self.tahsildar_city and self.tahsildar_centre:
			card = frappe.db.sql("""select naming_series,card_series_from, card_series_to,card_last_series from `tabDignity Card Series Master` where parent = %s and tahsildar_city = %s and card_centre = %s""",(self.tahsildar_state,self.tahsildar_city,self.tahsildar_centre))
			if card:
				naming_series = card[0][0]
				card_series_from = card[0][1]
				card_series_to = card[0][2]
				card_last_series_no = card[0][3]
			else:
				frappe.throw(_("Number series is not set up for State, City and Centre combination."))
		#Check Tahsildar Combination
		if self.tahsildar_state and self.tahsildar_city and self.tahsildar_name:
			tahsildar = frappe.db.sql("""select tahsildar_series_from,tahsildar_last_series from `tabDignity Tahsildar Master` where parent = %s and tahsildar_city = %s and tahsildar_centre = %s""",(self.tahsildar_state,self.tahsildar_city,self.tahsildar_name))
			if tahsildar:
				tahsildar_series_from = tahsildar[0][0]
				tahsildar_last_series = tahsildar[0][1]
			else:
				frappe.throw(_("Number series is not set up for State, City and Tahsildar Centre combination."))
		# Generate the card Number, validate range and Insert
			new_series_no = card_last_series_no + 1
			new_tahsildar_no = tahsildar_last_series + 1
		if new_series_no > card_series_to:
			frappe.throw(_("You have used all existing series numbers in the setup. Please update series number in Master Set Up accordingly"))
		str_len_new_series_no = len(cstr(new_series_no))
		str_new_series_no = cstr(new_series_no)
		#new tahsildar series no
		str_len_new_tahsildar_series_no = len(cstr(new_tahsildar_no))
		str_new_tahsildar_series_no = cstr(new_tahsildar_no)
		#zero padding center series
		if str_len_new_series_no < 5:
			no_of_leading_zeroes = 5 - str_len_new_series_no
			str_new_series_no.ljust(no_of_leading_zeroes,"0")
		#zero padding tahsildar series
		if str_len_new_tahsildar_series_no < 5:
			no_of_leading_zeroes = 5 - str_len_new_tahsildar_series_no
			str_new_tahsildar_series_no.ljust(no_of_leading_zeroes,"0")
		#new card number
		new_card_no = naming_series + str_new_series_no
		self.new_series_no = new_series_no
		self.card_number = new_card_no
		#new tahsildar number
		self.tahsildar_no = str_new_tahsildar_series_no
		#check if card number already exists to avoid data duplication
		card_check = frappe.db.sql("""select 'X' from `tabDignity Senior Citizen` where card_number = %s""",self.card_number)
		#check if tahsildar series number already exists to avoid data duplication
		tahsildar_check = frappe.db.sql("""select 'X' from `tabDignity Senior Citizen` where tahsildar_no = %s""",self.tahsildar_no)
		if card_check:
			frappe.throw(_("Senior Citizen Card No already exists"))
		if tahsildar_check:
			frappe.throw(_("Tahsildar No already exists"))
		if self.tahsildar_state and self.tahsildar_city and self.tahsildar_centre:
			frappe.db.sql("""update `tabDignity Card Series Master` set card_last_series = %s where parent = %s and tahsildar_city = %s and card_centre = %s""",(self.new_series_no,self.tahsildar_state,self.tahsildar_city,self.tahsildar_centre))
		if self.tahsildar_state and self.tahsildar_city and self.tahsildar_name:
			frappe.db.sql("""update `tabDignity Tahsildar Master` set tahsildar_last_series = %s where parent = %s and tahsildar_city = %s and tahsildar_centre = %s""",(self.tahsildar_no,self.tahsildar_state,self.tahsildar_city,self.tahsildar_name))

@frappe.whitelist()
def get_tahsildar(state,city,centre):
	conditions=""
	if state and city and centre:
		filters = {}
		filters["state"]= state
		filters["city"] = city
		filters["centre"] = centre
		if state:
			conditions += " and parent = %(state)s"
		if city:
			conditions += " and tahsildar_city = %(city)s"
		if centre:
			conditions += " and card_centre = %(centre)s"
		card = frappe.db.sql("""select naming_series from `tabDignity Card Series Master` where 1=1 %s""" % (conditions,),filters)
	return (card[0][0]) if card else ("MU")