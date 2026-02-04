# Online Retail Analytics

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
[![CI](https://github.com/KSQOrganization/python-for-analytics/workflows/CI/badge.svg)](https://github.com/KSQOrganization/python-for-analytics/actions)

## Overview

A production-ready Kedro project for analyzing Online Retail / Ecommerce Transactions. This project provides a complete development toolkit including automated testing, linting, formatting, and CI/CD workflows.

## Features

- 🚀 **Kedro Pipeline**: Modular data processing pipeline for retail analytics
- 🧪 **Testing Framework**: Pytest with coverage reporting
- 🔍 **Code Quality**: Flake8, Pylint, Black, isort, and MyPy configured
- 🔧 **Makefile**: Common development tasks automated
- 🎣 **Pre-commit Hooks**: Automatic code quality checks before commits
- 📊 **Data Pipelines**: Sample pipelines for transaction processing and customer analytics
- 🔄 **CI/CD**: GitHub Actions workflow for automated testing and deployment

## Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KSQOrganization/python-for-analytics.git
   cd python-for-analytics
   ```

2. **Set up the development environment**:
   ```bash
   make setup
   ```
   This will install all dependencies and set up pre-commit hooks.

3. **Alternative: Manual installation**:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   pre-commit install
   ```

## Development Toolkit

### Makefile Commands

The project includes a comprehensive Makefile with the following targets:

```bash
make help                # Show all available commands
make install             # Install project dependencies
make install-dev         # Install development dependencies
make test                # Run tests with coverage
make test-quick          # Run tests without coverage
make lint                # Run linters (flake8, pylint)
make format              # Format code (black, isort)
make format-check        # Check formatting without changes
make type-check          # Run mypy type checking
make quality-check       # Run all quality checks
make clean               # Clean generated files
make build               # Build the package
make run                 # Run Kedro pipeline
make jupyter             # Launch Jupyter Lab
make kedro-viz           # Visualize pipelines
make pre-commit-run      # Run pre-commit on all files
```

### Code Quality Tools

The project is configured with:

- **Black**: Code formatter (line length: 100)
- **isort**: Import statement organizer
- **Flake8**: Style guide enforcement
- **Pylint**: Code analysis
- **MyPy**: Static type checker
- **Pytest**: Testing framework with coverage

Run all quality checks with:
```bash
make quality-check
```

## Project Structure

```
.
├── conf/                   # Configuration files
│   ├── base/              # Base configuration
│   │   ├── catalog.yml    # Data catalog definitions
│   │   └── parameters*.yml # Pipeline parameters
│   └── local/             # Local configuration (gitignored)
├── data/                  # Data directory (gitignored)
│   ├── 01_raw/           # Raw data
│   ├── 02_intermediate/  # Intermediate processed data
│   ├── 03_primary/       # Primary data
│   ├── 04_feature/       # Feature datasets
│   ├── 05_model_input/   # Model input data
│   ├── 06_models/        # Trained models
│   ├── 07_model_output/  # Model outputs
│   └── 08_reporting/     # Reporting outputs
├── src/                   # Source code
│   └── online_retail_analytics/
│       ├── pipelines/    # Kedro pipelines
│       │   └── data_processing/  # Example pipeline
│       ├── __init__.py
│       ├── __main__.py
│       └── settings.py
├── tests/                 # Test files
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── .github/
│   └── workflows/        # CI/CD workflows
├── Makefile              # Development commands
├── pyproject.toml        # Project configuration
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## Pipelines

### Data Processing Pipeline

The `data_processing` pipeline includes:

1. **Clean Transactions**: Remove duplicates, handle missing values, filter invalid data
2. **Add Features**: Calculate derived features (total amount, date components)
3. **Aggregate Metrics**: Generate customer-level metrics

Run the pipeline:
```bash
kedro run
```

Visualize the pipeline:
```bash
kedro viz
```

## Testing

Run the full test suite:
```bash
make test
```

Run tests without coverage:
```bash
make test-quick
```

Run specific test files:
```bash
pytest tests/unit/test_sample.py -v
```

## Data Management

Place your raw data files in `data/01_raw/`. The default pipeline expects:
- `data/01_raw/online_retail.csv` - Raw transaction data

The pipeline will process data through the following layers:
1. Raw data (01_raw)
2. Intermediate data (02_intermediate)
3. Primary data (03_primary)
4. Feature data (04_feature)

## CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- Runs on Python 3.10, 3.11, and 3.12
- Executes linters and type checkers
- Runs the test suite
- Builds the package

## Creating New Pipelines

Create a new pipeline:
```bash
make pipeline-create
# Or directly:
kedro pipeline create <pipeline_name>
```

## Working with Notebooks

Launch Jupyter Lab with Kedro context:
```bash
make jupyter
# Or:
kedro jupyter lab
```

Launch IPython with Kedro context:
```bash
kedro ipython
```

## Contributing

1. Install development dependencies: `make install-dev`
2. Install pre-commit hooks: `make pre-commit-install`
3. Create a feature branch
4. Make your changes
5. Run quality checks: `make quality-check`
6. Run tests: `make test`
7. Submit a pull request

## License

See [LICENSE](LICENSE) file for details.

## Resources

- [Kedro Documentation](https://docs.kedro.org)
- [Kedro Tutorial](https://docs.kedro.org/en/stable/tutorial/tutorial_template.html)
- [Data Engineering Best Practices](https://docs.kedro.org/en/stable/faq/faq.html)
