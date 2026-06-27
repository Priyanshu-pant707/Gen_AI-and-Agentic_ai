# 🤖 AI Resume Job Finder

An AI-powered Resume Analyzer that automatically extracts skills from a resume, understands the candidate's profile using a Large Language Model (LLM), searches the web for relevant job openings, and presents only the most useful information such as **Job Title**, **Role**, **Salary**, and **Apply Link**.

---

# 🚀 Features

* 📄 Upload and parse PDF resumes.
* 🧠 AI-powered resume analysis using Groq Llama 3.3.
* 💻 Extract:

  * Technical Skills
  * Soft Skills
  * Experience Level
  * Preferred Job Roles
  * Projects
* 🔍 Automatically generate optimized job search queries.
* 🌐 Search the latest job openings using Tavily Search API.
* ✨ Extract only important job information:

  * Job Title
  * Job Role
  * Salary
  * Apply Link
* ⚡ Fast and lightweight prototype built with Node.js.

---

# 📌 Problem Statement

Finding relevant jobs manually is time-consuming.

Candidates usually have to:

* Read their own resume.
* Identify their skills.
* Search multiple job portals.
* Open every job posting.
* Check whether the role matches their profile.

This project automates the entire process using AI.

---

# 🏗️ Project Workflow

```text
                Resume.pdf
                     │
                     ▼
          PDF Loader (LangChain)
                     │
                     ▼
             Resume Text Extraction
                     │
                     ▼
          Groq LLM Resume Analyzer
                     │
                     ▼
        Skills & Experience Extraction
                     │
                     ▼
        AI Search Query Generator
                     │
                     ▼
            Tavily Web Search API
                     │
                     ▼
        Latest Relevant Job Openings
                     │
                     ▼
       Groq Job Information Extractor
                     │
                     ▼
     Clean Job Details for the User
```

---

# 🧠 AI Pipeline

## Step 1 — Resume Loading

The application reads a PDF resume using LangChain's PDF Loader.

Output:

* Raw Resume Text

---

## Step 2 — Resume Analysis

The resume text is sent to Groq Llama 3.3.

The model extracts:

* Technical Skills
* Soft Skills
* Experience Level
* Preferred Roles
* Projects

Example:

```text
• React
• Node.js
• MongoDB
• Express
• FastAPI
• REST API
• Fresher
• Full Stack Developer
```

---

## Step 3 — Search Query Generation

Instead of manually writing search keywords, another LLM prompt generates an optimized search query.

Example:

```text
React Node.js MongoDB Full Stack Fresher Jobs India
```

---

## Step 4 — Job Search

The generated query is sent to Tavily Search API.

Tavily searches multiple trusted websites and returns the latest relevant job postings.

---

## Step 5 — AI Job Extraction

Raw search results usually contain large paragraphs.

The LLM extracts only useful information.

Example:

```json
{
  "jobTitle": "Software Engineer",
  "jobRole": "Backend Developer",
  "salary": "₹8-12 LPA",
  "link": "https://..."
}
```

---

# 📂 Tech Stack

## Backend

* Node.js
* JavaScript (ES Modules)

## AI

* LangChain
* Groq API
* Llama 3.3 70B

## Search

* Tavily Search API

## Resume Parsing

* LangChain PDF Loader

---

# 📁 Folder Structure

```text
AI-Resume-Job-Finder/

│
├── sample.pdf
├── index.js
├── package.json
├── .env
└── README.md
```

---

# 🔑 Environment Variables

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# 📦 Installation

Install dependencies

```bash
npm install
```

Run

```bash
node index.js
```

---

# 📤 Sample Output

```text
============= RESUME SUMMARY =============

• React
• Node.js
• MongoDB
• Express
• FastAPI

Experience:
Fresher

Preferred Role:
Backend Developer

================ JOB OPENINGS ================

Job 1

Title :
Software Engineer

Role :
Backend Developer

Salary :
₹8-12 LPA

Apply :
https://company.com/jobs/123

------------------------------------------

Job 2

Title :
Associate Software Engineer

Role :
Full Stack Developer

Salary :
Not Mentioned

Apply :
https://company.com/jobs/456
```

---

# 💡 Future Improvements

* LangGraph Workflow
* Multi-Agent Architecture
* ATS Score Calculation
* Resume Improvement Suggestions
* Skill Gap Analysis
* Semantic Resume Matching
* Vector Database
* Company Recommendation Engine
* One-click Job Application
* AI Career Advisor
* Daily Job Notifications
* Job Bookmarking
* Dashboard with Analytics

---

# 🔮 Planned LangGraph Architecture

```text
                   START
                      │
                      ▼
               Resume Parser
                      │
                      ▼
             Skill Extraction
                      │
                      ▼
         Search Query Generator
                      │
                      ▼
             Tavily Tool Node
                      │
                      ▼
          Job Information Extractor
                      │
                      ▼
            Resume Job Matcher
                      │
                      ▼
             ATS Score Generator
                      │
                      ▼
                Final Results
                      │
                      ▼
                     END
```

---

# 🎯 Use Cases

* Freshers searching for jobs
* Resume screening
* AI Recruitment Assistant
* Placement Cell Automation
* Career Guidance Platform
* ATS Resume Analysis
* Job Recommendation Systems

---

# 👨‍💻 Author

**Priyanshu Pant**

B.Tech Computer Science Engineering

Graphic Era Hill University

---

# ⭐ Future Vision

The current project is a working prototype.

The long-term vision is to build an **AI Career Assistant** capable of:

* Reading resumes
* Understanding user skills
* Finding real-time jobs
* Calculating ATS scores
* Recommending missing skills
* Suggesting learning resources
* Tracking job applications
* Acting as an intelligent career coach powered by LangGraph agents.
`