import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Cấu hình trình duyệt headless (có thể bỏ dòng này nếu muốn chạy với giao diện)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Chạy headless (không hiển thị giao diện)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Đảm bảo xác định đường dẫn đầy đủ tới chromedriver
chromedriver_path = "/usr/bin/chromedriver"
service = Service(chromedriver_path)

# Khởi tạo trình duyệt cho website thứ nhất
driver1 = webdriver.Chrome(service=service, options=chrome_options)

# URL trang chủ thứ nhất
url1 = "https://anivia9001s.blogspot.com"
driver1.get(url1)
print(f"Đang mở trang: {url1}")

# Khởi tạo trình duyệt cho website thứ hai
driver2 = webdriver.Chrome(service=service, options=chrome_options)

# URL trang chủ thứ hai
url2 = "https://ads.alexamaster.com/?id=182"  # Bạn có thể thay đổi URL này
driver2.get(url2)
print(f"Đang mở trang: {url2}")

# Tạm dừng trong 24 giờ (24 * 60 * 60 giây) để giữ các trang này mở
time.sleep(24 * 60 * 60)  # 24 giờ = 24 * 60 * 60 giây

# Sau 24 giờ, trình duyệt sẽ tự động đóng
driver1.quit()
driver2.quit()
