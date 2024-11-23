# 🚀 InterSim API Documentation

Welcome to our fun and friendly Job Similarity API! Let's explore amazing job opportunities together! 🎯

## 🛠️ Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/InterSim-lab/JobSimilarity.git
cd JobSimilarity
```

### Install Dependencies
We recommend creating a **Virtual Environment** first! 🌟

```bash
# Windows
pip install -r requirements.txt
# Or Linux
pip3 install -r requirements.txt
```

### Run the API
```bash
uvicorn app.main:app --reload
```

## 🔍 Available Endpoints

### 1. Health Check 🏥
Check if our API is alive and kicking!

```
GET /
```

**Response:**
```json
{
    "message": "Hello World"
}
```

### 2. Random Jobs 🎲
Discover random job opportunities!

```
GET /api/jobs/random?limit=10
```

**Parameters:**
- `limit` (optional): Number of jobs to return (default: 10)

**Example:**
```
GET /api/jobs/random?limit=20
```

### 3. Jobs by Category 📑
Find jobs in your favorite category!

```
GET /api/jobs/category/{category}?limit=10
```

**Parameters:**
- `category`: The job category (e.g., "Operations", "Technology")
- `limit` (optional): Number of jobs to return (default: 10)

**Example:**
```
GET /api/jobs/category/Operations?limit=15
```

### 4. Job Details 📋
Get all the juicy details about a specific job!

```
GET /api/jobs/{id}
```

**Parameters:**
- `id`: The unique ID of the job

**Example:**
```
GET /api/jobs/85
```

### 5. Similar Jobs 🤝
Find jobs that are similar to one you like!

```
GET /api/jobs/{id}/similar?limit=10
```

**Parameters:**
- `id`: The job ID you want to find similar jobs for
- `limit` (optional): Number of similar jobs to return (default: 10)

**Example:**
```
GET /api/jobs/85/similar?limit=20
```

### 6. Search Jobs by Title 🔎
Search for your dream job!

```
GET /api/jobs?title=Flutter%20Developer%20Intern
```

**Parameters:**
- `title` (required): The job title you're looking for

## 📝 Response Format

Each job in the response will include these details:
```json
{
    "id": 85,
    "title": "Personal Assistant",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "3-5 years experience",
    "description": "...",
    "url": "https://..."
}
```

## ⚠️ Error Handling
If something goes wrong, you'll get an error message like this:
```json
{
    "detail": "Error message here"
}
```

Common error codes:
- 400: Bad Request (Missing or invalid parameters) 😕
- 404: Not Found (Job or resource doesn't exist) 🔍
- 500: Server Error (Something went wrong on our end) 😱