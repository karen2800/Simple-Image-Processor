import json

data = {}  

data['start'] = []  

data['start'].append({  
    'action': 'provide image',
    'method': 'GET',
    'reference': '/<image>'
})

def generateData(image):
    data['actions'] = [] 

    data['actions'].append({  
        'action': 'flip horizontal',
        'method': 'GET',
        'reference': '/' + image + '/flip_h'
    })
    data['actions'].append({  
        'action': 'flip vertically',
        'method': 'GET',
        'reference': '/' + image + '/flip_v'
    })
    data['actions'].append({  
        'action': 'Rotate n degrees',
        'method': 'GET',
        'reference': '/' + image + '/rotate_n/<n>'
    })
    data['actions'].append({  
        'action': 'Convert to grayscale',
        'method': 'GET',
        'reference': '/' + image + '/grayscale'
    })
    data['actions'].append({  
        'action': 'Resize',
        'method': 'GET',
        'reference': '/' + image + '/resize/<width>/<height>'
    })
    data['actions'].append({  
        'action': 'Generate thumbnail',
        'method': 'GET',
        'reference': '/' + image + '/thumbnail'
    })
    data['actions'].append({  
        'action': 'Rotate left',
        'method': 'GET',
        'reference': '/' + image + '/rotate_l'
    })
    data['actions'].append({  
        'action': 'Rotate right',
        'method': 'GET',
        'reference': '/' + image + '/rotate_r'
    })
    data['actions'].append({  
        'action': 'provide image',
        'method': 'GET',
        'reference': '/<image>'
    })

def getData():
    return data

