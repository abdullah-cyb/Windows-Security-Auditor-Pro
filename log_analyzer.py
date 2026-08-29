# log_analyzer.py

import subprocess


def analyze_logs():

    result = {

        "name": "Security Log Analysis",

        "status": True,

        "details": ""

    }


    try:

        command = """

        Get-WinEvent -LogName Security -MaxEvents 50 |
        Select-Object Id,Message

        """


        output = subprocess.check_output(

            [
                "powershell",
                "-Command",
                command
            ],

            text=True,

            timeout=15,

            stderr=subprocess.STDOUT

        )


        failed = output.count(
            "4625"
        )


        if failed > 10:


            result["status"] = False

            result["details"] = (

                f"Suspicious activity detected: "
                f"{failed} failed login events"

            )


        else:


            result["details"] = (

                "No suspicious security events detected"

            )


    except Exception as e:


        result["status"] = True

        result["details"] = (

            "Log analysis unavailable: "
            + str(e)

        )


    return result