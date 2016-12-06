categories = {
    'test_category_1':{
        'title': 'test_category_1',
        'description': 'test category 1',
        'slug': 'test_category_1',
        'featured': True,
        'active': True
    },
    'test_category_2': {
        'title': 'test_category_2',
        'description': 'test category 2',
        'slug': 'test_category_2',
        'featured': True,
        'active': True
    },
    'test_category_3': {
        'title': 'test_category_3',
        'description': 'test category 3',
        'slug': 'test_category_3',
        'featured': True,
        'active': True
    },
}

images = {
    'test_image_1': {
        'image': 'products/images/search.jpg',
        'featured': True,
        'thumbnail': True,
        'active': True
    }
}

products = [
    {
        'categories': [
            categories['test_category_1'],
            categories['test_category_2']
        ],
        'images': [
            images['test_image_1'],
        ],
        'title': 'test_product_1',
        'description': 'test product 1',
        'price': 9.99,
        'sale_price': 5.99,
        'slug': 'test_product_1',
        'featured': True,
        'active': True
    }
]
