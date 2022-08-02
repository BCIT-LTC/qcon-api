import re
import pypandoc

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
    html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_dollars", to="html", extra_args=['--mathjax', '--ascii'])
    # html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_dollars", to="html", extra_args=['--mathjax', '--ascii'])
    # soup_text = BeautifulSoup(html_text, "html.parser")
    # soup_text_math = soup_text.find_all("span", {"class": "math"})
            
    # if len(soup_text_math) > 0:
    #     for span_math in soup_text_math:
    #         # print(span_math)
    #         # math_text = re.sub(r"\\(?=[^a-zA-Z\(\)\d\s:])", "", span_math.string)
    #         mathml_text = pypandoc.convert_text(span_math, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_single_backslash", to="html", extra_args=['--mathml', '--ascii']).removeprefix('<p>').removesuffix('</p>')
    #         # print("\n", mathml_text)
    #         soup_math = BeautifulSoup(mathml_text, "html.parser")
    #         span_math.string = ''
    #         span_math.append(soup_math)
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
