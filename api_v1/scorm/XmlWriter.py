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
import pypandoc

class XmlWriter():

	def __init__(self, question_library, questions) :

		ident = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		sectionIdent = 'SECT_' + ident
		questionLibraryIdent = 'QLIB_' + ident

		self.root = ET.Element("questestinterop")
		self.objectbank = ET.SubElement(self.root, "objectbank", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': questionLibraryIdent})
		self.section = ET.SubElement(self.objectbank, "section", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': sectionIdent, 'title': question_library.section_name})
		self.presentation_material()
		self.sectionproc_extension()

		self.questions = questions
		self.parse_question(questions)

		self.questiondb_string = self.xml_to_string(self.root)


	def xml_to_string(self, xml) :
		rough_string = ET.tostring(xml, 'utf-8')
		reparsed = parseString(rough_string)
		pretty_xml = reparsed.toprettyxml(indent="\t")
		return pretty_xml
		# sys.exit()
		
	def parse_question(self, questions) :
		ident_prefix = int(datetime.date.today().strftime("%y%m%d")) + int(UUID(int=0x12345678123456781234567812345678))
		index = 1
		for question in questions:
			ident = str(ident_prefix + index)
			question_ident = 'QUES_' + ident

			title_prefix = ''
			question_text = question.question_body
			if isinstance(question.question_body, list) :
				question_text = " ".join(question.question_body)
			plain_text = pypandoc.convert_text(question_text, format="html", to="plain").replace('\n', ' ')
			title = title_prefix + str(question.title if question.title != "" else plain_text)
			
			it = ET.Element("item", {'ident': 'OBJ_' + ident, 'label': question_ident, 'd2l_2p0:page': '1', 'title': title})	
			if question.question_type == 'MC':
				self.generate_multiple_choice(it, question_ident, question)
			elif question.question_type == 'MS':
				self.generate_multi_select(it, question_ident, question)
			elif question.question_type == 'FIB':
				self.generate_fill_in_the_blanks(it, question_ident, question)
			elif question.question_type == 'ORD':
				self.generate_ordering(it, question_ident, question)
			elif question.question_type == 'WR':
				self.generate_written_response(it, question_ident, question)
			elif question.question_type == 'MT':
				self.generate_matching(it, question_ident, question)
			elif question.question_type == 'TF':
				self.generate_true_false(it, question_ident, question)

			self.section.append(it)
			index +=1
		pass

	
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
		it_weighting_entry.text = "{:.4f}".format(float(question.points)) if question.points else "1"


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
		question_text = question.question_body
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
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': ('yes' if question.randomize_answers else 'no')})

		#Add hint
		if question.hint != None:
			self.generate_hint(it, question.hint)

		#Reprocessing
		it_res = ET.SubElement(it, "resprocessing")

		#Add General feedback
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.append(CDATA(answer.answer_body))

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition' + str(index)})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer + str(index)
			it_res_set_var = ET.SubElement(it_res_con, "setvar", {'action' : 'Set'})
			it_res_set_var.text = '100.0000' if answer.is_correct == True else '0.0000'
			it_res_dis = ET.SubElement(it_res_con, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
			if answer.answer_feedback != None:
				self.generate_feedback(it, question_ident_feedback + str(index), answer.answer_feedback)
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
		question_text = question.question_body
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
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = answer.answer_body

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition' + str(index)})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer + str(index)
			it_res_set_var = ET.SubElement(it_res_con, "setvar", {'action' : 'Set'})
			it_res_set_var.text = '100.0000' if answer.is_correct == True else '0.0000'
			it_res_dis = ET.SubElement(it_res_con, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
			if answer.answer_feedback != None:
				self.generate_feedback(it, question_ident_feedback + str(index), answer.answer_feedback)
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
		question_text = question.question_body
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
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': ('yes' if question.randomize_answers else 'no')})

		#Add hint
		if question.hint != None:
			self.generate_hint(it, question.hint)

		#Reprocessing
		it_res = ET.SubElement(it, "resprocessing")
		it_out = ET.SubElement(it_res, "outcomes")
		it_out_score = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'que_score', 'minvalue': '0', 'maxvalue': '100'})
		it_out_correct = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Correct', 'minvalue': '0'})
		it_out_incorrect = ET.SubElement(it_out, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Incorrect', 'minvalue': '0'})

		#Add General feedback
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			response_label = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flow_mat = ET.SubElement(response_label, "flow_mat")
			material = ET.SubElement(flow_mat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = answer.answer_body

			#Reprocessing -> Respcondition
			it_res_con = ET.SubElement(it_res, "respcondition", {'title': 'Response Condition', 'continue': 'yes'})
			it_res_con_var = ET.SubElement(it_res_con, "conditionvar")
			it_res_con_var_equal = ET.SubElement(it_res_con_var, "varequal", {'respident': question_lid})
			it_res_con_var_equal.text = question_ident_answer

			it_res_con_var_equal.text = question_ident_answer + str(index)
			if answer.is_correct == True :
				it_res_set_var = ET.SubElement(it_res_con, "setvar", {'varname':'D2L_Correct', 'action' : 'Add'})
			else :
				it_res_set_var = ET.SubElement(it_res_con, "setvar", {'varname':'D2L_Incorrect', 'action' : 'Add'})

			#Add Answer specific feedback
			if answer.answer_feedback != None:
				self.generate_feedback(it, question_ident_feedback + str(index), answer.answer_feedback)
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
		for fib in question.get_fib():
			question_str = question_ident + str(idx) + '_STR'
			question_ans = question_ident + str(idx) + '_ANS'
			if fib.type == 'answer':
    			#Presentation -> Flow -> Response_str
				it_pre_flow_str = ET.SubElement(it_pre_flow, "response_str", {'rcardinality': 'Single', 'ident': question_str})
				it_pre_flow_str_render = ET.SubElement(it_pre_flow_str, "render_fib", {'fibtype': 'String', 'prompt': 'Box', 'columns': '30', 'rows': '1'})
				it_pre_flow_str_render_label = ET.SubElement(it_pre_flow_str_render, "response_label", {'ident': question_ans})
				idx += 1
			elif fib.type == 'question':
				#Presentation -> Flow -> Material
				it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")
				it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
				question_text = fib.text
				it_pre_flow_mat_text.append(CDATA(question_text))

		#Add hint
		if question.hint != None:
			self.generate_hint(it, question.hint)

		#Resprocessing
		it_res = ET.SubElement(it, "resprocessing")
		it_out = ET.SubElement(it_res, "outcomes")

		index = 1
		for fib in question.get_fib_answers():
			answers = [a.strip() for a in fib.text.split(',')]
			
			answer_weight = str(100.0 / len(question.get_fib_answers()))
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
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)


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
		question_text = question.question_body
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
		if question.hint != None:
			self.generate_hint(it, question.hint)

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
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)
			
		index = 1
		for answer in question.get_answers():
			ident_num = question_o + str(index)
			#Presentation -> Flow -> Response_grp -> response_label
			it_pre_flow_res_grp_render_flow_res = ET.SubElement(it_pre_flow_res_grp_render_flow, "response_label", {'ident': ident_num})
			it_pre_flow_res_grp_render_flow_res_flow = ET.SubElement(it_pre_flow_res_grp_render_flow_res, "flow_mat")
			it_pre_flow_res_grp_render_flow_res_flow_mat = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow, "material")
			it_pre_flow_res_grp_render_flow_res_flow_mat_text = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow_mat, "mattext", {'texttype': 'text/html'})
			question_text = answer.answer_body
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
			if answer.answer_feedback != None:
				self.generate_feedback(it, question_ident_feedback + str(index), answer.answer_feedback)
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
		question_text = question.question_body
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_mat_res_ext = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_mat_res_ext_sign = ET.SubElement(it_pre_flow_mat_res_ext, "d2l_2p0:has_signed_comments")
		it_pre_flow_mat_res_ext_sign.append(CDATA("no"))
		it_pre_flow_mat_res_ext_editor = ET.SubElement(it_pre_flow_mat_res_ext, "d2l_2p0:has_htmleditor")
		
		#Change it to "no" to deactivate student HTML editor answer
		it_pre_flow_mat_res_ext_editor.append(CDATA("no"))

		#Presentation -> Flow -> Response_str
		it_pre_flow_mat_res_str = ET.SubElement(it_pre_flow, "response_str", {'rcardinality': 'Multiple', 'ident': question_ident_str})
		it_pre_flow_mat_res_str_render = ET.SubElement(it_pre_flow_mat_res_str, "render_fib", {'fibtype': 'String', 'prompt': 'Box', 'columns': '100', 'rows': '15'})
		it_pre_flow_mat_res_str_render_label = ET.SubElement(it_pre_flow_mat_res_str_render, "response_label", {'ident': question_ident_la})
		it_pre_flow_mat_res_str_render_label_mat = ET.SubElement(it_pre_flow_mat_res_str_render_label, "material")
		it_pre_flow_mat_res_str_render_label_mat_text = ET.SubElement(it_pre_flow_mat_res_str_render_label_mat, "mattext", {'texttype': 'text/html'})

		#Add hint
		if question.hint != None:
			self.generate_hint(it, question.hint)
		#Add General feedback
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)
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
		answer_key = ""
		for answer in question.get_answers():
			# TODO: ADD PREFIX OR SOLVE LIST INSIDE LIST
			answer_key = answer_key + answer.answer_body

		it_ans_mat_flow_mat_text.append(CDATA(answer_key))

	def generate_matching(self, it, question_ident, question) :
		
		self.itemetadata(it, 'Matching', question)
		self.itemproc_extension(it)

		question_lid = question_ident + '_LID'
		question_ident_answer = question_ident + '_A'
		question_ident_feedback = question_ident + '_IF'

		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")

		#Add hint
		if question.hint != None:
			self.generate_hint(it, question.hint)

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
		question_text = question.question_body
		it_pre_flow_mat_text.append(CDATA(question_text))

		#Presentation -> Flow -> Response_extension
		it_pre_flow_res = ET.SubElement(it_pre_flow, "response_extension")
		it_pre_flow_res_grading_type = ET.SubElement(it_pre_flow_res, "d2l_2p0:grading_type")
		it_pre_flow_res_grading_type.text = '0'

		#Presentation -> Flow -> Response_grp -> Render_choice
		it_pre_flow_res_grp_ren = ET.Element("render_choice", {'shuffle': 'no'})
		it_pre_flow_res_grp_ren_flow = ET.SubElement(it_pre_flow_res_grp_ren, "flow_label", {'class': 'Block'})

		respcondition_string = "<group>"

		index = 1
		for answer in question.get_answers():

			question_answer_index = question_ident_answer + str(index) 

			it_grp_ren_flow_lab = ET.SubElement(it_pre_flow_res_grp_ren_flow, "response_label", {'ident': question_answer_index })
			it_grp_ren_flow_lab_flow = ET.SubElement(it_grp_ren_flow_lab, "flow_mat")
			it_grp_ren_flow_lab_flow_mat = ET.SubElement(it_grp_ren_flow_lab_flow, "material")
			it_grp_ren_flow_lab_flow_mat_text = ET.SubElement(it_grp_ren_flow_lab_flow_mat, "mattext", {'texttype': 'text/html'})
			it_grp_ren_flow_lab_flow_mat_text.append(CDATA(answer.match_right))
			index +=1

			it_respcondition = ET.Element("respcondition")
			it_respcondition_var = ET.SubElement(it_respcondition, "conditionvar")
			it_respcondition_varequal = ET.SubElement(it_respcondition_var, "varequal", {'respident': '##question_lid##'})
			it_respcondition_varequal.text = question_answer_index
			it_resp_setvar = ET.SubElement(it_respcondition, "setvar", {'varname': 'D2L_Incorrect', 'action': 'Add'})
			it_resp_setvar.text = "1"

			respcondition_string += ET.tostring(it_respcondition, 'utf-8').decode("utf-8") + "\n"

		respcondition_string += "</group>"

		index = 1
		for answer in question.get_answers():

			question_index = question_lid + str(index)
			question_answer_index = question_ident_answer + str(index)

			#Presentation -> Flow -> Response_grp
			it_pre_flow_res_grp = ET.SubElement(it_pre_flow, "response_grp", {'respident': question_index, 'rcardinality': 'Single'})
			
			#Presentation -> Flow -> Response_grp -> Material
			it_pre_flow_res_grp_mat = ET.SubElement(it_pre_flow_res_grp, "material")
			it_pre_flow_res_grp_mattext = ET.SubElement(it_pre_flow_res_grp_mat, "mattext", {'texttype': 'text/html'})
			it_pre_flow_res_grp_mattext.append(CDATA(answer.match_left))

			#Presentation -> Flow -> Response_grp -> Render_choice
			it_pre_flow_res_grp.append(it_pre_flow_res_grp_ren)

			respcondition_elem_string = respcondition_string.replace("##question_lid##", question_index)
			respcondition_elem_string = re.sub(r'(<respcondition.*?' + question_answer_index + r'.*?)(D2L_Incorrect)(.*?<\/respcondition>)', r'\1D2L_Correct\3', respcondition_elem_string, re.MULTILINE)
			respcondition_elem_string = respcondition_elem_string.replace("\n", "")
			
			elem = ET.fromstring(respcondition_elem_string)
			it_res.extend(list(elem))
			index +=1


		it_respcondition = ET.SubElement(it_res, "respcondition")
		it_respcondition_var = ET.SubElement(it_respcondition, "conditionvar")
		it_respcondition_var_other = ET.SubElement(it_respcondition_var, "other")
		it_resp_setvar = ET.SubElement(it_respcondition, "setvar", {'varname': 'que_score', 'action': 'Set'})
		it_resp_setvar.text = "D2L_Correct"


		#Add General feedback
		if question.question_feedback != None:
			self.generate_feedback(it, question_ident, question.question_feedback)