# report.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime

import platform
import psutil



class ReportGenerator:


    def __init__(self, data):

        self.data = data



    def get_system_info(self):

        return [

            ["System", platform.system()],

            ["Computer Name", platform.node()],

            ["CPU", platform.processor()],

            ["RAM",
             f"{round(psutil.virtual_memory().total / (1024**3),2)} GB"
            ]

        ]



    def generate_pdf(
        self,
        filename="Security_Audit_Report.pdf"
    ):


        document = SimpleDocTemplate(
            filename
        )


        styles = getSampleStyleSheet()


        content = []



        # Title

        content.append(

            Paragraph(
                "Windows Security Auditor Pro",
                styles["Title"]
            )

        )


        content.append(
            Spacer(1,20)
        )



        content.append(

            Paragraph(

                f"Report Date: {datetime.now()}",

                styles["Normal"]

            )

        )


        content.append(
            Spacer(1,20)
        )



        # Score


        content.append(

            Paragraph(

                f"""
                Security Score:
                {self.data['score']}%

                <br/>

                Security Level:
                {self.data['level']}
                """,

                styles["Heading2"]

            )

        )


        content.append(
            Spacer(1,20)
        )



        # System Information


        content.append(

            Paragraph(

                "System Information",

                styles["Heading2"]

            )

        )


        system_table = Table(
            self.get_system_info()
        )


        system_table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),0.5,None)

            ])

        )


        content.append(
            system_table
        )


        content.append(
            Spacer(1,20)
        )



        # Checks


        content.append(

            Paragraph(

                "Security Checks",

                styles["Heading2"]

            )

        )



        rows = [

            [
                "Check",
                "Status",
                "Details"
            ]

        ]



        for item in self.data["checks"]:


            status = (

                "PASS"

                if item["status"]

                else

                "FAIL"

            )


            rows.append(

                [

                    item["name"],

                    status,

                    str(item["details"])

                ]

            )



        table = Table(
            rows
        )


        table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),0.5,None)

            ])

        )


        content.append(
            table
        )


        content.append(
            Spacer(1,20)
        )



        # Recommendations


        content.append(

            Paragraph(

                "Recommendations",

                styles["Heading2"]

            )

        )



        for fix in self.data.get(
            "recommendations",
            []
        ):


            content.append(

                Paragraph(

                    "• " + fix,

                    styles["Normal"]

                )

            )



        document.build(
            content
        )


        return filename