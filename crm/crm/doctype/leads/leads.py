# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sanjeesh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Leads(Document):
	pass

@frappe.whitelist()
def get_customer_details(customer):
	customer =  frappe.get_doc("Customer", customer)
	return customer
