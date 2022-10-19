import numpy as np


def troca_linha(M, i, j):
  M[[i, j], :] = M[[j, i], :]

  return M
 

def divide_linha(M, i, k):
  M[i, :] = M[i, :]/k

  return M
  
  
  def subtrai_linha(M, i, j, k=1):
    M[i, :] = M[i, :] - k*M[j, :]

  return M
  
  
  def acha_pivo(M, i):
    for j, linha in enumerate(M):
      for coluna, valor in enumerate(linha):
        if valor != 0:
          if coluna == i:
            return j
          break
    return 
  
  
  def ajeita_matriz(M):
    """
    Função para colocar a Matriz M na forma correta do Gauus-Jordan
    """
    ja_foi = -1
    for col in range(len(M[0]) - 1):

      if col < ja_foi: continue

      for lin in range(len(M)):
        if M[lin][col] == 0:
          num = acha_pivo(M, col)

          if num is not None:
            M = troca_linha(M, num, lin)
            ja_foi = col
            break

    return M
  
  
  def gauss_jordan(A, b):
    A = np.column_stack((A, b))
    A = ajeita_matriz(A)

    for coluna in range(len(A[0])):
      linha_pivo = acha_pivo(A, coluna)

      if linha_pivo is not None:
        k = A[linha_pivo][coluna]
        A = divide_linha(A, linha_pivo, k)

        for chave, linha0 in enumerate(A[:, coluna]):
          if linha0 == 0:
            linha_aux = chave
            break
          else:
            linha_aux = linha_pivo

        for indice, linha in enumerate(A):
          if indice == linha_pivo:
            continue
        
          A = subtrai_linha(A, indice, linha_pivo, A[indice][coluna])
        
    #Nesse ponto a matriz já está pronta, você pode modificar o código
    #para imprimi-la se quiser
  
    tam = len(A)
    for i in range(tam):
        if A[i, i] == 0:
          for j in range(i + 1, len(A[0]) - 1):
            if  A[i, j] != 0: 
              return "O Sistema possui infinitas soluções"

          return "O Sistema não possui solução"

    return A
