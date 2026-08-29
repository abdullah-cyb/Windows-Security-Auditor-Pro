# score.py


SECURITY_WEIGHTS = {

    "Windows Firewall": 15,

    "Windows Updates": 15,

    "Open Ports": 10,

    "Windows Defender": 15,

    "Disk Encryption": 15,

    "Security Log Analysis": 20

}




def calculate_security_score(results):


    score = 0


    total_weight = 0



    for item in results:


        name = item["name"]


        weight = SECURITY_WEIGHTS.get(
            name,
            10
        )


        total_weight += weight



        if item["status"]:


            score += weight



    if total_weight == 0:

        return 0



    final_score = int(

        (score / total_weight) * 100

    )


    return final_score





def security_level(score):


    if score >= 90:

        return "Excellent"



    elif score >= 75:

        return "Good"



    elif score >= 50:

        return "Medium"



    else:

        return "Critical"





def security_color(score):


    if score >= 90:

        return "green"



    elif score >= 75:

        return "blue"



    elif score >= 50:

        return "orange"



    else:

        return "red"





def recommendations(results):


    fixes = []



    for item in results:


        if not item["status"]:



            if item["name"] == "Windows Firewall":


                fixes.append(
                    "Enable Windows Firewall"
                )



            elif item["name"] == "Windows Updates":


                fixes.append(
                    "Enable automatic Windows Updates"
                )



            elif item["name"] == "Windows Defender":


                fixes.append(
                    "Enable Windows Defender Real Time Protection"
                )



            elif item["name"] == "Disk Encryption":


                fixes.append(
                    "Enable BitLocker encryption"
                )



            elif item["name"] == "Security Log Analysis":


                fixes.append(
                    "Investigate suspicious security events"
                )



            elif item["name"] == "Open Ports":


                fixes.append(
                    "Close unnecessary open ports"
                )



    return fixes