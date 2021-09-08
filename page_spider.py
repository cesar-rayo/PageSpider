import argparse
import os

from utilities import url_utilities, database_utilities


def main(database, url_list_file):
    words_list = []
    print(database)
    print(url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading {}".format(url))
        page_content = url_utilities.load_page(url)
        words = url_utilities.scrape_page(page_content)
        words_list.extend(words)

    os.chdir(os.path.dirname(__file__))
    database_path = os.path.join(os.getcwd(), "words.db")
    database_utilities.create_database(database_path)
    database_utilities.save_words_to_database(database_path, words_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")

    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database_file, input_file)
