st = 'Print only the words that start with s in this sentence'
count = 0
for words in st.split():
    if words[0] == "s":
         print(words)


for num in range(0,11):
    if num%2 == 0:
        print(num)


mylist = [num for num in range(1,51) if num%3 == 0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word)

for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
        #print(num)
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)


st = 'Create a list of the first letters of every word in this string'
mylist = [num[0] for num in st.split()]
print(mylist)
