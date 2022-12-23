import subprocess
from lxml import etree, objectify
import json, xmltodict
from subprocess import check_output


def DTD_validation(file_XML, file_DTD):
    try:
        dtd = etree.DTD(open(file_DTD, 'rb'))
        tree = objectify.parse(open(file_XML, 'rb'))
        if dtd.validate(tree):
            status = True
            msg = "Xml is Valid"
        else:
            status = False
            msg = dtd.error_log.filter_from_errors()[0]
        return status, msg
    except Exception as e:    
            status = False
            msg = str(e)
            return status,msg


def XSD_Validate(xml_path, xsd_path) -> bool:
    try:
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        xml_doc = etree.parse(xml_path)

        if xmlschema.validate(xml_doc):
            status = True
            msg = "Xml is Valid"
        else:
            status = False
            msg = xmlschema.error_log.filter_from_errors()[0]
        return status, msg
    except Exception as e:    
            status = False
            msg = str(e)
            return status,msg


def xml_to_json(xml_file):
    try:
        with open(xml_file) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())

            # generate the object using json.dumps() corresponding to json data
            json_data = json.dumps(data_dict, indent=4)

            with open("media/data.json", "w") as json_file:
                json_file.write(json_data)

        return json_data
    except Exception as e:        
        return str(e)


def xslt_transformer_to_html(xml_file, xslt_file):
    try:
        xslt_doc = etree.parse(xslt_file)
        xslt_transformer = etree.XSLT(xslt_doc)

        source_doc = etree.parse(xml_file)
        output_doc = xslt_transformer(source_doc)

        output_doc.write("templates/output-toc.html", pretty_print=True)

        return True,"output-toc.html"
    except Exception as e:        
        return False,str(e)

#https://www.w3.org/2000/04/schema_hack/
def DTD_to_XSD(dtd_file):
    try:
        #Exécutez la commande avec des arguments et renvoyez sa sortie.
        out = check_output(
            ["perl", "xmlproject/dtd2xsd/dtd2xsd.pl", dtd_file],
            stdin=subprocess.PIPE).decode("utf-8")
    except Exception as e:
        out = str(e)
    return out
