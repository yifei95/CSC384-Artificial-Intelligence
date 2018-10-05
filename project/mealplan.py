class mealplan:
    food = {'apple': ['apple','fruit', 95, 1, 'serving', 1, 1, 1,1.15], 'apricot': ['apricot','fruit', 29, 100, 'g', 1, 1, 1,1.10], 
        'avocado': ['avocado','fruit', 135, 0.5, 'serving', 1, 1, 1, 1.20], 'banana': ['banana','fruit', 95, 1, 'serving', 1, 1, 1, 1.05],
        'blackberries': ['blackberries','fruit', 25, 1, 'serving', 1, 1, 1,2.40], 
        'blueberries': ['blueberries','fruit', 30, 1, 'serving', 1, 1, 1,0.70], 
        'cranberries': ['cranberries','fruit', 15, 1, 'serving', 1, 1, 1,0.9],
        #'cherimoya': ['fruit', 115, 1, 'serving', 1, 1, 1,3.6], 'dates': ['fruit', 107, 1, 'serving', 1, 1, 1,3.96], 
        #'fig': ['fruit', 43, 50, 'g', 1, 1, 1, 1.27], 
        'grapefruit': ['grapefruit','fruit', 48, 1, 'serving', 1, 1, 1,1.69],
        'grapes': ['grapes','fruit', 60, 1, 'serving', 1, 1, 1,2.40], 'kiwi': ['kiwi','fruit', 29, 1, 'serving', 1, 1, 1,0.80], 
	 'mango': ['mango','fruit', 107, 1, 'serving', 1, 1, 1,4.49],
        'melon': ['melon','fruit', 26, 1, 'serving', 1, 1, 1,2.09], 'nectarine': ['nectarine','fruit', 60, 1, 'serving', 1, 1, 1,1.23], 
        'orange': ['orange','fruit', 60, 1, 'serving', 1, 1, 1,1.38],'papaya': ['papaya','fruit', 74, 1, 'serving', 1, 1, 1,1.49], 
        'peach': ['peach','fruit', 36, 1, 'serving', 1, 1, 1,1.32], 'pear': ['pear','fruit', 64, 1, 'serving', 1, 1, 1,1.21], 
        'pineapple': ['pineapple','fruit', 41, 2, 'ring', 1, 1, 1, 1.00], 'plum': ['plum','fruit', 34, 2, 'serving', 1, 1, 1,2.36],
        #'raisins': ['fruit', 136, 50, 'g', 1, 1, 1,0.43], 
        'raspberries': ['raspberries', 'fruit', 25, 100, 'g', 1, 1, 1,2.85], 
        'strawberries': ['strawberries', 'fruit', 27, 100, 'g', 1, 1, 1,1.16],
        'tomato': ['tomato', 'fruit', 22, 1, 'serving', 1, 1, 1,0.53], 'watermelon': ['watermelon', 'fruit', 46, 1, 'cup', 1, 1, 1,0.50], 
        #'veal': ['meat', 94, 100, 'g', 1, 1, 1, 2.65],
        #'venison': ['meat', 94, 100, 'g', 1, 1, 1,8.13], 
        'lamb': ['lamb', 'meat', 178, 100, 'g', 1, 1, 1,1.98], 'beef': ['beef', 'meat', 164, 1, 'serving', 1, 1, 1,1.76], 
        'pork': ['pork', 'meat', 171, 100, 'g', 1, 1, 1,1.59], 
        'chicken': ['chicken', 'meat', 75, 100, 'g', 1, 1, 1,1.54], 'duck': ['duck', 'meat', 192, 100, 'g', 1, 1, 1, 6.12], 
        'egg': ['egg', 'meat', 71, 1, 'each', 1, 1, 1, 0.37], 'goose': ['goose', 'meat', 227, 100, 'g', 1, 1, 1, 1.43], 
        'turkey': ['turkey', 'meat', 122, 100, 'g', 1, 1, 1, 3.59], 'milk': ['milk', 'beverage', 50, 1, 'serving', 1, 1, 1, 0.14],
        'yogurt': ['yogurt', 'dairy', 97, 100, 'g', 1, 1, 1, 0.49], 'cheese': ['cheese', 'dairy', 201, 50, 'g', 1, 1, 1, 1.75], 
        'apple juice': ['apple juice', 'beverage', 113, 1, 'cup', 1, 1, 1, 0.53], 'orange juice': ['orange juice', 'beverage', 111, 1, 'cup', 1, 1, 1, 0.29], 
        'salmon': ['salmon', 'seafood', 155, 3, 'oz', 1, 1, 1, 4.42], 'tuna': ['tuna', 'seafood', 99, 3, 'oz', 1, 1, 1, 3.75], 
        'shrimp': ['shrimp', 'seafood', 101, 3, 'oz', 1, 1, 1, 2.94], 'scallops': ['scallops', 'seafood', 75, 3, 'oz', 1, 1, 1, 11.02], 
        'sprouted': ['sprouted', 'vegetable', 5, 1, 'serving', 1, 1, 1, 0.44], 
        'artichoke': ['artichoke', 'vegetable', 67, 1, 'serving', 1, 1, 1, 1.2], 
        'asparagus': ['asparagus', 'vegetable', 36, 1, 'cup', 1, 1, 1, 1.54], 
        #'beetroot': ['vegetable', 30, 1, 'serving', 1, 1, 1, 0.69], 
        'bok choy': ['boy choy', 'vegetable', 50, 0.5, 'serving', 1, 1, 1, 0.33], 
        'broccoli': ['broccoli', 'vegetable', 40, 1, 'cup', 1, 1, 1, 0.76], 
        'squash': ['squash', 'vegetable', 139, 1, 'serving', 1, 1, 1, 0.5], 'carrots': ['carrots', 'vegetable', 30, 1, 'serving', 1, 1, 1, 0.7], 
        'cauliflower': ['cauliflower', 'vegetable', 28, 1, 'serving', 1, 1, 1, 0.76], 'celery': ['celery', 'vegetable', 9, 3, 'stalk', 1, 1, 1, 0.88], 
        'chard': ['chard', 'vegetable', 32, 1, 'serving', 1, 1, 1, 2.5], 
        'corn': ['corn', 'vegetable', 140, 1, 'cup', 1, 1, 1, 0.37], 
        'cucumbers': ['cucumbers', 'vegetable', 30, 1, 'each', 1, 1, 1, 0.88], 
        'eggplant': ['eggplant', 'vegetable', 38, 1, 'cup', 1, 1, 1, 0.99], 
        #'garlic': ['vegetable', 4, 1, 'serving', 1, 1, 1, 1.3], 
        'beans': ['beans', 'vegetable', 31, 1, 'cup', 1, 1, 1, 1.17], 
        'green pepper': ['green pepper', 'vegetable', 16, 0.2, 'pound', 1, 1, 1, 0.55], 'kale': ['kale', 'vegetable', 43, 1, 'cup', 1, 1, 1, 2.49], 
        #'kidney beans': ['vegetable', 230, 1, 'serving', 1, 1, 1, 0.47], 
        #'lentils': ['vegetable', 212, 1, 'each', 1, 1, 1, 0.3], 
        'lettuce': ['lettuce', 'vegetable', 7, 1, 'serving', 1, 1, 1, 1.8], 
        #'lima beans': ['vegetable', 189, 1, 'cup', 1, 1, 1, 0.58], 
        'mushrooms': ['mushrooms', 'vegetable', 20, 1, 'serving', 1, 1, 1, 0.88], 
        #'navy beans': ['vegetable', 224, 1, 'serving', 1, 1, 1, 0.4], 
        'okra': ['okra', 'vegetable', 170, 1, 'serving', 1, 1, 1, 0.8],
        #'olives': ['vegetable', 45, 10, 'large', 1, 1, 1, 0.74], 
        'onions': ['onions', 'vegetable', 65, 1, 'cup', 1, 1, 1, 0.35], 'peas': ['peas', 'vegetable', 115, 1, 'serving', 1, 1, 1, 0.88], 
        #'pickles': ['vegetable', 115, 1, 'cup', 1, 1, 1, 0.5], 
        'potatoes': ['potatoes', 'main', 77, 100, 'g', 1, 1, 1, 0.4], 
        'rice': ['rice', 'main', 223, 1, 'serving', 1, 1, 1, 0.1], 
        'pasta': ['pasta', 'main', 131, 1, 'serving', 1, 1, 1, 0.46], 
        'bread': ['bread', 'main', 53, 1, 'slice', 1, 1, 1, 0.21], 
        #'snow peas': ['vegetable', 70, 1, 'serving', 1, 1, 1, 1.76], 
        'spinach': ['spinach', 'vegetable', 46, 1, 'cup', 1, 1, 1, 0.66], 
        'turnip': ['turnip', 'vegetable', 29, 1, 'serving', 1, 1, 1, 1.28], 'zucchini': ['zucchini', 'vegetable', 22, 1, 'serving', 1, 1, 1, 0.3]}


















































#class mealplan:
    #food = {'apple': ['fruit', 95, 1, 'serving', 1, 1, 1,1.15], 'apricot': ['fruit', 29, 100, 'g', 1, 1, 1,1.10], 
        #'avocado': ['fruit', 135, 0.5, 'serving', 1, 1, 1, 1.20], 'banana': ['fruit', 95, 1, 'serving', 1, 1, 1, 1.05],
        #'blackberries': ['fruit', 25, 1, 'serving', 1, 1, 1,2.40], 
        #'blueberries': ['fruit', 30, 1, 'serving', 1, 1, 1,0.70], 
        #'cranberries': ['fruit', 15, 1, 'serving', 1, 1, 1,0.9],
        ##'cherimoya': ['fruit', 115, 1, 'serving', 1, 1, 1,3.6], 'dates': ['fruit', 107, 1, 'serving', 1, 1, 1,3.96], 
        ##'fig': ['fruit', 43, 50, 'g', 1, 1, 1, 1.27], 
        #'grapefruit': ['fruit', 48, 1, 'serving', 1, 1, 1,1.69],
        #'grapes': ['fruit', 60, 1, 'serving', 1, 1, 1,2.40], 'kiwi': ['fruit', 29, 1, 'serving', 1, 1, 1,0.80], 
	 #'mango': ['fruit', 107, 1, 'serving', 1, 1, 1,4.49],
        #'melon': ['fruit', 26, 1, 'serving', 1, 1, 1,2.09], 'nectarine': ['fruit', 60, 1, 'serving', 1, 1, 1,1.23], 
        #'orange': ['fruit', 60, 1, 'serving', 1, 1, 1,1.38],'papaya': ['fruit', 74, 1, 'serving', 1, 1, 1,1.49], 
        #'peach': ['fruit', 36, 1, 'serving', 1, 1, 1,1.32], 'pear': ['fruit', 64, 1, 'serving', 1, 1, 1,1.21], 
        #'pineapple': ['fruit', 41, 2, 'ring', 1, 1, 1, 1.00], 'plum': ['fruit', 34, 2, 'serving', 1, 1, 1,2.36],
        ##'raisins': ['fruit', 136, 50, 'g', 1, 1, 1,0.43], 
        #'raspberries': ['fruit', 25, 100, 'g', 1, 1, 1,2.85], 
        #'strawberries': ['fruit', 27, 100, 'g', 1, 1, 1,1.16],
        #'tomato': ['fruit', 22, 1, 'serving', 1, 1, 1,0.53], 'watermelon': ['fruit', 46, 1, 'cup', 1, 1, 1,0.50], 
        ##'veal': ['meat', 94, 100, 'g', 1, 1, 1, 2.65],
        ##'venison': ['meat', 94, 100, 'g', 1, 1, 1,8.13], 
        #'lamb': ['meat', 178, 100, 'g', 1, 1, 1,1.98], 'beef': ['meat', 164, 1, 'serving', 1, 1, 1,1.76], 
        #'pork': ['meat', 171, 100, 'g', 1, 1, 1,1.59], 
        #'chicken': ['meat', 75, 100, 'g', 1, 1, 1,1.54], 'duck': ['meat', 192, 100, 'g', 1, 1, 1, 6.12], 
        #'egg': ['meat', 71, 1, 'each', 1, 1, 1, 0.37], 'goose': ['meat', 227, 100, 'g', 1, 1, 1, 1.43], 
        #'turkey': ['meat', 122, 100, 'g', 1, 1, 1, 3.59], 'milk': ['beverage', 50, 1, 'serving', 1, 1, 1, 0.14],
        #'yogurt': ['dairy', 97, 100, 'g', 1, 1, 1, 0.49], 'cheese': ['dairy', 201, 50, 'g', 1, 1, 1, 1.75], 
        #'apple juice': ['beverage', 113, 1, 'cup', 1, 1, 1, 0.53], 'orange juice': ['beverage', 111, 1, 'cup', 1, 1, 1, 0.29], 
        #'salmon': ['seafood', 155, 3, 'oz', 1, 1, 1, 4.42], 'tuna': ['seafood', 99, 3, 'oz', 1, 1, 1, 3.75], 
        #'shrimp': ['seafood', 101, 3, 'oz', 1, 1, 1, 2.94], 'scallops': ['seafood', 75, 3, 'oz', 1, 1, 1, 11.02], 
        #'sprouted': ['vegetable', 5, 1, 'serving', 1, 1, 1, 0.44], 
        #'artichoke': ['vegetable', 67, 1, 'serving', 1, 1, 1, 1.2], 
        #'asparagus': ['vegetable', 36, 1, 'cup', 1, 1, 1, 1.54], 
        ##'beetroot': ['vegetable', 30, 1, 'serving', 1, 1, 1, 0.69], 
        #'bok choy': ['vegetable', 50, 0.5, 'serving', 1, 1, 1, 0.33], 
        #'broccoli': ['vegetable', 40, 1, 'cup', 1, 1, 1, 0.76], 
        #'squash': ['vegetable', 139, 1, 'serving', 1, 1, 1, 0.5], 'carrots': ['vegetable', 30, 1, 'serving', 1, 1, 1, 0.7], 
        #'cauliflower': ['vegetable', 28, 1, 'serving', 1, 1, 1, 0.76], 'celery': ['vegetable', 9, 3, 'stalk', 1, 1, 1, 0.88], 
        #'chard': ['vegetable', 32, 1, 'serving', 1, 1, 1, 2.5], 
        #'corn': ['vegetable', 140, 1, 'cup', 1, 1, 1, 0.37], 
        #'cucumbers': ['vegetable', 30, 1, 'each', 1, 1, 1, 0.88], 
        #'eggplant': ['vegetable', 38, 1, 'cup', 1, 1, 1, 0.99], 
        ##'garlic': ['vegetable', 4, 1, 'serving', 1, 1, 1, 1.3], 
        #'beans': ['vegetable', 31, 1, 'cup', 1, 1, 1, 1.17], 
        #'green pepper': ['vegetable', 16, 0.2, 'pound', 1, 1, 1, 0.55], 'kale': ['vegetable', 43, 1, 'cup', 1, 1, 1, 2.49], 
        ##'kidney beans': ['vegetable', 230, 1, 'serving', 1, 1, 1, 0.47], 
        ##'lentils': ['vegetable', 212, 1, 'each', 1, 1, 1, 0.3], 
        #'lettuce': ['vegetable', 7, 1, 'serving', 1, 1, 1, 1.8], 
        ##'lima beans': ['vegetable', 189, 1, 'cup', 1, 1, 1, 0.58], 
        #'mushrooms': ['vegetable', 20, 1, 'serving', 1, 1, 1, 0.88], 
        ##'navy beans': ['vegetable', 224, 1, 'serving', 1, 1, 1, 0.4], 
        #'okra': ['vegetable', 170, 1, 'serving', 1, 1, 1, 0.8],
        ##'olives': ['vegetable', 45, 10, 'large', 1, 1, 1, 0.74], 
        #'onions': ['vegetable', 65, 1, 'cup', 1, 1, 1, 0.35], 'peas': ['vegetable', 115, 1, 'serving', 1, 1, 1, 0.88], 
        ##'pickles': ['vegetable', 115, 1, 'cup', 1, 1, 1, 0.5], 
        #'potatoes': ['main', 77, 100, 'g', 1, 1, 1, 0.4], 
        #'rice': ['main', 223, 1, 'serving', 1, 1, 1, 0.1], 
        ##'snow peas': ['vegetable', 70, 1, 'serving', 1, 1, 1, 1.76], 
        #'spinach': ['vegetable', 46, 1, 'cup', 1, 1, 1, 0.66], 
        #'turnip': ['vegetable', 29, 1, 'serving', 1, 1, 1, 1.28], 'zucchini': ['vegetable', 22, 1, 'serving', 1, 1, 1, 0.3]}



