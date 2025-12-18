"""pfSense Automation Utility (Example)

SOC Operations Center used custom Python utilities to support response actions such as blocking a source IP on pfSense.

Environment variables:
- PFSENSE_URL
- PFSENSE_USERNAME
- PFSENSE_PASSWORD
- PFSENSE_VERIFY_TLS   (true/false)
- IP_TO_BLOCK          (provided by SOAR runtime)
"""

import os
import urllib3
import requests
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class PfSenseAutomator:
    def __init__(self, base_url: str, username: str, password: str, verify_tls: bool = True):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.verify = verify_tls
        self.session.headers.update(
            {
                "User-Agent": "SOC-Operations-Center/1.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": f"{self.base_url}/index.php",
                "Upgrade-Insecure-Requests": "1",
            }
        )

    def _csrf_token(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        csrf = soup.find("input", {"name": "__csrf_magic"})
        if not csrf or not csrf.get("value"):
            raise RuntimeError("CSRF token not found")
        return csrf["value"]

    def login(self) -> None:
        login_page = self.session.get(f"{self.base_url}/index.php")
        token = self._csrf_token(login_page.text)

        login_data = {
            "__csrf_magic": token,
            "usernamefld": self.username,
            "passwordfld": self.password,
            "login": "Sign In",
        }

        resp = self.session.post(f"{self.base_url}/index.php", data=login_data, allow_redirects=True)
        if "Dashboard" not in resp.text:
            raise RuntimeError("Login failed (check credentials / UI language / pfSense version).")

    def add_block_rule(self, ip_to_block: str, interface: str = "wan") -> None:
        edit_url = f"{self.base_url}/firewall_rules_edit.php?if={interface}&after=-1"
        edit_page = self.session.get(edit_url)
        token = self._csrf_token(edit_page.text)

        rule_data = {
            "__csrf_magic": token,
            "type": "block",
            "interface": interface,
            "ipprotocol": "inet",
            "proto": "any",
            "srctype": "single",
            "src": ip_to_block,
            "dsttype": "any",
            "descr": f"SOC Operations Center - block {ip_to_block}",
            "statetype": "keep state",
            "after": "-1",
            "ruleid": "",
            "save": "Save",
        }

        rule_resp = self.session.post(edit_url, data=rule_data, allow_redirects=True)
        apply_token = self._csrf_token(rule_resp.text)

        apply_resp = self.session.post(
            f"{self.base_url}/firewall_rules.php?if={interface}",
            data={"__csrf_magic": apply_token, "apply": "Apply Changes"},
            allow_redirects=True,
        )

        if "The changes have been applied successfully" not in apply_resp.text:
            raise RuntimeError("pfSense did not confirm rule application; verify permissions and UI.")


def _env_bool(key: str, default: bool) -> bool:
    v = os.getenv(key)
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "y", "on"}


if __name__ == "__main__":
    pfsense_url = os.getenv("PFSENSE_URL", "")
    username = os.getenv("PFSENSE_USERNAME", "")
    password = os.getenv("PFSENSE_PASSWORD", "")
    verify_tls = _env_bool("PFSENSE_VERIFY_TLS", True)

    ip_to_block = os.getenv("IP_TO_BLOCK", "")

    if not (pfsense_url and username and password and ip_to_block):
        raise SystemExit("Missing env vars: PFSENSE_URL/PFSENSE_USERNAME/PFSENSE_PASSWORD/IP_TO_BLOCK")

    automator = PfSenseAutomator(pfsense_url, username, password, verify_tls=verify_tls)
    automator.login()
    automator.add_block_rule(ip_to_block)
