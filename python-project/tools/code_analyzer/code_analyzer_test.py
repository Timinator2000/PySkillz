###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '____tools____'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the ____tools____ folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


class CodeAnalyzer(pyskillz_tools.TechioInteraction):

    def __init__(self):
        super().__init__(__file__)


    def run(self):
        money_channel = pyskillz_tools.Channel(f'Lines of Code and Python Statements #️⃣', 'LOC#️⃣>')
        summary_channel = pyskillz_tools.Channel(f'Code Summary 🤔', 'Sum🤔>')
        details_channel = pyskillz_tools.Channel(f'Detailed Statement Breakdown (Nested) 🔍', 'Det🔍>')

        self.send_multiline_text(money_channel, self.get_code_analysis('basic_stats'))
        self.send_multiline_text(summary_channel, self.get_code_analysis('summary'))
        self.send_multiline_text(details_channel, self.get_code_analysis('details'))


if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    analyzer.run()