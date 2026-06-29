import os

base_dir = r"C:\Users\CORTEC\Downloads\plan_txt\New_System_Blueprint"

# Add Integration Registry to Phase 1
phase1_path = os.path.join(base_dir, "Phase_1_Collaborative_Design", "06_Integration_Registry.txt")
with open(phase1_path, "w", encoding="utf-8") as f:
    f.write("──────────────────────────────────────────\n")
    f.write("FILE: 06_Integration_Registry.txt\n")
    f.write("──────────────────────────────────────────\n\n")
    f.write("سجل الإضافات (Integration Registry):\n")
    f.write("الهدف: إذا أراد أي شخص إضافة ملف txt جديد لفكرة أو مكون جديد (مثلاً إضافة شات بوت أو ميزة إشعارات)، يجب عليه تسجيله هنا.\n")
    f.write("بهذه الطريقة النظام يستوعب الإضافات دون أن ينكسر العمل الأصلي للطرف الآخر.\n\n")
    f.write("طريقة التسجيل:\n")
    f.write("1. أنشئ ملفك الجديد في مجلد Extensions الخاص بك.\n")
    f.write("2. اكتب هنا اسم الميزة، اسم الملف، وهل تتطلب تعديلاً في الـ API الأساسي أم أنها ميزة مستقلة (Standalone).\n")
    f.write("──────────────────────────────────────────\n")
    f.write("سجل المكونات المضافة حديثاً:\n")

# Add Extensions folders for Abdelkader
abd_ext_path = os.path.join(base_dir, "Phase_2_Abdelkader_Execution", "04_Extensions_and_New_Modules")
os.makedirs(abd_ext_path, exist_ok=True)
with open(os.path.join(abd_ext_path, "README.txt"), "w", encoding="utf-8") as f:
    f.write("ضع هنا أي ملفات txt إضافية تصممها لعناصر جديدة في النظام.\n")
    f.write("مبدأ العمل: أي ملف يضاف هنا هو 'مكون مستقل' (Modular Component) لا يغير في الملفات الأساسية 01، 02، 03 لكي لا يتأثر عمل يوسف.\n")
    f.write("لا تنسَ تسجيل المكون الجديد في ملف 06_Integration_Registry.txt في المرحلة الأولى.")

# Add Extensions folders for Youcef
you_ext_path = os.path.join(base_dir, "Phase_2_Youcef_Execution", "05_Extensions_and_New_Modules")
os.makedirs(you_ext_path, exist_ok=True)
with open(os.path.join(you_ext_path, "README.txt"), "w", encoding="utf-8") as f:
    f.write("ضع هنا أي ملفات txt إضافية تصممها لعناصر جديدة في النظام.\n")
    f.write("مبدأ العمل: أي ملف يضاف هنا هو 'مكون مستقل' (Modular Component) لا يغير في الملفات الأساسية 01، 02، 03 لكي لا يتأثر عمل عبد القادر.\n")
    f.write("لا تنسَ تسجيل المكون الجديد في ملف 06_Integration_Registry.txt في المرحلة الأولى.")

print("Enhancements added.")
