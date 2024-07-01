# VIM  Task

This project is designed to automate testing for ESH Login page focusing on login functionality using Selenium with pytest.

## Python Version

- **Python Version**: 3.12.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/raviv-steinberg/getvim_task.git
    cd getvim_task
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Ensure that `config.yaml` is properly configured with the necessary settings. Example configuration:

```yaml
settings:
  url: 'https://www.saucedemo.com/'
  ```

## Running Tests

UI Tests with pytest and Selenium
To run all UI tests:

 ```bash
 pytest
 ```

## Running Specific Tests

Using pytest tags
To run tests with a specific tag (e.g., login/inventory):

```bash
 pytest -m login
 ```



