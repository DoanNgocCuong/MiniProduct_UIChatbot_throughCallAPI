# Đây là file frontend.py, nó chứa code để tạo giao diện cho ứng dụng chat

# Nhập thư viện streamlit để tạo giao diện web
import streamlit as st

# Tạo một lớp để quản lý giao diện chat
class ChatAssistantFrontend:
    def __init__(self):
        # Đặt tiêu đề cho trang web
        st.title("CSKH-StepUpEducation Assistant")
        # Khởi tạo trạng thái cho phiên chat
        self.initialize_session_state()

    def initialize_session_state(self):
        # Tạo một nơi để lưu trữ các tin nhắn trong cuộc trò chuyện
        # Nếu chưa có tin nhắn nào, tạo một danh sách trống
        if "messages" not in st.session_state: 
            st.session_state.messages = []

    def display_chat_history(self):
        # Hiển thị tất cả các tin nhắn đã có trong cuộc trò chuyện
        for message in st.session_state.messages:
            # Tạo một khung chat cho mỗi tin nhắn
            with st.chat_message(message["role"]):
                # Hiển thị nội dung tin nhắn
                st.markdown(message["content"])

    def get_user_input(self):
        # Tạo một ô nhập liệu để người dùng đặt câu hỏi
        return st.chat_input("What is your question?")

    def display_user_message(self, message):
        # Hiển thị tin nhắn của người dùng trong khung chat
        st.chat_message("user").markdown(message)

    def display_assistant_message(self, message):
        with st.chat_message("assistant"):
            try:
                st.markdown(message)
            except Exception as e:
                st.error(f"Error displaying message: {str(e)}")

    def display_error_message(self, message):
        # Hiển thị thông báo lỗi nếu có vấn đề xảy ra
        with st.chat_message("assistant"):
            st.error(message)

    def update_chat_history(self, role, content):
        # Thêm tin nhắn mới vào lịch sử cuộc trò chuyện
        # Nếu chưa có lịch sử, tạo một danh sách mới
        if "messages" not in st.session_state:
            st.session_state.messages = []
        # Thêm tin nhắn mới vào cuối danh sách
        st.session_state.messages.append({"role": role, "content": content})

    def get_chat_history(self):
        # Lấy toàn bộ lịch sử cuộc trò chuyện hiện tại
        return st.session_state.messages

    def clear_chat_history(self):
        # Xóa toàn bộ lịch sử cuộc trò chuyện khi bắt đầu cuộc trò chuyện mới
        st.session_state.messages = []
