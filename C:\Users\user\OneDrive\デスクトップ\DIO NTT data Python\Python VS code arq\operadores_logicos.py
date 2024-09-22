# and = para ser True_tudo_tem_que_ser_True
# or = para ser True_apenas_um_tem_que_ser_True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)
