import frappe
import json
from frappe.utils.pdf import get_pdf
import ast
# @frappe.whitelist()
# def render_pdf(doctype, name, format=None):
# 	# name can include names of many docs of the same doctype.
# 	totalhtml = ""
# 	# Pagebreak to be added between each doc html
# 	pagebreak = """<p style="page-break-after:always;"></p>"""

# 	options = {}

# 	import json
# 	result = json.loads(name)
# 	# Get html of each doc and combine including page breaks
# 	for i, ss in enumerate(result):
# 		html = frappe.get_print(doctype, ss, format)
# 		if i == len(result)-1:
# 			totalhtml = totalhtml + html
# 		else:
# 			totalhtml = totalhtml + html + pagebreak

# 	frappe.local.response.filename = "{doctype}.pdf".format(doctype=doctype.replace(" ", "-").replace("/", "-"))

# 	# Title of pdf
# 	options.update({
# 		'title': doctype,
# 	})

# 	frappe.local.response.filecontent = get_pdf(totalhtml, options)
# 	frappe.local.response.type = "download"


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

	pdf_options = { "page-size" : "A5", "title": "Dignity Memberships" }

	frappe.local.response.filename = "{filename}.pdf".format(filename="memberships".replace(" ", "-").replace("/", "-"))	
	frappe.local.response.filecontent = get_pdf(html, pdf_options)
	frappe.local.response.type = "download"
	