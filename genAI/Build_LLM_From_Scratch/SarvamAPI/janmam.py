import time

import requests
YOUR_API_KEY='sk_iam3dtvk_AUWCEwLOAIfR4FvWoVRCzPwT'

BASE = "https://api.sarvam.ai/doc-ai/v1"
HEADERS = {"api-subscription-key": YOUR_API_KEY}
TERMINAL = {"completed", "partially_completed", "failed", "rejected"}

# Submit the job — one multipart request, no pre-upload needed.
with open("jan_pic.png", "rb") as document:
    submit = requests.post(
        f"{BASE}/job/digitise",
        headers=HEADERS,
        files={"file": ("jan_pic.png", document)},
        data={
            "language": "or-IN",
            "output_format": "html",
            "content_type": "printed",
            "auto_orient": "true",
        },
        timeout=120,
    )
submit.raise_for_status()
job_id = submit.json()["job_id"]
print(f"Job created: {job_id}")

# Poll until the job reaches a terminal status.
while True:
    status = requests.get(f"{BASE}/job/{job_id}/status", headers=HEADERS, timeout=30).json()
    usage = status["usage"]
    print(f'{status["status"]} — {usage["pages_processed"]}/{usage["pages_total"]} pages')
    if status["status"] in TERMINAL:
        break
    time.sleep(2)

if status["status"] in {"failed", "rejected"}:
    raise SystemExit(f'Job {status["status"]}')

# Mint a download URL for the rendered output and save it
link = requests.get(f"{BASE}/job/{job_id}/download-url", headers=HEADERS, timeout=30).json()
output = requests.get(link["url"], headers=link.get("headers") or {}, timeout=300)
with open("output.zip", "wb") as f:
    f.write(output.content)
print("Saved output.zip")