# 📄 Markdown to HTML Converter

A simple Python script to convert **Markdown** files to **HTML** format.

* * *

## 📌 Features

  * Converts Markdown files to HTML.
  * Handles various Markdown syntax (headers, lists, code blocks, etc.).
  * Simple and easy-to-use "interface".
  * Error handling for missing files.

## 🛠️ Requirements

Ensure you have Python and the `markdown` package installed:

    
    
    pip install markdown

## 🚀 Installation

1\. Clone this repository or download the script:

    
    
    git clone https://github.com/michaelninder/markdown-to-HTML-Converter.git
    cd markdown-to-html

2\. Ensure you have Python 3 installed:

    
    
    python --version

## ▶️ Usage

Place your Markdown content in `input.md` and run the script:

    
    
    python markdown_to_html.py

The output will be saved in `output.html`.

### ✅ Example

#### input.md

    
    
    # Hello, World!
    
    This is a sample markdown file.
    
    - Item 1
    - Item 2
    
    **Bold Text** and *Italic Text*.
    
    ```python
    print("Hello, Python!")
    ```
            

#### output.html

    
    
    <h1>Hello, World!</h1>
    
    
    This is a sample markdown file.
    
    
    
    
    
     
      * Item 1
     
      * Item 2
     
    
    
    
    
    **Bold Text** and _Italic Text_.
    
    
    
    
    
    
     print("Hello, Python!") 

`

## 📚 Markdown Syntax Supported

  * Headers (H1-H6)
  * Bold, Italic, Strikethrough
  * Lists (ordered/unordered)
  * Code blocks and inline code
  * Links and images
  * Blockquotes
  * Horizontal rules
  * Tables (with extra extensions)

## ❗ Notes

  * Ensure the `input.md` exists before running the script.
  * Customize the input/output file paths as needed.
  * Uses the Python `markdown` package.

## 🧑‍💻 Contributing

Feel free to contribute by opening issues or submitting pull requests!

## 📜 License

This project is licensed under the MIT License.

```

