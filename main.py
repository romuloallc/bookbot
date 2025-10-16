import sys
from stats import count_words, count_chars, sort_dict, report

def main():
   if len(sys.argv) == 1:
       sys.exit("Usage: python3 main.py <path_to_book>")

   report(sys.argv[1])

main()
