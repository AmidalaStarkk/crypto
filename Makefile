.PHONY: help install_requirements streamlit clean test lint format

# Default target
help:
	@echo "Available commands:"
	@echo "  make install_requirements  - Install Python dependencies"
	@echo "  make streamlit            - Run Streamlit web server"
	@echo "  make clean               - Clean up temporary files"
	@echo "  make test                - Run tests"
	@echo "  make lint                - Run linting checks"
	@echo "  make format              - Format code"

# Install dependencies
install_requirements:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt

# Run Streamlit application
streamlit:
	@echo "Starting Streamlit server..."
	streamlit run app.py

# Alternative streamlit command if main file has different name
streamlit-main:
	@echo "Starting Streamlit server..."
	streamlit run main.py

# Clean temporary files
clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name ".DS_Store" -delete

# Run tests
test:
	@echo "Running tests..."
	python -m pytest tests/ -v

# Run linting
lint:
	@echo "Running linting checks..."
	flake8 .
	pylint *.py

# Format code
format:
	@echo "Formatting code..."
	black .
	isort .

# Install development dependencies
install_dev:
	@echo "Installing development dependencies..."
	pip install pytest flake8 pylint black isort

# Run the application in development mode
dev: install_requirements
	@echo "Running in development mode..."
	streamlit run app.py --server.runOnSave true

# Create requirements.txt if it doesn't exist
freeze:
	@echo "Creating requirements.txt..."
	pip freeze > requirements.txt

