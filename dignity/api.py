import frappe
import json
from frappe.utils.pdf import get_pdf
import pdfkit	
import os


@frappe.whitelist()
def bulk_print_memberships(names):
	if not frappe.has_permission("Dignity Senior Citizen", "write"):
		frappe.throw(_("Not permitted"), frappe.PermissionError)

	if len(names) == 0:
		frappe.msgprint("No rows selected.")
	
	final_html = prepare_bulk_print_html(names)

	pdf_options = { 
					"page-height" : "25.4cm",
					"page-width" : "17.5cm",
					"margin-top": "0mm",
					"margin-bottom": "0mm",
					"margin-left": "0mm",
					"margin-right": "0mm",
					"no-outline": None,
					"encoding": "UTF-8",
					"title": "Senior Citizen List"
				}
		
	frappe.local.response.filename = "{filename}.pdf".format(filename="senior_citizen_list".replace(" ", "-").replace("/", "-"))
	frappe.local.response.filecontent = dignity_get_pdf(final_html, options=pdf_options) #get_pdf(final_html, pdf_options)
	frappe.local.response.type = "download"
	
def prepare_bulk_print_html(names):
	names = names.split(",")

	if len(names) > 4:
		frappe.throw("The system cannot print more than 4 Senior Citizen records at a time.")

	html = ""
	sc_list = []

	for name in names:
		sc_list.append(frappe.get_doc("Dignity Senior Citizen", name))

	has_sc_with_disease = [sc for sc in sc_list if (sc.allergic_to or sc.disease or sc.medication)]
	html_params = { "sc_list": sc_list, "has_sc_with_disease": has_sc_with_disease }
	final_html = frappe.render_template("dignity/templates/includes/dignity_sc_bulk_print.html", html_params)

	return final_html


@frappe.whitelist()
def bulk_print_memberships_marathi(names):
	if not frappe.has_permission("Dignity Senior Citizen Marathi", "write"):
		frappe.throw(_("Not permitted"), frappe.PermissionError)

	if len(names) == 0:
		frappe.msgprint("No rows selected.")
	
	final_html = prepare_bulk_print_html_marathi(names)

	pdf_options = { 
					"page-height" : "25.4cm",
					"page-width" : "17.5cm",
					"margin-top": "0mm",
					"margin-bottom": "0mm",
					"margin-left": "0mm",
					"margin-right": "0mm",
					"no-outline": None,
					"encoding": "UTF-8",
					"title": "Senior Citizen List"
				}
		
	frappe.local.response.filename = "{filename}.pdf".format(filename="senior_citizen_list".replace(" ", "-").replace("/", "-"))
	frappe.local.response.filecontent = dignity_get_pdf(final_html, options=pdf_options) #get_pdf(final_html, pdf_options)
	frappe.local.response.type = "download"

def prepare_bulk_print_html_marathi(names):
	names = names.split(",")

	if len(names) > 4:
		frappe.throw("The system cannot print more than 4 Senior Citizen records at a time.")

	html = ""
	sc_list = []

	for name in names:
		sc_list.append(frappe.get_doc("Dignity Senior Citizen Marathi", name))

	has_sc_with_disease = [sc for sc in sc_list if (sc.allergic_to or sc.disease or sc.medication)]
	html_params = { "sc_list": sc_list, "has_sc_with_disease": has_sc_with_disease }
	final_html = frappe.render_template("dignity/templates/includes/dignity_sc_bulk_print_marathi.html", html_params)

	
	return final_html


def dignity_get_pdf(html, options=None):
	fname = os.path.join("/tmp", "dignity-sc-list-{0}.pdf".format(frappe.generate_hash()))

	try:
		pdfkit.from_string(html, fname, options=options or {})

		with open(fname, "rb") as fileobj:
			filedata = fileobj.read()

	except IOError, e:
		if ("ContentNotFoundError" in e.message
			or "ContentOperationNotPermittedError" in e.message
			or "UnknownContentError" in e.message
			or "RemoteHostClosedError" in e.message):

			# allow pdfs with missing images if file got created
			if os.path.exists(fname):
				with open(fname, "rb") as fileobj:
					filedata = fileobj.read()

			else:
				frappe.throw(_("PDF generation failed because of broken image links"))
		else:
			raise

	finally:
		cleanup(fname)


	return filedata

def cleanup(fname):
	if os.path.exists(fname):
		os.remove(fname)