# encryption_check.py

import subprocess




def check_encryption():


    result = {

        "name": "Disk Encryption",

        "status": False,

        "details": ""

    }



    try:


        command = [

            "powershell",

            "-Command",

            "Get-BitLockerVolume"

        ]



        output = subprocess.check_output(

            command,

            text=True,

            stderr=subprocess.DEVNULL

        )



        if "FullyEncrypted" in output or "EncryptionPercentage" in output:


            result["status"] = True


            result["details"] = (

                "BitLocker encryption detected"

            )


        else:


            result["details"] = (

                "Disk encryption not enabled"

            )



    except Exception as e:


        result["details"] = str(e)



    return result






if __name__ == "__main__":


    print(
        check_encryption()
    )