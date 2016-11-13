frappe.listview_settings['Dignity Senior Citizen'] = {
	onload: function(listview) {
		listview.page.add_menu_item(__("Print Bulk"), function() {
			names=[];
			$.each(listview.get_checked_items(), function(key, value){
				names.push(value._name);
			});
			var w = window.open("/api/method/dignity.api.bulk_print_memberships?"
							+"names="+encodeURIComponent(names));
	
			if(!w) {
				frappe.msgprint(__("Please enable pop-ups")); return;
			}
		});
	}
};