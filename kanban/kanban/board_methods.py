import frappe
import json


@frappe.whitelist()
def get_columns(doc):
    doc = json.loads(doc)
    columns = [column for column in doc['board_column']]
    return_data = {}
    for column in columns:
        return_data[column['column_title']] = get_docs_in_column(column)
    return return_data


def get_docs_in_column(board_column):
    column_info = frappe.client.get("Board Column", board_column['name'])
    dt = column_info['dt']
    filters = {
        column_info['field_name']: column_info['field_option']
        }
    docs = frappe.client.get_list(dt, filters=filters, limit_page_length=None)
    return docs


@frappe.whitelist()
def get_fields(doc):
    doc = json.loads(doc)
    meta = frappe.desk.form.meta.get_meta(doc['dt'])
    fields = [field for field in meta.fields]
    field_names = [name.label for name in fields]
    return field_names


@frappe.whitelist()
def get_field_options(doc, chosen_field):
    doc = json.loads(doc)
    meta = frappe.desk.form.meta.get_meta(doc['dt'])
    fields = [field for field in meta.fields]
    options = [field.options for field in fields if field.label == chosen_field][0]
    return options
