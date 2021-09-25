
yes= 'yes'
no = 'no'
def retry():
    choi_lai= input("let's play!!\n type[yes] to play again the game or [no] to quit the game  ")
    while True:
        if choi_lai == yes:
            play()
        elif choi_lai == no:
            print('Thanks for spending time to play our game\n Have a nice day')
            break
        else:    
            print('Incorrect ans!\n please try again')
from random import randint
def play():
    print('Nhap: keo, bua, bao')
    nguoi_choi= input()
    may_tinh = randint(0,2)
    if may_tinh== 0:
        may_tinh ='bua'
    if may_tinh == 1:
        may_tinh ='keo'
    if may_tinh == 2:
        may_tinh ='bao'
    print('-----')
    print('nguoi_choi chooses:'+ str(nguoi_choi))
    print('may_tinh chooses:'+ str(may_tinh))
    print('-----')
    if nguoi_choi == may_tinh:
        print('draw')
    else:
        if nguoi_choi  == 'keo':
            if may_tinh == 'bua':
                print('ohh!! you lose')
            else:
                print('congratulation!! you win')
        elif nguoi_choi  == 'bua':
            if may_tinh == 'keo':
                 print('ohh!! you lose')
            else:
                 print('congratulation!! you win')
        elif nguoi_choi  == 'bao':
            if may_tinh == 'keo':
                 print('ohh!! you lose')
            else:
                 print('congratulation!! you win')       
        else:
            print('nhap sai du lieu')
    retry() 
play()           

