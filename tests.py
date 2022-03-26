from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):
    text_elements = ['john lennon', 'john winston ono lennon', 'are the songs he wrote',
                     'imagine', 'norwegian wood', 'come together', 'in my life', 'hey jude']

    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        if 'list of albums' in reply.lower():
            return CheckResult.wrong('The example in the Example section is for reference only.\n'
                                     'You need to print the raw markdown code of the snippet '
                                     'shown in the Objectives section.')

        reply = reply.strip().splitlines()
        while '' in reply:
            reply.remove('')
        for reply_line, text_element in zip(reply, self.text_elements):
            if text_element not in reply_line.lower():
                return CheckResult.wrong('The output of your program does not include all the lines from the text.\n'
                                         'You need to print the raw markdown code of the snippet '
                                         'shown in the Objectives section.')

        if reply[0].strip().lower().split() != ['#', 'john', 'lennon']:
            return CheckResult.wrong(f'Incorrect Markdown syntax for the heading:\n'
                                     f"'{reply[0]}'\n"
                                     f"To make a heading, use the hash sign (#).")
        elif reply[1].strip('. ').lower().split() != ['or', '***john', 'winston', 'ono', 'lennon***',
                                                      'was', 'one', 'of', '*the', 'beatles*']:
            return CheckResult.wrong(f'Incorrect Markdown syntax for the following line:\n'
                                     f"'{reply[1]}'\n"
                                     f"The phrase 'John Winston Ono Lennon' should be both bold and italic "
                                     f"and 'The Beatles' should be italic.")

        unordered_list = reply[3:]
        for item in unordered_list:
            if not item.startswith(('* ', '+ ', '- ')):
                return CheckResult.wrong(f'Incorrect Markdown syntax for an unordered list.\n'
                                         f'You need to use the -, *, or + symbol with a whitespace '
                                         f'in front of list items, for example:\n'
                                         f"'* Imagine'")

        last_line = '~~hey jude~~ (that was *mccartney*)'.split()
        for el in last_line[:2]:
            if el not in unordered_list[-1].strip().lower().split():
                return CheckResult.wrong(f'Incorrect Markdown syntax for the following line:\n'
                                         f"'{unordered_list[-1]}'\n"
                                         f"Most likely, you did not make the song title strikethrough.")
        if last_line[-1] not in unordered_list[-1].strip().lower().split():
            return CheckResult.wrong(f'Incorrect Markdown syntax for the following line:\n'
                                     f"'{unordered_list[-1]}'\n"
                                     f"Most likely, you did not make the name italic.")

        return CheckResult.correct()


if __name__ == '__main__':
    SumTest().run_tests()