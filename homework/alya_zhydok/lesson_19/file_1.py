import requests


def all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def new_post():
    body = {
        "name": "new_name",
        "data": {}
    }
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body
    )
    return response.json()['id']


def one_post():
    id = new_post()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{id}')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data['id'] == id


def post_a_post():
    body = {
        "name": "new_name",
        "data": {}
    }
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    data = response.json()
    assert data['name'] == 'new_name'
    assert data['data'] == {}
    return response.json()['id']


def clear(id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{id}')


def put_a_post():
    id = new_post()
    body = {
        "name": "new_name1",
        "data": {}
    }
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    data = response.json()
    assert data['name'] == 'new_name1'
    assert data['data'] == {}
    return response.json()['id']


def patch_a_post():
    id = new_post()
    body = {
        "name": "new_name1"
    }
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    data = response.json()
    assert data['name'] == 'new_name1'
    assert data['data'] == {}
    return response.json()['id']


def delete_a_post():
    id = new_post()
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{id}'
    )
    assert response.status_code == 200, 'Status code is incorrect'


delete_a_post()
