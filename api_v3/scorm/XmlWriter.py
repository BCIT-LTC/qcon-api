# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import shutil
import datetime
import re
import xml.etree.cElementTree as ET
from uuid import UUID
from .xmlcdata import CDATA
from os import makedirs, path, walk
from os.path import basename
from django.conf import settings
from xml.dom.minidom import parseString
from zipfile import *

class XmlWriter():

	def __init__(self, question_library, json_output) :
		json_output = {"general_header": "General Header","randomize_answer":False,"total_question_errors": "1","total_document_errors": "0","sections": [{"title": "Section title","is_title_displayed":False,"text":None,"is_text_displayed":False,"shuffle":False,"questions": [{"title": "MC title","text": "Question text","point": 3.5,"difficulty": 3,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice": {"randomize":True,"enumeration": 1,"multiple_choices_answers": [{"answer": "MC first answer text","answer_feedback": "MC first answer feedback","weight": 100},{"answer": "MC second answer text","answer_feedback": "MC second answer feedback","weight": 0}]},"true_false":None,"fib":None,"multiple_select":None,"written_response":None},{"title": "TF title","text": "Question text","point": 1,"difficulty": 1,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false": {"true_weight": 100,"true_feedback": "True feedback","false_weight": 0,"false_feedback": "True feedback","enumeration": 2},"fib":None,"multiple_select":None,"written_response":None},{"title": "MS title","text": "Question text","point": 1,"difficulty": 1,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib":None,"multiple_select": {"randomize":True,"enumeration": 1,"style": 2,"multiple_select_answers": [{"answer": "MS first answer text","answer_feedback": "MS first answer feedback","is_correct":True},{"answer": "MS second answer text","answer_feedback": "MS second answer feedback","is_correct":True}]},"written_response":None},{"title": "WR title","text": "Question text","point": 5,"difficulty": 5,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib":None,"multiple_select":None,"written_response": {"enable_student_editor":False,"initial_text":None,"answer_key": "WR answer key","enable_attachments":False}},{"title": "FIB title","text": "Question text","point": 4,"difficulty": 3,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": [{"type": "fibquestion","text": "1+15?","order": 1,"size":None,"weight":None},{"type": "fibanswer","text": "16","order": 2,"size": 3,"weight": 100}],"multiple_select":None,"written_response":None},{"title": "Ordering title","text": "Question text","point": 6,"difficulty": 2,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": None,"multiple_select":None,"ordering": [{"text": "Order 1","order": 1,"ord_feedback": "Ordering 1 feedback"},{"text": "Order 1","order": 2,"ord_feedback": "Ordering 2 feedback"},{"text": "Order 1","order": 3,"ord_feedback": "Ordering 3 feedback"}],"matching":None,"written_response":None},{"title": "Matching title","text": "Question text","point": 6,"difficulty": 2,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": None,"multiple_select":None,"ordering": None,"matching": {"grading_type": 1,"matching_choices": [{"choice_text": "Choice 1","matching_answers": [{"answer_text": "Choice 1 answer a"},{"answer_text": "Choice 1 answer b"}]},{"choice_text": "Choice 2","matching_answers": [{"answer_text": "Choice 2 answer a"},{"answer_text": "Choice 2 answer b"}]}]},"written_response":None}]}]}

		
		ident = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		sectionIdent = 'SECT_' + ident
		questionLibraryIdent = 'QLIB_' + ident

		self.root = ET.Element("questestinterop")
		self.objectbank = ET.SubElement(self.root, "objectbank", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': questionLibraryIdent})
		self.section = ET.SubElement(self.objectbank, "section", {'ident': sectionIdent, 'title': json_output["general_header"]})
		# self.presentation_material()
		self.sectionproc_extension()

		self.json_output = json_output
		self.parse_json_to_xml(json_output)

		self.questiondb_string = self.xml_to_string(self.root)


	def xml_to_string(self, xml) :
		rough_string = ET.tostring(xml, 'utf-8')
		reparsed = parseString(rough_string)
		pretty_xml = reparsed.toprettyxml(indent="\t")
		return pretty_xml
		# sys.exit()
		
	def parse_json_to_xml(self, json_output) :
		ident_prefix = int(datetime.date.today().strftime("%y%m%d")) + int(UUID(int=0x12345678123456781234567812345678))
		index = 1

		for item in json_output:
			match item:
				case "general_header":
					print(json_output["general_header"])
				case "randomize_answer":
					print(json_output["randomize_answer"])
				case "total_question_errors":
					print(json_output["total_question_errors"])
				case "total_document_errors":
					print(json_output["total_document_errors"])
				case "sections":
					for section in json_output["sections"]:
						print("\t", section["title"])
						print("\t", section["is_title_displayed"])
						print("\t", section["text"])
						print("\t", section["is_text_displayed"])
						print("\t", section["shuffle"])

						for question in section["questions"]:
							ident = str(ident_prefix + index)
							question_ident = 'QUES_' + ident
							it = ET.Element("item", {'ident': 'OBJ_' + ident, 'label': question_ident, 'd2l_2p0:page': '1', 'title': question["title"]})
							
							if question["multiple_choice"]:
								self.generate_multiple_choice(it, question_ident, question)
								
							elif question["true_false"] :
								self.generate_true_false(it, question_ident, question)

							elif question["fib"] :
								self.generate_fill_in_the_blanks(it, question_ident, question)

							elif question["multiple_select"]:
								self.generate_multi_select(it, question_ident, question)

							elif question["matching"]:
								self.generate_matching(it, question_ident, question)

							elif question["ordering"]:
								self.generate_ordering(it, question_ident, question)
								
							elif question["written_response"]:
								self.generate_written_response(it, question_ident, question)
							else:
								print("NO QUESTION TYPE")

	
	def create_manifest(self, manifest_entity, folder_path):
		path = folder_path + '/imsmanifest.xml'
		root = ET.Element("manifest", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'xmlns': 'http://www.imsglobal.org/xsd/imscp_v1p1', 'identifier': 'MANIFEST_1'})
		doc = ET.SubElement(root, "resources")

		for resource in manifest_entity.resources:
			ET.SubElement(doc, "resource", {'identifier':resource.identifier, 'type': resource.resource_type, 'd2l_2p0:material_type': resource.material_type,
				'href': resource.href, 'd2l_2p0:link_target' : resource.link_target,
				'title' : resource.title})

		tree = ET.ElementTree(root)
		# tree.write(path)
		return tree

	def presentation_material(self) :
		#presentation_material Node
		sec_pres_mat = ET.SubElement(self.section, "presentation_material")
		sec_pres_mat_flo = ET.SubElement(sec_pres_mat, "flow_mat")
		sec_pres_mat_flo_flo = ET.SubElement(sec_pres_mat_flo, "flow_mat")
		sec_pres_mat_flo_flo_mat = ET.SubElement(sec_pres_mat_flo_flo, "material")
		sec_pres_mat_flo_flo_mat_text = ET.SubElement(sec_pres_mat_flo_flo, "mattext", {'texttype': 'text/html'})


	def sectionproc_extension(self) :
		#presentation_material Node
		sec_proc = ET.SubElement(self.section, "sectionproc_extension")
		sec_proc_dis_name = ET.SubElement(sec_proc, "d2l_2p0:display_section_name")
		sec_proc_dis_name.text = 'yes'
		sec_proc_dis_line = ET.SubElement(sec_proc, "d2l_2p0:display_section_line")
		sec_proc_dis_line.text = 'no'
		sec_proc_dis_sec = ET.SubElement(sec_proc, "d2l_2p0:type_display_section")
		sec_proc_dis_sec.text = '1'


	def itemetadata(self, it, question_type, question) :
		#ItemData Node
		it_metadata = ET.SubElement(it, "itemmetadata")
		it_metadata_qtidata = ET.SubElement(it_metadata, "qtimetadata")
		it_computer_scored = ET.SubElement(it_metadata_qtidata, "qti_metadatafield")
		it_computer_scored_label = ET.SubElement(it_computer_scored, "fieldlabel")
		it_computer_scored_label.text = 'qmd_computerscored'
		it_computer_scored_entry = ET.SubElement(it_computer_scored, "fieldentry")
		it_computer_scored_entry.text = 'yes'
		it_question_type = ET.SubElement(it_metadata_qtidata, "qti_metadatafield")
		it_question_type_label = ET.SubElement(it_question_type, "fieldlabel")
		it_question_type_label.text = 'qmd_questiontype'
		it_question_type_entry = ET.SubElement(it_question_type, "fieldentry")
		it_question_type_entry.text = question_type
		it_weighting = ET.SubElement(it_metadata_qtidata, "qti_metadatafield")
		it_weighting_label = ET.SubElement(it_weighting, "fieldlabel")
		it_weighting_label.text = 'qmd_weighting'
		it_weighting_entry = ET.SubElement(it_weighting, "fieldentry")
		it_weighting_entry.text = "{:.4f}".format(question["point"])


	def itemproc_extension(self, it) :
		#Itemproc_extension Node
		it_proc = ET.SubElement(it, "itemproc_extension")
		it_proc_difficulty = ET.SubElement(it_proc, "d2l_2p0:difficulty")
		it_proc_difficulty.text = '1'
		it_proc_isbonus = ET.SubElement(it_proc, "d2l_2p0:isbonus")
		it_proc_isbonus.text = 'no'
		it_proc_ismandatory = ET.SubElement(it_proc, "d2l_2p0:ismandatory")
		it_proc_ismandatory.text = 'no'


	def generate_feedback(self, it, ident, feedback) :
		it_fb = ET.SubElement(it, "itemfeedback", {'ident': ident})
		it_fb_mat = ET.SubElement(it_fb, "material")
		it_fb_mat_text = ET.SubElement(it_fb_mat, "mattext", {'texttype' : 'text/html'})
		it_fb_mat_text.append(CDATA(feedback))


	def generate_hint(self, it, hint) :
		it_hint = ET.SubElement(it, "hint")
		it_hint_mat = ET.SubElement(it_hint, "hintmaterial")
		it_hint_mat_flow = ET.SubElement(it_hint_mat, "flow_mat")
		it_hint_mat_flow_mat = ET.SubElement(it_hint_mat_flow, "material")
		it_hint_mat_flow_text = ET.SubElement(it_hint_mat_flow_mat, "mattext", {'texttype': 'text/html'})
		it_hint_mat_flow_text.append(CDATA(hint))


	def generate_multiple_choice(self, it, question_ident, question) :
		self.itemetadata(it, 'Multiple Choice', question)
		self.itemproc_extension(it)

		question_lid = question_ident + '_LID'
		question_ident_answer = question_ident + '_A'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Presentation -> Flow
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")

		#Presentation -> Material
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_display_style = ET.SubElement(it_pre_flow_res, "d2l_2p0:display_style")
		it_pre_flow_res_display_style.text = '2'
		it_pre_flow_res_enumeration = ET.SubElement(it_pre_flow_res, "d2l_2p0:enumeration")
		it_pre_flow_res_enumeration.text = '4'
		it_pre_flow_res_grading_type = ET.SubElement(it_pre_flow_res, "d2l_2p0:grading_type")
		it_pre_flow_res_grading_type.text = '0'

		#Presentation -> Flow -> Response_lid
		it_pre_flow_lid = ET.SubElement(it_pre_flow, "response_lid", {'ident': question_lid, 'rcardinality': 'Multiple'})

		# Commented this to deactivate MC randomized answer order
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': ('yes' if self.json_output["randomize"] else 'no')})

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])

		#Reprocessing
		it_res = ET.SubElement(it, "resprocessing")

		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])

		index = 1
		for mc_answers in question["multiple_choice"]["multiple_choices_answers"]:

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.append(CDATA(mc_answers["answer"]))

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition' + str(index)})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer + str(index)
			it_res_set_var = ET.SubElement(it_res_con, "setvar", {'action' : 'Set'})
			it_res_set_var.text = '100.0000' if mc_answers["weight"] else '0.0000'
			it_res_dis = ET.SubElement(it_res_con, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
			if mc_answers["answer_feedback"]:
				self.generate_feedback(it, question_ident_feedback + str(index), mc_answers["answer_feedback"])
			index += 1


	def generate_true_false(self, it, question_ident, question) :
		
		self.itemetadata(it, 'True/False', question)
		self.itemproc_extension(it)

		question_lid = question_ident + '_LID'
		question_ident_answer = question_ident + '_A'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Presentation -> Flow
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")

		#Presentation -> Material
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_display_style = ET.SubElement(it_pre_flow_res, "d2l_2p0:display_style")
		it_pre_flow_res_display_style.text = '2'
		it_pre_flow_res_enumeration = ET.SubElement(it_pre_flow_res, "d2l_2p0:enumeration")
		it_pre_flow_res_enumeration.text = '6'
		it_pre_flow_res_grading_type = ET.SubElement(it_pre_flow_res, "d2l_2p0:grading_type")
		it_pre_flow_res_grading_type.text = '0'

		#Presentation -> Flow -> Response_lid
		it_pre_flow_lid = ET.SubElement(it_pre_flow, "response_lid", {'ident': question_lid, 'rcardinality': 'Single'})
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': 'no'})	

		#Reprocessing
		it_res = ET.SubElement(it, "resprocessing")

		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])

		index = 1
		answer_text = ["True", "False"]
		while index <= 2:
			tf = answer_text[index].lower()
			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/plain'})
			mattext.text = answer_text[index]

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition' + str(index)})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer + str(index)
			it_res_set_var = ET.SubElement(it_res_con, "setvar", {'action' : 'Set'})
			it_res_set_var.text = '100.0000' if question["true_false"][f'{tf}_weight'] else '0.0000'

			it_res_dis = ET.SubElement(it_res_con, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
			if  question["true_false"][f'{tf}_feedback']:
				self.generate_feedback(it, question_ident_feedback + str(index), question["true_false"][f'{tf}_feedback'])
			
			index += 1
	
	def generate_multi_select(self, it, question_ident, question) :
		self.itemetadata(it, 'Multi-Select', question)
		self.itemproc_extension(it)

		question_lid = question_ident + '_LID'
		question_ident_answer = question_ident + '_A'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Presentation -> Flow
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")

		#Presentation -> Material
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_display_style = ET.SubElement(it_pre_flow_res, "d2l_2p0:display_style")
		it_pre_flow_res_display_style.text = '2'
		it_pre_flow_res_enumeration = ET.SubElement(it_pre_flow_res, "d2l_2p0:enumeration")
		it_pre_flow_res_enumeration.text = '6'
		it_pre_flow_res_grading_type = ET.SubElement(it_pre_flow_res, "d2l_2p0:grading_type")
		it_pre_flow_res_grading_type.text = '2'

		#Presentation -> Flow -> Response_lid
		it_pre_flow_lid = ET.SubElement(it_pre_flow, "response_lid", {'ident': question_lid, 'rcardinality': 'Multiple'})
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': ('yes' if self.json_output["randomize"] else 'no')})

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])

		#Reprocessing
		it_res = ET.SubElement(it, "resprocessing")
		it_out = ET.SubElement(it_res, "outcomes")
		it_out_score = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'que_score', 'minvalue': '0', 'maxvalue': '100'})
		it_out_correct = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Correct', 'minvalue': '0'})
		it_out_incorrect = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Incorrect', 'minvalue': '0'})

		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])

		index = 1
		for ms_answers in question["multiple_select"]["multiple_select_answers"]:

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = ms_answers["answer"]

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition', 'continue': 'yes'})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer

			it_res_con_var_equal.text = question_ident_answer + str(index)
			if ms_answers["is_correct"] == True :
				it_res_set_var = ET.SubElement(it_res_con, "setvar", {'varname':'D2L_Correct', 'action' : 'Add'})
			else :
				it_res_set_var = ET.SubElement(it_res_con, "setvar", {'varname':'D2L_Incorrect', 'action' : 'Add'})

			#Add Answer specific feedback
			if ms_answers["answer_feedback"]:
				self.generate_feedback(it, question_ident_feedback + str(index), ms_answers["answer_feedback"])
			index += 1

		it_res_con = ET.SubElement(it_res, "respcondition")
		it_res_set_var = ET.SubElement(it_res_con, "setvar", {'varname':'que_score', 'action' : 'Set'})
		it_res_set_var.text = 'D2L_Correct'


	def generate_fill_in_the_blanks(self, it, question_ident, question) :	
		self.itemetadata(it, 'Fill in the Blanks', question)
		self.itemproc_extension(it)
		
		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")
		#Presentation -> Flow
		
		idx = 1
		for fib in question["fib"]:
			question_str = question_ident + str(idx) + '_STR'
			question_ans = question_ident + str(idx) + '_ANS'
			if fib["type"] == 'fibanswer':
    			#Presentation -> Flow -> Response_str
				it_pre_flow_str = ET.SubElement(it_pre_flow, "response_str", {'rcardinality': 'Single', 'ident': question_str})
				it_pre_flow_str_render = ET.SubElement(it_pre_flow_str, "render_fib", {'fibtype': 'String', 'prompt': 'Box', 'columns': '30', 'rows': '1'})
				it_pre_flow_str_render_label = ET.SubElement(it_pre_flow_str_render, "response_label", {'ident': question_ans})
				idx += 1
			elif fib["type"] == 'fibquestion':
				#Presentation -> Flow -> Material
				it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")
				it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
				question_text = fib["text"]
				it_pre_flow_mat_text.append(CDATA(question_text))

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])

		#Resprocessing
		it_res = ET.SubElement(it, "resprocessing")
		it_out = ET.SubElement(it_res, "outcomes")

		index = 1
		key_value = ['fibanswer']
		fib_answers = [fib for fib in question["fib"] if fib['type'] in key_value]

		for fib in fib_answers:
			answers = [a.strip() for a in fib["text"].split(',')]
			
			answer_weight =  fib["weight"] if fib["weight"] else str(100.0 / len(fib_answers))
			question_ans = question_ident + str(index) + '_ANS'
			for answer in answers:
				it_res_con = ET.SubElement(it_res, "respcondition")
				it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
				it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'case': 'no', 'respident': question_ans})
				it_res_con_var_equal.text = answer
				it_res_set_var = ET.SubElement(it_res_con, "setvar", {'action' : 'Set'})
				it_res_set_var.text = answer_weight
			
			it_out_score = ET.SubElement(it_out, "decvar", {'varname': 'Blank_'+ str(index), 'maxvalue': '100', 'minvalue': '0', 'vartype': 'Integer'})

			index += 1

		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])


	def generate_ordering(self, it, question_ident, question) :
		self.itemetadata(it, 'Ordering', question)
		self.itemproc_extension(it)

		question_o = question_ident + '_O'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Presentation -> Flow

		#Presentation -> Flow -> Material
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res_ext = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_ext_grading = ET.SubElement(it_pre_flow_res_ext, "d2l_2p0:grading_type")
		grading_type = 0 #Equally weighted, All or nothing, Right minus wrong
		it_pre_flow_res_ext_grading.append(CDATA(grading_type))

		#Presentation -> Flow -> Response_grp
		it_pre_flow_res_grp = ET.SubElement(it_pre_flow, "response_grp", {'ident': question_o, 'rcardinality': 'Ordered'})
		it_pre_flow_res_grp_render = ET.SubElement(it_pre_flow_res_grp, "render_choice", {'shuffle': 'yes'})
		it_pre_flow_res_grp_render_flow = ET.SubElement(it_pre_flow_res_grp_render, "flow_label", {'class': 'Block'}) #populated in the loop

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])

		#Resprocessing
		it_res = ET.SubElement(it, "resprocessing") #populated in the loop
		it_out = ET.SubElement(it_res, "outcomes")
		
		it_out_correct = ET.SubElement(it_out, "decvar", {'maxvalue': '100', 'minvalue': '0', 'varname': 'D2L_Correct', 'defaultval': '0', 'vartype': 'Integer'})
		it_out_incorrect = ET.SubElement(it_out, "decvar", {'minvalue': '0', 'varname': 'D2L_Incorrect', 'defaultval': '0', 'vartype': 'Integer'})
		it_out_que_score = ET.SubElement(it_out, "decvar", {'minvalue': '0', 'varname': 'que_score', 'defaultval': '0', 'vartype': 'Integer'})

		it_res_con_other = ET.SubElement(it_res, "respcondition")
		it_res_con_other_var = ET.SubElement(it_res_con_other, "conditionvar")
		it_res_con_other_var_other = ET.SubElement(it_res_con_other_var, "other")
		it_res_con_other_setvar = ET.SubElement(it_res_con_other, "setvar", {'varname': "que_score", 'action': 'Set'})
		it_res_con_other_setvar.text = "D2L_Correct"

		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])
			
		index = 1
		for ord_obj in question["ordering"]:
			ident_num = question_o + str(index)
			#Presentation -> Flow -> Response_grp -> response_label
			it_pre_flow_res_grp_render_flow_res = ET.SubElement(it_pre_flow_res_grp_render_flow, "response_label", {'ident': ident_num})
			it_pre_flow_res_grp_render_flow_res_flow = ET.SubElement(it_pre_flow_res_grp_render_flow_res, "flow_mat")
			it_pre_flow_res_grp_render_flow_res_flow_mat = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow, "material")
			it_pre_flow_res_grp_render_flow_res_flow_mat_text = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow_mat, "mattext", {'texttype': 'text/html'})
			question_text = ord_obj["text"]
			it_pre_flow_res_grp_render_flow_res_flow_mat_text.append(CDATA(question_text))

			#Resprocessing -> Respcondition
			it_res_con_correct = ET.SubElement(it_res, "respcondition", {'title': 'Correct Condition'})
			it_res_con_correct_var = ET.SubElement(it_res_con_correct, "conditionvar")
			it_res_con_correct_var_equal = ET.SubElement(it_res_con_correct_var, "varequal", {'respident': ident_num})
			it_res_con_correct_var_equal.text = str(index)
			it_res_con_correct_setvar = ET.SubElement(it_res_con_correct, "setvar", {'varname': "D2L_Correct", 'action': 'Add'})
			it_res_con_correct_setvar.text = str(1)

			it_res_con_incorrect = ET.SubElement(it_res, "respcondition", {'title': 'Incorrect Condition'})
			it_res_con_incorrect_var = ET.SubElement(it_res_con_incorrect, "conditionvar")
			it_res_con_incorrect_var_not = ET.SubElement(it_res_con_incorrect_var, "not")
			it_res_con_incorrect_var_not_equal = ET.SubElement(it_res_con_incorrect_var_not, "varequal", {'respident': ident_num})
			it_res_con_incorrect_var_not_equal.text = str(index)
			it_res_con_incorrect_setvar = ET.SubElement(it_res_con_incorrect, "setvar", {'varname': "D2L_Incorrect", 'action': 'Add'})
			it_res_con_incorrect_setvar.text = str(1)

			#Add Answer specific feedback
			if ord_obj["ord_feedback"]:
				self.generate_feedback(it, question_ident_feedback + str(index), ord_obj["ord_feedback"])
			index += 1

	def generate_written_response(self, it, question_ident, question) :	
		self.itemetadata(it, 'Long Answer', question)
		self.itemproc_extension(it)
		
		question_ident_str = question_ident + '_STR'
		question_ident_la = question_ident + '_LA'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Presentation -> Flow
		#Presentation -> Flow -> Material
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_mat_res_ext = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_mat_res_ext_sign = ET.SubElement(it_pre_flow_mat_res_ext, "d2l_2p0:has_signed_comments")
		it_pre_flow_mat_res_ext_sign.append(CDATA("no"))
		it_pre_flow_mat_res_ext_editor = ET.SubElement(it_pre_flow_mat_res_ext, "d2l_2p0:has_htmleditor")
		
		has_editor = "yes" if question["written_response"]["enable_student_editor"] else 'no'
		it_pre_flow_mat_res_ext_editor.append(CDATA(has_editor))

		#Presentation -> Flow -> Response_str
		it_pre_flow_mat_res_str = ET.SubElement(it_pre_flow, "response_str", {'rcardinality': 'Multiple', 'ident': question_ident_str})
		it_pre_flow_mat_res_str_render = ET.SubElement(it_pre_flow_mat_res_str, "render_fib", {'fibtype': 'String', 'prompt': 'Box', 'columns': '100', 'rows': '15'})
		it_pre_flow_mat_res_str_render_label = ET.SubElement(it_pre_flow_mat_res_str_render, "response_label", {'ident': question_ident_la})
		it_pre_flow_mat_res_str_render_label_mat = ET.SubElement(it_pre_flow_mat_res_str_render_label, "material")
		it_pre_flow_mat_res_str_render_label_mat_text = ET.SubElement(it_pre_flow_mat_res_str_render_label_mat, "mattext", {'texttype': 'text/html'})

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])
		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])
		#Initial_text
		it_init_text = ET.SubElement(it, "initial_text")
		it_init_text_mat = ET.SubElement(it, "initial_text_material")
		it_init_text_mat_flow = ET.SubElement(it_init_text_mat, "flow_mat")
		it_init_text_mat_flow_mat = ET.SubElement(it_init_text_mat_flow, "material")
		it_init_text_mat_flow_mat_text = ET.SubElement(it_init_text_mat_flow_mat, "mattext", {'texttype': 'text/html'})
		#Answer_key
		it_ans = ET.SubElement(it, "answer_key")
		it_ans_mat = ET.SubElement(it_ans, "answer_key_material")
		it_ans_mat_flow = ET.SubElement(it_ans_mat, "flow_mat")
		it_ans_mat_flow_mat = ET.SubElement(it_ans_mat_flow, "material")
		it_ans_mat_flow_mat_text = ET.SubElement(it_ans_mat_flow_mat, "mattext", {'texttype': 'text/html'})
		it_ans_mat_flow_mat_text.append(CDATA(question["written_response"]["answer_key"]))

	def generate_matching(self, it, question_ident, question) :
		
		self.itemetadata(it, 'Matching', question)
		self.itemproc_extension(it) #shouldn't be here

		question_lid = question_ident + '_LID'
		question_ident_answer = question_ident + '_A'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Add hint
		if question["hint"]:
			self.generate_hint(it, question["hint"])

		#Resprocessing Node
		it_res = ET.SubElement(it, "resprocessing")

		#Resprocessing -> Outcomes
		it_res_out = ET.SubElement(it_res, "outcomes")
		it_res_out_dec_correct = ET.SubElement(it_res_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Correct', 'minvalue': '0', 'maxvalue': '100'})
		it_res_out_dec_incorrect = ET.SubElement(it_res_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Incorrect', 'minvalue': '0', 'maxvalue': '100'})
		it_res_out_dec_score = ET.SubElement(it_res_out, "decvar", {'vartype': 'Decimal', 'defaultval': '0', 'varname': 'que_score', 'minvalue': '0', 'maxvalue': '100'})

		#Presentation -> Flow
		it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")

		#Presentation -> Material
		it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
		question_text = question["text"]
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_grading_type = ET.SubElement(it_pre_flow_res, "d2l_2p0:grading_type")
		it_pre_flow_res_grading_type.text = '0'

		#Presentation -> Flow -> Response_grp -> Render_choice
		it_pre_flow_res_grp_ren = ET.Element("render_choice", {'shuffle': 'yes'})
		it_pre_flow_res_grp_ren_flow = ET.SubElement(it_pre_flow_res_grp_ren, "flow_label", {'class': 'Block'})

		respcondition_string = "<group>"

		index = 1
		for choice in question["matching"]["matching_choices"]:

			question_answer_index = question_ident_answer + str(index)

			it_grp_ren_flow_lab = ET.SubElement(it_pre_flow_res_grp_ren_flow, "response_label", {'ident': question_answer_index })
			it_grp_ren_flow_lab_flow = ET.SubElement(it_grp_ren_flow_lab, "flow_mat")
			it_grp_ren_flow_lab_flow_mat = ET.SubElement(it_grp_ren_flow_lab_flow, "material")
			it_grp_ren_flow_lab_flow_mat_text = ET.SubElement(it_grp_ren_flow_lab_flow_mat, "mattext", {'texttype': 'text/html'})
			it_grp_ren_flow_lab_flow_mat_text.append(CDATA(choice["choice_text"]))
			index +=1

			it_respcondition = ET.Element("respcondition")
			it_respcondition_var = ET.SubElement(it_respcondition, "conditionvar")
			it_respcondition_varequal = ET.SubElement(it_respcondition_var, "varequal", {'respident': '##question_lid##'})
			it_respcondition_varequal.text = question_answer_index
			it_resp_setvar = ET.SubElement(it_respcondition, "setvar", {'varname': 'D2L_Incorrect', 'action': 'Add'})
			it_resp_setvar.text = "1"

			respcondition_string += ET.tostring(it_respcondition, 'utf-8').decode("utf-8") + "\n"

			answer_index = 1
			for answer in choice["matching_answers"]:
				question_index = question_lid + str(answer_index)
				question_answer_index = question_ident_answer + str(answer_index)

				#Presentation -> Flow -> Response_grp
				it_pre_flow_res_grp = ET.SubElement(it_pre_flow, "response_grp", {'respident': question_index, 'rcardinality': 'Single'})
				
				#Presentation -> Flow -> Response_grp -> Material
				it_pre_flow_res_grp_mat = ET.SubElement(it_pre_flow_res_grp, "material")
				it_pre_flow_res_grp_mattext = ET.SubElement(it_pre_flow_res_grp_mat, "mattext", {'texttype': 'text/html'})
				it_pre_flow_res_grp_mattext.append(CDATA(answer["answer_text"]))

				#Presentation -> Flow -> Response_grp -> Render_choice
				it_pre_flow_res_grp.append(it_pre_flow_res_grp_ren)

				respcondition_elem_string = respcondition_string.replace("##question_lid##", question_index)
				respcondition_elem_string = re.sub(r'(<respcondition.*?' + question_answer_index + r'.*?)(D2L_Incorrect)(.*?<\/respcondition>)', r'\1D2L_Correct\3', respcondition_elem_string, re.MULTILINE)
				respcondition_elem_string = respcondition_elem_string.replace("\n", "")
				
				elem = ET.fromstring(respcondition_elem_string)
				it_res.extend(list(elem))
				answer_index +=1

		respcondition_string += "</group>"


		it_respcondition = ET.SubElement(it_res, "respcondition")
		it_respcondition_var = ET.SubElement(it_respcondition, "conditionvar")
		it_respcondition_var_other = ET.SubElement(it_respcondition_var, "other")
		it_resp_setvar = ET.SubElement(it_respcondition, "setvar", {'varname': 'que_score', 'action': 'Set'})
		it_resp_setvar.text = "D2L_Correct"


		#Add General feedback
		if question["feedback"]:
			self.generate_feedback(it, question_ident, question["feedback"])