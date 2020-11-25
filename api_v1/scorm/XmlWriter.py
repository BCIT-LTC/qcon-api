import os
import shutil
import datetime
import re
import xml.etree.cElementTree as ET
from uuid import UUID
from api_v1.scorm.xmlcdata import CDATA
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
			title = title_prefix + str(question.title if question.title is not None else plain_text)
			
			it = ET.Element("item", {'ident': 'OBJ_' + ident, 'label': question_ident, 'd2l_2p0:page': '1', 'title': title})

			if question.question_type == 'MC':
				self.generate_multiple_choice(it, question_ident, question)
			# elif question.question_type == question.QUESTION_TYPE_MULTI_SELECT:
			# 	self.generate_multi_select(it, question_ident, question)
			# elif question.question_type == question.QUESTION_TYPE_FILL_IN_BLANK:
			# 	self.generate_fill_in_the_blanks(it, question_ident, question)
			# elif question.question_type == question.QUESTION_TYPE_ORDERING:
			# 	self.generate_ordering(it, question_ident, question)
			# elif question.question_type == question.QUESTION_TYPE_LONG_ANSWER:
			# 	self.generate_written_response(it, question_ident, question)	
			# elif question.question_type == question.QUESTION_TYPE_MATCHING:
			# 	self.generate_matching(it, question_ident, question)
			elif question.question_type == 'TF':
				self.generate_true_false(it, question_ident, question)

			self.section.append(it)
			index +=1
		pass

	
	def create_manifest(self, manifestEntity, folder_path):
		path = folder_path + '/imsmanifest.xml'
		root = ET.Element("manifest", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'xmlns': 'http://www.imsglobal.org/xsd/imscp_v1p1', 'identifier': 'MANIFEST_1'})
		doc = ET.SubElement(root, "resources")

		for resource in manifestEntity.resources:
			ET.SubElement(doc, "resource", {'identifier':resource.identifier, 'type': resource.resourceType, 'd2l_2p0:material_type': resource.materialType, 
				'href': resource.href, 'd2l_2p0:link_target' : resource.linkTarget,
				'title' : resource.title})

		tree = ET.ElementTree(root)
		# tree.write(path)
		return tree

	def presentation_material(self) :
		#presentation_material Node
		secPresMat = ET.SubElement(self.section, "presentation_material")
		secPresMatFlo = ET.SubElement(secPresMat, "flow_mat")
		secPresMatFloFlo = ET.SubElement(secPresMatFlo, "flow_mat")
		secPresMatFloFloMat = ET.SubElement(secPresMatFloFlo, "material")
		secPresMatFloFloMatText = ET.SubElement(secPresMatFloFlo, "mattext", {'texttype': 'text/html'})


	def sectionproc_extension(self) :
		#presentation_material Node
		secProc = ET.SubElement(self.section, "sectionproc_extension")
		secProcDisName = ET.SubElement(secProc, "d2l_2p0:display_section_name")
		secProcDisName.text = 'yes'
		secProcDisLine = ET.SubElement(secProc, "d2l_2p0:display_section_line")
		secProcDisLine.text = 'no'
		secProcDisSec = ET.SubElement(secProc, "d2l_2p0:type_display_section")
		secProcDisSec.text = '1'


	def itemetadata(self, it, questionType, question) :
		#ItemData Node
		itMetadata = ET.SubElement(it, "itemmetadata")
		itTimedata = ET.SubElement(itMetadata, "qtimetadata")
		itComputerScored = ET.SubElement(itTimedata, "qti_metadatafield")
		itComputerScoredLabel = ET.SubElement(itComputerScored, "fieldlabel")
		itComputerScoredLabel.text = 'qmd_computerscored'
		itComputerScoredEntry = ET.SubElement(itComputerScored, "fieldentry")
		itComputerScoredEntry.text = 'yes'
		itQuestionType = ET.SubElement(itTimedata, "qti_metadatafield")
		itQuestionTypeLabel = ET.SubElement(itQuestionType, "fieldlabel")
		itQuestionTypeLabel.text = 'qmd_questiontype'
		itQuestionTypeEntry = ET.SubElement(itQuestionType, "fieldentry")
		itQuestionTypeEntry.text = questionType
		itWeighting = ET.SubElement(itTimedata, "qti_metadatafield")
		itWeightingLabel = ET.SubElement(itWeighting, "fieldlabel")
		itWeightingLabel.text = 'qmd_weighting'
		itWeightingEntry = ET.SubElement(itWeighting, "fieldentry")
		itWeightingEntry.text = "{:.4f}".format(float(question.points)) if question.points else "1"


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
		if feedback is not None:
			it_fb_mat_text.append(CDATA(feedback))


	def generate_hint(self, it, hint) :
		itHint = ET.SubElement(it, "hint")
		itHintMat = ET.SubElement(itHint, "hintmaterial")
		itHintMatFlow = ET.SubElement(itHintMat, "flow_mat")
		itHintMatFlowMat = ET.SubElement(itHintMatFlow, "material")
		itHintMatFlowText = ET.SubElement(itHintMatFlowMat, "mattext", {'texttype': 'text/html'})
		itHintMatFlowText.append(CDATA(hint))


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
		if question.hint is not None:
			self.generate_hint(it, question.hint)

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")

		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			responseLabel = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flowMat = ET.SubElement(responseLabel, "flow_mat")
			material = ET.SubElement(flowMat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.append(CDATA(answer.answer_body))

			#Reprocessing -> Respcondition
			itResCon = ET.SubElement(itRes, "respcondition", {'title': 'Response Condition' + str(index)})
			itResConVar = ET.SubElement(itResCon, "conditionvar")
			itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'respident': question_lid})
			itResConVarEqual.text = question_ident_answer + str(index)
			itResSetVar = ET.SubElement(itResCon, "setvar", {'action' : 'Set'})
			itResSetVar.text = '100.0000' if answer.is_correct == True else '0.0000'
			itResDis = ET.SubElement(itResCon, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
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
		it_pre_flow_lid_render_choice = ET.SubElement(it_pre_flow_lid, "render_choice", {'shuffle': ('yes' if question.randomize_answers else 'no')})	

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")

		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			responseLabel = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flowMat = ET.SubElement(responseLabel, "flow_mat")
			material = ET.SubElement(flowMat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = answer.answer_body.replace("<p>", "").replace("</p>", "").strip()

			#Reprocessing -> Respcondition
			itResCon = ET.SubElement(itRes, "respcondition", {'title': 'Response Condition' + str(index)})
			itResConVar = ET.SubElement(itResCon, "conditionvar")
			itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'respident': question_lid})
			itResConVarEqual.text = question_ident_answer + str(index)
			itResSetVar = ET.SubElement(itResCon, "setvar", {'action' : 'Set'})
			itResSetVar.text = '100.0000' if answer.is_correct == True else '0.0000'
			itResDis = ET.SubElement(itResCon, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': question_ident_feedback + str(index)})

			#Add Answer specific feedback
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
		if question.hint is not None:
			self.generate_hint(it, question.hint)

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")
		itOut = ET.SubElement(itRes, "outcomes")
		itOutScore = ET.SubElement(itOut, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'que_score', 'minvalue': '0', 'maxvalue': '100'})
		itOutCorrect = ET.SubElement(itOut, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Correct', 'minvalue': '0'})
		itOutIncorrect = ET.SubElement(itOut, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Incorrect', 'minvalue': '0'})

		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)

		index = 1
		for answer in question.get_answers():

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(it_pre_flow_lid_render_choice, "flow_label", {'class': 'Block'})
			responseLabel = ET.SubElement(flow, "response_label", {'ident': question_ident_answer + str(index)})
			flowMat = ET.SubElement(responseLabel, "flow_mat")
			material = ET.SubElement(flowMat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = answer.answer_body

			#Reprocessing -> Respcondition
			itResCon = ET.SubElement(itRes, "respcondition", {'title': 'Response Condition', 'continue': 'yes'})
			itResConVar = ET.SubElement(itResCon, "conditionvar")
			itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'respident': question_lid})
			itResConVarEqual.text = question_ident_answer

			itResConVarEqual.text = question_ident_answer + str(index)
			if answer.is_correct == True :
				itResSetVar = ET.SubElement(itResCon, "setvar", {'varname':'D2L_Correct', 'action' : 'Add'})
			else :
				itResSetVar = ET.SubElement(itResCon, "setvar", {'varname':'D2L_Incorrect', 'action' : 'Add'})

			#Add Answer specific feedback
			self.generate_feedback(it, question_ident_feedback + str(index), answer.answer_feedback)
			index += 1

		itResCon = ET.SubElement(itRes, "respcondition")
		itResSetVar = ET.SubElement(itResCon, "setvar", {'varname':'que_score', 'action' : 'Set'})
		itResSetVar.text = 'D2L_Correct'

	def generate_fill_in_the_blanks(self, it, question_ident, question) :	
		self.itemetadata(it, 'Fill in the Blanks', question)
		self.itemproc_extension(it)
		
		#Presentation Node
		it_pre = ET.SubElement(it, "presentation")
		it_pre_flow = ET.SubElement(it_pre, "flow")
		#Presentation -> Flow
		
		idx = 1
		for question_text in question.question_body:
			questionStr = question_ident + str(idx) + '_STR'
			questionAns = question_ident + str(idx) + '_ANS'
			if question_text == '##ANSWER##':
    			#Presentation -> Flow -> Response_str
				it_pre_flow_str = ET.SubElement(it_pre_flow, "response_str", {'rcardinality': 'Single', 'ident': questionStr})
				it_pre_flow_str_render = ET.SubElement(it_pre_flow_str, "render_fib", {'fibtype': 'String', 'prompt': 'Box', 'columns': '30', 'rows': '1'})
				it_pre_flow_str_render_label = ET.SubElement(it_pre_flow_str_render, "response_label", {'ident': questionAns})
				idx += 1
			else:
				#Presentation -> Flow -> Material
				it_pre_flow_mat = ET.SubElement(it_pre_flow, "material")
				it_pre_flow_mat_text = ET.SubElement(it_pre_flow_mat, "mattext", {'texttype': 'text/html'})
				question_text = question_text
				it_pre_flow_mat_text.append(CDATA(question_text))

		#Add hint
		if question.hint is not None:
			self.generate_hint(it, question.hint)

		#Resprocessing
		itRes = ET.SubElement(it, "resprocessing")
		itOut = ET.SubElement(itRes, "outcomes")

		index = 1
		for answer in question.get_answers():
			match = re.search(r"^(\s{0,}?\<p\>)(.*)(<\/p>\s{0,}?)$", answer.answer_body)
			answers = [a.strip() for a in match.group(2).split(',')]
			
			answerWeight = str(100.0 / len(answers))
			questionAns = question_ident + str(index) + '_ANS'
			for answer in answers:
				itResCon = ET.SubElement(itRes, "respcondition")
				itResConVar = ET.SubElement(itResCon, "conditionvar")
				itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'case': 'no', 'respident': questionAns})
				itResConVarEqual.text = answer
				itResSetVar = ET.SubElement(itResCon, "setvar", {'action' : 'Set'})
				itResSetVar.text = answerWeight
			
			itOutScore = ET.SubElement(itOut, "decvar", {'varname': 'Blank_'+ str(index), 'maxvalue': '100', 'minvalue': '0', 'vartype': 'Integer'})

			index += 1

		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)


	def generate_ordering(self, it, question_ident, question) :
		self.itemetadata(it, 'Ordering', question)
		self.itemproc_extension(it)

		questionO = question_ident + '_O'
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
		gradingType = 0 #Equally weighted, All or nothing, Right minus wrong
		it_pre_flow_res_ext_grading.append(CDATA(gradingType))

		#Presentation -> Flow -> Response_grp
		it_pre_flow_res_grp = ET.SubElement(it_pre_flow, "response_grp", {'ident': questionO, 'rcardinality': 'Ordered'})
		it_pre_flow_res_grp_render = ET.SubElement(it_pre_flow_res_grp, "render_choice", {'shuffle': ('yes' if question.randomize_answers else 'no')})
		it_pre_flow_res_grp_render_flow = ET.SubElement(it_pre_flow_res_grp_render, "flow_label", {'class': 'Block'}) #populated in the loop

		#Add hint
		if question.hint is not None:
			self.generate_hint(it, question.hint)

		#Resprocessing
		itRes = ET.SubElement(it, "resprocessing") #populated in the loop
		itOut = ET.SubElement(itRes, "outcomes")
		
		itOutCorrect = ET.SubElement(itOut, "decvar", {'maxvalue': '100', 'minvalue': '0', 'varname': 'D2L_Correct', 'defaultval': '0', 'vartype': 'Integer'})
		itOutIncorrect = ET.SubElement(itOut, "decvar", {'minvalue': '0', 'varname': 'D2L_Incorrect', 'defaultval': '0', 'vartype': 'Integer'})
		itOutQueScore = ET.SubElement(itOut, "decvar", {'minvalue': '0', 'varname': 'que_score', 'defaultval': '0', 'vartype': 'Integer'})

		itResConOther = ET.SubElement(itRes, "respcondition")
		itResConOtherVar = ET.SubElement(itResConOther, "conditionvar")
		itResConOtherVarOther = ET.SubElement(itResConOtherVar, "other")
		itResConOtherSetVar = ET.SubElement(itResConOther, "setvar", {'varname': "que_score", 'action': 'Set'})
		itResConOtherSetVar.text = "D2L_Correct"

		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)
			
		index = 1
		for answer in question.get_answers():
			identNum = questionO + str(index)
			#Presentation -> Flow -> Response_grp -> response_label
			it_pre_flow_res_grp_render_flow_res = ET.SubElement(it_pre_flow_res_grp_render_flow, "response_label", {'ident': identNum})
			it_pre_flow_res_grp_render_flow_res_flow = ET.SubElement(it_pre_flow_res_grp_render_flow_res, "flow_mat")
			it_pre_flow_res_grp_render_flow_res_flow_mat = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow, "material")
			it_pre_flow_res_grp_render_flow_res_flow_mat_text = ET.SubElement(it_pre_flow_res_grp_render_flow_res_flow_mat, "mattext", {'texttype': 'text/html'})
			question_text = answer.answer_body
			it_pre_flow_res_grp_render_flow_res_flow_mat_text.append(CDATA(question_text))

			#Resprocessing -> Respcondition
			itResConCorrect = ET.SubElement(itRes, "respcondition", {'title': 'Correct Condition'})
			itResConCorrectVar = ET.SubElement(itResConCorrect, "conditionvar")
			itResConCorrectVarEqual = ET.SubElement(itResConCorrectVar, "varequal", {'respident': identNum})
			itResConCorrectVarEqual.text = str(index)
			itResConCorrectSetVar = ET.SubElement(itResConCorrect, "setvar", {'varname': "D2L_Correct", 'action': 'Add'})
			itResConCorrectSetVar.text = str(1)

			itResConIncorrect = ET.SubElement(itRes, "respcondition", {'title': 'Incorrect Condition'})
			itResConIncorrectVar = ET.SubElement(itResConIncorrect, "conditionvar")
			itResConIncorrectVarNot = ET.SubElement(itResConIncorrectVar, "not")
			itResConIncorrectVarNotEqual = ET.SubElement(itResConIncorrectVarNot, "varequal", {'respident': identNum})
			itResConIncorrectVarNotEqual.text = str(index)
			itResConIncorrectSetVar = ET.SubElement(itResConIncorrect, "setvar", {'varname': "D2L_Incorrect", 'action': 'Add'})
			itResConIncorrectSetVar.text = str(1)

			#Add Answer specific feedback
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
		if question.hint is not None:
			self.generate_hint(it, question.hint)
		
		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)

		#Initial_text
		itInitText = ET.SubElement(it, "initial_text")
		itInitTextMat = ET.SubElement(it, "initial_text_material")
		itInitTextMatFlow = ET.SubElement(itInitTextMat, "flow_mat")
		itInitTextMatFlowMat = ET.SubElement(itInitTextMatFlow, "material")
		itInitTextMatFlowMatText = ET.SubElement(itInitTextMatFlowMat, "mattext", {'texttype': 'text/html'})

		#Answer_key
		itAns = ET.SubElement(it, "answer_key")
		itAnsMat = ET.SubElement(itAns, "answer_key_material")
		itAnsMatFlow = ET.SubElement(itAnsMat, "flow_mat")
		itAnsMatFlowMat = ET.SubElement(itAnsMatFlow, "material")
		itAnsMatFlowMatText = ET.SubElement(itAnsMatFlowMat, "mattext", {'texttype': 'text/html'})
		itAnsMatFlowMatText.append(CDATA(question.get_answers()[0].text))

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
		if question.hint is not None:
			self.generate_hint(it, question.hint)

		#Resprocessing Node
		itRes = ET.SubElement(it, "resprocessing")

		#Resprocessing -> Outcomes
		itResOut = ET.SubElement(itRes, "outcomes")
		itResOutDecCorrect = ET.SubElement(itResOut, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Correct', 'minvalue': '0', 'maxvalue': '100'})
		itResOutDecIncorrect = ET.SubElement(itResOut, "decvar", {'vartype': 'Integer', 'defaultval': '0', 'varname': 'D2L_Incorrect', 'minvalue': '0', 'maxvalue': '100'})
		itResOutDecScore = ET.SubElement(itResOut, "decvar", {'vartype': 'Decimal', 'defaultval': '0', 'varname': 'que_score', 'minvalue': '0', 'maxvalue': '100'})

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
		it_pre_flow_res_grp_ren = ET.Element("render_choice", {'shuffle': ('yes' if question.randomize_answers else 'no')})
		it_pre_flow_res_grp_ren_flow = ET.SubElement(it_pre_flow_res_grp_ren, "flow_label", {'class': 'Block'})

		respconditionString = "<group>"

		index = 1
		for answer in question.get_answers():

			questionAnswerIndex = question_ident_answer + str(index) 

			itGrpRenFlowLab = ET.SubElement(it_pre_flow_res_grp_ren_flow, "response_label", {'ident': questionAnswerIndex })
			itGrpRenFlowLabFlow = ET.SubElement(itGrpRenFlowLab, "flow_mat")
			itGrpRenFlowLabFlowMat = ET.SubElement(itGrpRenFlowLabFlow, "material")
			itGrpRenFlowLabFlowMatText = ET.SubElement(itGrpRenFlowLabFlowMat, "mattext", {'texttype': 'text/html'})
			itGrpRenFlowLabFlowMatText.append(CDATA(answer.match_right))
			index +=1

			itRespcondition = ET.Element("respcondition")
			itRespconditionvar = ET.SubElement(itRespcondition, "conditionvar")
			itRespconditionvarqual = ET.SubElement(itRespconditionvar, "varequal", {'respident': '##question_lid##'})
			itRespconditionvarqual.text = questionAnswerIndex
			itRespsetvar = ET.SubElement(itRespcondition, "setvar", {'varname': 'D2L_Incorrect', 'action': 'Add'})
			itRespsetvar.text = "1"

			respconditionString += ET.tostring(itRespcondition, 'utf-8').decode("utf-8") + "\n"

		respconditionString += "</group>"

		index = 1
		for answer in question.get_answers():

			questionIndex = question_lid + str(index)
			questionAnswerIndex = question_ident_answer + str(index)

			#Presentation -> Flow -> Response_grp
			it_pre_flow_res_grp = ET.SubElement(it_pre_flow, "response_grp", {'respident': questionIndex, 'rcardinality': 'Single'})
			
			#Presentation -> Flow -> Response_grp -> Material
			it_pre_flow_res_grp_mat = ET.SubElement(it_pre_flow_res_grp, "material")
			it_pre_flow_res_grp_mattext = ET.SubElement(it_pre_flow_res_grp_mat, "mattext", {'texttype': 'text/html'})
			it_pre_flow_res_grp_mattext.append(CDATA(answer.match_left))

			#Presentation -> Flow -> Response_grp -> Render_choice
			it_pre_flow_res_grp.append(it_pre_flow_res_grp_ren)

			respconditionElemString = respconditionString.replace("##question_lid##", questionIndex)
			respconditionElemString = re.sub(r'(<respcondition.*?' + questionAnswerIndex + r'.*?)(D2L_Incorrect)(.*?<\/respcondition>)', r'\1D2L_Correct\3', respconditionElemString, re.MULTILINE)
			respconditionElemString = respconditionElemString.replace("\n", "")
			
			elem = ET.fromstring(respconditionElemString)
			itRes.extend(list(elem))
			index +=1


		itRespcondition = ET.SubElement(itRes, "respcondition")
		itRespconditionvar = ET.SubElement(itRespcondition, "conditionvar")
		itRespconditionvarother = ET.SubElement(itRespconditionvar, "other")
		itRespsetvar = ET.SubElement(itRespcondition, "setvar", {'varname': 'que_score', 'action': 'Set'})
		itRespsetvar.text = "D2L_Correct"


		#Add General feedback
		self.generate_feedback(it, question_ident, question.question_feedback)