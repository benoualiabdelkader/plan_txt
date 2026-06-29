import os
import shutil

base_dir = r"C:\Users\CORTEC\Downloads\plan_txt\New_System_Blueprint"

# Remove old directories
old_dirs = ["00_Shared_Foundation", "01_Abdelkader_Tasks", "02_Youcef_Tasks"]
for d in old_dirs:
    path = os.path.join(base_dir, d)
    if os.path.exists(path):
        shutil.rmtree(path)

# Define new phased structure
structure = {
    "Phase_1_Collaborative_Design": {
        "01_Project_Goals_and_Scope.txt": "الهدف من النظام، نطاق العمل، والمستخدمين المستهدفين.\n(هذه المرحلة الأولى: اجلسوا معاً، ناقشوا هذا الملف واتفقوا عليه بالكامل)",
        "02_Master_Architecture.txt": "المخطط الهيكلي الشامل للمشروع وكيفية تواصل الأجزاء مع بعضها.\n(مرحلة النقاش والمراجعة المشتركة)",
        "03_Database_Schema.txt": "هيكلية الجداول، العلاقات، وأنواع البيانات.\n(الأساس الذي ستبنون عليه، لا تنتقلوا للمرحلة 2 قبل اعتماده ومراجعته جيداً)",
        "04_API_and_Data_Contracts.txt": "شكل البيانات (JSON) المتبادلة بين أجزاء النظام.\n(هذا بمثابة العقد بينك وبين يوسف، بمجرد الاتفاق عليه ينفصل العمل كلياً)",
        "05_Algorithms_Distribution_Plan.txt": "خطة توزيع الخوارزميات بدقة: الاتفاق على ماهية خوارزميات عبد القادر وماهية خوارزميات يوسف."
    },
    "Phase_2_Abdelkader_Execution": {
        "01_Data_Ingestion_and_Preprocessing.txt": "كيفية جلب البيانات، تنظيفها، وتجهيزها للعمليات الحسابية.\n(مساحتك الخاصة، انطلق فيها وحدك بعد انتهاء المرحلة 1)",
        "02_Algorithms_Part_1.txt": "تفاصيل خوارزميات عبد القادر (المتفق عليها في ملف التوزيع).\n- المدخلات:\n- المخرجات:\n- المنطق الرياضي/البرمجي:",
        "03_Backend_Services_and_Security.txt": "الخدمات الخلفية (Backend)، إدارة الجلسات، والحماية."
    },
    "Phase_2_Youcef_Execution": {
        "01_Rules_Engine_and_Logic.txt": "القواعد المنطقية (Rules Engine) وكيفية اتخاذ القرارات.\n(مساحة يوسف الخاصة، ينطلق فيها وحده فور انتهاء المرحلة 1)",
        "02_Algorithms_Part_2.txt": "تفاصيل خوارزميات يوسف (المتفق عليها في ملف التوزيع).\n- المدخلات:\n- المخرجات:\n- المنطق الرياضي/البرمجي:",
        "03_User_Interface_and_UX.txt": "تصميم الواجهات، رحلة المستخدم، وكيفية عرض النتائج.",
        "04_System_Testing_and_Validation.txt": "كيفية اختبار النظام للتأكد من صحة النتائج ومنع الأخطاء."
    }
}

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

print("Reorganization complete.")
