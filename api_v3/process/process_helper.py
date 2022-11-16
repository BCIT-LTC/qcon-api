import re
import pypandoc

def add_info_message(question, info_message):
    if question.info:
        if info_message not in question.info:
            question.info = question.info + "\n" + info_message
            question.save()

    else:
        question.info =  info_message
        question.save()

def add_warning_message(question, warning_message):
    if question.warning:
        if warning_message not in question.warning:
            question.warning = question.warning + "\n" + warning_message
            question.save()

    else:
        question.warning =  warning_message
        question.save()

def add_error_message(question, error_message):
    if question.error:
        if error_message not in question.error:
            question.error = question.error + "\n" + error_message
            question.save()

    else:
        question.error =  error_message
        question.save()

def trim_text(txt):
    text = txt.strip()
    text = re.sub('<!-- -->', '', text)
    text = re.sub('<!-- NewLine -->', '\n', text)
    text = text.strip("\n")
    return text

def markdown_to_plain(text):
    plain_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji", to="plain", extra_args=['--wrap=none'])
    return plain_text

def markdown_to_html(text):
    html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_dollars", to="html", extra_args=['--mathml', '--ascii'])
    return str(html_text)

def trim_md_to_plain(text):
    text_content = trim_text(text)
    text_content = markdown_to_plain(text_content)
    return text_content

def trim_md_to_html(text):
    text_content = trim_text(text)
    text_content = markdown_to_html(text_content)
    text_content = text_content.strip('\n')
    return text_content
