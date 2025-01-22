# Mini Fleet Telemetry System

## Project Overview

I am currently building a Mini Fleet Telemetry System that simulates data collection and processing for a small fleet of vehicles. This project demonstrates key components and challenges in building a large-scale telemetry system.

## Current Implementation

The system consists of the following components:

1. **Vehicle Simulator**
   - Python script simulating multiple vehicles sending telemetry data (GPS, speed, battery level, etc.) using MQTT protocol.

2. **Data Ingestion Service**
   - MQTT broker (Mosquitto) set up to receive data from vehicle simulators.
   - Service that consumes MQTT messages and pushes them to Apache Kafka.

3. **Data Processing Service**
   - Stream processing service that consumes data from Kafka.
   - Implements real-time analytics (e.g., average speed calculation, geofencing alerts).

4. **Data Storage**
   - PostgreSQL for persistent storage of processed telemetry data.

5. **API Layer**
   - FastAPI service providing endpoints for querying processed data and analytics.

6. **Visualization**
   - Streamlit dashboard for visualizing real-time vehicle data and fleet analytics.

## Planned Enhancements

- Implement batch processing for historical data analysis
- Implement Redis for caching
- Add machine learning models for predictive maintenance
- Enhance real-time visualization capabilities
- Implement geofencing functionality
- Integrate with external APIs for data enrichment
- Demonstrate scalability and fault tolerance
- Add security features and compliance reporting

## Technologies Used

- Python
- MQTT
- Apache Kafka
- PostgreSQL
- FastAPI
- Streamlit

## Getting Started

(Instructions for setting up and running the project will be added as development progresses)

## Contributing

This project is currently under active development. Contributions, ideas, and feedback are welcome!

## License

[MIT License](LICENSE)
