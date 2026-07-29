
# API Automation Testing Framework

### *Robust Validation for Medicine Data REST Services*

## 📌 Overview

This repository hosts a modular and scalable **API Automation Testing Framework** built using **Python and Pytest**.

The suite is engineered to provide high-confidence validation for the **Medicine Data REST API**, a backend service developed to manage information for over 17K medicines. By utilizing abstraction principles, the framework separates request management from test logic, ensuring it remains reusable across various microservices.

## 🏗️ Architecture & Design

The framework adheres to a decoupled structure to promote maintainability and clean code:

```text
api-automation-testing/
│
├── utils/
│   ├── base_test.py          # Core request abstraction and performance metrics
│
├── tests/
│   ├── test_medicine_api.py  # Functional, Negative, and Boundary test cases
│
├── requirements.txt          # Dependency specifications
└── README.md

```

## 🧪 Testing Strategy

The suite implements a multi-layered testing approach to ensure API robustness:

### **1. Functional Validation**

* Verifies successful `POST` requests to the `/get_medicine_info` endpoint.
* Confirms response payload integrity with mandatory schema keys: `medicine_name`, `composition`, `uses`, and `side_effects`.

### **2. Negative & Boundary Testing**

* **Missing Fields**: Ensures the API returns a `400 Bad Request` when required fields are omitted.
* **Invalid Queries**: Validates `404 Not Found` responses for non-existent medicine entries.
* **Empty Strings**: Handles boundary cases where payloads contain empty values, enforcing strict input validation.

### **3. Performance Benchmarking**

* The framework tracks request latency using a high-precision timer in the utility layer.
* Automated assertions enforce a strict performance threshold of **< 2.0 seconds** for standard responses.

## 🛠️ Getting Started

### **Prerequisites**

* Python 3.x
* Pip

### **Installation**

1. **Clone the Repository:**
```bash
git clone https://github.com/jainrochak05/api-automation-testing.git
cd api-automation-testing

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```



### **Configuration**

The base URL is centralized in `utils/base_test.py`. Ensure it points to your target environment:

```python
BASE_URL = "https://medicine-data-lstd.onrender.com"

```

## 🚀 Execution

Execute all tests with verbose reporting:

```bash
PYTHONPATH=. pytest -v

```

## 🔮 Future Roadmap

* [ ] **CI/CD Integration**: Implementing GitHub Actions to trigger automated test runs on every pull request.
* [ ] **Data-Driven Testing**: Utilizing `@pytest.mark.parametrize` to scale test coverage across thousands of medicine data points.
* [ ] **Enhanced Reporting**: Integration with Allure or HTML reports for stakeholder-friendly execution summaries.

---

**Rochak Kr. Jain** 

