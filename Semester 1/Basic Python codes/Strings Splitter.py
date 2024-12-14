def main():
    array = input("Enter string with space: ")
    array1 = ''
    array2 = ''
    i = 0
    while i < len(array) and array[i] != ' ':
        array1 += array[i]
        i += 1
    i += 1
    while i < len(array):
        array2 += array[i]
        i += 1
    print("First String:", array1)
    print("Second String:", array2)

main()
