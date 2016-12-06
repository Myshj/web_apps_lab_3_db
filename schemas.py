category = {
    'title': {
        'type': 'string',
        #'minLength': 1,
        #'maxLength': 120,
        'required': True
    },
    'description': {
        'type': 'string',
        'required': False
    },
    'slug': {
        'type': 'string',
        #'minLength': 1,
        'required': True,
        'unique': True
    },
    'featured': {
        'type': 'boolean',
        'required': True
    },
    'active': {
        'type': 'boolean',
        'default': True
    }
}

image = {
    'image': {
        'type': 'string',
        'required': True
    },
    'featured': {
        'type': 'boolean',
        'default': False
    },
    'thumbnail': {
        'type': 'boolean',
        'default': True,
    },
    'active': {
        'type': 'boolean',
        'default': True
    }
}

product = {
    'categories': {
        'type': 'list',
        # 'schema': {
        #     'type': 'dict',
        #     'schema': category
        # },
        'required': True
    },
    'images': {
        'type': 'list',
        # 'schema': {
        #     'type': 'dict',
        #     'schema': image
        # },
        'required': True
    },
    'title': {
        'type': 'string',
        #'minLength': 1,
        #'maxLength': 120,
        'required': True
    },
    'description': {
        'type': 'string',
        'required': False
    },
    'price': {
        'type': 'float',
        'required': True
    },
    'sale_price': {
        'type': 'float',
        'required': False
    },
    'slug': {
        'type': 'string',
        #'minLength': 1,
        'required': True,
        'unique': True
    },
    'featured': {
        'type': 'boolean'
    },
    'active': {
        'type': 'boolean',
        'default': True
    }
}
