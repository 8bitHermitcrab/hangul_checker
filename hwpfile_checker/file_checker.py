import subprocess
from hanspell import spell_checker


def extract_text_from_hwp(file_path):
    # HWP 파일에서 텍스트를 추출하기 위해 pyhwp를 사용합니다.
    process = subprocess.run(['hwp5txt', file_path], capture_output=True, text=True)
    return process.stdout

hwp_text = extract_text_from_hwp('khs_example.hwp')


print(hwp_text)

def check_spelling(text):
    result = spell_checker.check(text)
    corrections = {err.word: err.suggestions[0] if err.suggestions else err.word for err in result.errors}
    return corrections, result.checked

corrections, checked_text = check_spelling(hwp_text)


def apply_corrections(text, corrections):
    for incorrect, correct in corrections.items():
        text = text.replace(incorrect, f'<span style="color: red;">{correct}</span>')
    return text

highlighted_text = apply_corrections(checked_text, corrections)


import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.uno import Exception as UnoException
from com.sun.star.connection import NoConnectException

def connect_to_libreoffice(port=2002):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_context)
    try:
        context = resolver.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
        return context
    except NoConnectException:
        raise Exception("Failed to connect to LibreOffice. Ensure that LibreOffice is running with a listening port.")

def create_document_with_text(text, context):
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, ())
    text_cursor = doc.Text.createTextCursor()
    text_cursor.CharColor = 0xFF0000  # Set text color to red
    doc.Text.insertString(text_cursor, text, False)
    return doc

def save_document(doc, output_path):
    output_url = uno.systemPathToFileUrl(output_path)
    props = (PropertyValue("FilterName", 0, "Hangul WP 97", 0),)
    doc.storeToURL(output_url, props)
    doc.close(True)

# Ensure LibreOffice is running with the following command:
# soffice --accept="socket,host=localhost,port=2002;urp;"

# Connect to LibreOffice
context = connect_to_libreoffice()

# Create a new document with the corrected text
corrected_text = "Here is the corrected text with red highlights."
doc = create_document_with_text(corrected_text, context)

# Save the document
save_path = "output.hwp"  # Change the path and filename as needed
save_document(doc, save_path)
