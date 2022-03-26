import string


def apply_formatter(mk_format: str):
    formatted_string = ""
    if mk_format in ("header", "plain", "bold", "italic", "inline-code"):
        if mk_format == "header":
            while True:
                header_lvl = int(input("Level:"))
                if 1 <= header_lvl <= 6:
                    break
                print("The level should be within the range of 1 to 6")
            formatted_string += f"{header_lvl * '#'} "
        text = input("Text:")
        formatted_string += formatters[mk_format].substitute(text=text)
    elif mk_format == "link":
        label = input("Label:")
        url = input("URL:")
        formatted_string += formatters[mk_format].substitute(label=label, url=url)
    else:
        formatted_string += formatters[mk_format]
    return formatted_string


def markdown_params():
    output = ""
    while True:
        mk_format = input("Choose a formatter:")
        while mk_format not in tuple(list(formatters.keys())) + commands:
            print("Unknown formatting type or command")
            mk_format = input("Choose a formatter:")
        else:
            if mk_format == "!help":
                print("Available formatters:", *tuple(list(formatters.keys())))
                print("Available commands:", *commands)
            elif mk_format == "!done":
                break
            output += apply_formatter(mk_format)
            print(output)


def main():
    markdown_params()


if __name__ == '__main__':
    commands = ("!help", "!done")

    formatters = {
        "header": string.Template("$text \n"),
        "plain": string.Template("$text"),
        "bold": string.Template("**$text**"),
        "italic": string.Template("*$text*"),
        "inline-code": string.Template("`$text`"),
        "new-line": "\n",
        "link": string.Template("[$label]($url)"),
    }
    main()
