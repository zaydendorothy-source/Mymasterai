import os
from pypdf import PdfReader
from docx import Document


class FileReader:

    def read(self, filepath):

        if not os.path.exists(filepath):
            return "File not found."

        extension = os.path.splitext(filepath)[1].lower()

        try:

            if extension == ".txt":
                with open(filepath, "r", encoding="utf-8") as file:
                    return file.read()

            elif extension == ".pdf":
                reader = PdfReader(filepath)

                text = ""

                for page in reader.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

                return text

            elif extension == ".docx":

                document = Document(filepath)

                text = ""

                for paragraph in document.paragraphs:
                    text += paragraph.text + "\n"

                return text

            else:
                return "Unsupported file type."

        except Exception as e:
            return str(e)


if __name__ == "__main__":

    reader = FileReader()

    while True:

        path = input("\nFile path (or exit): ")

        if path.lower() == "exit":
            break

        print()
        print(reader.read(path))