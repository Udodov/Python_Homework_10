import csv
import json
import xml.etree.ElementTree as ET


class Converter:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def convert(self):
        raise NotImplementedError("Конвертация должна быть реализована в подклассе.")


class CsvToTxtConverter(Converter):
    def convert(self):
        with open(self.input_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            contacts = list(reader)

        with open(self.output_filename, 'w', encoding='utf-8') as txtfile:
            for contact in contacts:
                txtfile.write(', '.join(contact) + '\n')


class CsvToXmlConverter(Converter):
    def convert(self):
        root = ET.Element('Phonebook')

        with open(self.input_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)

            for row in reader:
                contact = ET.SubElement(root, 'Contact')
                for i, header in enumerate(headers):
                    child = ET.SubElement(contact, header)
                    child.text = row[i]

        tree = ET.ElementTree(root)
        tree.write(self.output_filename, encoding='utf-8', xml_declaration=True)


class CsvToJsonConverter(Converter):
    def convert(self):
        with open(self.input_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(self.output_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)


class CsvToHtmlConverter(Converter):
    def convert(self):
        with open(self.input_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)

            with open(self.output_filename, 'w', encoding='utf-8') as htmlfile:
                htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Phonebook</title>\n</head>\n<body>\n')
                htmlfile.write('<table border="1">\n<tr>\n')

                for header in headers:
                    htmlfile.write(f'<th>{header}</th>\n')

                htmlfile.write('</tr>\n')

                for row in reader:
                    htmlfile.write('<tr>\n')
                    for cell in row:
                        htmlfile.write(f'<td>{cell}</td>\n')
                    htmlfile.write('</tr>\n')

                htmlfile.write('</table>\n</body>\n</html>')
