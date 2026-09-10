# Backend Architecture & Security Guidelines

Welcome to the e-commerce backend team! To maintain PCI compliance and system stability, all Pull Requests must adhere to the following rules:

## 1. Database Connections
**Rule ID: arch_db_001**
Never instantiate a database `Session()` directly inside an API route. This causes connection pool leaks. You must always use the `get_db_session()` context manager.

## 2. Timezone Management
**Rule ID: arch_time_002**
Never use local time `datetime.now()`. Our servers run in multiple global regions. All timestamps must be generated using strict UTC time: `datetime.now(timezone.utc)`.

## 3. Secret Management
**Rule ID: sec_key_003**
Never hardcode API keys, Stripe tokens, or database passwords in the source code. Always fetch them dynamically using `os.getenv("SECRET_NAME")`.