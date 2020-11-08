def to_camel_case(text):
  y = []
  for i in text :
    if i not in y:
        y.append(i)
  text = ''.join(y)
  print(text)
  text = text.replace('_',' ').replace('-',' ').title().split(' ')

  text = ''.join(text)
  print(text)



to_camel_case("A-BBC")
