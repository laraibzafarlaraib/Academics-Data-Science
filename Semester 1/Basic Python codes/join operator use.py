def main():
    score = int(input('Amount of numbers:'))
    x = [0] * score
    if score <= 100:
        print('Elements:')
        for i in range(score):
            x[i] = int(input())
        print(' '.join(str(i) for i in x))

main()
