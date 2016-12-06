from schemas import product, category

products = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'schema': product,
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },
}

categories = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'schema': category,
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },
}
