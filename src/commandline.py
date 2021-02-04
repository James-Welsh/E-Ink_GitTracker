import get_data as gd

data = gd.get_display_data()

print('______________________________________\n')
print("NAME: " + data['name'])
print("TIME: " + data['updated'])
print('______________________________________')
