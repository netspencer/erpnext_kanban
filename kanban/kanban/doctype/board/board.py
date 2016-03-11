# -*- coding: utf-8 -*-
# Copyright (c) 2015, Alec Ruiz-Ramon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Board(Document):
	pass


def get_columns(self):
	filters = {"parent": self.name}
	return frappe.client.get_list("Board Column", fields=fields,
	                              filters=filters, limit_page_length=None)

def get_docs_in_column(self, board_column):
	column_info = frappe.client.get("Board Column", name=board_column)
	dt = column_info['dt']
	return dt
	# status = column_info['doc_status']
	# fields = [board_column['title_field']].append(board_column['card_fields'])
	# filters = {"status": status}
	# docs = frappe.client.get_list(dt, fields=fields, filters=filters)
