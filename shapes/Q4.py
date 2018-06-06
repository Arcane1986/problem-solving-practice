from Q1 import hashtag_line

def space_line(spaces,line_length):
  space_and_break="'"*spaces
  return space_and_break+hashtag_line(line_length)

def main():
  print(space_line(5,3))
  print(space_line(8,4))

if __name__ == '__main__':
  main()