import frappe
import json
from frappe.utils.pdf import get_pdf

@frappe.whitelist()
def bulk_print_memberships(names):
	if not frappe.has_permission("Dignity Senior Citizen", "write"):
		frappe.throw(_("Not permitted"), frappe.PermissionError)

	if len(names) == 0:
		frappe.throw("No rows selected.")

	names = names.split(",")

	html = ""

	for name in names:

		#dm = frappe.get_doc("Dignity Membership", name)
		sc_fn = frappe.db.get_value("Dignity Senior Citizen", name, "first_name")
		sc_ln = frappe.db.get_value("Dignity Senior Citizen", name, "surname")

		dm = { "sc_name": sc_fn + ' ' + sc_ln if sc_ln else sc_fn }
		html += frappe.render_template("dignity/templates/includes/dignity_senior_citizen_bulk_print.html", dm)

	pdf_options = { 
					"page-height" : "4.0in",
					"page-width" : "4.0in",
				    "margin-top": "0.75in",
				    "margin-right": "0.75in",
				    "margin-bottom": "0.75in",
				    "margin-left": "0.75in",
				    "encoding": "UTF-8",
				    "no-outline": None,
					"title": "Senior Citizen List" }

	frappe.local.response.filename = "{filename}.pdf".format(filename="senior_citizen_list".replace(" ", "-").replace("/", "-"))	
	frappe.local.response.filecontent = get_pdf(html, pdf_options)
	frappe.local.response.type = "download"
	