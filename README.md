# Markdown to HTML Converter

This Python script allows you to convert Markdown files to HTML format. You can convert individual Markdown files or automatically convert all Markdown files in the current directory.

## Usage

```bash
usage: markdown2html [-h] [-i INPUT] [-o OUTPUT] [-a]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file name/text
  -o OUTPUT, --output OUTPUT
                        output file name
  -a, --auto            increase output verbosity
```

### Options

- `-i` or `--input`: Specifies the input file name or text.
- `-o` or `--output`: Specifies the output file name.
- `-a` or `--auto`: Automatically convert all Markdown files in the current directory to HTML.

## Example Usage

### Convert a single Markdown file to HTML

```bash
markdown2html -i input.md -o output.html
```

### Convert all Markdown files in the current directory to HTML

```bash
markdown2html -a
```

## Author

- Author: [@hirusha-adi](https://github.com/hirusha-adi)

## Version

- Version: v1.0

## License

This script is open-source and available under the [MIT License](LICENSE).

## How to Install

1. Clone the repository or download the script.
2. Ensure you have Python 3 installed.
3. Run the script using the provided usage instructions.
