
import formatter


def create_section_name():
    pass

# Input markdown , Output Root elements(optional RootHeader, Mandatory Body and optional Answers)
# No writing to model here
def markdown_to_root_elements(questionlibrary):

    from api_v3.formatter.formatter import formatter

    formatter(questionlibrary)


    pass

# Input Body , Output Array of 1 or more sections
# No writing to model here
def body_to_sections():
    pass

# Input section, Output Array of 1 or more Questions 
# No writing to model here
def section_to_questions():
    pass

# This function will most likely writes directly to model. Might need to move to model instead 
def run_parser():
    pass


def process(questionlibrary):

    # ====================== Convert to markdown
    # print(questionlibrary.pandoc_string)
    markdown_to_root_elements(questionlibrary)

    pass