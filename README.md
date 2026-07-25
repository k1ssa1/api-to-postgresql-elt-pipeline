# Incremental Normalization of Semi-Structured API Product Data: An ELT Pipeline Case Study

## Overview

This case study demonstrates the design and implementation of an **ELT (Extract, Load, Transform)** pipeline that transforms semi-structured product data obtained from the DummyJSON API into a normalized PostgreSQL relational database.

Unlike a traditional ETL pipeline, the raw data is first loaded into PostgreSQL as `JSONB` documents. The transformation process is then performed inside the database using PostgreSQL's native JSONB functionality and SQL.

The project explores the application of database normalization principles (1NF, 2NF, and 3NF) to convert semi-structured JSON data into a structured relational model.

The complete case study article is published on dev.to :

https://dev.to/kitchen_code/incremental-relational-normalization-of-semi-structured-api-product-data-an-elt-pipeline-case-study-54l1

---

## Objectives

- Extract product data from the DummyJSON API.
- Load raw JSON documents into PostgreSQL using the `JSONB` data type.
- Transform the semi-structured data into a normalized relational schema.
- Analyze the resulting model against the First, Second, and Third Normal Forms.
- Demonstrate PostgreSQL's JSONB capabilities for ELT workflows.

---

## Technologies

- Python with the HTTP library `requests`
- PostgreSQL
- psycopg
- python-dotenv

---

## Project Structure

```text
.

├── extract/
├── main.py
├── database.py
├── requirements.txt
└── README.md
```

---

## ELT Workflow

1. Extract product data from the DummyJSON API.
2. Load the raw JSON into PostgreSQL as `JSONB` documents.
3. Transform the JSONB data into relational tables.
4. Apply and evaluate database normalization principles.
5. Produce the final relational model.

---

## Relational Tables

- `raw_products_data`
- `products_stage`
- `product_images`
- `product_reviews`
- `tags`
- `product_tags`

the `raw_products_data` should be dropped once the other tables are created to ensure normalization. 

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=your_port_number
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=product_catalog
```

### 6. Run the pipeline

```bash
python main.py
```

---

## Learning Outcomes

This project demonstrates:

- ELT pipeline design
- PostgreSQL JSONB processing
- SQL-based data transformation
- Relational database design
- Database normalization (1NF, 2NF, and 3NF)
- Primary and foreign key relationships
- One-to-many and many-to-many relationship modeling

---

## Data Source

DummyJSON Products API under MIT license

https://dummyjson.com

---

## License

This project is intended for educational and portfolio purposes.