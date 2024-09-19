**Automated PDF Summarizer and Exam Generator
**********This project is an automated solution for summarizing long PDF documents and generating exams based on their content using OpenAI's GPT API. It is designed to handle very large text documents by bypassing token limitations of standard APIs like chatgpt.com (chat.openai.com), which restrict text submissions to only a few thousand words, making it especially useful for generating exams, quizzes, or summaries from extensive lecture materials.

**Key Features:
******PDF Summarization: Summarizes large PDF files, breaking them into manageable chunks.
Exam Generation: Generates exams or quizzes based on the lecture materials in the PDF file.
Token Limitation Bypass: Handles lengthy documents by processing them page by page.

**Prerequisites:
**To use this project, you will need an OpenAI API key, which requires an active subscription to the OpenAI API service. Make sure you have signed up for OpenAI and obtained your API key from OpenAI's API platform.

**Deployment Instructions (Google Colab):
**This script can be easily deployed and run in a Google Colab Jupyter notebook. Follow the steps below:

**Step 1: Setup Google Colab
**Open Google Colab.
Create a new Python notebook.

**Step 2: Install Dependencies
**You need to install the necessary packages in your Colab notebook. Run the following commands in a Colab cell to install the required libraries:

!pip install openai
!pip install PyPDF2

**Step 3: Upload PDF File
**Upload your PDF file to the Google Colab notebook by clicking on the Files tab on the left panel.
Drag and drop your PDF file into the content folder.

**Step 4: Update the Script
**In your Colab notebook, update the script as follows:

Replace the OpenAI API key: Add your actual OpenAI API key to the api_key parameter in the script. Make sure to keep this key secure and do not hardcode it in your repository.

Replace the PDF file name: After uploading the PDF to the content folder, replace "file_name.pdf" with the actual name of the uploaded file.

**Running the Script
**Once you've updated the API key and PDF file name, you can run the script in the notebook. You can also adjust the role (system) and user prompts to fit your needs.

Click the play button, and watch as your summarized and exam-generated .txt file shows up in the content folder! For very large text files (hundreds of thousands of words), the script may take some time to complete. However, you can periodically refresh your content folder and download the .txt file as it gets filled with more content. The summary file will typically start to appear after just a few seconds, regardless of the file word count.

Happy studying!
