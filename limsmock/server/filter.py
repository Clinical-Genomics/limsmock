from pathlib import Path
import xml.etree.ElementTree as ET
import requests


class Filter:
    # remaining is to handle unioon of combinations when many process types or inputs are given
    def __init__(self, file_path: str, params: list, entity_type: dict, base_uri: str):
        self.file_path = Path(file_path)
        self.params = params
        self.entity_type = entity_type
        self.base_uri = base_uri
        self.udf_tag = '{http://genologics.com/ri/userdefined}field'
        self.related_entity_tags = ['project', 'submitter', 'artifact', 'reagent-label']  # handlde these

    def _parse(self, root):
        parsed_xml = []
        for child in root.iter():
            if child.tag == self.udf_tag:
                udf = child.attrib.get('name')
                parsed_xml.append( (f"udf.{udf}", child.text) )
            elif child.tag in self.related_entity_tags:
                continue
            elif child.tag == 'input':
                parsed_xml.append(('inputartifactlimsid', child.attrib.get('limsid')))
            elif child.tag == 'parent-process':
                uri = child.attrib.get('uri')
                r = requests.get(uri)
                tree = ET.fromstring(r.content)
                parsed_xml.append(('process-type', tree.findall('type')[0].text))
            elif child.tag == 'sample':
                parsed_xml.append(('samplelimsid', child.attrib.get('limsid')))
            else:
                parsed_xml.append((child.tag, child.text))
        return parsed_xml

    def _filter(self, root):
        parsed_xml = self._parse(root)
        if set(self.params) <= set(parsed_xml):
            return True
        return False

    def make_entity_xml(self):
        entitiy_xml = [
            f'<smp:{self.entity_type["plur"]} xmlns:smp="http://genologics.com/ri/{self.entity_type["sing"]}">']
        for file in self.file_path.glob('*.xml'):
            entity_id = file.stem
            tree = ET.parse(file)
            root = tree.getroot()
            if self._filter(root):
                path = f'<{self.entity_type["sing"]} uri="{self.base_uri}/api/v2/{self.entity_type["plur"]}/{entity_id}" limsid="{entity_id}"/>'
                entitiy_xml.append(path)
        entitiy_xml.append(f'</smp:{self.entity_type["plur"]}>')
        return '\n'.join(entitiy_xml)
