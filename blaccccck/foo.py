from pathlib import Path


def main():     
    path = Path(__file__).parent.joinpath("foo", 'bar', "baz_1234567890123456789012345678901234567890123456789012345678901234567890")
    print(path) # ここにプリントされる

if __name__ == '__main__':
    main()
