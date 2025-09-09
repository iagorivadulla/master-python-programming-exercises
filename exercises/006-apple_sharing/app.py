def apple_sharing(n,k):
  apples_got = k // n
  apples_basket = k % n
  return apples_got, apples_basket
 

print(apple_sharing(6,50))
