// Copyright (c) 2016, Alec Ruiz-Ramon and contributors
// For license information, please see license.txt

frappe.ui.form.on("Board", "onload", function(doc, cdt, cdn){ //onload for testing
	var doc = locals[cdt][cdn]
	frappe.call({
		method: "kanban.kanban.board_methods.get_columns",
		args: {
			"doc" : doc
		},
   	callback: function(r){
		  console.log(r.message) // log for now, since in testing
	  }
  })
});

frappe.ui.form.on("Board Column", "dt", function(doc, cdt, cdn){
	var doc = locals[cdt][cdn]
	frappe.call({
		method: "kanban.kanban.board_methods.get_fields",
		args: {
			"doc": doc
		},
		callback: function(r){
			var chosen_field = frappe.prompt(
				{label: "Field Name", fieldtype: "Select", options: r.message},
				function(data) {
				  console.log(data.field_name)
			    doc.field_name = data.field_name;
					cur_frm.refresh();
					frappe.call({
						method: "kanban.kanban.board_methods.get_field_options",
						args: {
							"doc": doc,
							"chosen_field": doc.field_name
						},
						callback: function(r){
							console.log(r.message)
							var chosen_option = frappe.prompt(
								{label: "Field Option", fieldtype: "Select",
								options: r.message},
								function(data) {
									console.log(data.field_option);
									doc.field_option = data.field_option;
									cur_frm.refresh();
								})
						}
				})
			});
		}
	})
});
