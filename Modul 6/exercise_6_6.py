from pathlib import Path

path = Path('C:/Users/User/Downloads/Receptions')

text = '60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil' \
       '60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon' \
       '60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce' \
       '60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese' \
       '60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water'

with open(path, 'w') as fh:
    fh.write(text)


def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        list_lines = fh.readlines()
        for line in list_lines:
            line = line.replace('\n', '')
            list_str = line.split(',')
            if list_str[0] == search_id:
                dict_line = {
                    'id': list_str[0],
                    'name': list_str[1],
                    'ingredients': [
                        list_str[2],
                        list_str[3],
                        list_str[4]
                    ]
                }
                return dict_line
            else:
                return None


print(get_recipe(path, "60b90c1c13067a15887e1ae1"))
