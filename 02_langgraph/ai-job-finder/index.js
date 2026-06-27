import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { ChatGroq } from "@langchain/groq";
import { tavily } from "@tavily/core";
import dotenv from "dotenv";

dotenv.config();

// =======================================
// LLM
// =======================================

const llm = new ChatGroq({
  apiKey: process.env.GROQ_API_KEY,
  model: "llama-3.3-70b-versatile",
});

// =======================================
// Tavily
// =======================================

const tvly = tavily({
  apiKey: process.env.TAVILY_API_KEY,
});

// =======================================
// Load Resume
// =======================================

const loader = new PDFLoader("sample.pdf");

const docs = await loader.load();

const resumeText = docs
  .map((doc) => doc.pageContent)
  .join("\n");

// =======================================
// Resume Analysis
// =======================================

const summary = await llm.invoke([
  {
    role: "system",
    content: `
You are an AI Resume Analyzer.

Extract only:

- Technical Skills
- Soft Skills
- Experience Level
- Preferred Job Roles
- Projects

Return only bullet points.
`,
  },
  {
    role: "user",
    content: resumeText,
  },
]);

console.log("\n================ RESUME SUMMARY ================\n");
console.log(summary.content);

// =======================================
// Generate Search Query
// =======================================

const queryResponse = await llm.invoke([
  {
    role: "system",
    content: `
Generate ONE Google search query for finding jobs.

Example:

React Node.js MongoDB Fresher Jobs India

Return only one line.
`,
  },
  {
    role: "user",
    content: summary.content,
  },
]);

const searchQuery = queryResponse.content.trim();

console.log("\n================ SEARCH QUERY ================\n");
console.log(searchQuery);

// =======================================
// Tavily Search
// =======================================

const searchResults = await tvly.search(searchQuery, {
  topic: "general",
  searchDepth: "advanced",
  maxResults: 5,
});

// =======================================
// Format Search Results
// =======================================

const jobs = searchResults.results.map((job) => ({
  title: job.title,
  content: job.content,
  url: job.url,
}));

// =======================================
// Extract Required Fields using LLM
// =======================================

const extractedJobs = await llm.invoke([
  {
    role: "system",
    content: `
You are a Job Information Extractor.

From the provided search results extract ONLY these fields.

Return ONLY valid JSON.

Format:

[
  {
    "jobTitle":"",
    "jobRole":"",
    "salary":"",
    "link":""
  }
]

Rules:

1. Salary:
   - If unavailable write "Not Mentioned"

2. Link:
   - Use given URL

3. No explanation

4. No markdown

5. Return JSON only
`,
  },
  {
    role: "user",
    content: JSON.stringify(jobs),
  },
]);

// =======================================
// Parse JSON
// =======================================

let finalJobs = [];

try {
  finalJobs = JSON.parse(extractedJobs.content);
} catch (err) {
  console.log("Couldn't parse LLM response.");
  console.log(extractedJobs.content);
  process.exit(0);
}

// =======================================
// Print Jobs
// =======================================

console.log("\n================ JOB OPENINGS ================\n");

finalJobs.forEach((job, index) => {
  console.log(`Job ${index + 1}`);
  console.log("Title  :", job.jobTitle);
  console.log("Role   :", job.jobRole);
  console.log("Salary :", job.salary);
  console.log("Apply  :", job.link);
  console.log("------------------------------------------");
});