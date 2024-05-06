def main():
  book_path = "books/frankenstein.txt"
  print(f"--- Begin report of {book_path} ---")
  text = get_book_text(book_path)
  words = get_num_words(text)
  print(f"{words} words found in document")
  letters = count_letters(text)
  print("--- End report ---")


def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents

def get_num_words(text):
  words = text.split()
  return len(words)


def count_letters(text):
  letters = {}
  for c in text:
    if c.isalpha():
      lowered = c.lower()
      if lowered in letters:
        letters[lowered] += 1
      else:
        letters[lowered] = 1

  sorted_letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))

  for letter, count in sorted_letters.items():
    print(f"The letter '{letter}' appears {count} times")

  return sorted_letters





main()