# main.py

from scanner import SecurityScanner
from database import Database
from report import ReportGenerator



class SecurityAuditorApp:


    def __init__(self):

        self.scanner = SecurityScanner()

        self.database = Database()



    def run_scan(self):

        print("\n[+] Running Security Audit...\n")


        # تشغيل الفحص
        report_data = self.scanner.start_scan()



        # حفظ في قاعدة البيانات

        details = str(
            report_data["checks"]
        )


        self.database.save_scan(

            report_data["score"],

            report_data["level"],

            details

        )



        # إنشاء التقرير

        report = ReportGenerator(
            report_data
        )


        filename = report.generate_html()


        print(
            "[+] Report Created:",
            filename
        )


        return report_data




    def show_history(self):


        history = self.database.get_history()


        print("\n====== Scan History ======")


        for item in history:

            print(
                f"""
ID: {item[0]}
Date: {item[1]}
Score: {item[2]}%
Level: {item[3]}
-------------------------
"""
            )



    def close(self):

        self.database.close()





if __name__ == "__main__":


    app = SecurityAuditorApp()


    try:

        result = app.run_scan()


        print("\n========== RESULT ==========")


        print(
            "Score:",
            result["score"],
            "%"
        )


        print(
            "Level:",
            result["level"]
        )



    finally:

        app.close()