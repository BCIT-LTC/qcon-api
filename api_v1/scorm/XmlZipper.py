import xml.etree.cElementTree as ET
import logging

from zipfile import *
from os.path import basename
from os import makedirs, path, walk
from shutil import rmtree
from django.conf import settings
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity

class XmlZipper():

	def createManifest(manifestEntity, folderPath):

		path = folderPath + '/imsmanifest.xml'
		root = ET.Element("manifest", {'xmlns:d2l_2p0':'http://desire2learn.com/xsd/d2lcp_v2p0', 'xmlns': 'http://www.imsglobal.org/xsd/imscp_v1p1', 'identifier': 'MANIFEST_1'})
		doc = ET.SubElement(root, "resources")

		for resource in manifestEntity.resources:
			ET.SubElement(doc, "resource", {'identifier':resource.identifier, 'type': resource.resourceType, 'd2l_2p0:material_type': resource.materialType, 
				'href': resource.href, 'd2l_2p0:link_target' : resource.linkTarget,
				'title' : resource.title})

		tree = ET.ElementTree(root)
		tree.write(path)


	def createQuestionLibrary(questionLibraryEntity, parsedQuestionsXml):

		try:
			folderPath = settings.QCON['RESPONDUS_XML_ROOT'] + questionLibraryEntity.zipFileName
			zipPath = settings.QCON['RESPONDUS_XML_ROOT'] + questionLibraryEntity.zipFileName + '.zip'

			if not path.exists(folderPath):
				makedirs(folderPath)
			
			questionXMLPath = folderPath + '/questiondb.xml'
			manifestXMLPath = folderPath + '/imsmanifest.xml'
			manifestEntity = ManifestEntity()
			manifestResource = ManifestResourceEntity('res_question_library', 'webcontent', 'd2lquestionlibrary', 'questiondb.xml', 'Question Library')
			manifestEntity.addResource(manifestResource)
			XmlZipper.createManifest(manifestEntity, folderPath)
			tree = ET.ElementTree(parsedQuestionsXml)
			tree.write(questionXMLPath)
			with ZipFile(zipPath, 'w') as myzip:
				myzip.write(questionXMLPath, basename(questionXMLPath))
				myzip.write(manifestXMLPath, basename(manifestXMLPath))
				for root, dirs, files in walk(questionLibraryEntity.imageLocalFolder) :
					for filename in files :
						myzip.write(path.join(root, filename), questionLibraryEntity.imageFolder + '/' + filename)
			
			if path.exists(folderPath):	
				rmtree(folderPath)

			if path.exists(questionLibraryEntity.imageLocalFolder):	
				rmtree(questionLibraryEntity.imageLocalFolder)

			# return QuestionLibraryResponseEntity(status=True, zipUrl=questionLibraryEntity.zipFileName + '.zip')

		except Exception as e:
			pass
			print(e)
			# TODO CREATE ERROR MESSAGE FOR ZIPPING ERROR
			# return QuestionLibraryResponseEntity(status=False, message=str(e))
