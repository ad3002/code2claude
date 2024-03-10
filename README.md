# code2claude: Code Consolidator

A Python tool that consolidates code from a repository into a unified format for AI-assisted analysis and manipulation.

Code Consolidator is a Python tool that traverses a code repository, extracts code from various files, and consolidates it into a unified format. The consolidated code is optimized for AI-assisted analysis and manipulation, enabling seamless collaboration between humans and AI in understanding and working with the codebase.

## Features

- Traverses a code repository and identifies relevant code files based on specified file extensions.
- Extracts code from each file and applies necessary preprocessing steps.
- Consolidates the extracted code into a single, unified format.
- Includes metadata such as file paths and module names for context.
- Provides options for code organization, dependency management, and documentation.
- Facilitates AI-assisted code analysis, manipulation, and collaboration.

## Installation


1. Clone the repository:

   ```
   git clone https://github.com/ad3002/code2claude
   ```

2. Navigate to the project directory:
   ```
   cd code2claude
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Update the `config.py` file with the necessary configurations, such as the repository path and file extensions to consider.

2. Run the code consolidator:
   ```
   python code2claude.py
   ```

3. The consolidated code will be generated and saved in the specified output format.

4. Provide the consolidated code to an AI system for analysis and manipulation.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
