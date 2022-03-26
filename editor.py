def markdown_params():
    mk_format = input("Choose a formatter:")
    while mk_format not in formatters + commands:
        print("Unknown formatting type or command")
        mk_format = input("Choose a formatter:")
    else:
        if mk_format == "!help":
            print("Available formatters:", *formatters)
            print("Available commands:", *commands)
        elif mk_format == "!done":
            return

        return markdown_params()


def main():
    markdown_params()


if __name__ == '__main__':
    formatters = ("plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                  "unordered-list", "new-line")
    commands = ("!help", "!done")
    main()
