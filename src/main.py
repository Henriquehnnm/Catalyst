from utils.extractors.reader import reader
from utils.loaders.writer import writer


def main():
    data = reader()
    print(data)
    writer(data, "./output.csv")


if __name__ == "__main__":
    main()
