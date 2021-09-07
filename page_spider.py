import argparse

def main(database, url_list_file):
    print(database)
    print(url_list_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")

    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database_file, input_file)

