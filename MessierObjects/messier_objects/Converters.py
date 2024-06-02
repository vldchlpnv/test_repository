class Regex:

    regex = r'M[0-9]{1,3}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

class DateConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value