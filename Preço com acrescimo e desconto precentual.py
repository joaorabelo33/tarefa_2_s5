dinheiro=float(input())
porcentagem=float(input())
formula=porcentagem/100
acrecimo=dinheiro+(dinheiro*formula)
desconto=dinheiro-(dinheiro*formula)
print(f'{acrecimo:.2f}')
print(f'{desconto:.2f}')
