# -*- coding: utf-8 -*-
# LOGEDOSOFT

from __future__ import unicode_literals
import frappe, json
from frappe import msgprint, _
from frappe.utils.user import get_user_fullname

from erpnext.buying.doctype.request_for_quotation.request_for_quotation import RequestforQuotation

STANDARD_USERS = ("Guest", "Administrator")

class CustomRFQ(RequestforQuotation):
	def on_submit(self):
		super().on_submit()

	def send_to_supplier(self):
		"""Sends RFQ mail to involved suppliers."""
		for rfq_supplier in self.suppliers:
			if rfq_supplier.email_id is not None and rfq_supplier.send_email:
				self.validate_email_id(rfq_supplier)

				# make new user if required
				#update_password_link, contact = self.update_supplier_contact(rfq_supplier, self.get_link())
				update_password_link = ""
				contact = ""

				self.update_supplier_part_no(rfq_supplier.supplier)
				self.supplier_rfq_mail(rfq_supplier, update_password_link, self.get_link())
				rfq_supplier.email_sent = 1
				if not rfq_supplier.contact:
					rfq_supplier.contact = contact
				rfq_supplier.save()

	def supplier_rfq_mail(self, data, update_password_link, rfq_link, preview=False):
		full_name = get_user_fullname(frappe.session["user"])
		if full_name == "Guest":
			full_name = "Administrator"

		# send document dict and some important data from suppliers row
		# to render message_for_supplier from any template
		doc_args = self.as_dict()
		doc_args.update({"supplier": data.get("supplier"), "supplier_name": data.get("supplier_name")})

		# Get Contact Full Name
		supplier_name = None
		if data.get("contact"):
			contact_name = frappe.db.get_value(
				"Contact", data.get("contact"), ["first_name", "middle_name", "last_name"]
			)
			supplier_name = (" ").join(x for x in contact_name if x)  # remove any blank values

		args = {
			"update_password_link": update_password_link,
			"message": frappe.render_template(self.message_for_supplier, doc_args),
			"rfq_link": rfq_link,
			"user_fullname": full_name,
			"supplier_name": supplier_name or data.get("supplier_name"),
			"supplier_salutation": self.salutation or "",
		}

		subject = self.subject or _("Request for Quotation")
		template = "templates/emails/ld_request_for_quotation.html"
		sender = frappe.session.user not in STANDARD_USERS and frappe.session.user or None
		message = frappe.get_template(template).render(args)

		if preview:
			return message

		attachments = self.get_attachments()

		self.send_email(data, sender, subject, message, attachments)

	"""def before_save(self):
		frappe.msgprint("TEST OK1")
		print("=============OK============")
		self.my_custom_code()
		#super().on_update()
		frappe.log_error("TEST", "TEST")
		frappe.log_error(_("TEST 3"), _("Jet Kitchen"))

	def on_validate(self):
		frappe.msgprint("TEST OK")
		print("=============OK============")
		self.my_custom_code()
		#super().on_update()
		frappe.log_error("TEST", "TEST")
		frappe.log_error(_("TEST 3"), _("Jet Kitchen"))

	def on_update(self):
		print("=============OK============")
		frappe.msgprint("TEST OK")
		self.my_custom_code()
		#super().on_update()
		frappe.log_error("TEST", "TEST")
		frappe.log_error(_("TEST 3"), _("Jet Kitchen"))

	def my_custom_code(self):
		print("=============OK============")
		frappe.msgprint("TEST OK 2")
		frappe.log_error("TEST2", "TEST2")
		frappe.log_error(_("TEST 3"), _("Jet Kitchen"))"""