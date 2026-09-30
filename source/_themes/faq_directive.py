"""
Custom Sphinx directive for FAQ entries.

Converts:
    .. faq-entry:: Question text?
    
       Answer content here...

Into:
    .. container:: question
    
       .. collapse:: Question text?
       
          Answer content here...
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList


class FAQEntryDirective(Directive):
    """
    A custom directive for FAQ entries that automatically wraps content
    in a question container with a collapse directive.
    """
    
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    
    def run(self):
        # Get the question text from the argument
        question = self.arguments[0]
        
        # Create the RST lines for the full structure
        rst_lines = [
            ".. container:: question",
            "",
            "   .. collapse:: " + question,
            ""
        ]
        
        # Indent all content by 6 spaces (3 for container, 3 for collapse)
        for line in self.content:
            if line.strip():
                rst_lines.append("      " + line)
            else:
                rst_lines.append("")
        
        # Parse this as a StringList
        rst_block = StringList(rst_lines)
        
        # Create a container to hold the parsed content
        container = nodes.container()
        
        # Parse the RST into the container
        self.state.nested_parse(rst_block, self.content_offset, container)
        
        return container.children


def setup(app):
    """Register the directive with Sphinx."""
    app.add_directive('faq-entry', FAQEntryDirective)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
