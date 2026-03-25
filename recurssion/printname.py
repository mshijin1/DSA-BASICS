def print_name(name:str, n:int, limit:int):
    if n==limit:
        return 
    print(name )
    print_name(name, n+1, limit)
    
print_name("shijin", 0, 5)