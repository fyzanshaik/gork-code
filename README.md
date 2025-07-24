
# Gork CLI

Gork CLI is a custom-made AI coding agent that can perform various tasks like listing files, reading files, writing to files, and executing python scripts.

## Setup and Installation

This project uses `uv` for package management.

1.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

    You will need to create a `requirements.txt` file with the following content:
    ```
    python-dotenv
    google-generativeai
    ```

## How to Run

To run the Gork CLI, you need to provide a prompt as a command-line argument.

```bash
python main.py "Your prompt here"
```

**Example:**
```bash
python main.py "list all files in the current directory"
```

You also need to set up your Gemini API key in a `.env` file.

1. Create a `.env` file in the root of the project.
2. Add the following line to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key
   ```

## Function Calls

Gork CLI uses a set of predefined functions to interact with the local file system. Here is a list of available functions:

### `get_files_info(directory=".")`

Lists files and directories at the specified path, relative to the agent's working directory.

-   `directory` (optional): The directory to inspect. Defaults to the current directory.

### `get_file_content(file_path)`

Reads the content of a specified file.

-   `file_path`: The path to the file to be read, relative to the working directory.

### `write_file(file_path, content)`

Writes content to a specified file. This will overwrite the file if it already exists, or create a new file if it does not.

-   `file_path`: The path of the file to write to, relative to the working directory.
-   `content`: The content to be written to the file.

### `run_python_file(file_path, args=[])`

Executes a Python file.

-   `file_path`: The path of the Python file to be executed, relative to the working directory.
-   `args` (optional): A list of command-line arguments to pass to the Python script.

## Project Structure
```
.
├── main.py             # Main entry point of the application
├── utils.py            # Utility functions for path validation
├── config.py           # Configuration file for prompts and settings
├── functions/
│   ├── __init__.py
│   ├── call_function.py    # Handles routing of function calls
│   ├── get_file_content.py # Function to read file content
│   ├── get_files_info.py   # Function to list files
│   ├── run_python_file.py  # Function to execute Python files
│   ├── write_file.py       # Function to write to files
│   └── schema_function.py  # Defines the schema for all available functions
├── tests.py            # Tests for the application
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock
```
