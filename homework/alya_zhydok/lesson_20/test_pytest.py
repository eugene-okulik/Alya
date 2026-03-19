import requests
import pytest


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def new_object_id():
    body = {"name": "new_name", "data": {}}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body
    )
    object_id = response.json()['id']
    print(object_id)
    yield object_id
    print('deleting object')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')


@pytest.mark.critical
def test_get_all_object(hello):
    print('before test')
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200
    print('after test')


@pytest.mark.medium
def test_get_one_object(new_object_id, hello):
    print('before test')
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    assert response['id'] == new_object_id
    print('after test')


@pytest.mark.parametrize('body', [{"name": "new_name_1", "data": {}},{"name": "new_name_2", "data": {}}, {"name": "new_name_3", "data": {}}])
def test_add_3_object(body, hello):
    print('before test')
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body
    )
    id = response.json()['id']
    assert response.status_code == 200
    data = response.json()
    print('deleting object')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{id}')
    print('after test')


def test_put_object(new_object_id, hello):
    body = {
        "name": "update_name",
        "data": {}
    }
    print('before test')
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body
    )
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'update_name'
    print('after test')


def test_patch_object(new_object_id, hello):
    body = {
        "name": "patch_name"
    }
    print('before test')
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body
    )
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'patch_name'
    assert data['data'] == {}
    print('after test')