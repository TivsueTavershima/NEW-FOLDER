meaning = 40

if meaning > 60:
   print("ride on!")
else:
    print("not today")
    
    
cast = (1980)
sentence = "i like rock music in " + str(cast) + "s"
print(sentence)

multiline = '''
hello, how are you doing 
                    just checking in!
                                                                          all good.
'''
print(multiline)



print(len(multiline))
multiline +="                                                              "
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
# build menu

title = "menu".upper()
print(title.center(20, "="))

sentence = f"{"====" * 5}\nHello, how are you?\n{"====" * 5}"
print(sentence)

print("coffee".ljust(20, ".") + "$1".rjust(4))