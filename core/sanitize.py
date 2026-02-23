import bleach

ALLOWED_TAGS = [
    "a", "abbr", "acronym", "b", "blockquote", "br", "caption", "cite",
    "code", "col", "colgroup", "dd", "del", "dfn", "div", "dl", "dt",
    "em", "figure", "figcaption", "h1", "h2", "h3", "h4", "h5", "h6",
    "hr", "i", "img", "ins", "kbd", "li", "mark", "ol", "p", "pre",
    "q", "s", "samp", "small", "span", "strong", "sub", "sup", "table",
    "tbody", "td", "tfoot", "th", "thead", "time", "tr", "u", "ul", "var",
]

ALLOWED_ATTRIBUTES = {
    "*": ["class", "id", "style"],
    "a": ["href", "title", "rel", "target"],
    "abbr": ["title"],
    "acronym": ["title"],
    "img": ["src", "alt", "width", "height"],
    "td": ["colspan", "rowspan"],
    "th": ["colspan", "rowspan", "scope"],
    "time": ["datetime"],
}

ALLOWED_STYLES = [
    "color", "background-color", "font-size", "font-weight", "font-style",
    "text-align", "text-decoration", "border", "border-color", "border-width",
    "border-style", "padding", "margin", "width", "height",
]


def sanitize_html(html: str) -> str:
    if not html:
        return html
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        strip=True,
    )
