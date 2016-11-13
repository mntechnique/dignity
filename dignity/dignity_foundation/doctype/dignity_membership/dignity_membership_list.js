frappe.listview_settings['Dignity Membership'] = {
	onload: function(listview) {
		listview.page.add_menu_item(__("Print Bulk"), function() {
			names=[];
			$.each(listview.get_checked_items(), function(key, value){
				names.push(value._name);
			});
			//console.log(names);
			//console.log(listview.get_checked_items());
			//console.log(listview.get_checked_items())
			var w = window.open("/api/method/dignity.api.bulk_print_memberships?"
							+"names="+encodeURIComponent(names));
	
			if(!w) {
				frappe.msgprint(__("Please enable pop-ups")); return;
			}
		});
	}
};