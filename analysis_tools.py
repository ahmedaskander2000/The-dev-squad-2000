# -*- coding: utf-8 -*-
"""
أدوات تحليل كلمات المرور
"""

from core_functions import calculate_entropy, detect_leet_substitutions, check_patterns

def analyze_password(password, wordlist):
    """تحليل كلمة مرور واحدة"""
    print(f"\n{'='*50}")
    print(f"Analyzing Password: {password}")
    print(f"{'='*50}")
    
    results = {
        'password': password,
        'length': len(password),
        'entropy': 0,
        'score': 0,
        'issues': [],
        'recommendations': [],
        'leet_detected': False
    }
    
    # 1. التحقق من الطول
    if len(password) < 8:
        results['issues'].append("Password is too short (less than 8 characters)")
        results['recommendations'].append("Add more characters")
    elif len(password) >= 12:
        results['score'] += 2
    
    # 2. حساب الإنتروبيا
    entropy = calculate_entropy(password)
    results['entropy'] = entropy
    
    if entropy < 30:
        results['issues'].append("Low entropy (low randomness)")
        results['recommendations'].append("Use different types of characters")
    elif entropy > 60:
        results['score'] += 3
    
    # 3. التحقق من القاموس
    lower_password = password.lower()
    if lower_password in wordlist:
        results['issues'].append("Very common password")
        results['score'] -= 2
        results['recommendations'].append("Avoid common words")
    
    # 4. كشف استبدالات الليت
    leet_version = detect_leet_substitutions(password)
    if leet_version != password.lower():
        results['leet_detected'] = True
        if leet_version in wordlist:
            results['issues'].append("Leet substitutions on a common word")
            results['recommendations'].append("Leet speak alone is not enough to secure common words")
    
    # 5. التحقق من الأنماط
    patterns = check_patterns(password)
    if patterns:
        results['issues'].extend(patterns)
        results['score'] -= len(patterns)
        results['recommendations'].append("Avoid predictable patterns")
    
    # 6. حساب النتيجة النهائية
    if any(c.islower() for c in password): results['score'] += 1
    if any(c.isupper() for c in password): results['score'] += 1
    if any(c.isdigit() for c in password): results['score'] += 1
    if any(not c.isalnum() for c in password): results['score'] += 1
    
    # تحديد مستوى القوة
    if results['score'] >= 7:
        results['strength'] = "Very Strong"
    elif results['score'] >= 5:
        results['strength'] = "Strong"
    elif results['score'] >= 3:
        results['strength'] = "Medium"
    elif results['score'] >= 1:
        results['strength'] = "Weak"
    else:
        results['strength'] = "Very Weak"
    
    return results