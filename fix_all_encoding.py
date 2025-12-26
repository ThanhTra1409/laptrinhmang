# -*- coding: utf-8 -*-
# This script will fix all encoding issues in generate_static.py

with open('generate_static.py', 'rb') as f:
    data = f.read()

# The file was saved with wrong encoding - strings are actually Latin-1 encoded UTF-8
# We need to decode as Latin-1, then re-encode to UTF-8
text = data.decode('latin-1')

# Now fix the double-encoded strings
corrections = {
    'âœ"': '✓',
    'ThÃ´ng tin cÃ¡ nhÃ¢n': 'Thông tin cá nhân',
    'CÃ´ng nghá»‡ luÃ´n thay Ä'á»•i, tÃ´i chá»n cÃ¡ch há»c há»i má»—i ngÃ y Ä'á»ƒ khÃ´ng bá»‹ bá» láº¡i phÃ­a sau.': 'Công nghệ luôn thay đổi, tôi chọn cách học hỏi mỗi ngày để không bị bỏ lại phía sau.',
    'Láº­p trÃ¬nh hÆ°á»›ng Ä'á»'i tÆ°á»£ng (OOP)': 'Lập trình hướng đối tượng (OOP)',
    'Cáº¥u trÃºc dá»¯ liá»‡u & Giáº£i thuáº­t': 'Cấu trúc dữ liệu & Giải thuật',
    'Láº­p trÃ¬nh máº¡ng & Distributed Systems': 'Lập trình mạng & Distributed Systems',
    'CÃ¡c bÃ i viáº¿t trong blog lÃ  cÃ¡c kiáº¿n thá»©c mÃ  tÃ´i Ä'Ã£ Ä'Æ°á»£c há»c:': 'Các bài viết trong blog là các kiến thức mà tôi đã được học:',
    'XÃ¢y dá»±ng TCP/UDP Server vá»›i Java': 'Xây dựng TCP/UDP Server với Java',
    'PhÃ¡t triá»ƒn RESTful API vá»›i Node.js & Express': 'Phát triển RESTful API với Node.js & Express',
    'Triá»ƒn khai WebSocket real-time communication': 'Triển khai WebSocket real-time communication',
    'Há»c váº¥n': 'Học vấn',
    'Äáº¡i há»c CÃ´ng nghá»‡ TP.HCM (HUTECH)': 'Đại học Công nghệ TP.HCM (HUTECH)',
    'NgÃ nh': 'Ngành',
    'CÃ´ng nghá»‡ Pháº§n má»m': 'Công nghệ Phần mềm',
    'Kiáº¿n thá»©c chuyÃªn mÃ´n:': 'Kiến thức chuyên môn:',
    'Ká»¹ nÄƒng láº­p trÃ¬nh Ä'Ã£ há»c': 'Kỹ năng lập trình đã học',
    'Dá»± Ã¡n & Portfolio': 'Dự án & Portfolio',
    'Ä'á»‹a chá»‰': 'địa chỉ',
    'TP. Há»" ChÃ­ Minh': 'TP. Hồ Chí Minh',
    'SÄT': 'SĐT',
    'Chia sáº» kiáº¿n thá»©c vÃ  kinh nghiá»‡m trong láº­p trÃ¬nh máº¡ng vá»›i Java vÃ  JavaScript': 'Chia sẻ kiến thức và kinh nghiệm trong lập trình mạng với Java và JavaScript',
    'Xin chÃ o, mÃ¬nh lÃ ': 'Xin chào, mình là',
    'Nguyá»…n Thanh TrÃ ': 'Nguyễn Thanh Trà',
    'â˜°': '☰',
    'â€¢': '•',
    'Â©': '©',
}

for wrong, correct in corrections.items():
    text = text.replace(wrong, correct)

# Write with proper UTF-8
with open('generate_static.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed all encoding issues!')
