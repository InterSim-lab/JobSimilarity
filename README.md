# 🚀 InterSim Job Similarity API Documentation

## 📖 Overview
Welcome to the InterSim Job Similarity API! This comprehensive API helps job seekers and employers discover and explore job opportunities through intelligent matching and search capabilities.

## 🎯 Key Features
- Discover random jobs
- Search jobs by category
- Find similar job recommendations
- Retrieve detailed job information
- Generate interview preparation questions
- Create personalized job summaries

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/InterSim-lab/JobSimilarity.git
   cd JobSimilarity
   ```

2. **Create Virtual Environment**
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

4. **Run the API**
   ```bash
   # Start the development server
   uvicorn app.main:app --reload
   ```

## 🌐 API Endpoints

### 1. Health Check 🏥
- **Endpoint:** `GET /`
- **Description:** Verify API is running
- **Response:** 
  ```json
  {
      "message": "Hello World",
      "status": "API is healthy",
      "version": "0.2.0"
  }
  ```

### 2. Random Jobs Discovery 🎲
- **Endpoint:** `GET /api/jobs/random`
- **Parameters:**
  - `limit` (optional): Number of random jobs to retrieve
  - **Default:** 10
  - **Max:** 50
- **Example:** `/api/jobs/random?limit=20`

### 3. Jobs by Category 📑
- **Endpoint:** `GET /api/jobs/category/{category}`
- **Parameters:**
  - `category`: Job category (e.g., "Operations", "Technology")
  - `limit` (optional): Number of jobs to return
  - **Default:** 10
  - **Max:** 50
- **Example:** `/api/jobs/category/Technology?limit=15`

### 4. Job Details 📋
- **Endpoint:** `GET /api/jobs/{id}`
- **Parameters:**
  - `id`: Unique job identifier
- **Example:** `/api/jobs/85`

### 5. Similar Jobs Recommendation 🤝
- **Endpoint:** `GET /api/jobs/{id}/similar`
- **Parameters:**
  - `id`: Base job ID for similarity search
  - `limit` (optional): Number of similar jobs
  - **Default:** 10
  - **Max:** 50
- **Example:** `/api/jobs/85/similar?limit=20`

### 6. Job Title Search 🔎
- **Endpoint:** `GET /api/jobs`
- **Parameters:**
  - `title` (required): Job title search term
- **Example:** `/api/jobs?title=Flutter%20Developer%20Intern`

## 💡 Interview Preparation Features
BASE URL: `https://intersim-qs-model-8724644534.asia-southeast2.run.app`
### 7. Generate Interview Questions
- **Endpoint:** `POST https://intersim-qs-rebuild-8724644534.us-central1.run.app/generate/questions`
- **Request Body:**
  ```json
  {
      "id": [jobId]
  }
  ```
- **Response Example:**
  ```json
  {
    "uuid": "f1007d0c-37a2-45fd-8e4a-d09932acbfa5",
    "generated_at": "2024-12-13T08:52:15.827131",
    "questions": [
        {
            "id": "q1",
            "question": "Bagaimana perjalanan Anda ke sini hari ini?",
            "type": "Warm-up"
        },
        {
            "id": "q2",
            "question": "Apa hal yang membuat Anda tertarik dengan posisi Sales Executive di PT. MEA DIGITAL MARKETING?",
            "type": "Warm-up"
        }
    ]
  }
  ```

### 8. Generate Interview Summary
- **Endpoint:** `POST /generate/summary`
- **Request Body:**
  ```json
  {
      "questions": [generated questions],
      "answers": [user's answers]
  }
  ```
- **Response Example:**
```json
{
    "uuid": "cd412df2-393c-47d3-86fc-e32b18948a3b",
    "generated_at": "2024-12-13T08:48:07.719392",
    "summary": "## Summary\n\n💡 **Potensi & Kemampuan**: Kamu memiliki potensi yang baik sebagai Host untuk live streaming, kamu memiliki kemampuan komunikasi yang baik dan dapat menarik perhatian pemirsa. Kamu juga memiliki pengalaman dalam kegiatan debat dan teater yang membantu kamu mengembangkan kemampuan komunikasi yang baik.\n\n🎓 **Pengetahuan**: Kamu memiliki pengetahuan yang cukup tentang bagaimana menghadapi situasi yang membuat kamu tidak nyaman di depan umum, dan kamu tahu cara mengelola waktu untuk membuat laporan hasil pekerjaan.\n\n🗣️ **Kemampuan Komunikasi**: Kamu memiliki kemampuan komunikasi yang baik, kamu dapat menjelaskan produk baru dengan cara yang mudah dipahami oleh pemirsa, dan kamu juga dapat meningkatkan interaksi pemirsa dengan isi acara live streaming.\n\n🌟 **Catatan Khusus**: Kamu memiliki goal yang jelas dalam beberapa tahun ke depan, yaitu menjadi seorang Host yang profesional, dan kamu juga tertarik dengan Nuenco karena perusahaan ini memiliki visi yang baik.\n\n🌈 **Saran & Dukungan**: Teruslah meningkatkan kemampuan komunikasi kamu dan jangan takut untuk mencoba hal-hal baru. Kami percaya bahwa kamu memiliki potensi yang besar dan kita sangat ingin melihat kamu berkembang dalam posisi Host untuk live streaming ini. Keep shining, you got this! 💪"
}
```

## 📝 Job Object Schema
```json
{
    "id": 85,
    "title": "Personal Assistant",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "3-5 years experience",
    "description": "Detailed job description...",
    "url": "https://job-application-link"
}
```
