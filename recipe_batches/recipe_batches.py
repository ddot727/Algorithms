#!/usr/bin/python
'''
Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

```python
{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
```
[Notes]

Need to take in 2 dict: one = recipe, other = what you gotz

Compare what you gotz to the recipe, see if basic cookies can be made

If so, see how many batches can be made. **Make sure you use the key with the lowest amount of batches as answer**

'''

import math


def recipe_batches(recipe, ingredients):
    store = []

    if len(ingredients) != len(recipe):
        return 0
    else:
        for i in recipe:
            for j in ingredients:
                if(i == j):
                    store.append(ingredients[j] / recipe[i])
    num_of_batches = int(min(store))

    return num_of_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
