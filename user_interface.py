# -*- coding: utf-8 -*-
"""
واجهة المستخدم للبرنامج
"""

from core_functions import load_wordlist
from analysis_tools import analyze_password
from reporting import display_report, display_summary, save_to_file

def main():
    """الدالة الرئيسية للواجهة"""
    print(f"{'Password Strength Analyzer':^60}")
    print(f"{'='*60}")
    
    # تحميل قائمة الكلمات
    wordlist = load_wordlist()
    
    # طلب كلمات المرور من المستخدم
    print("\nEnter passwords (separate with commas, or type 'end' to finish):")
    print("Example: password123, P@ssw0rd, qwerty, MyStrongPass!2024")
    
    all_results = []
    
    while True:
        user_input = input("\nEnter passwords: ").strip()
        
        if user_input.lower() == 'end':
            break
        
        if user_input:
            passwords = [p.strip() for p in user_input.split(',')]
            
            for password in passwords:
                if password:
                    # تحليل كلمة المرور
                    results = analyze_password(password, wordlist)
                    all_results.append(results)
                    # عرض التقرير
                    display_report(results)
        
        more = input("\nDo you want to add more? (yes/no): ").strip().lower()
        if more not in ['yes', 'y', '']:
            break
    
    # عرض الملخص النهائي
    if all_results:
        display_summary(all_results)
        
        # حفظ التقرير في ملف
        save_report = input("\n💾 Do you want to save the report to a file? (yes/no): ").strip().lower()
        if save_report in ['yes', 'y']:
            save_to_file(all_results)
            print("✅ Report saved to password_report.txt")
    else:
        print("\n⚠️  No passwords were entered for analysis.")
    
    print("\n🎉 Analysis completed. Thank you for using the tool!")