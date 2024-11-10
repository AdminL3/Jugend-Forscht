import os


def get_output_path(path):

    set = path.split(r'/')
    topic = set[2]
    filename = set[5].split(".")[0]
    date = filename.split("_")
    index = date[3]
    day = date[2]
    month = date[1]
    year = set[3]
    return [f"data/word_count/{topic}/{year}/month{month}/day{day}/", f"{index}.txt"]


start_year = 2020
amount_years = 1
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
            files = []
            if os.path.exists(files_path):
                for file in os.listdir(files_path):
                    if file.endswith('.txt'):
                        files.append(os.path.join(files_path, file))
            for file in files:
                with open(file, 'r', encoding='utf-8') as f:
                    article_text = f.read()

                output = get_output_path(file)
                os.makedirs(output[0], exist_ok=True)
                output_file_path = output[0] + output[1]

                word_count = len(article_text.split(" "))
                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write(word_count)
