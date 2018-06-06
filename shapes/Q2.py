from Q1 import hashtag_line
def hashtag_square(height,width):
  empty_string = ""
  for _ in range(height):
    empty_string += hashtag_line(width)
  return empty_string
     

print(hashtag_square(5,5))
print(hashtag_square(20,20))