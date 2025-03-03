import markdown
import os


def convert_markdown_to_html(markdown_file_path, output_html_file_path):
    if not os.path.exists(markdown_file_path):
        print(f"Error: The file {markdown_file_path} does not exist.")
        return

    with open(markdown_file_path, 'r', encoding='utf-8') as markdown_file:
        markdown_text = markdown_file.read()

    html = markdown.markdown(markdown_text)

    with open(output_html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html)

    print(f"Markdown file successfully converted to HTML and saved as {output_html_file_path}")


if __name__ == "__main__":
    input_markdown_file = 'input.md'
    output_html_file = 'output.html'

    convert_markdown_to_html(input_markdown_file, output_html_file)
