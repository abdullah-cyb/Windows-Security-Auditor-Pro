# defender_check.py

import subprocess



def check_defender():

    result = {

        "name": "Windows Defender",

        "status": False,

        "details": ""

    }


    try:

        command = [

            "powershell",

            "-Command",

            "Get-MpComputerStatus"

        ]


        output = subprocess.check_output(

            command,

            text=True,

            stderr=subprocess.DEVNULL

        )


        if "RealTimeProtectionEnabled : True" in output:


            result["status"] = True

            result["details"] = (
                "Real Time Protection is enabled"
            )


        else:

            result["details"] = (
                "Real Time Protection is disabled"
            )


    except Exception as e:


        result["details"] = str(e)



    return result





if __name__ == "__main__":


    print(
        check_defender()
    )