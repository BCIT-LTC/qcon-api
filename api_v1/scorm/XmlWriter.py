import os
import shutil
import datetime
import re
import xml.etree.cElementTree as ET
from uuid import UUID
from api_v1.scorm.xmlcdata import CDATA
from django.conf import settings
from xml.dom.minidom import parseString

class XmlWriter():


	def __init__(self, questions) :

		ident = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		sectionIdent = 'SECT_' + ident
		questionLibraryIdent = 'QLIB_' + ident


		self.questionFolder = "questionFolder"
		self.imageFolder = "imageFolder"
		self.imageLocalFolder = "imageLocalFolder"

		self.root = ET.Element("questestinterop")
		self.objectbank = ET.SubElement(self.root, "objectbank", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': questionLibraryIdent})
		self.section = ET.SubElement(self.objectbank, "section", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': sectionIdent, 'title': self.questionFolder})
		self.sectionPresentationMaterial()
		self.sectionProcExtension()

		self.questions = questions
		self.parseQuestion(questions)

		# self.questionFolder = questionLibraryEntity.questionFolder
		# self.imageFolder = questionLibraryEntity.imageFolder
		# self.imageLocalFolder = questionLibraryEntity.imageLocalFolder

		# self.root = ET.Element("questestinterop")
		# self.objectbank = ET.SubElement(self.root, "objectbank", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': questionLibraryIdent})
		# self.section = ET.SubElement(self.objectbank, "section", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'ident': sectionIdent, 'title': self.questionFolder})
		# self.sectionPresentationMaterial()
		# self.sectionProcExtension()

		# self.questions = questions
		# self.parseQuestion(questions)

	def getXml(self) :
		self.debug()
		return None

	def debug(self) :
		rough_string = ET.tostring(self.root, 'utf-8')
		reparsed = parseString(rough_string)
		print(reparsed.toprettyxml(indent="\t"))
		# sys.exit()
		
	def parseQuestion(self, questions) :
		identPrefix = int(datetime.date.today().strftime("%y%m%d")) + int(UUID(int=0x12345678123456781234567812345678))
		index = 1
		for questionEntity in questions:
			
			ident = str(identPrefix + index)
			questionIdent = 'QUES_' + ident

			titlePrefix = ''

			
			questionText = questionEntity.questionbody
			if isinstance(questionEntity.questionbody, list) :
				questionText = " ".join(questionEntity.questionbody)

			title = titlePrefix + str(questionEntity.title if questionEntity.title is not None else questionText)
			
			it = ET.Element("item", {'ident': 'OBJ_' + ident, 'label': questionIdent, 'd2l_2p0:page': '1', 'title': title})

			if questionEntity.question_type == 'MC':
				self.multipleChoice(it, questionIdent, questionEntity)
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
			# elif questionEntity.question_type == questionEntity.QUESTION_TYPE_TRUE_FALSE:
			# 	self.trueFalse(it, questionIdent, questionEntity)

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


	def multipleChoice(self, it, questionIdent, questionEntity) :
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
		questionText = questionEntity.questionbody #+ self.getElementImage(questionEntity)
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
		itPreFlowLidRen = ET.SubElement(itPreFlowLid, "render_choice", {'shuffle': ('yes' if questionEntity.randomizeAnswers else 'no')})

		#Add hint
		if questionEntity.hint is not None:
			self.generateHint(it, questionEntity.hint)

		#Reprocessing
		itRes = ET.SubElement(it, "resprocessing")

		#Add General feedback
		self.generateFeedback(it, questionIdent, questionEntity.feedback)

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
			itResSetVar.text = '100.0000' if questionAnswerEntity.isCorrect == True else '0.0000'
			itResDis = ET.SubElement(itResCon, "displayfeedback", {'feedbacktype' : 'Response', 'linkrefid': questionFeedBackIdent + str(index)})

			#Add Answer specific feedback
			self.generateFeedback(it, questionFeedBackIdent + str(index), questionAnswerEntity.feedback)
			index += 1

