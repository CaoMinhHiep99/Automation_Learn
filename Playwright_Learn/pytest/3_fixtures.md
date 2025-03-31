# I. Prepare
```python
pip install pytest playwright
python -m playwright install
```
# II. Fixtures trong Playwright với Pytest

Fixtures là một cách để cấu hình và chuẩn bị các tài nguyên mà các bài kiểm tra (tests) cần. Playwright đã setup sẵn fixture trong file `pytest_playwright.py`.

## 1. **Function scope fixtures:**

- **context**: Tạo một bối cảnh trình duyệt mới cho mỗi bài kiểm tra. Bối cảnh này tương tự như một phiên làm việc của người dùng, có thể chứa nhiều trang và session.
- **page**: Tạo một trang mới trong trình duyệt cho mỗi bài kiểm tra. Một trang là một cửa sổ hoặc tab trong trình duyệt.
- **new_context**: Tạo một bối cảnh trình duyệt mới, cho phép bạn kiểm tra nhiều người dùng hoặc tình huống với các session độc lập. Bạn có thể tùy chỉnh các tham số của bối cảnh thông qua `browser.new_context()`.

## 2. **Session scope fixtures:**

- **playwright**: Cung cấp đối tượng Playwright để tương tác với API của Playwright. Bạn không cần phải tự khởi tạo Playwright vì nó đã được cung cấp bởi fixture này.
- **browser_type**: Cung cấp một đối tượng BrowserType cho trình duyệt cụ thể (Chromium, Webkit, Firefox). Đây là loại trình duyệt mà bạn sẽ sử dụng trong các bài kiểm tra.
- **browser**: Khởi tạo một đối tượng trình duyệt (browser instance) và mở ra cho các bài kiểm tra. Đây là đối tượng cơ bản cho việc tương tác với trình duyệt.
- **browser_name**: Trả về tên của trình duyệt dưới dạng chuỗi (ví dụ: "chromium", "webkit", "firefox").
- **browser_channel**: Trả về tên kênh trình duyệt, ví dụ như kênh "chrome-beta".
- **is_chromium, is_webkit, is_firefox**: Các giá trị boolean cho biết trình duyệt hiện tại là Chromium, WebKit, hay Firefox.

## 3. **Tùy chỉnh fixture:**

- **browser_type_launch_args**: Ghi đè các tham số khởi tạo cho `browser_type.launch()`. Đây là nơi bạn có thể cấu hình các tùy chọn như các tham số dòng lệnh khi khởi tạo trình duyệt.
- **browser_context_args**: Ghi đè các tham số khởi tạo cho `browser.new_context()`. Tham số này cho phép bạn cấu hình bối cảnh trình duyệt, như thiết lập múi giờ, ngôn ngữ, v.v.

# III. How to use

## 1. Function scope fixtures:
### a. context fixture:
```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def context(playwright):
    # Tạo bối cảnh trình duyệt mới
    browser = playwright.chromium.launch()
    context = browser.new_context()
    yield context
    context.close()
    browser.close()

def test_example(context):
    # Mỗi bài kiểm tra sẽ có một bối cảnh trình duyệt mới
    page = context.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
```
### b. page fixture:
```python
@pytest.fixture(scope="function")
def page(context):
    # Tạo một trang mới cho mỗi bài kiểm tra
    page = context.new_page()
    yield page
    page.close()

def test_example(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```
### c. new_context fixture:
```python
@pytest.fixture(scope="function")
def new_context(playwright):
    # Tạo một bối cảnh trình duyệt mới với các tùy chỉnh
    browser = playwright.chromium.launch()
    context = browser.new_context(user_agent="my-custom-agent")
    yield context
    context.close()
    browser.close()

def test_example(new_context):
    # Mỗi bài kiểm tra sẽ có một bối cảnh trình duyệt mới và có thể tùy chỉnh
    page = new_context.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
```
## 2. Session scope fixtures:
### a. playwright fixture:
```python
@pytest.fixture(scope="session")
def playwright():
    # Cung cấp đối tượng Playwright cho toàn bộ phiên
    with sync_playwright() as playwright:
        yield playwright

def test_example(playwright):
    # Sử dụng đối tượng Playwright trong toàn bộ bài kiểm tra
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
    browser.close()
```
### b. browser_type fixture:
``` python
@pytest.fixture(scope="session")
def browser_type(playwright):
    # Cung cấp đối tượng BrowserType cho trình duyệt cụ thể
    return playwright.chromium

def test_example(browser_type):
    # Sử dụng đối tượng BrowserType
    browser = browser_type.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
    browser.close()
```
### c. browser fixture:
```python
@pytest.fixture(scope="session")
def browser(playwright):
    # Khởi tạo trình duyệt và cung cấp nó cho toàn bộ phiên
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

def test_example(browser):
    # Sử dụng trình duyệt trong toàn bộ bài kiểm tra
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
```
### d. browser_name fixture:
```python
@pytest.fixture(scope="session")
def browser_name(playwright):
    # Trả về tên của trình duyệt
    return playwright.chromium.name

def test_example(browser_name):
    assert browser_name == "chromium"
```
## 3. Tùy chỉnh fixture:
### a. browser_type_launch_args:
```python
@pytest.fixture(scope="session")
def browser_type_launch_args():
    # Tùy chỉnh các tham số khởi tạo khi launch trình duyệt
    return {"headless": False}

def test_example(playwright, browser_type_launch_args):
    # Khởi động trình duyệt với các tham số tùy chỉnh
    browser = playwright.chromium.launch(**browser_type_launch_args)
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
    browser.close()
```
### b. browser_context_args:
```python
@pytest.fixture(scope="session")
def browser_context_args():
    # Tùy chỉnh các tham số khi tạo bối cảnh trình duyệt
    return {"locale": "en-US", "timezone_id": "America/New_York"}

def test_example(playwright, browser_context_args):
    # Khởi tạo trình duyệt và tạo bối cảnh với các tham số tùy chỉnh
    browser = playwright.chromium.launch()
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()
    browser.close()
```