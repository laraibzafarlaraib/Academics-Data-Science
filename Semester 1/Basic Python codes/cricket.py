from random import *
def main():
    over = 1
    total=0
    wickets=0
    innings=1
    flag=0
    print('1st inning')
    while innings<=2:
        
        while over < 7:
            print (f'Over {over}:',end=' ')
            balls = 0
            a=0
            while balls < 6:
                ball = randint(0, 9)
                if ball >= 0 and ball <= 6:
                    print(ball, end = ' ')
                    a=a+ball
                    total=total+a
                    a=0
                elif ball == 7:
                    out = randint(0, 3)
                    o=0
                    if out == 0:
                        print(end = 'B ')
                        o=o+1 
                    elif out == 1:
                        print(end = 'C ')
                        o=o+1
                    elif out == 2:
                        print(end = 'S ')
                        o=o+1
                    else:
                        print(end = 'R ')
                        o=o+1
                    
                    wickets=wickets+o
           
                    
                elif ball == 8:
                    print(end = 'W ')
                    balls -= 1
                else:
                    print(end = 'N ')
                    balls -= 1
                
                balls += 1
            over+=1
            print(f'   Total: {total}' ,end='  ')
            print(f'Wickets: {wickets}' ,end='  ')
            print()
            if wickets >=5:
                print()
                print('inning is finished')
                flag=1
                break
        if flag==1:
            break
        innings+=1

        
    over = 1
    total2=0
    wickets=0
    innings=1
    flag=0
    print(end='\n')
    print('2nd inning')
    while innings<=2:
       
        while over < 7:
            
            print (f'Over {over}:',end=' ')
            balls = 0
            a=0
            while balls < 6:
                ball = randint(0, 9)
                if ball >= 0 and ball <= 6:
                    print(ball, end = ' ')
                    a=a+ball
                    total2=total2+a
                    a=0
                elif ball == 7:
                    out = randint(0, 3)
                    o=0
                    if out == 0:
                        print(end = 'B ')
                        o=o+1 
                    elif out == 1:
                        print(end = 'C ')
                        o=o+1
                    elif out == 2:
                        print(end = 'S ')
                        o=o+1
                    else:
                        print(end = 'R ')
                        o=o+1
                    
                    wickets=wickets+o
           
                    
                elif ball == 8:
                    print(end = 'W ')
                    balls -= 1
                else:
                    print(end = 'N ')
                    balls -= 1
                
                balls += 1
            over+=1
            print(f'   Total2: {total2}' ,end='  ')
            print(f'Wickets: {wickets}' ,end='  ')
            print()
            if wickets >=5:
                print()
                print(f'{innings}Inning is finished.')
                flag=1
                break
        if flag==1:
            break
        innings+=1
    if total > total2:
        print('Team 1 won!!')
    else:
        print('Team 2 won!!')
    
main()
