from django import template
import markdown
import bleach
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def firstparagraph(text):
    html = markdown.markdown(text)

    # linkify_html = bleach.linkify(html)
    # tags = ['img', 'p', 'em', 'strong', 'a', 'span', 'b', 'i', 'blockquote', 'hr'] # bleach.ALLOWED_TAGS
    # attributes = {
    #     '*': ['class', 'style'],
    #     'a': ['href', 'rel'],
    #     'img': ['src', 'alt', 'style'],
    # }
    # styles = ['float','font-weight', 'width']
    
    # clean_html = bleach.clean(linkify_html, styles=styles, tags=tags, attributes=attributes, strip=True)
    try:
        firstparagraph = BeautifulSoup(html).find('p').text #clean_html
    except:
        firstparagraph = ""
    return firstparagraph


 
