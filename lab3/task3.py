s = input()

clean = s.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(clean)