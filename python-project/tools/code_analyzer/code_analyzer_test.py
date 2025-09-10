###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '----tools----'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the tools folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


class CodeAnalyzer(pyskillz_tools.TechioObject):

    def __init__(self):
        super().__init__(__file__)


    def run(self):
        summary = self.code_analysis
        money_channel = pyskillz_tools.Channel(f'Show Me the Money 💲', '$$$💲>')
        summary_channel = pyskillz_tools.Channel(f'Code Summary 🤔', 'Sum🤔>')
        details_channel = pyskillz_tools.Channel(f'Detailed Statement Breakdown (Nested) 🔍', 'Det🔍>')

        filename = summary["filename"]
        source = summary["source"]
        categories = summary["categories"]
        total_count = summary["total_count"]
        kept = summary["kept"]
        skipped = summary["skipped"]
        total_lines = summary["total_lines"]
        non_blank_lines = summary["non_blank_lines"]
        comment_lines = summary["comment_lines"]
        effective_code_lines = summary["effective_code_lines"]

        self.send_msg(money_channel, f"Lines of Code : {effective_code_lines}")
        self.send_msg(money_channel, f"Statements    : {total_count}")

        self.send_msg(summary_channel, f"Total Lines     : {total_lines}")
        self.send_msg(summary_channel, f"Non-Blank Lines : {non_blank_lines}")
        self.send_msg(summary_channel, f"Comment Lines   : {comment_lines}")
        self.send_msg(summary_channel, f"Effective Code  : {effective_code_lines}")

        self.send_msg(summary_channel, '')
        self.send_msg(summary_channel, "Summary of Statement Categories")
        self.send_msg(summary_channel, "---------------- ----------------")
        self.send_msg(summary_channel, "Statements Kept (Counted):")
        
        length = 0 if not kept else max(len(key) for key in kept)
        for cat, n in kept.items():
            self.send_msg(summary_channel, f"  {cat:{length}} : {n}")
        if not kept:
            self.send_msg(summary_channel, "  (none)")

        self.send_msg(summary_channel, '')
        self.send_msg(summary_channel, "Statements sKipped:")

        length = 0 if not skipped else max(len(key) for key in skipped)
        for cat, n in skipped.items():
            self.send_msg(summary_channel, f"  {cat:{length}} : {n}")
        if not skipped:
            self.send_msg(summary_channel, "  (none)")

        self.send_msg(summary_channel, '')
        self.send_msg(summary_channel, "Summary Totals:")
        self.send_msg(summary_channel, f"  Total Statements Found : {len(categories)}")
        self.send_msg(summary_channel, f"  Counted Statements     : {total_count}")
        self.send_msg(summary_channel, f"  Skipped Statements     : {len(categories) - total_count}")
        self.send_msg(summary_channel, '')
        self.send_msg(summary_channel, f"Final Statement Count    : {total_count}")

        self.send_msg(details_channel, "Detailed Statement Breakdown (Nested)")
        self.send_msg(details_channel, "-------------------------------------")
        for node, cat, keep, depth in sorted(categories, key=lambda x: getattr(x[0], "lineno", 0)):
            lineno = getattr(node, "lineno", None)
            lineinfo = f"line {lineno}" if lineno is not None else "no line"
            status = "COUNTED" if keep else "SKIPPED"

            snippet = ""
            if lineno is not None:
                try:
                    snippet = source.splitlines()[lineno - 1].strip()
                except IndexError:
                    snippet = "<source unavailable>"

            indent = "    " * depth
            self.send_msg(details_channel, f"{indent}{lineinfo:>8} | {cat:<25} | {status:<7} | {snippet}")


if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    analyzer.run()