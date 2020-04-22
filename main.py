from lxml import html, etree


# Constant definitions
def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)


class XPathQuery(object):
    @constant
    def GET_LESSONS() -> str:
        return '/timetable/dayOfWeek/subject/@name'

    @constant
    def GET_AUDIENCE():
        return '/timetable/dayOfWeek/subject/auditory/text()'

    @constant
    def GET_PRACTICALS():
        return '/timetable/dayOfWeek/subject[type="Практика"]/@name'

    @constant
    def GET_LECTURES_FROM_239():
        return '/timetable/dayOfWeek/subject[type="Лекция" and auditory="239 (2 корпус, 2 этаж)"]/@name'

    @constant
    def GET_TEACHERS_FROM_239():
        return '/timetable/dayOfWeek/subject[auditory="239 (2 корпус, 2 этаж)"]/lecturer/@name'

    @constant
    def GET_LAST_LESSONS():
        return '/timetable/dayOfWeek/subject[last()]/@name'

    @constant
    def GET_LESSONS_COUNT():
        return 'count(/timetable/dayOfWeek/subject)'


QUERIES = XPathQuery()


def do_xPath_queries(tree: etree):
    lessons = tree.xpath(QUERIES.GET_LESSONS)
    print('All lessons: {}'.format(lessons))

    audience = tree.xpath(QUERIES.GET_AUDIENCE)
    print('Audience: {}'.format(audience))

    practicals = tree.xpath(QUERIES.GET_PRACTICALS)
    print('Practicals: {}'.format(practicals))

    lectures = tree.xpath(QUERIES.GET_LECTURES_FROM_239)
    print('Lectures from 239: {}'.format(lectures))

    teachers = tree.xpath(QUERIES.GET_TEACHERS_FROM_239)
    print('Teachers from 239: {}'.format(teachers))

    last_lessons = tree.xpath(QUERIES.GET_LAST_LESSONS)
    print('Last lessons: {}'.format(last_lessons))

    lessons_count = int(tree.xpath(QUERIES.GET_LESSONS_COUNT))
    print('Lessons count: {}'.format(lessons_count))


# XSLT to TXT
def xml_to_txt(source: bytes) -> str:
    xslt_to_txt_tree = etree.XML(source)
    xslt_to_txt_transform = etree.XSLT(xslt_to_txt_tree)
    return xslt_to_txt_transform(doc_root)


# XSLT to HTML
def xml_to_html(source: bytes) -> str:
    xslt_to_html_tree = etree.XML(source)
    xslt_to_html_transform = etree.XSLT(xslt_to_html_tree)
    return xslt_to_html_transform(doc_root)


if __name__ == '__main__':
    with open('data/timetable.xml', 'r') as xml_file:
        xml_file_content = xml_file.read()
        xml_tree = html.fromstring(xml_file_content)
        doc_root = etree.XML(xml_file_content)

        # XSLT to TXT
        with open('data/xml_to_txt.xslt', 'rb') as xslt_to_txt_file:
            xslt_to_txt_file_content = xslt_to_txt_file.read()
            xslt_to_txt_result = xml_to_txt(xslt_to_txt_file_content)
            with open('dist/xslt_to_txt.txt', 'w') as xslt_to_txt_result_file:
                xslt_to_txt_result_file.write('{}'.format(xslt_to_txt_result))

        # XSLT to HTML
        with open('data/xml_to_html.xslt', 'rb') as xslt_to_html_file:
            xslt_to_html_file_content = xslt_to_html_file.read()
            xslt_to_html_result = xml_to_txt(xslt_to_html_file_content)
            with open('dist/xslt_to_html.html', 'w') as xslt_to_html_result_file:
                xslt_to_html_result_file.write('{}'.format(xslt_to_html_result))

        # Do xPath queries
        do_xPath_queries(xml_tree)
