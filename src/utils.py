import json
import docx


def convert_doc_to_json(doc_file):
    """Convert Word doc to JSON format"""
    doc = docx.Document(doc_file)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text)
    return json.dumps({"content": content})
