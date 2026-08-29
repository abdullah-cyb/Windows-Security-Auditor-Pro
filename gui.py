# gui.py

import customtkinter as ctk
from tkinter import messagebox
import threading

from scanner import SecurityScanner
from score import security_color
from report import ReportGenerator



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



class SecurityAuditorGUI:


    def __init__(self, root):

        self.root = root

        self.root.title(
            "🛡 Security Auditor Pro"
        )

        self.root.geometry(
            "1100x750"
        )


        self.scanner = SecurityScanner()


        self.last_report = None


        self.create_widgets()



    def create_widgets(self):


        # =====================
        # Title
        # =====================

        self.header = ctk.CTkLabel(

            self.root,

            text="🛡 Security Auditor Pro",

            font=(
                "Arial",
                32,
                "bold"
            )

        )

        self.header.pack(
            pady=20
        )



        # =====================
        # Score Card
        # =====================

        self.score_frame = ctk.CTkFrame(

            self.root,

            width=400,

            height=120

        )

        self.score_frame.pack(
            pady=10
        )



        self.score_label = ctk.CTkLabel(

            self.score_frame,

            text="Security Score\n-- %",

            font=(
                "Arial",
                28,
                "bold"
            )

        )


        self.score_label.pack(
            padx=80,
            pady=25
        )



        # =====================
        # Scan Button
        # =====================


        self.scan_button = ctk.CTkButton(

            self.root,

            text="🚀 START FULL SECURITY SCAN",

            width=400,

            height=50,

            font=(
                "Arial",
                18,
                "bold"
            ),

            command=self.start_scan

        )


        self.scan_button.pack(
            pady=10
        )



        # =====================
        # Export Button
        # =====================


        self.report_button = ctk.CTkButton(

            self.root,

            text="📄 EXPORT PDF REPORT",

            width=300,

            height=40,

            command=self.export_report

        )


        self.report_button.pack(
            pady=5
        )



        # =====================
        # Progress Bar
        # =====================


        self.progress = ctk.CTkProgressBar(

            self.root,

            width=700

        )


        self.progress.set(0)


        self.progress.pack(
            pady=10
        )



        # =====================
        # Results Box
        # =====================


        self.result_box = ctk.CTkTextbox(

            self.root,

            width=950,

            height=320,

            font=(
                "Consolas",
                14
            )

        )


        self.result_box.pack(
            pady=15
        )




    # ==========================
    # Start Scan
    # ==========================


    def start_scan(self):


        self.scan_button.configure(

            state="disabled"

        )


        self.result_box.delete(

            "0.0",

            "end"

        )


        thread = threading.Thread(

            target=self.run_scan

        )


        thread.start()





    # ==========================
    # Scanner Thread
    # ==========================


    def run_scan(self):


        self.progress.start()


        data = self.scanner.start_scan()


        self.last_report = data


        self.progress.stop()



        score = data["score"]


        color = security_color(

            score

        )



        self.score_label.configure(

            text=f"Security Score\n{score}%",

            text_color=color

        )



        self.result_box.insert(

            "end",

            "\n========== SECURITY REPORT ==========\n\n"

        )



        self.result_box.insert(

            "end",

            f"Security Level: {data['level']}\n\n"

        )



        for item in data["checks"]:


            icon = (

                "✅"

                if item["status"]

                else

                "⚠"

            )


            self.result_box.insert(

                "end",

                f"{icon} {item['name']}\n"

            )


            self.result_box.insert(

                "end",

                f"   {item['details']}\n\n"

            )



        if data.get("recommendations"):


            self.result_box.insert(

                "end",

                "\n========== RECOMMENDATIONS ==========\n\n"

            )


            for fix in data["recommendations"]:


                self.result_box.insert(

                    "end",

                    f"• {fix}\n"

                )



        self.scan_button.configure(

            state="normal"

        )





    # ==========================
    # Export PDF
    # ==========================


    def export_report(self):


        try:


            if not self.last_report:


                messagebox.showwarning(

                    "No Scan",

                    "Please run a security scan first."

                )

                return



            generator = ReportGenerator(

                self.last_report

            )



            file = generator.generate_pdf()



            messagebox.showinfo(

                "Report Created",

                f"PDF report created:\n{file}"

            )



        except Exception as e:


            messagebox.showerror(

                "Report Error",

                str(e)

            )







if __name__ == "__main__":


    root = ctk.CTk()


    app = SecurityAuditorGUI(

        root

    )


    root.mainloop()