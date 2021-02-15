from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Master"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"label": _("Customer"),
					"description": _("Customer"),
                    "onboard": 1,
				}
                
            ]
        },
        {
			"label": _("Transactions"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Leads",
					"label": _("Leads"),
					"description": _("Leads"),
                    "onboard": 1,
				}
                
            ]
        },
        {
			"label": _("Reports"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Leads",
					"label": _("Leads"),
					"description": _("Leads"),
                    "onboard": 1,
				}
                
            ]
        }
    ]
   