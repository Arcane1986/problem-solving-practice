from Q1 import hashtag_line
def hashtag_rectangle(width,height):
  empty_string = ""
  for _ in range(height):
    empty_string += hashtag_line(width)
  return empty_string
     

print(hashtag_rectangle(10,5))
print(hashtag_rectangle(20,10))