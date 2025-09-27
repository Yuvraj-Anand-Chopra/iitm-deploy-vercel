# Eshopco Latency API

This project is a FastAPI application that serves latency data from a JSON file. It provides insights into service performance across different regions and services.

## Project Structure

```
eshopco-latency-api
├── src
│   ├── main.py          # Entry point of the application
│   ├── telemetry
│   │   └── q-vercel-latency.json  # JSON file containing latency data
│   └── types
│       └── index.py     # Pydantic models for data validation
├── requirements.txt      # Project dependencies
├── vercel.json           # Vercel deployment configuration
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd eshopco-latency-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the application is running, you can access the latency data by navigating to the following endpoint in your browser or using a tool like Postman:

```
http://localhost:8000/latency
```

This will return the latency data in JSON format.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.