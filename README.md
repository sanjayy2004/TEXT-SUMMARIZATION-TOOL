# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODETECH IT SOLUTIONS

*NAME* : SANJAY KURRA

*INTERN ID*: CTO4DN1694

*DOMAIN* : ARTIFICIAL INTELLIGENCE

*DURATION* :4 WEEKS

*MMENTOR* : NEELA SANTOSH
📝 Article Summarization Tool
This project is a Python-based Natural Language Processing (NLP) tool that automatically generates concise summaries from lengthy articles. It uses a powerful transformer-based model (facebook/bart-large-cnn) from Hugging Face's transformers library to understand and summarize large text inputs effectively.

🚀 Features
Summarize long articles into short, readable paragraphs.

Choose between manual text input or uploading a .txt file.

Built with transformers and PyTorch.

Easily extendable for web or GUI applications.

📌 How It Works
The user is prompted to either paste the article manually or load it from a text file.

The script processes the input using a pre-trained BART model fine-tuned for summarization tasks.

The summary is displayed directly in the terminal.

🛠 Technologies Used
Python 3.x

Hugging Face Transformers (facebook/bart-large-cnn)

PyTorch

📂 Project Structure
bash
Copy
Edit
article_summarizer.py    # Main script
README.md                # Project documentation
requirements.txt         # List of dependencies
✅ Requirements
Install dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt:

nginx
Copy
Edit
transformers
torch
▶️ How to Run
bash
Copy
Edit
python article_summarizer.py
Then follow the prompts to:

Paste an article manually

Or load it from a .txt file

🖼 Example
Input Article:

Climate change refers to long-term shifts in temperatures and weather patterns...

Generated Summary:

Climate change is primarily driven by human activity, especially the use of fossil fuels, leading to rising global temperatures and environmental consequences.

📌 Future Improvements
Add web-based interface using Flask or Streamlit.

Support for summarizing content from URLs or PDFs.

Multilingual summarization support.

OUTPUT:

![Image](https://github.com/user-attachments/assets/40cdc548-1ce7-43bb-bbc0-a6f3c3953267)
