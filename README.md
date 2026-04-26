# deccan-ai-catalyst-ai-scout
Parnikaa's submission for Deccan AI's Catalyst Hackathon April 2026

#  AI-Powered Talent Scouting & Engagement Agent

## Problem Statement

Recruiters spend significant time searching for candidates and assessing their interest. This project builds an **AI agent** that automates:
* Job Description (JD) parsing
* Candidate matching
* Simulated outreach to gauge interest
* Final ranked shortlist

---

## Features

### 1. JD Parsing

* Extracts structured information from raw job description texts:
  * Role
  * Skills
  * Experience

### Intelligent Candidate Matching

* Matches candidates based on:
  * Skill overlap (with synonym-based and fuzzy matching)
  * Minimum number of years of experience
    
* Provides **explanations**:
  * Matched skills
  * Missing skills

### Conversational Outreach (Simulated)

* Uses LLM (Gemini-2.5-flash) to simulate candidate responses
* Determines **interest level**

###  Scoring & Ranking

Each candidate is scored on:

* **Match Score** (skills + experience)
* **Interest Score** (based on response)

Final ranking:

```text
Final Score = 0.7 × Match Score + 0.3 × Interest Score
```

###  Output

* Ranked shortlist
* Top candidate highlighted

---

##  Architecture

```
Job Description
      ↓
JD Parser (LLM - Gemini)
      ↓
Candidate Dataset (JSON)
      ↓
Matching Engine (Synonyms + Fuzzy matches)
      ↓
Outreach (LLM)
      ↓
Interest Scoring
      ↓
Ranking Engine
      ↓
Streamlit UI
      ↓
Top Candidate Matched
```

---

## Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **LLM**: Google Gemini API (models/gemini-2.5-flash)
* **Data**: JSON-based candidate and JD datasets

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/paribr777/deccan-ai-catalyst-ai-scout
cd deccan-ai-catalyst-ai-scout
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the app

```bash
streamlit run app.py
```

---

## Sample Input

```
We are hiring a Software Engineer skilled in UI/UX with at least 6 years of experience.
```

---

##  Sample Output

*  Top Match: Aarav (1 skill matched)
* Ranked candidates with:

  * Match Score
  * Interest Score
  * Matched & Missing Skills
  * Simulated Responses

---

##  Key Design Decisions

###  Synonym-Based Matching

Handles real-world variations:

* UI/UX ↔ Frontend / React
* Speech Tech ↔ NLP / Audio

###  Batch LLM Calls

* Avoids API rate exhaustion
* Improves efficiency

---

## Demo Video

(Add your demo video link here)


