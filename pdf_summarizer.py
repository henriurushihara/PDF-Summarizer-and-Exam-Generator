import os
import PyPDF2
import re
from openai import OpenAI  # OpenAI official Python package

# Add your OpenAI API key here
client = OpenAI(
    api_key="your-openai-api-key"
)

# Set the string that will contain the summary
pdf_summary_text = ""

# Open the PDF file (update with your actual file name)
pdf_file_path = "/content/your_file_name.pdf"

# Read the PDF file using PyPDF2
pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Loop through all the pages in the PDF file
for page_num in range(len(pdf_reader.pages)):
    # Extract the text from the page
    page_text = pdf_reader.pages[page_num].extract_text().lower()

    # The response from the API is not a subscriptable object. You must access its attributes.

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {
                "role": "system",
                "content": "You are my Modern Software Design and Development Course Professor Dr. Phil."
            },
            {
                "role": "user",
                "content": f"Generate a final exam for the class that covers the material from the provided lecture material. Use the provided final review to structure the exam {page_text}"
            },
        ],
    )

    page_summary = completion.choices[0].message.content
    pdf_summary_text += page_summary + "\n"
    pdf_summary_file = pdf_file_path.replace(os.path.splitext(pdf_file_path)[1], "_summary.txt")
    with open(pdf_summary_file, "w+") as file:
        file.write(pdf_summary_text)

pdf_file.close()
