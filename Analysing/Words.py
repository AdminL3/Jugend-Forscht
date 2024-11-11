import os


def get_output_path(path):
    set = path.split(r'/')
    base = r"data/word_count/"

    return [str(base)+str(set[2])+"/"+str(set[3])+"/"+str(set[4])+"/"+str(set[5])+"/", str(set[6])]


def word_count(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split()
    word_count = len(words)
    return str(word_count)


start_year = 2020
amount_years = 2
topics = ["politics", "world"]

for topic in topics:
    print(topic)
    for i in range(amount_years):
        year = start_year + i
        print(year)
        for j in range(12):
            numbers = [str(h).zfill(2) for h in range(1, 13)]
            month = numbers[j]
            print(month)
            files_path = f"data/articles/{topic}/{year}/month{month}/"
            days = []
            if os.path.exists(files_path):
                for item in os.listdir(files_path):
                    item_path = os.path.join(files_path, item)
                    days.append(item_path)
            else:
                print(f"Folder does not exist: {files_path}")

            files = []
            for day in days:
                for file in os.listdir(day):
                    if file.endswith('.txt'):
                        files.append(os.path.join(day, file))

            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    article_text = f.read()
                path = file.replace("\\", "/")

                print(path)
                output = get_output_path(path)

                os.makedirs(output[0], exist_ok=True)
                output_path = output[0]+output[1]
                word_counter = word_count(article_text)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(word_counter)
