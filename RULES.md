# CSD203 Data Structures & Algorithms Development Rules

Tài liệu quy chuẩn triển khai thuật toán, phong cách code và quy trình theo dõi tiến trình nội bộ dành riêng cho repository **CSD203-DSA-Python**.

---

## 1. Phong Cách Lập Trình (Personal CSD Conventions)

Khi mở rộng hoặc bổ sung code vào thư mục `src/`:
1. **Tính Tương Thích Kép (Dual Compatibility):**
   - Luôn hỗ trợ song song cả chuẩn OOP Python và tên hàm quen thuộc trong đề thi Practical Exam (PE) của FPT University:
     - `isEmpty()` song song với `check_empty()`
     - `length()` song song với `__len__()`
     - `insertLast()`, `insertFirst()` song song với `append()`, `prepend()`
     - `display()` in các phần tử cách nhau bởi khoảng trắng (`end=" "`)
   - Với đồ thị (`Graph`), luôn hỗ trợ đầu vào cả dạng số nguyên (`0`, `1`, `...`) và ký tự đỉnh (`'A'`, `'B'`, `...`) qua hàm chuyển đổi:
     ```python
     s = ord(start.upper()) - 65 if isinstance(start, str) else start
     chr(u + 65)
     ```
2. **Triển Khai Thuần DSA (Pure DSA Implementation):**
   - Không dùng thư viện dựng sẵn ngoài luồng để giải quyết bài toán cốt lõi. Ưu tiên tự cài đặt logic giải thuật để phục vụ việc học tập, thi cử và ôn luyện phỏng vấn.
3. **Mã Nguồn Tinh Gọn & Sáng Rõ:**
   - Đặt tên biến trực quan, có type hints nhẹ nhàng, docstring giải thích ngắn gọn mục đích và độ phức tạp thời gian/không gian Big-O ($O(V+E)$, $O(E \log V)$, $O(n \log n)$, $O(\log n)$, v.v.).

---

## 2. Quy Chuẩn Kiểm Thử Tự Động (Unit Testing)

- **Vị trí file test:** Toàn bộ test suite được đặt tập trung tại `tests/test_dsa.py`.
- **Yêu cầu độ phủ:** Mọi cấu trúc dữ liệu hoặc thuật toán mới BẮT BUỘC phải có unit test tương ứng trong `test_dsa.py`.
- **Kiểm tra trước khi commit:** Chạy lệnh `python tests/test_dsa.py` và bảo đảm **100% tests pass (OK)** trước khi push.

---

## 3. Quy Trình Quản Lý Tiến Trình (Algorithm Roadmap Protocol)

- Toàn bộ danh mục thuật toán và phân bổ theo từng buổi (Session) được theo dõi tại **[`ALGORITHM_PROGRESS.md`](ALGORITHM_PROGRESS.md)**.
- **Ký hiệu trạng thái:**
  - `[x]` **Hoàn thành:** Đã viết mã nguồn, có test suite pass 100%, đã cập nhật tài liệu và push lên GitHub.
  - `[-]` **Đang thực hiện:** Thuật toán đang code hoặc đang debug trong phiên làm việc.
  - `[ ]` **Chưa thực hiện:** Thuật toán trong danh mục chờ của các phiên tiếp theo.
- Khi bắt đầu một buổi mới: Mở `ALGORITHM_PROGRESS.md`, chọn Session tiếp theo và triển khai theo danh sách `[ ]`.

---

## 4. Quy Chuẩn Git Commit & Push

- **Remote:** `https://github.com/huanight19RaH/CSD203-DSA-Python.git`
- **Nhánh chính:** `main`
- **Author commit BẮT BUỘC:** `--author="RaH11 <hungnguyen.190206@gmail.com>"`
- **Quy chuẩn thông điệp commit:** Conventional Commits (`feat(graph): ...`, `feat(heap): ...`, `docs: ...`, `test: ...`).
