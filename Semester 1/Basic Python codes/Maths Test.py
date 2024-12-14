from random import*
def main():
    lenght=10
    print('lenght=10')
    x1=[0]*lenght
    x2=[0]*lenght
    x3=[0]*lenght
    score=0
    for i in range (lenght):
        x1[i]=randint(1,10)
        x2[i]=randint(1,10)
        print(f'{x1[i]}+{x2[i]}=', end=' ')
        summ =x1[i]+x2[i]
        sum2=int(input())
        if sum2 == summ:
            score+=1
        if sum2!= summ:
            x3[i]=sum2
    print(f'score:{score}')
    print(f'Incorrect\t\tcorrect')
    for i in range (len(x3)):
        if x3[i] !=x1[i] + x2[i]:
            print(f'{x1[i]} + {x2[i]} = {x3[i]}\t\t{x1[i]} + {x2[i]} = {x1[i] + x2[i]} ')
main()
            
