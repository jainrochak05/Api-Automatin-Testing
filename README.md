

# API Automation Testing Framework  
### Customized for Medicine Data REST API

---

## Overview

This repository contains a modular and scalable **API Automation Testing Framework** built using **Python and PyTest**.

The framework is specifically configured to test the **Medicine Data REST API**, a backend service developed by the author. It validates functional correctness, error handling, response schema integrity, and performance thresholds.

Although currently tuned for the Medicine Data API, the framework is designed with abstraction principles, making it easily adaptable to test any REST API with minimal structural changes.

---

## Target API Details

### Endpoint Under Test

```
POST /get_medicine_info
```

### Request Format

**Headers**
```
Content-Type: application/json
```

**Body**
```json
{
  "medicine_name": "<medicine_name>"
}
```

### Expected Responses

| Status Code | Description |
|-------------|-------------|
| 200 | Valid medicine found |
| 400 | Missing or invalid input |
| 404 | Medicine not found |
| 500 | Internal server error |

---

## Framework Architecture

```
api-automation-testing-framework/
│
├── utils/
│   ├── __init__.py
│   └── base_test.py          # Core request abstraction layer
│
├── tests/
│   ├── __init__.py
│   └── test_medicine_api.py  # Functional and negative test cases
│
├── requirements.txt
└── README.md
```

---

## Design Principles

- Modular test structure  
- Separation of request abstraction and validation logic  
- Reusable and scalable for regression testing  
- Strict payload validation for POST endpoints  
- Performance-aware validation using response time assertions  

---

## Features Implemented

### Functional Testing
Validates successful API response for valid medicine queries.

### Negative Testing
Tests system behavior for:
- Missing fields
- Empty input
- Invalid medicine names

### Schema Validation
Ensures response contains expected JSON keys:
- `medicine_name`
- `composition`
- `uses`
- `side_effects`

### Boundary Testing
Validates handling of edge input conditions.

### Performance Validation
Measures response time and enforces acceptable latency thresholds.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository_url>
cd api-automation-testing-framework
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Base URL

Update the following in `utils/base_test.py`:

```python
BASE_URL = "http://127.0.0.1:5000"
```

Modify the base URL if the API is deployed remotely.

---

## Running the Tests

Ensure the Medicine Data API server is running:

```
python app.py
```

Then execute:

```
PYTHONPATH=. pytest -v
```

Example output:

```
4 passed in 0.85s
```

---

## Extending the Framework

To adapt this framework for another API:

1. Update the `BASE_URL`
2. Modify endpoint paths
3. Adjust payload structures
4. Update schema assertions in test files
5. Add new test modules under the `tests/` directory

The abstraction layer ensures minimal duplication and easier scalability.

---

## Future Enhancements

- CI/CD integration using GitHub Actions  
- Automated test reporting  
- Environment-based configuration management  
- Data-driven testing using parametrization  
- Logging and structured execution reports  

---

## About This Project

The Medicine Data REST API tested in this framework was independently developed by the author.  
This automation suite was built to validate its correctness, robustness, and performance under various operational scenarios.

---

## License

This project is intended for educational and demonstration purposes.
