# 🌍 Global Earthquakes Visualization

This project provides a visual representation of earthquakes around the world over the past week using Streamlit.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Project](#running-the-project)
- [Dockerizing the Application](#dockerizing-the-application)

## 🛠 Prerequisites

1. **Python 3.9+**
   
   Ensure you have Python 3.9 or newer installed:
   ```bash
   python --version
   ```

2. **Poetry**
   
   This project uses [Poetry](https://python-poetry.org/) for dependency management. Install it by following the [official installation guide](https://python-poetry.org/docs/#installation).

3. **Docker** (Optional)
   
   If you intend to run this project using Docker, ensure Docker is installed on your machine. Follow the installation instructions provided for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [macOS](https://docs.docker.com/docker-for-mac/install/), or [Windows](https://docs.docker.com/docker-for-windows/install/).

## 🚀 Installation & Setup

1. **Clone the Repository**:
   
   ```bash
   gh repo clone octavedbc/Toolkit
   ```

2. **Activate the Virtual Environment**:
   
   Poetry will create and manage a virtual environment for you. Activate it with:
   ```bash
   poetry shell
   ```

3. **Install Dependencies**:
   
   Within the virtual environment, install the project's dependencies:
   ```bash
   poetry install
   ```

## 🎯 Running the Project

With everything set up, run the Streamlit app using:

```bash
streamlit run earthquake_viz.py
```

This will start the app, and it should be accessible in your web browser at `http://localhost:8501`.

## 🐳 Dockerizing the Application

If you prefer to run the project within a Docker container:

1. **Build the Docker Image**:

   ```bash
   sudo docker build -t earthquake_viz .
   ```

2. **Run the Docker Container**:

   ```bash
   sudo docker run -p 8501:8501 earthquake_viz
   ```

After executing these commands, you can access the Streamlit app by navigating to `http://localhost:8501` in your browser.


3. **Stop the Docker container**:

   First, list all running Docker containers:

   ```bash
   sudo docker ps
   ```

   Look for the container ID or name associated with the image `earthquake_viz` or whichever image is running on port `8501`.

   Once you have identified the container ID or name, stop it using:

   ```bash
   sudo docker stop [CONTAINER_ID_OR_NAME]
   ```

   Replace `[CONTAINER_ID_OR_NAME]` with the actual container ID or name from the `docker ps` command.