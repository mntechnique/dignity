import frappe
import json
from frappe.utils.pdf import get_pdf

@frappe.whitelist()
def bulk_print_memberships(names):
	if not frappe.has_permission("Dignity Membership", "write"):
		frappe.throw(_("Not permitted"), frappe.PermissionError)

	if len(names) == 0:
		frappe.throw("No rows selected.")

	names = names.split(",")

	html = ""

	for name in names:

		#dm = frappe.get_doc("Dignity Membership", name)
		dm = { "member_name": frappe.db.get_value("Dignity Membership", name, "member_name") }
		html += frappe.render_template("dignity/templates/includes/dignity_membership_bulk_print.html", dm)

	pdf_options = { 
					"page-height" : "4.0in",
					"page-width" : "4.0in",
				    "margin-top": "0.75in",
				    "margin-right": "0.75in",
				    "margin-bottom": "0.75in",
				    "margin-left": "0.75in",
				    "encoding": "UTF-8",
				    "no-outline": None,
					"title": "Dignity Memberships" }

	frappe.local.response.filename = "{filename}.pdf".format(filename="memberships".replace(" ", "-").replace("/", "-"))	
	frappe.local.response.filecontent = get_pdf(html, pdf_options)
	frappe.local.response.type = "download"
	