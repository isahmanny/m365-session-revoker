# M365 Session Revoker

A white-hat Python security tool that simulates Microsoft 365 
sign-in session analysis, flags suspicious sessions based on 
risk indicators, and generates a professional HTML report.

## Features
- Detects high-risk country logins (RU, CN, KP, IR)
- Flags legacy authentication (IMAP, POP3, SMTP Auth)
- Identifies stale session tokens (30+ days)
- Detects failed sign-in attempts
- One-click session revocation (simulated)
- Generates a dark-themed HTML risk dashboard

## Risk Scoring
| Level | Triggers |
|-------|----------|
| HIGH | 2+ risk indicators |
| MEDIUM | 1 risk indicator |
| LOW | No indicators |

## Tools Used
- Python 3.12
- Microsoft Graph API (architecture)
- MSAL authentication library

## Project Context
Built as part of AltSchool Africa Cybersecurity programme.
Covers: Session Protection, Identity Security, SOC monitoring.
