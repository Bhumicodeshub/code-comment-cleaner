def remove_python_comments(input_file, output_file):
    """
    Removes single-line comments from a Python file.
    """

    try:
        with open(input_file, "r", encoding="utf-8") as source_file:
            lines = source_file.readlines()
    except FileNotFoundError:
        print("Input file not found. Please check the file name.")
        return

    cleaned_lines = []

    for line in lines:
        stripped = line.lstrip()


        if stripped.startswith("#"):
            continue

        cleaned_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.writelines(cleaned_lines)

    print("Comment cleaning completed successfully.")


if __name__ == "__main__":
    remove_python_comments(
        "transaction_manager.py",
        "transaction_manager_cleaned.py"
    )
