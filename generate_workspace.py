import os

base_dir = r"C:\Users\CORTEC\Downloads\plan_txt\New_System_Blueprint"

structure = {
    "00_Shared_Foundation": {
        "00_Project_Goals_and_Scope.txt": "الهدف من النظام، نطاق العمل، والمستخدمين المستهدفين.\n(يتم تعبئته بالتعاون بين عبد القادر ويوسف كأول خطوة)",
        "01_Master_Architecture.txt": "المخطط الهيكلي الشامل للمشروع وكيفية تواصل الأجزاء مع بعضها.",
        "02_Database_Schema.txt": "هيكلية الجداول، العلاقات، وأنواع البيانات.\n(الاتفاق عليها مبكراً هو سر العمل المتوازي الناجح)",
        "03_API_and_Data_Contracts.txt": "شكل البيانات (JSON) المتبادلة. بمجرد تحديد المدخلات والمخرجات، يمكن لكل شخص برمجة الخوارزميات الخاصة به بشكل مستقل."
    },
    "01_Abdelkader_Tasks": {
        "04_Data_Ingestion_and_Preprocessing.txt": "كيفية جلب البيانات، تنظيفها، وتجهيزها للعمليات الحسابية.",
        "05_Algorithms_Part_1.txt": "تفاصيل النصف الأول من الخوارزميات (مثال: التحليل، استخراج الميزات، المعالجة الأولية).\n- المدخلات:\n- المخرجات:\n- المنطق الرياضي/البرمجي:",
        "06_Backend_Services_and_Security.txt": "الخدمات الخلفية (Backend)، إدارة الجلسات، التوثيق، والحماية."
    },
    "02_Youcef_Tasks": {
        "07_Rules_Engine_and_Logic.txt": "القواعد المنطقية (Rules Engine) وكيفية اتخاذ القرارات وربطها بمخرجات الخوارزميات.",
        "08_Algorithms_Part_2.txt": "تفاصيل النصف الثاني من الخوارزميات (مثال: التصنيف، التنبؤ، أو اتخاذ القرار المتقدم).\n- المدخلات:\n- المخرجات:\n- المنطق الرياضي/البرمجي:",
        "09_User_Interface_and_UX.txt": "تصميم الواجهات، رحلة المستخدم، وكيفية عرض النتائج على الشاشة.",
        "10_System_Testing_and_Validation.txt": "كيفية اختبار النظام للتأكد من صحة النتائج ومنع الأخطاء."
    }
}

os.makedirs(base_dir, exist_ok=True)

for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    for filename, content in files.items():
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("──────────────────────────────────────────\n")
            f.write(f"FILE: {filename}\n")
            f.write("──────────────────────────────────────────\n\n")
            f.write("الوصف والمحتوى المطلوب:\n")
            f.write(content + "\n\n")
            f.write("──────────────────────────────────────────\n")
            f.write("ابدأ الكتابة هنا:\n")

print("Workspace created successfully.")
