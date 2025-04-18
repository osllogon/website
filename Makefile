# Declare all phony targets
.PHONY: install clean lint code_check pipeline all

# Default command
.DEFAULT_GOAL := all

# Variables
SRC_PROJECT_NAME ?= website

# Allows the installation of project dependencies
install:
	@echo "Installing requirements..."
	uv sync
	@echo ""

# Allows cache clearing
clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	@echo ""

# Check format and quality of the code
lint:
	@echo "Checking code format with Black..."
	black --check $(SRC_PROJECT_NAME)/
	@echo "Checking code style with Flake8..."
	flake8 $(SRC_PROJECT_NAME)/
	@echo "Checking code quality with Pylint..."
	pylint --fail-under=8 $(SRC_PROJECT_NAME)/
	@echo ""

# Check
code_check:
	@echo "Checking code complexity with complexipy..."
	complexipy -d low $(SRC_PROJECT_NAME)/
	@echo "Checking type annotations with Mypy..."
	mypy $(SRC_PROJECT_NAME)/
	@echo ""

# Run all tasks of the pipeline without install and doc
pipeline: clean lint code_check
	@echo ""

# Run all tasks in sequence
all: install clean lint code_check
	@echo ""
