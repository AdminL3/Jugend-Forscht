import re

for number in range(6):
    # Open and read the file contents
    with open(f"test/get/{number}.txt", "r", encoding="utf-8") as f:
        html = f.read()

    # Find all matches for the specified pattern
    matches = re.findall(r'"text":"(.*?)"', html)

    # Remove duplicates by converting to a dictionary and back to a list
    matches = list(dict.fromkeys(matches))

    # Prepare the text with each match on a new line
    text = "\n".join(matches)

    # Write the output to a new file
    with open(f"test/set/{number}.txt", "w", encoding="utf-8") as f:
        f.write(text)
