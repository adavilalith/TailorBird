🚀 TailorBird

An end-to-end, self-hosted automation ecosystem designed to bridge the gap between job hunting and professional identity management. This project uses **n8n** to orchestrate a seamless flow between **LLM-powered resume generation**, **LaTeX-based high-fidelity PDFs**, and **automated application tracking** via Google Sheets and Gmail.

### 🛠️ The Tech Stack

* **Orchestration:** [n8n](https://n8n.io/) (Self-hosted on OCI via Docker)
* **Logic Engine:** [FastAPI](https://fastapi.tiangolo.com/) (Managed with `uv`)
* **Database:** [Google Sheets API](https://developers.google.com/sheets/api) (Application Tracker)
* **Intelligence:** OpenAI / Meta (Tailoring & Email Categorization)
* **Rendering:** LaTeX (Professional PDF Generation)
* **Automation:** Gmail API (Live Status Updates)

### ✨ Key Features

* **🎯 Smart Tailoring:** Automatically rewrites resume bullet points to align with specific Job Descriptions while maintaining technical accuracy.
* **📄 LaTeX Precision:** Supports both raw LaTeX input for power users and AI-generated LaTeX strings for professional, ATS-optimized formatting.
* **📊 Unified Dashboard:** A Google Sheet acts as a "live database," tracking every application, the resume version used, and the current status.
* **📩 Inbox Intelligence:** A background n8n worker monitors Gmail for recruitment updates (Interviews, Rejections, Offers) and updates the Tracker sheet in real-time using AI categorization.
* **🔄 Version Control:** Stores every generated resume in Google Drive with unique identifiers linked directly to your application history.
