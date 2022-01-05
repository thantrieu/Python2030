import json


class Subject:
    def __init__(self, sid, name, credit, lesson):
        self.__subject_id = sid
        self.__name = name
        self.__credit = credit
        self.__lesson = lesson

    def __str__(self):
        return f'Subject[subject_id={self.__subject_id}, name={self.__name},' \
               f'credit={self.__credit}, lesson={self.__lesson}]'


def decode_subject(dct):
    if 'subject_id' in dct:
        subject_id = dct['subject_id']
        name = dct['subject_name']
        credit = int(dct['subject_credit'])
        lesson = int(dct['subject_lesson'])
        return Subject(subject_id, name, credit, lesson)
    else:
        return None


if __name__ == '__main__':
    source = 'data1.json'
    with open(source) as json_reader:
        data = json_reader.read()
        subject = json.loads(data, object_hook=decode_subject)
        print(subject)
