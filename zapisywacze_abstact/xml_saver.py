import xml.etree.ElementTree as ET
from zapisywacze_abstact.DataSaver import DataSaver


class XMLSaver(DataSaver):
    def save_data(self, data, file_path):
        root = ET.Element("Data")
        for position in data:
            element = ET.SubElement(root, "Position")
            for k, v in position.items():
                sub_element = ET.SubElement(element, k)
                sub_element.text = str(v)
        tree = ET.ElementTree(root)
        tree.write(file_path)
