import os
import re
import xml.etree.cElementTree as ET

fileNames = os.listdir('data/')
urls = []
for fileName in fileNames:
	new_f = re.sub(r"', '", "/", fileName)
	new_f = re.sub(r"\['", "", new_f)
	new_f = re.sub(r"'\].txt","",new_f)
	urls.append(new_f)

for i in range(0, len(fileNames)):
	add = ET.Element("add")
	doc = ET.SubElement(add, "doc")

	field1 = ET.SubElement(doc, "field")
	field1.set("name","id")
	field1.text = urls[i]

#	field2 = ET.SubElement(doc, "field")
#	field2.set("name","url")
#	field2.text = urls[i]

	field3 = ET.SubElement(doc, "field")
	field3.set("name","links")
	field3.text = urls[i]

	field4 = ET.SubElement(doc, "field")
	field4.set("name","content")
	# open file
	raw = open('data/' + fileNames[i]).read()
	text = raw.decode('utf-8').encode('ascii','ignore')
	field4.text = text

	names = urls[i].split('/')
	names.remove("http:")
	names.remove("")
	names.remove("leagueoflegends.wikia.com")
	name = '.'.join(names)
	
	field3 = ET.SubElement(doc, "field")
	field3.set("name","title")
	field3.text = name


	tree = ET.ElementTree(add)
	tree.write('xmlData/' + name + '.xml')
