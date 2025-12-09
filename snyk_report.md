# Snyk Security Report

**Project:** peoplepulse  
**Date:** Nov 25, 2025  
**Command Used:** `snyk test`

---

## Summary
Snyk identified 6 vulnerabilities in the project's Python dependencies:

- **5 Medium**
- **1 Low**

All issues were related to outdated dependencies in `requirements.txt`.

---

## Vulnerabilities Found

### 1. zipp@3.15.0 — Infinite Loop (Medium)
- Introduced via: sqlalchemy, uliweb-alembic
- Fixed in: zipp@3.19.1
- **Action taken:** pinned `zipp==3.19.1`

### 2–3. requests@2.31.0 — (Medium x2)
- Sensitive information leak
- Control flow vulnerability
- **Action taken:** upgraded to `requests==2.32.4`

### 4–6. urllib3@2.0.7 — (Medium x3)
- Open Redirect
- Sensitive info exposure
- **Action taken:** upgraded to `urllib3==2.2.2`

### 7. sentry-sdk@1.28.1 — Information Exposure (Low)
- **Action taken:** upgraded to `sentry-sdk==2.8.0`

---

## Post-Fix Scan
After upgrading all dependencies, a new Snyk scan was performed.

**Result:**  
- All previously found issues resolved  
- No new vulnerabilities detected  

---

## Conclusion
Snyk scan successfully identified outdated and vulnerable dependencies.  
After remediation, the project's dependency tree is secure.
