# scanner.py

import threading

from security_checks import run_all_checks

from score import (
    calculate_security_score,
    security_level,
    recommendations
)


# Windows Defender
try:
    from defender_check import check_defender
except ImportError:
    check_defender = None


# Encryption
try:
    from encryption_check import check_encryption
except ImportError:
    check_encryption = None


# Logs
try:
    from log_analyzer import analyze_logs
except ImportError:
    analyze_logs = None



class SecurityScanner:


    def __init__(self):

        self.results = []



    def safe_run(self, function, name):

        result = []


        def runner():

            try:

                result.append(
                    function()
                )

            except Exception as e:

                result.append({

                    "name": name,

                    "status": False,

                    "details": str(e)

                })


        thread = threading.Thread(
            target=runner
        )


        thread.start()


        # أقصى انتظار 10 ثواني

        thread.join(
            timeout=10
        )


        if thread.is_alive():

            return {

                "name": name,

                "status": False,

                "details":
                "Scan timeout - skipped"

            }


        return result[0]



    def start_scan(self):


        print("[+] Starting Security Scan...")


        self.results = []



        # ==========================
        # Basic Checks
        # ==========================

        try:

            basic = run_all_checks()

            self.results.extend(
                basic
            )


        except Exception as e:


            self.results.append({

                "name":
                "Basic Security Checks",

                "status":
                False,

                "details":
                str(e)

            })



        # ==========================
        # Defender
        # ==========================

        if check_defender:


            self.results.append(

                self.safe_run(

                    check_defender,

                    "Windows Defender"

                )

            )



        # ==========================
        # Encryption
        # ==========================

        if check_encryption:


            self.results.append(

                self.safe_run(

                    check_encryption,

                    "Disk Encryption"

                )

            )



        # ==========================
        # Logs
        # ==========================

        if analyze_logs:


            self.results.append(

                self.safe_run(

                    analyze_logs,

                    "Security Log Analysis"

                )

            )



        # ==========================
        # Score
        # ==========================


        score = calculate_security_score(

            self.results

        )


        level = security_level(

            score

        )


        fixes = recommendations(

            self.results

        )



        print("[+] Scan Completed")



        return {

            "score":
            score,

            "level":
            level,

            "checks":
            self.results,

            "recommendations":
            fixes

        }



if __name__ == "__main__":


    scanner = SecurityScanner()


    result = scanner.start_scan()


    print(result)