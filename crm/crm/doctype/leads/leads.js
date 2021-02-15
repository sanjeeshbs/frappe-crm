// Copyright (c) 2021, Sanjeesh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leads', {
	// refresh: function(frm) {

	// }

	customer: function(frm){
		if(frm.doc.customer){
			frappe.call({
				method: "crm.crm.doctype.leads.leads.get_customer_details",
				args: {
					customer: frm.doc.customer
				},
				callback: function(r){
					frm.set_value({
						company: r.message.company,
						contact_person: r.message.name1,
						mobile_number: r.message.mobile,
	
					})
				}
	
			})
		}else{
			frm.set_value({
				company: '',
				contact_person:'',
				mobile_number: '',

			})
		}
			
		

	}
});
