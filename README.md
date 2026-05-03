AWS S3 Auto Remediation Project

Overview

In cloud environments, storage misconfigurations are one of the most common security risks.
One small mistake—like making an S3 bucket public—can expose sensitive data to anyone on the internet.

This project solves that problem by building an automated security system that detects risky changes in real time and fixes them without human intervention.

Instead of relying on manual monitoring, the system enforces security automatically using AWS serverless services.

⚙️ What This Project Does
Simulates a public S3 bucket misconfiguration
Detects the risky change instantly
Triggers an automated response
Fixes the security issue automatically
Restores the bucket to a secure state

👉 In simple words:
If someone makes the bucket public, the system immediately detects it and locks it back down automatically.

🏗️ Architecture

S3 → CloudTrail → EventBridge → Lambda → Auto Remediation

Simple flow explanation:
Amazon S3 → Stores data (where misconfiguration happens)
CloudTrail → Records all AWS activity (who changed what)
EventBridge → Detects specific risky events
Lambda → Executes automatic fix logic
Auto Remediation → Restores secure configuration

👉 This is an event-driven security automation system.

Project Demonstration

The project is validated using two states:

🟥 BEFORE STATE (Risk Condition)
S3 bucket has public access enabled
Security warning is visible
System detects misconfiguration

https://github.com/Eshapatel03/aws-s3-auto-remediation/blob/main/before-block-public-access-off.png
https://github.com/Eshapatel03/aws-s3-auto-remediation/blob/main/before-public-policy-visible.png

🟩 AFTER STATE (Secure Condition)
Public access is removed or blocked
Bucket is secured automatically
No manual intervention required

https://github.com/Eshapatel03/aws-s3-auto-remediation/blob/main/after-block-public-access-on.png
https://github.com/Eshapatel03/aws-s3-auto-remediation/blob/main/after-policy-removed.png
👉 These screenshots prove real-time detection and automatic remediation.

🛠️ Tech Stack
Amazon S3 → Storage service used for simulation
AWS Lambda → Executes remediation logic automatically
Amazon EventBridge → Triggers actions based on events
AWS CloudTrail → Tracks API activity and changes
🎯 Key Learning Outcome

This project demonstrates:

Event-driven architecture design
Serverless automation using AWS
Real-time security monitoring concepts
Cloud security best practices (DevSecOps mindset)
💡 Why This Project Matters

In real-world cloud environments:

Misconfigured S3 buckets are a major security risk
Manual monitoring is slow and unreliable
Automated remediation reduces breach risk

👉 This system shows how security can be self-healing instead of reactive

📌 Summary

This project is a lightweight AWS security automation system that:

Detects risky cloud configuration changes
Automatically fixes them in real time
Demonstrates serverless DevSecOps principles
