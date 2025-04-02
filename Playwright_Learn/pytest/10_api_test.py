import pytest
from playwright.sync_api import sync_playwright, Page

# Fixture tạo API client
@pytest.fixture(scope="module")
def api_client():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Dùng context.request để gửi API requests
        client = context.request
        yield client
        browser.close()

# Kiểm thử GET request
def test_get_request(api_client):
    response = api_client.get('https://jsonplaceholder.typicode.com/posts/1')

    # Kiểm tra mã trạng thái HTTP là 200
    assert response.status == 200

    # Kiểm tra nội dung phản hồi (Response)
    json_response = response.json()
    assert json_response['id'] == 1
    assert json_response['userId'] == 1

# Kiểm thử POST request
def test_post_request(api_client):
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.post('https://jsonplaceholder.typicode.com/posts', data=data)

    # Kiểm tra mã trạng thái HTTP là 201 (tạo mới thành công)
    assert response.status == 201

    # Kiểm tra dữ liệu trong phản hồi
    json_response = response.json()
    assert json_response['title'] == 'foo'
    assert json_response['body'] == 'bar'
    assert json_response['userId'] == 1
