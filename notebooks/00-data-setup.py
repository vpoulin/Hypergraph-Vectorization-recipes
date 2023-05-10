import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import csv

# We will make use of the recipe dataset. It consists of 39,774 recipes (hyperedges) that are sets of vertices (6,714 ingredients total). The largest recipe has 65 ingredients (must be good!). Each recipe is assigned to a country (edge label), 20 countries total. The data and some work done with it can be found here:

# This function 
# * reads the data
# * keeps only the recipes containing at least 3 ingredients (after this pruning we are left with 6,714 ingredients and 39,559 recipes)
# * chooses a country color mapping that respects countries' proximities, or continent - nearby countries are assigned to similar colors. This is to help with the eye-ball evaluation of the visualization.


def read_format_recipes(recipe_min_size=3):
    ingredients_id = pd.read_csv('../data/cat-edge-Cooking/node-labels.txt', sep='\t', header=None)
    ingredients_id.index = [x+1 for x in ingredients_id.index]
    ingredients_id.columns = ['Ingredient']
    
    recipes_with_id = []
    with open('../data/cat-edge-Cooking/hyperedges.txt', newline = '') as hyperedges:
        hyperedge_reader = csv.reader(hyperedges, delimiter='\t')
        for hyperedge in hyperedge_reader:
            recipes_with_id.append(hyperedge)
            
    recipes_all = [[ingredients_id.loc[int(i)]['Ingredient'] for i in x] for x in recipes_with_id]
    
    # Keep recipes with 3 ingredients and more
    keep_recipes = np.where(np.array([len(x) for x in recipes_all])>=recipe_min_size)[0]
    recipes = [recipes_all[i] for i in keep_recipes]
    
    recipes_label_id_all = pd.read_csv('../data/cat-edge-Cooking/hyperedge-labels.txt', sep='\t', header=None)
    recipes_label_id_all.columns = ['label']
    recipes_label_id = recipes_label_id_all.iloc[keep_recipes].reset_index()

    label_name = pd.read_csv('../data/cat-edge-Cooking/hyperedge-label-identities.txt', sep='\t', header=None)
    label_name.columns = ['country']
    label_name.index = [x+1 for x in label_name.index]
    
    grps_tmp = {
        'asian' : ('chinese', 'filipino', 'japanese','korean', 'thai', 'vietnamese'),
        'american' : ('brazilian', 'mexican', 'southern_us'),
        'english' : ('british', 'irish'),
        'islands' : ('cajun_creole', 'jamaican'),
        'europe' : ('french', 'italian', 'spanish'),
        'others' : ('greek', 'indian', 'moroccan', 'russian')
    }

    grps = {key:[key+'.'+x for x in value] for key, value in grps_tmp.items()}


    color_key = {}
    for l, c in zip(grps['asian'], sns.color_palette("Blues", 6)[0:]):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    for l, c in zip(grps['american'], sns.color_palette("Purples", 4)[1:]):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    for l, c in zip(grps['others'], sns.color_palette("YlOrRd", 4)):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    for l, c in zip(grps['europe'], sns.color_palette("light:teal", 4)[1:]):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    for l, c in zip(grps['islands'], sns.color_palette("light:#660033", 4)[1:3]):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    for l, c in zip(grps['english'], sns.color_palette("YlGn", 4)[1:]):
        color_key[l] = matplotlib.colors.rgb2hex(c)
    color_key["ingredient"] = "#777777bb"
    
    new_names = []
    for key, value in grps.items():
        new_names = new_names + value

    label_name['new_label'] = [new_name for x in label_name.country for new_name in new_names if x in new_name]
    
    # Perform data swaping to control the order of the legend in plots. Want order to be alphabetical order.
    # Not SUPER clean!
    
    n = label_name.shape[0]
    indices_to_front = [recipes_label_id[recipes_label_id.label==i].index[n] for i in label_name.sort_values('new_label').index]
    for i, j in enumerate(indices_to_front):
        recipes[i], recipes[j] = recipes[j], recipes[i]
        recipes_label_id.label[i], recipes_label_id.label[j] = recipes_label_id.label[j], recipes_label_id.label[i] 
    
    return(recipes, recipes_label_id, ingredients_id, label_name, color_key)

