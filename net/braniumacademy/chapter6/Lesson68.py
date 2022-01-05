import xml.etree.ElementTree as et

from net.braniumacademy.chapter6.student import FullName, Address, Student


def create_student(sid, gpa, first, mid, last, age, major):
    full_name = FullName(first, mid, last)
    address = Address('Giáp Bát', 'Hoàng Mai', 'Hà Nội')
    return Student(sid, full_name, age, major, address, gpa)


def create_student_xml(student):
    root = et.Element('students')
    new_element = et.SubElement(root, 'student')
    et.SubElement(new_element, 'id').text = student.student_id
    et.SubElement(new_element, 'age').text = str(student.age)
    et.SubElement(new_element, 'major').text = student.major
    et.SubElement(new_element, 'gpa').text = str(student.gpa)
    address = et.SubElement(new_element, 'address')
    et.SubElement(address, 'wards').text = student.address.wards
    et.SubElement(address, 'district').text = student.address.district
    et.SubElement(address, 'city').text = student.address.city
    full_name = et.SubElement(new_element, 'full_name')
    et.SubElement(full_name, 'first').text = student.full_name.first
    et.SubElement(full_name, 'mid').text = student.full_name.mid
    et.SubElement(full_name, 'last').text = student.full_name.last
    et.indent(root, space='\t')
    return str(et.tostring(root, encoding='UTF-8', xml_declaration=True), 'UTF-8')


def update_xml(file_name):
    tree = et.parse(file_name)
    root = tree.getroot()
    student = create_student('SV002', 3.87, 'Linh', 'Mai', 'Trần', 20, 'CNTT')
    new_element = et.Element('student')
    et.SubElement(new_element, 'id').text = student.student_id
    et.SubElement(new_element, 'age').text = str(student.age)
    et.SubElement(new_element, 'major').text = student.major
    et.SubElement(new_element, 'gpa').text = str(student.gpa)
    address = et.SubElement(new_element, 'address')
    et.SubElement(address, 'wards').text = student.address.wards
    et.SubElement(address, 'district').text = student.address.district
    et.SubElement(address, 'city').text = student.address.city
    full_name = et.SubElement(new_element, 'full_name')
    et.SubElement(full_name, 'first').text = student.full_name.first
    et.SubElement(full_name, 'mid').text = student.full_name.mid
    et.SubElement(full_name, 'last').text = student.full_name.last
    root.append(new_element)
    et.indent(root, space='\t')
    tree.write(file_name, encoding='UTF-8')
    

def write_xml_file(data, file_name):
    with open(file_name, 'w', encoding='UTF-8') as xml_writer:
        xml_writer.write(data)


if __name__ == '__main__':
    update_xml('output_student.xml')
    s = create_student('SV001', 3.56, 'Thanh', 'Văn', 'Hoàng', 20, 'CNTT')
    xml_data = create_student_xml(s)
    write_xml_file(xml_data, 'output_student.xml')
