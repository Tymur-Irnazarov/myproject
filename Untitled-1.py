o = open("text.txt", encoding="utf8")
word = input("Введіть слово: ")

f = False
for lines in o.read().split("\n\n"):
    if word in lines:
        print(f"---------\n{lines}")
        f = True
if f == False:
    print("Немає такого слова")