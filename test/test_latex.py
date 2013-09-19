'''
Test latex generator
'''

import unittest

if __name__ == "__main__":
    import sys
    sys.path.append("../src")

from tango.parser import Parser
from tango.processor import DocumentProcessor
from tango.processors import core
from tango.generators.latex.article import LatexArticleGenerator

class TestBasicLatex(unittest.TestCase):

    def test_basic_example(self):
        # 1) parsing
        
        parser = Parser()
        # BREAKPOINT >>> # import pdb; pdb.set_trace()  # <<< BREAKPOINT #
        doc = parser.parse_from_file("../examples/basic.tango.tex")

        # 2) processing
        processor = DocumentProcessor(doc)
        core.register_core_processors(processor)
        processor.process()

        # 3) generating
        generator = LatexArticleGenerator(doc)
        generator.generate()

        print("Output =\n" + str(generator.output))
        
        
if __name__ == '__main__':
    unittest.main()
