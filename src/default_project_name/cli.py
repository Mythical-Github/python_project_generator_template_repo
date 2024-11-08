from default_project_name import main

OPTIONS = {
    "module": main,
    "commands": {
        "print_text": {
            "function_name": "print_text",
            "arg_help_pairs": [
                {"text_to_print": "the text you want to print out"}
            ]
        }
    }
}
