a = int(input())
b = int(input())

print(f"{a*(b%10)}")
print(f"{a*(b%100//10)}")
print(f"{a*(b//100)}")
print(f"{a*b}")