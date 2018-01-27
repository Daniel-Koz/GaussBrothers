def Seidel(A,b,x,dr,limite):
    crit = 0
    continua = 1
    converge = 1
    while(continua == 1 & converge == 1):
        xTmp = x[:]
        for i in range(0,len(A)):
            aux = 0
            for j in range(0,len(A)):
                if (i != j):
                    aux += (A[i][j]*x[j])
                    x[i] = (b[i] - aux)/A[i][i]
        continua = testa(xTmp,x,dr)
        converge = conv(xTmp,x)
        if (crit > limite):
            continua = 0
            print("Sem solução satisfatória depois de",crit,"iterações")
    return x

def Jacobi(A,b,x,dr,limite):
    crit = 0
    continua = 1
    converge = 1
    while(continua == 1 & converge == 1):
        xTmp = x[:]
        for i in range(0,len(A)):
            aux = 0
            for j in range(0,len(A)):
                if (i != j):
                    aux += (A[i][j]*xTmp[j])
                    x[i] = (b[i] - aux)/A[i][i]
        continua = testa(xTmp,x,dr)
        converge = conv(xTmp,x)
        crit += 1
        if (crit > limite):
            continua = 0
            print("Sem solução satisfatória depois de",crit,"iterações")
    return x

def testa(r1,r2,dr):
    result = 0
    print("\nNo vetor resposta\n",r2)
    for i in range(0,len(r1)):
        print("Desvio x",(i+1),"=",abs(r1[i] - r2[i]))
        if (abs(r1[i] - r2[i]) >= dr ):
            result = 1
    return result

def conv(r1,r2):
    result = 1
    for i in range(0,len(r1)):
        if (abs(r1[i] - r2[i]) > 9999):
            result = 0
            print("Desvio muito grande, sistema não converge.")
            break
    return result

def escolha(A,b,x,dr,limite):
    validade = 1
    swi = input("1: Jacobi\n2: Seidel\n:")
    if (swi == "1"):
        print("Resposta:",Jacobi(A,b,x,dr,limite))
    elif (swi == "2"):
        print("Resposta:",Seidel(A,b,x,dr,limite))
    else:
        print("Opção inválida, retornando.")
        validade = 0
    return validade

def mainJS():
    limite = 999
    print("Iniciando Jacobi e Seidel")
    varQ = 1
    while(varQ >= 1):
        esco = 0
        varQ = int(input("Quantas variáveis? (0 para ancerrar):"))
        if(varQ >= 1):
            matX = [x[:] for x in [[0.0]*(varQ+1)]*varQ]
            
            for i in range(varQ):
                for j in range(varQ+1):
                    print("Sistema:",matX)
                    print("Linha:",i+1,"Coluna",j+1,":")
                    matX[i][j] = float(input())
            
            res = [0.0]*varQ
            vet = [0.0]*varQ
            mat = [x[:] for x in [[0.0]*(varQ)]*varQ]
            
            for i in range(0,varQ):
                vet[i] = matX[i][varQ]
                for j in range(0,varQ):
                    mat[i][j] = matX[i][j]
            
            desV = float(input("dr máximo:"))

            print("Sistema:",matX)
            
            while(esco == 0):
                print("Resolver Sistema utilizando qual metodo?")
                esco = escolha(mat,vet,res,desV,limite)
        else:
            print("Encerrando Jacobi e Seidel")

mainJS()
