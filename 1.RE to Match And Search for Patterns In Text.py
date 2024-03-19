import re
def main():
    text = input("Enter some text: ")
    pattern = r'\b[Aa]\w+'
    matches = re.findall(pattern, text)
    print("Words starting with 'A' or 'a':")
    for match in matches:
        print(match)
if __name__ == "__main__":
    main()
