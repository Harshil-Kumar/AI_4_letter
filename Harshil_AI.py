n=int(input("Enter the number of 4-letter prompts: "))
word=[]

for i in range(n):
    prompt = input(f"Enter prompt {i + 1}: ")
    if len(prompt) != 4:
        print("Prompt must be 4 letters long. Please try again.")
        exit(1)
    word.append(prompt)

x=[]
y=[]

for i in range(len(word) - 1):
    for j in range(len(word[0])):
        if word[i][j:]==word[i+1][:-j]:
            y.append(word[i])
            y.append(word[i+1])
            x.append(word[i][j:])

d=''.join([ele for ele in x])
n=len(x[0])
d=y[0][:-n]+d
final=d+y[len(y)-1][n:]

print("\n")
print("Common Elements : ", x)
print("Final Word : ", final)

for i in word:
    if i not in final:
        print("Other Word : ", i)