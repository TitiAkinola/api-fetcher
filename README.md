Project Overview
This repository contains a robust Python-based monitoring utility designed to perform automated health checks on web 
endpoints. Developed as part of an SRE automation toolkit, this script helps reduce manual "toil" by providing real-time 
visibility into service uptime and response reliability.

Key Features
Automated Status Verification: Leverages the requests library to validate HTTP response codes (2xx/3xx).

Resilient Error Handling: Implements try-except blocks to handle network timeouts, DNS resolution failures, and 
connection resets without crashing.

Operational Transparency: Provides clear, emoji-coded terminal output for rapid diagnostic assessment during incident 
response.

Performance Optimized: Configured with a 5-second timeout to prevent "hanging" processes in automation pipelines.

Technical Specifications
Language: Python 3.x

Primary Library: requests

Focus Areas: Network reliability, Error handling, Operational automation

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/TitiAkinola/service-uptime-monitor.git
cd service-uptime-monitor
Install dependencies:

Bash

pip install -r requirements.txt
Usage
To run a health check against the configured endpoints:

Bash

python monitor.py
Sample Output
Plaintext

--- Starting API Health Check ---
✅ UP: https://www.google.com (Status: 200)
⚠️ DOWN: https://httpstat.us/404 (Status: 404)
❌ DOWN: https://thisisafakesite123.com (Error: ConnectionError)
SRE & Roadmap Enhancements
This project was built with scalability in mind. Planned future enhancements include:

[ ] Multi-threading: Implementation of concurrent.futures to ping multiple endpoints in parallel.

[ ] Alerting Integration: Adding Slack or PagerDuty webhooks to notify on-call engineers when a 5xx error is detected.

[ ] Logging: Exporting results to a .log or .json file for long-term reliability trending.
