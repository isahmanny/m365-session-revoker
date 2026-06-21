"""
M365 Session Revoker - Mock Data Version
=========================================
Portfolio demonstration tool for AltSchool Africa Cybersecurity.
Simulates realistic Microsoft 365 sign-in sessions, performs risk
analysis, and generates a professional HTML report.

No Microsoft account or API credentials required.

Run:
    python session_revoker_mock.py
"""

import datetime
import random
import json
from pathlib import Path

# ─────────────────────────────────────────────
# MOCK DATA — realistic M365 sign-in sessions
# ─────────────────────────────────────────────

MOCK_USERS = [
    {"id": "u001", "displayName": "Amina Yusuf",       "upn": "amina.yusuf@contoso.onmicrosoft.com"},
    {"id": "u002", "displayName": "Chidi Okafor",      "upn": "chidi.okafor@contoso.onmicrosoft.com"},
    {"id": "u003", "displayName": "Fatima Al-Hassan",  "upn": "fatima.alhassan@contoso.onmicrosoft.com"},
    {"id": "u004", "displayName": "James Okonkwo",     "upn": "james.okonkwo@contoso.onmicrosoft.com"},
    {"id": "u005", "displayName": "Sarah Adeyemi",     "upn": "sarah.adeyemi@contoso.onmicrosoft.com"},
    {"id": "u006", "displayName": "Michael Eze",       "upn": "michael.eze@contoso.onmicrosoft.com"},
    {"id": "u007", "displayName": "Ngozi Ibrahim",     "upn": "ngozi.ibrahim@contoso.onmicrosoft.com"},
    {"id": "u008", "displayName": "Ahmed Musa",        "upn": "ahmed.musa@contoso.onmicrosoft.com"},
]

MOCK_SESSIONS = [
    # ── HIGH RISK ──────────────────────────────────────────────────────
    {
        "id": "s001",
        "userId": "u001",
        "userDisplayName": "Amina Yusuf",
        "userPrincipalName": "amina.yusuf@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=35)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "185.220.101.47",
        "location": {"city": "Moscow", "countryOrRegion": "RU"},
        "clientAppUsed": "python-requests/2.31",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "Unknown", "browser": "Unknown"},
    },
    {
        "id": "s002",
        "userId": "u003",
        "userDisplayName": "Fatima Al-Hassan",
        "userPrincipalName": "fatima.alhassan@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "103.75.190.12",
        "location": {"city": "Beijing", "countryOrRegion": "CN"},
        "clientAppUsed": "SMTP Auth",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "Unknown", "browser": "Unknown"},
    },
    {
        "id": "s003",
        "userId": "u006",
        "userDisplayName": "Michael Eze",
        "userPrincipalName": "michael.eze@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=40)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "91.108.56.22",
        "location": {"city": "Tehran", "countryOrRegion": "IR"},
        "clientAppUsed": "curl/7.88",
        "status": {"errorCode": 53003},
        "deviceDetail": {"operatingSystem": "Linux", "browser": "Unknown"},
    },

    # ── MEDIUM RISK ────────────────────────────────────────────────────
    {
        "id": "s004",
        "userId": "u002",
        "userDisplayName": "Chidi Okafor",
        "userPrincipalName": "chidi.okafor@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=32)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "197.210.54.101",
        "location": {"city": "Lagos", "countryOrRegion": "NG"},
        "clientAppUsed": "IMAP",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "Windows 10", "browser": "Unknown"},
    },
    {
        "id": "s005",
        "userId": "u005",
        "userDisplayName": "Sarah Adeyemi",
        "userPrincipalName": "sarah.adeyemi@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=10)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "41.58.99.34",
        "location": {"city": "Accra", "countryOrRegion": "GH"},
        "clientAppUsed": "Microsoft Office",
        "status": {"errorCode": 50126},
        "deviceDetail": {"operatingSystem": "Windows 11", "browser": "Edge 120"},
    },
    {
        "id": "s006",
        "userId": "u007",
        "userDisplayName": "Ngozi Ibrahim",
        "userPrincipalName": "ngozi.ibrahim@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(days=28)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "77.88.55.66",
        "location": {"city": "Abuja", "countryOrRegion": "NG"},
        "clientAppUsed": "POP3",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "Android 13", "browser": "Chrome Mobile"},
    },

    # ── LOW RISK ───────────────────────────────────────────────────────
    {
        "id": "s007",
        "userId": "u004",
        "userDisplayName": "James Okonkwo",
        "userPrincipalName": "james.okonkwo@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "102.89.45.23",
        "location": {"city": "Abuja", "countryOrRegion": "NG"},
        "clientAppUsed": "Microsoft Teams",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "Windows 11", "browser": "Edge 120"},
    },
    {
        "id": "s008",
        "userId": "u008",
        "userDisplayName": "Ahmed Musa",
        "userPrincipalName": "ahmed.musa@contoso.onmicrosoft.com",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "105.112.10.88",
        "location": {"city": "Kano", "countryOrRegion": "NG"},
        "clientAppUsed": "Outlook Mobile",
        "status": {"errorCode": 0},
        "deviceDetail": {"operatingSystem": "iOS 17", "browser": "Safari"},
    },
]

# ─────────────────────────────────────────────
# RISK RULES
# ─────────────────────────────────────────────
SUSPICIOUS_COUNTRIES    = {"RU", "CN", "KP", "IR"}
OLD_TOKEN_THRESHOLD_DAYS = 30
SUSPICIOUS_USER_AGENTS  = ["python-requests", "curl", "go-http-client", "axios", "scrapy"]
LEGACY_AUTH_APPS        = {"imap", "pop3", "smtp auth", "exchange active sync", "mapi over http"}


def assess_risk(session: dict) -> tuple[str, list[str]]:
    reasons = []

    # Suspicious country
    country = (session.get("location") or {}).get("countryOrRegion", "")
    if country in SUSPICIOUS_COUNTRIES:
        reasons.append(f"Login from high-risk country: {country}")

    # Suspicious user agent / client
    client = session.get("clientAppUsed", "").lower()
    for ua in SUSPICIOUS_USER_AGENTS:
        if ua in client:
            reasons.append(f"Suspicious client app: {session.get('clientAppUsed')}")
            break

    # Legacy auth
    if any(la in client for la in LEGACY_AUTH_APPS):
        reasons.append(f"Legacy authentication: {session.get('clientAppUsed')}")

    # Failed sign-in
    error = (session.get("status") or {}).get("errorCode", 0)
    if error != 0:
        reasons.append(f"Failed sign-in attempt (error code {error})")

    # Old token
    created_str = session.get("createdDateTime", "")
    if created_str:
        try:
            created  = datetime.datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            age_days = (datetime.datetime.now(datetime.timezone.utc) - created).days
            if age_days > OLD_TOKEN_THRESHOLD_DAYS:
                reasons.append(f"Stale session token: {age_days} days old")
        except ValueError:
            pass

    if len(reasons) >= 2:
        return "HIGH", reasons
    elif len(reasons) == 1:
        return "MEDIUM", reasons
    else:
        return "LOW", reasons


# ─────────────────────────────────────────────
# HTML REPORT
# ─────────────────────────────────────────────
def generate_report(sessions_with_risk: list[dict], revoked_ids: set[str]) -> str:
    now    = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    high   = [s for s in sessions_with_risk if s["risk"] == "HIGH"]
    medium = [s for s in sessions_with_risk if s["risk"] == "MEDIUM"]
    low    = [s for s in sessions_with_risk if s["risk"] == "LOW"]

    def badge(risk):
        colors = {"HIGH": "#dc2626", "MEDIUM": "#d97706", "LOW": "#16a34a"}
        return f'<span class="badge" style="background:{colors[risk]}">{risk}</span>'

    def rows(lst):
        if not lst:
            return '<tr><td colspan="7" class="empty">No sessions in this category.</td></tr>'
        out = ""
        for item in lst:
            s   = item["session"]
            uid = s.get("userId", "")
            loc = s.get("location") or {}
            rev = " &nbsp;<span class='rev-tag'>✓ REVOKED</span>" if uid in revoked_ids else ""
            out += f"""
            <tr class="{'revoked-row' if uid in revoked_ids else ''}">
              <td><strong>{s.get('userDisplayName','—')}</strong><br>
                  <small>{s.get('userPrincipalName','')}</small></td>
              <td class="mono">{s.get('createdDateTime','—')[:19].replace('T',' ')}</td>
              <td class="mono">{s.get('ipAddress','—')}</td>
              <td>{loc.get('city','—')}, {loc.get('countryOrRegion','—')}</td>
              <td>{s.get('clientAppUsed','—')}</td>
              <td>{badge(item['risk'])}</td>
              <td>{'<br>'.join(item['reasons']) if item['reasons'] else '—'}{rev}</td>
            </tr>"""
        return out

    def section(title, emoji, lst):
        return f"""
        <section>
          <h2>{emoji} {title} <span class="count">({len(lst)})</span></h2>
          <div class="table-wrap">
            <table>
              <thead><tr>
                <th>User</th><th>Sign-in Time (UTC)</th><th>IP Address</th>
                <th>Location</th><th>Client App</th><th>Risk</th><th>Flags / Notes</th>
              </tr></thead>
              <tbody>{rows(lst)}</tbody>
            </table>
          </div>
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>M365 Session Risk Report</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
  *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Inter',sans-serif;background:#0a0f1e;color:#e2e8f0;min-height:100vh;padding:2rem 2.5rem}}

  /* HEADER */
  header{{margin-bottom:2.5rem;padding-bottom:1.5rem;border-bottom:1px solid #1e293b}}
  .header-top{{display:flex;align-items:center;gap:1rem;margin-bottom:0.5rem}}
  .logo{{width:42px;height:42px;background:linear-gradient(135deg,#6366f1,#8b5cf6);border-radius:10px;
         display:flex;align-items:center;justify-content:center;font-size:1.3rem}}
  header h1{{font-size:1.6rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em}}
  .meta{{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#475569}}
  .meta span{{margin-right:1.5rem}}
  .mock-badge{{display:inline-block;background:#1e3a5f;color:#60a5fa;border:1px solid #2563eb;
               padding:0.2rem 0.6rem;border-radius:4px;font-size:0.65rem;font-weight:600;
               letter-spacing:0.08em;margin-left:0.75rem;vertical-align:middle}}

  /* STAT CARDS */
  .stats{{display:grid;grid-template-columns:repeat(5,1fr);gap:1rem;margin-bottom:2.5rem}}
  .card{{background:#0f172a;border:1px solid #1e293b;border-radius:12px;padding:1.25rem 1.5rem}}
  .card .label{{font-size:0.7rem;color:#64748b;text-transform:uppercase;letter-spacing:0.1em;font-weight:600}}
  .card .val{{font-size:2rem;font-weight:700;margin-top:0.3rem;font-family:'JetBrains Mono',monospace}}
  .card.total  .val{{color:#818cf8}}
  .card.high   .val{{color:#f87171}}
  .card.medium .val{{color:#fbbf24}}
  .card.low    .val{{color:#4ade80}}
  .card.revoked .val{{color:#38bdf8}}

  /* SECTIONS */
  section{{margin-bottom:2.5rem}}
  section h2{{font-size:0.95rem;font-weight:600;color:#94a3b8;margin-bottom:0.75rem;
              display:flex;align-items:center;gap:0.4rem}}
  .count{{color:#475569;font-weight:400}}

  /* TABLE */
  .table-wrap{{overflow-x:auto;border-radius:10px;border:1px solid #1e293b}}
  table{{width:100%;border-collapse:collapse;font-size:0.8rem}}
  thead th{{background:#0f172a;color:#475569;font-weight:600;text-transform:uppercase;
            letter-spacing:0.07em;font-size:0.68rem;padding:0.8rem 1rem;
            text-align:left;border-bottom:1px solid #1e293b}}
  tbody tr{{border-bottom:1px solid #0f172a;transition:background 0.12s}}
  tbody tr:hover{{background:#0f172a}}
  tbody tr:last-child{{border-bottom:none}}
  tbody td{{padding:0.75rem 1rem;color:#cbd5e1;vertical-align:top;line-height:1.6}}
  tbody td small{{color:#475569;font-size:0.7rem}}
  .mono{{font-family:'JetBrains Mono',monospace;font-size:0.75rem}}
  .empty{{text-align:center;color:#334155;padding:1.5rem!important}}
  .revoked-row{{opacity:0.55}}
  .rev-tag{{background:#0c4a6e;color:#38bdf8;font-size:0.65rem;padding:0.15rem 0.45rem;
             border-radius:3px;font-weight:600;font-family:'JetBrains Mono',monospace}}

  /* BADGE */
  .badge{{display:inline-block;padding:0.2rem 0.55rem;border-radius:4px;font-size:0.65rem;
          font-weight:700;letter-spacing:0.08em;color:#fff;font-family:'JetBrains Mono',monospace}}

  /* FOOTER */
  footer{{text-align:center;color:#334155;font-size:0.72rem;margin-top:3rem;
          font-family:'JetBrains Mono',monospace;padding-top:1.5rem;border-top:1px solid #1e293b}}
</style>
</head>
<body>

<header>
  <div class="header-top">
    <div class="logo">🛡</div>
    <h1>M365 Session Risk Report <span class="mock-badge">SIMULATED DATA</span></h1>
  </div>
  <div class="meta">
    <span>Generated: {now}</span>
    <span>Tool: session_revoker_mock.py</span>
    <span>Tenant: contoso.onmicrosoft.com</span>
    <span>Window: Last 7 days</span>
  </div>
</header>

<div class="stats">
  <div class="card total">
    <div class="label">Total Sessions</div>
    <div class="val">{len(sessions_with_risk)}</div>
  </div>
  <div class="card high">
    <div class="label">High Risk</div>
    <div class="val">{len(high)}</div>
  </div>
  <div class="card medium">
    <div class="label">Medium Risk</div>
    <div class="val">{len(medium)}</div>
  </div>
  <div class="card low">
    <div class="label">Low Risk</div>
    <div class="val">{len(low)}</div>
  </div>
  <div class="card revoked">
    <div class="label">Revoked</div>
    <div class="val">{len(revoked_ids)}</div>
  </div>
</div>

{section("High Risk Sessions", "🔴", high)}
{section("Medium Risk Sessions", "🟡", medium)}
{section("Low Risk Sessions", "🟢", low)}

<footer>
  session_revoker_mock.py &nbsp;|&nbsp; AltSchool Africa Cybersecurity Portfolio &nbsp;|&nbsp;
  White-hat defensive security tool &nbsp;|&nbsp; {now}
</footer>

</body>
</html>"""


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    print("\n╔══════════════════════════════════════╗")
    print("║   M365 Session Revoker v1.0 (Mock)   ║")
    print("║   AltSchool Cybersecurity Portfolio   ║")
    print("╚══════════════════════════════════════╝\n")

    print("[1/3] Loading simulated M365 sign-in sessions...")
    print(f"      {len(MOCK_SESSIONS)} sessions loaded.\n")

    print("[2/3] Analysing sessions for risk indicators...")
    sessions_with_risk = []
    for s in MOCK_SESSIONS:
        risk, reasons = assess_risk(s)
        sessions_with_risk.append({"session": s, "risk": risk, "reasons": reasons})

    high   = [x for x in sessions_with_risk if x["risk"] == "HIGH"]
    medium = [x for x in sessions_with_risk if x["risk"] == "MEDIUM"]
    low    = [x for x in sessions_with_risk if x["risk"] == "LOW"]

    print(f"      🔴 HIGH:   {len(high)}")
    print(f"      🟡 MEDIUM: {len(medium)}")
    print(f"      🟢 LOW:    {len(low)}\n")

    # Show suspicious sessions
    suspicious = high + medium
    revoked_ids = set()

    if suspicious:
        print("─" * 55)
        print(" SUSPICIOUS SESSIONS DETECTED:")
        print("─" * 55)
        for i, item in enumerate(suspicious):
            s = item["session"]
            loc = s.get("location") or {}
            print(f"  [{i+1}] {s.get('userDisplayName','?'):<20} "
                  f"{item['risk']:<6}  "
                  f"{s.get('ipAddress','?'):<18}  "
                  f"{loc.get('countryOrRegion','?')}")
            for r in item["reasons"]:
                print(f"       ↳ {r}")
        print("─" * 55)

        print("\nRevocation options:")
        print("  A — Revoke ALL suspicious sessions (simulated)")
        print("  S — Select specific sessions to revoke")
        print("  N — Skip (report only)\n")

        choice = input("Your choice [A/S/N]: ").strip().upper()

        if choice == "A":
            seen = set()
            for item in suspicious:
                uid  = item["session"].get("userId")
                name = item["session"].get("userDisplayName", uid)
                if uid and uid not in seen:
                    seen.add(uid)
                    print(f"  [SIM] Revoking sessions for {name}... ✓ Success")
                    revoked_ids.add(uid)

        elif choice == "S":
            nums = input("Enter numbers (comma-separated, e.g. 1,3): ").strip()
            indices = [int(x.strip()) - 1 for x in nums.split(",") if x.strip().isdigit()]
            seen = set()
            for idx in indices:
                if 0 <= idx < len(suspicious):
                    uid  = suspicious[idx]["session"].get("userId")
                    name = suspicious[idx]["session"].get("userDisplayName", uid)
                    if uid and uid not in seen:
                        seen.add(uid)
                        print(f"  [SIM] Revoking sessions for {name}... ✓ Success")
                        revoked_ids.add(uid)
        else:
            print("  Skipping revocation.\n")

    print(f"\n[3/3] Generating HTML report...")
    html = generate_report(sessions_with_risk, revoked_ids)
    out  = Path("session_report.html")
    out.write_text(html, encoding="utf-8")
    print(f"      ✓ Report saved → {out.resolve()}\n")
    print("  Open session_report.html in your browser to view the dashboard.")
    print()


if __name__ == "__main__":
    main()
