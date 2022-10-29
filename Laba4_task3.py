def delete(lis2, i):#Для удаления попробуйте использовать слайсирование, чтобы разбить список на два. А потом сложить списки без удаляемого значения.
    lis2 = lis2[ :i] + lis2[i + 1 :] #по требованию выполняю слайсирование
    lis2 = lis2[:-1]
    return(lis2)

lis = []
lis= input()
print(lis)

index = None
index = int(input())

print(delete(lis,index))
