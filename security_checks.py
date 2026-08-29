import subprocess
import platform
import socket


def check_firewall():
    result = {
        "name": "Windows Firewall",
        "status": False,
        "details": ""
    }

    try:
        cmd = [
            "powershell",
            "-Command",
            "Get-NetFirewallProfile | Select Enabled"
        ]

        output = subprocess.check_output(
            cmd,
            text=True,
            stderr=subprocess.DEVNULL
        )

        if "True" in output:
            result["status"] = True
            result["details"] = "Firewall is enabled"
        else:
            result["details"] = "Firewall is disabled"

    except Exception as e:
        result["details"] = str(e)

    return result


def check_updates():
    result = {
        "name": "Windows Updates",
        "status": False,
        "details": ""
    }

    try:
        cmd = [
            "powershell",
            "-Command",
            "Get-Service wuauserv"
        ]

        output = subprocess.check_output(
            cmd,
            text=True,
            stderr=subprocess.DEVNULL
        )

        if "Running" in output:
            result["status"] = True
            result["details"] = "Windows Update service is running"
        else:
            result["details"] = "Windows Update service stopped"

    except Exception as e:
        result["details"] = str(e)

    return result


def check_open_ports():
    result = {
        "name": "Open Ports",
        "status": True,
        "details": []
    }

    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        common_ports = [
            21,
            22,
            23,
            80,
            443,
            3389
        ]

        for port in common_ports:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            if sock.connect_ex((ip, port)) == 0:
                result["details"].append(
                    f"Port {port} is open"
                )

            sock.close()

    except Exception as e:
        result["status"] = False
        result["details"] = str(e)

    return result


def run_all_checks():

    checks = []

    checks.append(check_firewall())
    checks.append(check_updates())
    checks.append(check_open_ports())

    return checks