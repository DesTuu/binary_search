names = []

with open("names.txt", "r", encoding="UTF-8") as f:
    for line in f:
        name = "".join(line.strip())
        name = name.split(",")
        for n in name:
            if n == "":
                pass
            else:
                names.append(n.strip())

print(names)

def binary(names, your_name, low, high):
    if low > high:
        return -1
    mid = (high + low) // 2

    if names[mid] == your_name:
        return mid
    elif names[mid] < your_name:
        return binary(names, your_name, mid+1, high)
    elif names[mid] > your_name:
        return binary(names, your_name, low, mid-1)

user_input = str(input("Your name: "))

for index, string in enumerate(names):
    try:
        if string == user_input:
            print(index)
    except:
        print("error")

print(binary(names, user_input, 0, (len(names)-1)))
