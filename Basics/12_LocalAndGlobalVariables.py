a = 10          # global variable

def something():
    a = 15      # local variable
    globals()['a'] = 20   # modifies the GLOBAL variable
    print("inside :", a)
something()

print("outside :", a)
