animals = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
animal=input('I want to find:')
so_luong=len(animals)
for i in animals:
    if animal==i:
        print('There is',animal,'in list of animals')
        break
    else:
        print('Ko co')
print('Number of animals:',so_luong)