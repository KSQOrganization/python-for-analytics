.PHONY: help install install-dev test lint format type-check clean build run docs

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install project dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .

test: ## Run tests with pytest
	pytest tests/ -v --cov=src/online_retail_analytics --cov-report=html --cov-report=term

test-quick: ## Run tests without coverage
	pytest tests/ -v

lint: ## Run all linters (flake8, pylint)
	flake8 src/ tests/
	pylint src/online_retail_analytics

format: ## Format code with black and isort
	black src/ tests/
	isort src/ tests/

format-check: ## Check code formatting without making changes
	black --check src/ tests/
	isort --check-only src/ tests/

type-check: ## Run static type checking with mypy
	mypy src/online_retail_analytics

quality-check: format-check lint type-check ## Run all quality checks

clean: ## Clean up generated files and caches
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf build/ dist/ htmlcov/ .coverage .tox/

build: ## Build the project package
	python -m build

run: ## Run the Kedro pipeline
	kedro run

jupyter: ## Launch Jupyter Lab
	kedro jupyter lab

ipython: ## Launch IPython with Kedro context
	kedro ipython

kedro-viz: ## Launch Kedro Viz for pipeline visualization
	kedro viz

catalog-list: ## List all datasets in the catalog
	kedro catalog list

catalog-create: ## Create a new data catalog entry
	kedro catalog create

pipeline-create: ## Create a new pipeline
	@read -p "Enter pipeline name: " name; \
	kedro pipeline create $$name

docs: ## Generate project documentation
	@echo "Documentation generation not yet configured"

pre-commit-install: ## Install pre-commit hooks
	pre-commit install

pre-commit-run: ## Run pre-commit hooks on all files
	pre-commit run --all-files

setup: install-dev pre-commit-install ## Complete development environment setup
	@echo "Development environment setup complete!"
