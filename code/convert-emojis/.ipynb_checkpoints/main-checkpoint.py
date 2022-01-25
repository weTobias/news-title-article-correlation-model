import re
csv_string = open('all-the-news-2-1-cleaned-sample1000.csv', encoding="utf8")
csv_string = csv_string.read()
four_byte_pattern = re.compile("[\U0000FFFF-\U0010FFFF]", flags=re.UNICODE)
cleaned_csv_string = four_byte_pattern.sub(r'', csv_string)
with open("without-emojis.csv", "w", encoding="utf8") as text_file:
    text_file.write(cleaned_csv_string)
