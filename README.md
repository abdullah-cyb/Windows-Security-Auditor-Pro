# Windows Security Auditor Pro

أداة مبنية بلغة Python لفحص وتقييم إعدادات أمان نظام Windows واكتشاف الإعدادات التي قد تزيد من المخاطر الأمنية.

## المشكلة

قد تكون بعض إعدادات الحماية في Windows غير مفعلة أو غير مضبوطة بالشكل الصحيح، مما قد يترك الجهاز معرضًا لمخاطر أمنية.

## الحل

يقوم Windows Security Auditor Pro بفحص أهم مكونات أمان النظام، ثم يحلل النتائج ويحسب **درجة أمان من 100** مع إمكانية إنشاء تقرير بنتائج الفحص.

## أهم المميزات

- فحص Windows Firewall
- فحص Windows Defender
- فحص حالة التشفير
- تحليل Windows Event Logs
- اكتشاف مؤشرات التهديدات
- حساب Security Score من 100
- إنشاء تقارير أمنية
- تخزين النتائج باستخدام SQLite
- واجهة رسومية سهلة الاستخدام

## نظام التقييم

يتم حساب درجة الأمان بناءً على:

| المكون | النسبة |
|---|---:|
| Firewall | 20% |
| Windows Defender | 20% |
| Encryption | 15% |
| Event Logs | 25% |
| Threat Detection | 20% |

**الدرجة النهائية: 100/100**

## المتطلبات

- Windows 10 أو Windows 11
- Python 3.11 أو أحدث
- صلاحيات Administrator
- المكتبات الموجودة في `requirements.txt`

## المكتبات المستخدمة

- Python
- CustomTkinter
- PyWin32
- psutil
- SQLite
- ReportLab

## طريقة التشغيل

### 1. تحميل المشروع

```bash
git clone https://github.com/abdullah-cyb/Windows-Security-Auditor-Pro.git
```

### 2. الدخول إلى مجلد المشروع

```bash
cd Windows-Security-Auditor-Pro
```

### 3. تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 4. تشغيل البرنامج

يفضل تشغيل Terminal أو CMD بصلاحيات **Administrator** ثم:

```bash
python main.py
```

## الاستخدام

بعد تشغيل البرنامج، يبدأ بفحص إعدادات أمان Windows وعرض النتائج ودرجة الأمان، مع إمكانية إنشاء تقرير بنتائج الفحص.

## الهدف من المشروع

تم تطوير المشروع لأغراض **تعليمية ودفاعية** بهدف مساعدة المستخدمين والطلاب والمهتمين بالأمن السيبراني على فهم وفحص إعدادات أمان Windows.

## Disclaimer

هذا المشروع مخصص للتدقيق الأمني والدراسة وتحسين الحماية، وليس للاستخدام في أي نشاط ضار أو غير مصرح به.

## المطور

**Abdullah Nasser**

Cybersecurity Student & Developer
