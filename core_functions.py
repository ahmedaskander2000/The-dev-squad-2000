# -*- coding: utf-8 -*-
"""
الدوال الأساسية للبرنامج
"""

import math
import re
from datetime import datetime

def calculate_entropy(password):
    """حساب إنتروبيا كلمة المرور"""
    length = len(password)
    
    # تحديد مجموعة الأحرف المستخدمة
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(not c.isalnum() for c in password): charset_size += 32
    
    if charset_size == 0:
        return 0
    
    # حساب الإنتروبيا
    entropy = length * math.log2(charset_size)
    return round(entropy, 2)

def load_wordlist():
    """تحميل قائمة الكلمات الشائعة"""
    common_words = [
        # الإنجليزية العالمية
        '123456', 'password', '12345678', 'qwerty', '123456789',
        '12345', '1234', '111111', '1234567', 'dragon',
        '123123', 'baseball', 'abc123', 'football', 'monkey',
        'letmein', 'shadow', 'master', '666666', 'qwertyuiop',
        '123321', 'mustang', '1234567890', 'michael', '654321',
        'superman', '1qaz2wsx', '7777777', '121212', '000000',
        'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan',
        'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster',
        'soccer', 'harley', 'batman', 'andrew', 'tigger',
        'sunshine', 'iloveyou', '2000', 'charlie', 'robert',
        'thomas', 'hockey', 'ranger', 'daniel', 'starwars',
        'klaster', '112233', 'george', 'computer', 'michelle',
        'jessica', 'pepper', '1111', 'zxcvbn', '555555',
        '11111111', '131313', 'freedom', '777777', 'pass',
        'maggie', '159753', 'aaaaaa', 'ginger', 'princess',
        'joshua', 'cheese', 'amanda', 'summer', 'love',
        'ashley', 'nicole', 'chelsea', 'biteme', 'matthew',
        'access', 'yankees', '987654321', 'dallas', 'austin',
        'thunder', 'taylor', 'matrix', 'mobilemail', 'mom',
        'monitor', 'monitoring', 'montana', 'moon', 'moscow',
        'q1w2e3r4t5', '123456a', 'password1', 'password123',
        'admin', 'welcome', 'login', 'passw0rd',
        
        # العربية والعالم العربي
        'allah', 'mohammed', 'alhamdulillah', 'masr', 'algeria',
        'morocco', 'qatar', 'saudi', 'kuwait', 'habibi',
        'halawa', 'shokran', 'ahlan', 'salam', 'mabrook',
        'yalla', 'inshallah', 'yaani', 'wallah', 'ana',
        'enta', 'howa', 'hiya', 'ahlanwasahlan', 'maasalama',
        'mish', 'aywa', 'laa', 'aiwa', 'alfmabrook',
        'khalas', 'yaba', 'yamma', 'yaallah', 'yarab',
        'ouladi', 'benti', 'zawji', 'zawjati', 'hob',
        'gharam', '3eshq', '7ob', '7elm', 'amal',
        'hayat', 'ro7', 'qalb', 'shahd', 'asel',
        'qamr', 'shams', 'nour', 'noor', 'donia',
        'dunya', 'akhi', 'ukhti', 'sadiq', 'sadiqa',
        'jayid', 'mumtaz', 'mumtaza', 'qawi', 'qawiya',
        'jameel', 'jameela', '7elw', '7elwa', 'kabeer',
        'kabeera', 'sagheer', 'saghira', 'gameel', 'gameela',
        '3azeem', '3azeema', '7abibi', '7abibti', '3omri',
        'hayati', 'ro7i', 'albahr', 'assahra', 'alqamar',
        'annahr', 'alward', 'alwarda', 'al3asfour', 'alfeel',
        'alasad', 'alhisan', 'al7osan',
        
        # إضافات شائعة أخرى
        '12345678910', '123', 'abc', 'qwerty123', 'admin123',
        'welcome123', 'test', 'test123', 'user', 'guest',
        'info', 'root', 'administrator', 'sql', 'oracle',
        'mysql', 'web', 'server', 'network', 'system',
        'security', 'data', 'database', 'backup', 'server123',
        'adminadmin', 'super', 'user123', 'demo', 'demo123',
        'sample', 'sample123', 'temp', 'temp123', 'default',
        'change', 'changeme', 'newpassword', 'newpass', 'oldpassword',
        'secret', 'private', 'confidential', 'access123', 'login123',
        'pass123', 'pw123', 'letmein123', 'welcome1', 'password1234',
        'qwerty1', 'admin1', 'user1', 'test1', '1234561',
        'iloveyou1', 'sunshine1', 'princess1', 'football1', 'baseball1',
        'soccer1', 'hockey1', 'basketball', 'volleyball', 'tennis',
        'golf', 'swimming', 'cricket', 'rugby', 'marathon',
        'champion', 'winner', 'champion1', 'winner1', 'gold',
        'silver', 'bronze', 'medal', 'trophy', 'cup',
        'league', 'team', 'player', 'coach', 'manager',
        'director', 'president', 'ceo', 'manager1', 'director1',
        'boss', 'boss123', 'company', 'company123', 'business',
        'business123', 'work', 'office', 'office123', 'home',
        'home123', 'house', 'house123', 'family', 'family123',
        'friend', 'friend123', 'mother', 'father', 'sister',
        'brother', 'son', 'daughter', 'wife', 'husband',
        'parent', 'child', 'baby', 'baby123', 'pet',
        'pet123', 'dog', 'cat', 'bird', 'fish',
        'rabbit', 'hamster', 'turtle', 'snake', 'lizard',
        'dragon123', 'monkey123', 'tiger', 'lion', 'elephant',
        'giraffe', 'zebra', 'horse', 'cow', 'sheep',
        'goat', 'chicken', 'duck', 'pig', 'wolf',
        'fox', 'bear', 'deer', 'moose', 'eagle',
        'hawk', 'falcon'
    ]
    
    wordlist_set = set(common_words)
    print(f"✅ تم تحميل {len(wordlist_set)} كلمة شائعة للتحقق منها")
    return wordlist_set

def detect_leet_substitutions(password):
    """الكشف عن استبدالات الليت"""
    leet_map = {
        '4': 'a', '@': 'a', '8': 'b', '3': 'e',
        '6': 'g', '9': 'g', '1': 'i', '!': 'i',
        '0': 'o', '$': 's', '5': 's', '7': 't',
        '2': 'z'
    }
    
    original_word = password.lower()
    for leet_char, normal_char in leet_map.items():
        original_word = original_word.replace(leet_char, normal_char)
    
    return original_word

def check_patterns(password):
    """الكشف عن الأنماط الضعيفة"""
    patterns = []
    
    # تسلسلات رقمية
    if re.match(r'^12345678?9?$', password) or re.match(r'^98765432?1?$', password):
        patterns.append("Sequential numerical sequence")
    
    # تواريخ
    date_patterns = [
        r'\d{4}[-\/]\d{2}[-\/]\d{2}',  # YYYY-MM-DD
        r'\d{2}[-\/]\d{2}[-\/]\d{4}',  # DD-MM-YYYY
        r'\d{8}',  # YYYYMMDD
        r'\d{6}'   # YYMMDD
    ]
    
    for pattern in date_patterns:
        if re.search(pattern, password):
            patterns.append("Potential date pattern")
            break
    
    # أحرف متكررة
    if re.match(r'^(\w)\1+$', password):
        patterns.append("Repeated characters")
    
    # كيبورد متتابع
    keyboard_patterns = ['qwerty', 'asdfgh', 'zxcvbn', 'qazwsx']
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            patterns.append("Common keyboard pattern")
            break
    
    return patterns