print ('Wie heiße dich?')
name = input()
if name == 'Andrey' or name == 'Андрей': 
    print('Schön dich kennenzulernen, kleiner Filzstiefel, ', name, '!', sep='')
elif name == 'Yura' or name == 'Юра': 
        print('Es lebe der große, ', name, '!', sep='')
else:
        print('Guten Tag gewöhnliche Person, ', name, '!', sep='')
        
age = int(input('Wie alt bist du, ' + name + '?'))
print ('Ich dachte du wärst',  age + 1, 'Jahre alt!')



