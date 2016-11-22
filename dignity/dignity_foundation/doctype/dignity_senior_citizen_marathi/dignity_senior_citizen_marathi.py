# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.utils
from frappe.utils import flt, cstr
from frappe.model.document import Document

class DignitySeniorCitizenMarathi(Document):
	def validate(self):
		if not self.tahsildar_state or not self.tahsildar_city or not self.tahsildar_centre:
			frappe.throw(_("State, City and Card Center are mandatory fields"))
		if self.tahsildar_state and self.tahsildar_city and self.tahsildar_centre:
			card = frappe.db.sql("""select naming_series,card_series_from, card_series_to,card_last_series from `tabDignity Card Series Master` where parent = %s and tahsildar_city = %s and card_centre = %s""",(self.tahsildar_state,self.tahsildar_city,self.tahsildar_centre))
			if card:
				naming_series = card[0][0]
				card_series_from = card[0][1]
				card_series_to = card[0][2]
				card_last_series_no = card[0][3]
			if (self.new_series_no < card_series_from) or (self.new_series_no > card_series_to):
				frappe.throw(_("Card No should be between card series from and card series to set up in master"))

		def gen_update_card_series(state,city,centre,card_number):
			#Check if card number already exists
			if card_number:
				#check if card number already exists to avoid data duplication
				card_check = frappe.db.sql("""select name from `tabDignity Senior Citizen` where card_number = %s""",card_number)
				if card_check:
					name = card_check[0][0]
					if self.name == name:
						pass
					else:
						frappe.throw(_("Card Number already in use"))
				else:
					card = frappe.db.sql("""select card_last_series from `tabDignity Card Series Master` where parent = %s and tahsildar_city = %s and card_centre = %s""",(state,city,centre))
					if card:
						card_last_series_no = card[0][0]
						if self.new_series_no < card_last_series_no:
							pass
						else:
							frappe.db.sql("""update `tabDignity Card Series Master` set card_last_series = %s where parent = %s and tahsildar_city = %s and card_centre = %s""",(self.new_series_no,state,city,centre))
					else:
						#Check Card Center Combination
						card = frappe.db.sql("""select naming_series,card_series_from, card_series_to,card_last_series from `tabDignity Card Series Master` where parent = %s and tahsildar_city = %s and card_centre = %s""",(state,city,centre))
						if card:
							naming_series = card[0][0]
							card_series_from = card[0][1]
							card_series_to = card[0][2]
							card_last_series_no = card[0][3]
							# Generate the card Number, validate range and Insert
							new_series_no = card_last_series_no + 1
							if new_series_no > card_series_to:
								frappe.throw(_("You have used all existing series numbers in the setup. Please update series number in Master Set Up accordingly"))
							else:
								str_len_new_series_no = len(cstr(new_series_no))
								str_new_series_no = cstr(new_series_no)
								#zero padding center series
								if str_len_new_series_no < 5:
									no_of_leading_zeroes = 5 - str_len_new_series_no
									str_new_series_no.ljust(no_of_leading_zeroes,"0")
									#new card number
									new_card_no = naming_series + str_new_series_no
									self.new_series_no = new_series_no
									self.card_number = new_card_no
									frappe.db.sql("""update `tabDignity Card Series Master` set card_last_series = %s where parent = %s and tahsildar_city = %s and card_centre = %s""",(self.new_series_no,state,city,centre))
						else:
							frappe.throw(_("Number series is not set up for State, City and Centre combination."))
		gen_update_card_series(self.tahsildar_state,self.tahsildar_city,self.tahsildar_centre,self.card_number)
