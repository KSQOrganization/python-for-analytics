# Contributing to Online Retail Analytics

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## Development Environment Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-for-analytics.git
   cd python-for-analytics
   ```

2. **Set up your development environment**:
   ```bash
   make setup
   ```

   This command will:
   - Install all dependencies
   - Install the package in editable mode
   - Set up pre-commit hooks

## Code Quality Standards

This project maintains high code quality standards using multiple tools:

### Code Formatting

- **Black**: Code formatter (line length: 100 characters)
- **isort**: Import statement organizer

Format your code before committing:
```bash
make format
```

### Linting

- **Flake8**: Style guide enforcement
- **Pylint**: Code analysis

Run linters:
```bash
make lint
```

### Type Checking

- **MyPy**: Static type checker

Run type checking:
```bash
make type-check
```

### All Quality Checks

Run all quality checks at once:
```bash
make quality-check
```

## Testing

### Writing Tests

- Place unit tests in `tests/unit/`
- Place integration tests in `tests/integration/`
- Follow the naming convention: `test_*.py`
- Use descriptive test names: `test_<what>_<condition>_<expected_result>`

### Running Tests

Run all tests with coverage:
```bash
make test
```

Run tests without coverage:
```bash
make test-quick
```

Run specific tests:
```bash
pytest tests/unit/test_sample.py -v
```

## Pre-commit Hooks

Pre-commit hooks are automatically installed when you run `make setup`. They will run on every commit to ensure code quality.

To manually run pre-commit hooks on all files:
```bash
make pre-commit-run
```

## Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clear, concise commit messages
   - Add tests for new functionality
   - Update documentation as needed

3. **Run quality checks**:
   ```bash
   make quality-check
   make test
   ```

4. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**:
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure CI checks pass

## Code Style Guidelines

### Python Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Maximum line length: 100 characters
- Use type hints where appropriate

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Update README.md for significant changes

### Example Docstring

```python
def process_transactions(data: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Process transaction data by applying filters and transformations.

    Args:
        data: Raw transaction data
        threshold: Minimum transaction amount to include

    Returns:
        Processed transaction data

    Raises:
        ValueError: If threshold is negative
    """
    pass
```

## Creating New Pipelines

1. **Generate pipeline structure**:
   ```bash
   kedro pipeline create <pipeline_name>
   ```

2. **Implement nodes** in `src/online_retail_analytics/pipelines/<pipeline_name>/nodes.py`

3. **Define pipeline** in `src/online_retail_analytics/pipelines/<pipeline_name>/pipeline.py`

4. **Add data catalog entries** in `conf/base/catalog.yml`

5. **Write tests** in `tests/pipelines/<pipeline_name>/`

## Reporting Issues

When reporting issues, please include:

- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (Python version, OS, etc.)

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Reach out to the maintainers

Thank you for contributing! 🎉
