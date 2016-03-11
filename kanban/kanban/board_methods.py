import frappe
import json


@frappe.whitelist()
def get_columns(doc):
    doc = json.loads(doc)
    columns = [column for column in doc['board_column']]
    return columns

def get_docs_in_column(board_column):
	column_info = frappe.client.get("Board Column", name=board_column)
	dt = column_info['dt']
	return dt
	# status = column_info['doc_status']
	# fields = [board_column['title_field']].append(board_column['card_fields'])
	# filters = {"status": status}
	# docs = frappe.client.get_list(dt, fields=fields, filters=filters)


@frappe.whitelist()
def get_fields(doc):
    doc = json.loads(doc)
    meta = frappe.desk.form.meta.get_meta(doc['dt'])
    fields = [field for field in meta.fields]
    field_names = [name.label for name in fields]
    return field_names
#    for item in meta.fields:
#        print item#
#        print item.label
#        for thing in item:
#            print thing

@frappe.whitelist()
def get_field_options(doc, chosen_field):
    doc = json.loads(doc)
    meta = frappe.desk.form.meta.get_meta(doc['dt'])
    fields = [field for field in meta.fields]
    options = [field.options for field in fields if
                  field.label == chosen_field][0]
    return options
