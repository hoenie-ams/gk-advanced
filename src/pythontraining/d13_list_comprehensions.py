"""
Demo of list comprehensions
"""


def main():
    filenames = ["file1.pdf", "file2.pdf", "file3.pdf"]

    roots = []

    for file in filenames:
        root, extension = file.split(".")
        roots.append(root)

    roots = [file.split(".")[0] for file in filenames]
    print(roots)

    ingredients = ["SPAM", "SPAM", "haM", "EgGs"]

    # List comprehension
    ingredients = [i.lower() for i in ingredients]
    print(ingredients)

    languages = ["C", "Java", "JavaScript", "Python"]
    lang_lengths = {}
    for lang in languages:
        lang_lengths[lang] = len(lang)

    # Dictionary comprehension
    lang_lengths = {lang: len(lang) for lang in languages}
    print(lang_lengths)


if __name__ == "__main__":
    main()
