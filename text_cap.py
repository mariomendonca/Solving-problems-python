def to_jaden_case(string):
    test = string.split(' ')
    string_final = []
    for i in test: 
      x = i.capitalize()
      string_final.append(x)
    for i in string_final:
      print(i, end=' ')
      
to_jaden_case("How can mirrors be real if our eyes aren't real")