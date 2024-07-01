# U.S. Electricity Prices
This repository contains regression model generated from monthly data on electricity prices, sales, and revenue in the United States, disaggregated by state and sector (residential, commercial, industrial, and other) from 2001 onwards. The dataset includes variables such as the average price per kilowatt-hour (kWh), total revenue, total sales, and the number of customers (where available).

## Project Directory Structure
```
project/
│
├── .github/
│   └── workflows/
│       └── test_data.yml
│
├── data/
│   ├── cleaned_data/
│   ├── eda_images/
│   └── model/
│
├── src/
│   ├── exploratory_data_analysis.py
│   └── model_training.py
│
├── integration/
│   └── post_docker_run.ipypynb
│
├── tests/
│   ├── __init__.py
│   ├── test_example.py
│
├── ci-cd/
│   ├── ci-cd.py
│   └── app-deployment.py
|
├── .gitignore
├── requirements.txt
├── README.md
└── procfile
└── Dockerfile
```

## How to serve model on local
```
- Build Docker File
    docker build -t electricity_prices .
- Run Docker File
    docker run -p 4000:80 electricity_prices
- Check Server is UP
    http://127.0.0.1:4000/
```

## How to train model on local
```
- Create Virtual Environment
    conda create --name electricity_price python=3.8
- Activate Created Virtual Environment
    conda activate electricity_price
- Install dependencies
    pip install -r requirements.txt
- Run eda
    python src/exploratory_data_analysis.py
- Build Model
    python src/model_training.py
- serve model
    python src/app.py
- Check model status
    python integration/post_model_run.py
```

## Test Model Endpoint
```
- Endpoint 
    python integration/post_model_run.py
```

## High Level Flow

```
  +-----------------------+
  | Data Gathering       |
  | , Preprocessing      |
  | , code versioning    |
  +-----------+-----------+
              |
  +-----------v-----------+
  | Model Development     |
  |                       |
  |  +------+  +------+   |
  |  | EDA  |  | Train|   |
  |  +------+  +------+   |
  |     |         |       |
  |     v         v       |
  |  +------+  +------+   |
  |  | Eval |  |Valid.|   |
  |  +------+  +------+   |
  +-----------+-----------+
              |
  +-----------v-----------+
  | CI/CD Integration     |
  |                       |
  | +------+  +------+    |
  | | CI   |  | CD   |    |
  | +------+  +------+    |
  |     |         |       |
  |     v         v       |
  |  +------+  +------+   |
  |  | Test |  |Deploy|   |
  |  +------+  +------+   |
  +-----------+-----------+
              |
  +-----------v-----------+  
  | Monitoring and        | 
  | Feedback Loop         |
  +-----------------------+

```