#include <iostream>
#include <windows.h> // المكتبة السحرية للتحكم بنظام ويندوز

using namespace std;

int main()
{
    // تجهيز صندوق لاستقبال معلومات النظام
    SYSTEM_INFO si;
    GetNativeSystemInfo(&si);

    // فحص معمارية النظام بناءً على رقم المعالج
    if (si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64)
    {
        cout << "OS Architecture: 64-bit (x64)";
    }
    else if (si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_INTEL)
    {
        cout << "OS Architecture: 32-bit (x86)";
    }
    else
    {
        cout << "OS Architecture: Unknown Architecture";
    }

    return 0;
}