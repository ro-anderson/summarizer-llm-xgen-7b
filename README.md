# Summarizer with Salesforce LM Model XGen-7B

This repository is a demonstration of using the state-of-the-art language model XGen-7B developed by Salesforce for text summarization.

## Requirements

The code in this repository requires a GPU to run successfully as the model uses quantization. If you do not have access to a local GPU, you may consider running the code on a cloud platform that provides GPU instances such as Google Colab, AWS, Azure, etc.

The project is implemented in Python and depends on several libraries including PyTorch, Huggingface Transformers, Gradio, Tiktoken, and bitsandbytes.

## Installation

The repository includes a Makefile that automates the setup process. The setup includes creating a Python virtual environment and installing the necessary Python libraries.

To install the necessary libraries and setup the environment, you can run the following command:

```bash
make install
After running the installation command, activate the Python virtual environment with the following command:

bash
Copy code
source venv/bin/activate
You will see (venv) at the beginning of your command prompt, indicating that you are inside the virtual environment.

Usage
With the virtual environment activated, you can now run the app.py script:

bash
Copy code
python app.py
The app.py script will load the pre-trained XGen-7B model and create a Gradio interface for text summarization. You can input a long text, and the model will return a shorter summary.

By default, the application runs on 127.0.0.1:7861.

Disclaimer
This repository is for demonstration purposes. While the XGen-7B model produces high-quality text summaries, it requires significant computational resources and may not be suitable for all applications. Always consider the trade-off between performance and resource requirements when choosing a model for your application.

