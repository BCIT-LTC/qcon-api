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

	def __init__(self, questionLibraryEntity, questions) :

		ident = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		sectionIdent = 'SECT_' + ident
		questionLibraryIdent = 'QLIB_' + ident

		self.root = ET.Element("questestinterop")
		self.objectbank = ET.SubElement(self.root, "objectbank", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': questionLibraryIdent})
		self.section = ET.SubElement(self.objectbank, "section", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': sectionIdent, 'title': questionLibraryEntity.sectionFolderName})
		self.sectionPresentationMaterial()
		self.sectionProcExtension()

		self.questions = questions
		self.parseQuestion(questions)

		self.xml_string = self.xml_to_string(self.root)


	def xml_to_string(self, xml) :
		rough_string = ET.tostring(xml, 'utf-8')
		reparsed = parseString(rough_string)
		pretty_xml = reparsed.toprettyxml(indent="\t")
		return pretty_xml
		# sys.exit()
		
	def parseQuestion(self, questions) :
		identPrefix = int(datetime.date.today().strftime("%y%m%d")) + int(UUID(int=0x12345678123456781234567812345678))
		index = 1
		for questionEntity in questions:
			
			ident = str(identPrefix + index)
			questionIdent = 'QUES_' + ident

			titlePrefix = ''

			
			questionText = questionEntity.question_body
			if isinstance(questionEntity.question_body, list) :
				questionText = " ".join(questionEntity.question_body)
			plain_text = pypandoc.convert_text(questionText, format="html", to="plain").replace('\n', ' ')
			title = titlePrefix + str(questionEntity.title if questionEntity.title is not None else plain_text)
			
			it = ET.Element("item", {'ident': 'OBJ_' + ident, 'label': questionIdent, 'd2l_2p0:page': '1', 'title': title})

			if questionEntity.question_type == 'MC':
				self.generateMultipleChoice(it, questionIdent, questionEntity)
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_MULTI_SELECT:
			# 	self.multiSelect(it, questionIdent, questionEntity)
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_FILL_IN_BLANK:
			# 	self.fillInTheBlanks(it, questionIdent, questionEntity)
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_ORDERING:
			# 	self.ordering(it, questionIdent, questionEntity)
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_LONG_ANSWER:
			# 	self.longAnswer(it, questionIdent, questionEntity)	
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_MATCHING:
			# 	self.matching(it, questionIdent, questionEntity)
			elif questionEntity.question_type == 'TF':
				self.generateTrueFalse(it, questionIdent, questionEntity)

			self.section.append(it)
			index +=1
		pass



	def sectionPresentationMaterial(self) :
		#presentation_material Node
		secPresMat = ET.SubElement(self.section, "presentation_material")
		secPresMatFlo = ET.SubElement(secPresMat, "flow_mat")
		secPresMatFloFlo = ET.SubElement(secPresMatFlo, "flow_mat")
		secPresMatFloFloMat = ET.SubElement(secPresMatFloFlo, "material")
		secPresMatFloFloMatText = ET.SubElement(secPresMatFloFlo, "mattext", {'texttype': 'text/html'})


	def sectionProcExtension(self) :
		#presentation_material Node
		secProc = ET.SubElement(self.section, "sectionproc_extension")
		secProcDisName = ET.SubElement(secProc, "d2l_2p0:display_section_name")
		secProcDisName.text = 'yes'
		secProcDisLine = ET.SubElement(secProc, "d2l_2p0:display_section_line")
		secProcDisLine.text = 'no'
		secProcDisSec = ET.SubElement(secProc, "d2l_2p0:type_display_section")
		secProcDisSec.text = '1'


	def itemDataNode(self, it, questionType, questionEntity) :
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
		itWeightingEntry.text = "{:.4f}".format(float(questionEntity.points)) if questionEntity.points else "1"


	def itemprocExtension(self, it) :
		#Itemproc_extension Node
		itProc = ET.SubElement(it, "itemproc_extension")
		itProcDifficulty = ET.SubElement(itProc, "d2l_2p0:difficulty")
		itProcDifficulty.text = '1'
		itProcIsBonus = ET.SubElement(itProc, "d2l_2p0:isbonus")
		itProcIsBonus.text = 'no'
		itProcIsMandatory = ET.SubElement(itProc, "d2l_2p0:ismandatory")
		itProcIsMandatory.text = 'no'


	def generateFeedback(self, it, ident, feedback) :
		itFB = ET.SubElement(it, "itemfeedback", {'ident': ident})
		itFBMat = ET.SubElement(itFB, "material")
		itFBMatText = ET.SubElement(itFBMat, "mattext", {'texttype' : 'text/html'})
		if feedback is not None:
			itFBMatText.append(CDATA(feedback))


	def generateHint(self, it, hint) :
		itHint = ET.SubElement(it, "hint")
		itHintMat = ET.SubElement(itHint, "hintmaterial")
		itHintMatFlow = ET.SubElement(itHintMat, "flow_mat")
		itHintMatFlowMat = ET.SubElement(itHintMatFlow, "material")
		itHintMatFlowText = ET.SubElement(itHintMatFlowMat, "mattext", {'texttype': 'text/html'})
		itHintMatFlowText.append(CDATA(hint))


	def generateMultipleChoice(self, it, questionIdent, questionEntity) :
		self.itemDataNode(it, 'Multiple Choice', questionEntity)
		self.itemprocExtension(it)

		questionLid = questionIdent + '_LID'
		questionAnswerIdent = questionIdent + '_A'
		questionFeedBackIdent = questionIdent + '_IF'

		#Presentation Node
		itPre = ET.SubElement(it, "presentation")
		itPreFlow = ET.SubElement(itPre, "flow")

		#Presentation -> Flow
		itPreFlowMat = ET.SubElement(itPreFlow, "material")

		#Presentation -> Material
		itPreFlowMatText = ET.SubElement(itPreFlowMat, "mattext", {'texttype': 'text/html'})
		questionText = questionEntity.question_body #+ self.getElementImage(questionEntity)
		itPreFlowMatText.append(CDATA(questionText))

		#Presentation -> Flow -> Response_extension
		itPreFlowRes = ET.SubElement(itPreFlow, "response_extension")
		itPreFlowResDisplayStyle = ET.SubElement(itPreFlowRes, "d2l_2p0:display_style")
		itPreFlowResDisplayStyle.text = '2'
		itPreFlowResEnumeration = ET.SubElement(itPreFlowRes, "d2l_2p0:enumeration")
		itPreFlowResEnumeration.text = '4'
		itPreFlowResGradingType = ET.SubElement(itPreFlowRes, "d2l_2p0:grading_type")
		itPreFlowResGradingType.text = '0'

		#Presentation -> Flow -> Response_lid
		itPreFlowLid = ET.SubElement(itPreFlow, "response_lid", {'ident': questionLid, 'rcardinality': 'Multiple'})

		# Commented this to deactivate MC randomized answer order
		itPreFlowLidRen = ET.SubElement(itPreFlowLid, "render_choice", {'shuffle': ('yes' if questionEntity.randomize_answers else 'no')})

		#Add hint
		if questionEntity.hint is not None:
			self.generateHint(it, questionEntity.hint)

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")

		#Add General feedback
		self.generateFeedback(it, questionIdent, questionEntity.question_feedback)

		index = 1
		for questionAnswerEntity in questionEntity.answers:

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(itPreFlowLidRen, "flow_label", {'class': 'Block'})
			responseLabel = ET.SubElement(flow, "response_label", {'ident': questionAnswerIdent + str(index)})
			flowMat = ET.SubElement(responseLabel, "flow_mat")
			material = ET.SubElement(flowMat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.append(CDATA(questionAnswerEntity.answer_body))

			#Reprocessing -> Respcondition
			itResCon = ET.SubElement(itRes, "respcondition", {'title': 'Response Condition' + str(index)})
			itResConVar = ET.SubElement(itResCon, "conditionvar")
			itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'respident': questionLid})
			itResConVarEqual.text = questionAnswerIdent + str(index)
			itResSetVar = ET.SubElement(itResCon, "setvar", {'action' : 'Set'})
			itResSetVar.text = '100.0000' if questionAnswerEntity.is_correct == True else '0.0000'
			itResDis = ET.SubElement(itResCon, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': questionFeedBackIdent + str(index)})

			#Add Answer specific feedback
			self.generateFeedback(it, questionFeedBackIdent + str(index), questionAnswerEntity.answer_feedback)
			index += 1


	def generateTrueFalse(self, it, questionIdent, questionEntity) :
		
		self.itemDataNode(it, 'True/False', questionEntity)
		self.itemprocExtension(it)

		questionLid = questionIdent + '_LID'
		questionAnswerIdent = questionIdent + '_A'
		questionFeedBackIdent = questionIdent + '_IF'

		#Presentation Node
		itPre = ET.SubElement(it, "presentation")
		itPreFlow = ET.SubElement(itPre, "flow")

		#Presentation -> Flow
		itPreFlowMat = ET.SubElement(itPreFlow, "material")

		#Presentation -> Material
		itPreFlowMatText = ET.SubElement(itPreFlowMat, "mattext", {'texttype': 'text/html'})
		questionText = questionEntity.question_body #+ self.getElementImage(questionEntity)
		itPreFlowMatText.append(CDATA(questionText))

		#Presentation -> Flow -> Response_extension
		itPreFlowRes = ET.SubElement(itPreFlow, "response_extension")
		itPreFlowResDisplayStyle = ET.SubElement(itPreFlowRes, "d2l_2p0:display_style")
		itPreFlowResDisplayStyle.text = '2'
		itPreFlowResEnumeration = ET.SubElement(itPreFlowRes, "d2l_2p0:enumeration")
		itPreFlowResEnumeration.text = '6'
		itPreFlowResGradingType = ET.SubElement(itPreFlowRes, "d2l_2p0:grading_type")
		itPreFlowResGradingType.text = '0'

		#Presentation -> Flow -> Response_lid
		itPreFlowLid = ET.SubElement(itPreFlow, "response_lid", {'ident': questionLid, 'rcardinality': 'Single'})
		itPreFlowLidRen = ET.SubElement(itPreFlowLid, "render_choice", {'shuffle': ('yes' if questionEntity.randomize_answers else 'no')})	

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")

		#Add General feedback
		self.generateFeedback(it, questionIdent, questionEntity.question_feedback)

		index = 1
		for questionAnswerEntity in questionEntity.answers:

			#Presentation -> Flow -> Response_lid -> Render_choice -> Flow_label
			flow = ET.SubElement(itPreFlowLidRen, "flow_label", {'class': 'Block'})
			responseLabel = ET.SubElement(flow, "response_label", {'ident': questionAnswerIdent + str(index)})
			flowMat = ET.SubElement(responseLabel, "flow_mat")
			material = ET.SubElement(flowMat, "material")
			mattext = ET.SubElement(material, "mattext", {'texttype': 'text/html'})
			mattext.text = questionAnswerEntity.answer_body.replace("<p>", "").replace("</p>", "").strip()

			#Reprocessing -> Respcondition
			itResCon = ET.SubElement(itRes, "respcondition", {'title': 'Response Condition' + str(index)})
			itResConVar = ET.SubElement(itResCon, "conditionvar")
			itResConVarEqual = ET.SubElement(itResConVar, "varequal", {'respident': questionLid})
			itResConVarEqual.text = questionAnswerIdent + str(index)
			itResSetVar = ET.SubElement(itResCon, "setvar", {'action' : 'Set'})
			itResSetVar.text = '100.0000' if questionAnswerEntity.is_correct == True else '0.0000'
			itResDis = ET.SubElement(itResCon, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': questionFeedBackIdent + str(index)})

			#Add Answer specific feedback
			self.generateFeedback(it, questionFeedBackIdent + str(index), questionAnswerEntity.answer_feedback)
			index += 1