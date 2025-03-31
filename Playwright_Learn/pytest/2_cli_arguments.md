
# Thông số dòng lệnh Playwright

- `--headed`: Chạy thử nghiệm trong chế độ "headed" (hiển thị giao diện trình duyệt mặc định là "headless" tức là không hiển thị giao diện).

- `--browser`: Chạy thử nghiệm trên một trình duyệt khác, ví dụ như chromium, firefox hoặc webkit.
  Tham số này có thể được chỉ định nhiều lần nếu cần.

- `--browser-channel`: Xác định kênh trình duyệt cần sử dụng.

- `--slowmo`: Chạy các thử nghiệm với tốc độ chậm, giúp dễ dàng theo dõi quá trình thử nghiệm.

- `--device`: Thiết lập thiết bị giả lập để thử nghiệm trên thiết bị cụ thể như điện thoại di động, máy tính bảng.

- `--output`: Chỉ định thư mục để lưu trữ các tài liệu (artifacts) được tạo ra trong quá trình thử nghiệm.

- `--tracing`: Chọn xem có ghi lại trace (dấu vết) cho mỗi thử nghiệm hay không.
  Các tùy chọn có thể là "on", "off", hoặc "retain-on-failure" (ghi lại chỉ khi thử nghiệm thất bại).

- `--video`: Chọn xem có ghi video cho mỗi thử nghiệm hay không.
  Các tùy chọn tương tự như "tracing" (on, off, retain-on-failure).

- `--screenshot`: Chọn xem có tự động chụp ảnh màn hình sau mỗi thử nghiệm hay không.
  Các tùy chọn có thể là "on", "off", hoặc "only-on-failure" (chụp ảnh màn hình chỉ khi thử nghiệm thất bại). Không chụp ảnh màn hình nào cả.

# Workflow của CLI Arguments trong Pytest và Playwright

### 1. **Khởi tạo pytest**:
   - Khi bạn chạy pytest từ dòng lệnh, pytest bắt đầu khởi tạo và kiểm tra các tham số đầu vào (CLI arguments).
   
### 2. **Thêm tùy chọn CLI trong pytest**:
   - Trong file `conftest.py`, bạn có thể sử dụng hàm `pytest_addoption` để khai báo các tùy chọn CLI bạn muốn hỗ trợ. Ví dụ, bạn có thể khai báo một tham số `--headless` để xác định liệu Playwright có chạy trong chế độ headless (không giao diện) hay không.
   
### 3. **Tạo Fixture để xử lý CLI arguments**:
   - Sau khi khai báo các tham số CLI trong `conftest.py`, bạn cần tạo các fixture để trích xuất giá trị của các đối số này và chuyển chúng vào trong các test case. Ví dụ, fixture `headless_option` sẽ lấy giá trị của `--headless` từ dòng lệnh.
   
### 4. **Sử dụng giá trị CLI argument trong test**:
   - Trong các test, bạn có thể sử dụng fixture này để truyền giá trị từ CLI argument vào trong test. Ví dụ, bạn có thể sử dụng giá trị `headless_option` để quyết định xem trình duyệt sẽ được chạy trong chế độ headless hay không khi sử dụng Playwright.

### 5. **Chạy tests với các tham số CLI**:
   - Khi chạy pytest, bạn có thể cung cấp các tham số CLI để điều khiển cách thức thực thi của các tests. Ví dụ, bạn có thể chạy pytest với tham số `--headless` để chạy Playwright trong chế độ headless:
   
   ```bash
   pytest --headless

# Tạo tệp conftest.py để cấu hình pytest: Trong tệp conftest.py, bạn có thể sử dụng pytest_addoption để thêm các tham số CLI tùy chỉnh. Ví dụ:
```python
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=True, help="Run Playwright tests in headless mode"
    )

@pytest.fixture
def browser_context_args(request):
    headless = request.config.getoption("--headless")
    return {"headless": headless}
```

# How to use
```python
pytest --browser=chromium --tracing=on
```

