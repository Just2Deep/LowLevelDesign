import json

from xml_provider import XMLDataProvider
from reports import IReport


class XMLProviderAdapter(IReport):
    def __init__(self, xml_provider: XMLDataProvider):
        self.xml_provider = xml_provider

    def get_data(self, base_data: str = ""):
        # Convert XML data to a dictionary format
        xml_data = self.xml_provider.get_data(base_data)
        return self._parse_xml_to_dict(xml_data)

    def _parse_xml_to_dict(self, xml_data):
        import xml.etree.ElementTree as ET

        root = ET.fromstring(xml_data)
        return {child.tag: child.text for child in root}

    def get_json_data(self, base_data: str = ""):
        data_dict = self.get_data(base_data)
        return json.dumps(data_dict, indent=4)
