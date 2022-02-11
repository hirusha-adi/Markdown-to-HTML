#!/usr/bin/python3
import argparse
import os
import sys

import markdown


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file name/text")
    parser.add_argument("-o", "--output", help="output file name")
    parser.add_argument("-a", "--auto", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    all_args = {
        "input_file": args.input,
        "output_file": args.output,
        "auto_files": args.auto
    }
    return all_args


def toHTML(text: str):
    return markdown.markdown(text)


def main():
    args = getArgs()
    input_file = args["input_file"]
    output_file = args["output_file"]
    auto_files = args["auto_files"]

    if auto_files:
        html_files = [file for file in os.listdir(
            os.getcwd()) if file.lower().endswith(".md")]
        for html_file in html_files:
            with open(os.path.join(os.getcwd(), html_file), "r", encoding="utf-8") as fr:
                converted = toHTML(fr.read())
            newname = os.path.join(
                os.getcwd(), f"{str(html_file)[:-3]}.html")
            with open(newname, "w", encoding="utf-8") as fw:
                fw.write(converted)

    if not(input_file is None):
        if str(input_file).strip().lower().endswith(".md"):
            input_file_path = os.path.join(os.getcwd(), input_file)
            with open(input_file_path, "r", encoding="utf-8") as fr1:
                converted = toHTML(fr1.read())

            if (output_file is None):
                output_file = os.path.join(
                    os.getcwd(), f"{str(input_file)[:-3]}.html")
            else:
                if not(str(output_file).lower().endswith(".html") or str(output_file).lower().endswith(".htm")):
                    output_file += ".html"
                output_file = os.path.join(os.getcwd(), output_file)

            with open(output_file, "w", encoding="utf-8") as fw:
                fw.write(converted)

        else:
            html = toHTML(str(input_file))

            if (output_file is None):
                output_file = os.path.join(
                    os.getcwd(), f"{str(input_file)[:12].strip()}.html")
            else:
                if not(str(output_file).lower().endswith(".html") or str(output_file).lower().endswith(".htm")):
                    output_file += ".html"
                output_file = os.path.join(os.getcwd(), output_file)

            with open(output_file, "w", encoding="utf-8") as fw:
                fw.write(html)


if __name__ == "__main__":
    main()
