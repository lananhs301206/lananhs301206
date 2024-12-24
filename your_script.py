import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Cấu hình trình duyệt headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Chạy headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Khởi tạo trình duyệt với cấu hình trên
driver = webdriver.Chrome(options=chrome_options)

# URL trang web của bạn
base_url = "https://www.9xcongit.com"

# Hàm lấy tất cả các URL hợp lệ trên website (bao gồm các trang bài viết, trang chính, v.v.)
def get_all_links(url):
    driver.get(url)
    links = driver.find_elements(By.TAG_NAME, 'a')
    valid_links = set()  # Dùng set để loại bỏ trùng lặp

    for link in links:
        href = link.get_attribute('href')
        if href and href.startswith(base_url):  # Lọc chỉ lấy các liên kết trên website của bạn
            valid_links.add(href)

    return list(valid_links)

# Hàm để load ngẫu nhiên trang trên website và tạm dừng 2 đến 5 phút sau mỗi lần load
def load_random_page():
    visited_urls = set()  # Lưu lại các URL đã duyệt để tránh lặp lại

    while True:
        # Lấy tất cả các URL hợp lệ trên website
        all_links = get_all_links(base_url)

        # Lọc các URL chưa được duyệt
        remaining_links = [link for link in all_links if link not in visited_urls]

        # Nếu tất cả các trang đã được duyệt, reset lại danh sách đã duyệt
        if not remaining_links:
            print("Đã duyệt hết các trang, bắt đầu lại từ đầu.")
            visited_urls.clear()
            remaining_links = all_links  # Bắt đầu duyệt lại tất cả các trang

        # Chọn ngẫu nhiên một URL từ danh sách còn lại
        random_url = random.choice(remaining_links)
        print(f"Đang tải trang ngẫu nhiên: {random_url}")

        # Mở trang ngẫu nhiên
        driver.get(random_url)
        visited_urls.add(random_url)  # Thêm trang đã duyệt vào danh sách đã duyệt

        # Tạo thời gian ngẫu nhiên để tạm dừng giữa 2 đến 5 phút (120 giây đến 300 giây)
        wait_time = random.uniform(2 * 60, 5 * 60)
        print(f"Chờ {int(wait_time // 60)} phút {int(wait_time % 60)} giây trước khi chuyển sang trang tiếp theo...")
        time.sleep(wait_time)  # Tạm dừng ngẫu nhiên trong khoảng thời gian đã tính

# Bắt đầu quá trình duyệt ngẫu nhiên
load_random_page()

# Lưu ý: Trình duyệt vẫn mở, bạn có thể làm các thao tác khác hoặc kiểm tra thêm.
# driver.quit()  # Dòng này bị bỏ qua để không đóng trình duyệt
