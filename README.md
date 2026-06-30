# Welcom_to_System_Performance_Monitor-
# System Performance Monitor & Cleaner

مشروع رايق يجمع بين لغتي **Python** و **C++** لإدارة ومراقبة أداء النظام.

## المميزات:
1. **فحص الذاكرة:** قراءة حية ومباشرة لحجم الرام المستخدم والمتاح بالجيجابايت (بواسطة بايثون).
2. **تنظيف النظام:** حذف الملفات المؤقتة (Temp Files) بأمان وحماية الكود من الانهيار باستخدام (Try/Except).
3. **معلومات النظام (C++):** استدعاء ملف C++ خارجي ومترجم يقرأ معمارية المعالج وجهازك (64-bit) عبر Windows API.

## طريقة التشغيل:
1. قم بتجميع كود الـ C++ أولاً:
   `g++ sys_info.cpp -o sys_info.exe`
2. قم بتشغيل ملف البايثون الرئيسي:
   `python System_Performance_Monitor.py`
   =========================================================================================================================================
   # System Performance Monitor and Cleaner

A university project combining **Python** and **C++**.

## Features:
1. **Memory Monitoring:** Real-time reading of used and available RAM in gigabytes (using Python).
2. **System Cleanup:** Safely deletes temporary files, with error handling (Try/Except) to prevent crashes.
3. **System Information (C++):** Interfaces with an external C++ file to retrieve system architecture details (e.g., 64-bit) via the Windows API.

## How to Run:
1. Compile the C++ code:
   `g++ sys_info.cpp -o sys_info.exe`
2. Run the main Python script:
   `python System_Performance_Monitor.py`
