# code-flaten

This tool helps you to flatten your codebase. It extracts files form nested folders.

## Features

Recursively scans a source directory and all its subdirectories.
Organizes files into folders of a defined capacity within a target directory.
Flattens directory paths by substituting path separators with double dashes (--).
Supports an include list for directories and files to flatten, configured through a JSON file.
Automatically excludes files and directories listed in the .gitignore file.
Estimates token counts using NLTK and TikToken tokenizers.
Offers user notifications and robust error management.

## Usage

Create a config.json file in the source directory with the following format:

```
{
  "include": [
    "folder1",
    "folder2"
  ]
}
```

Put in the folders and files that you want to flatten.

An example of run command would be:
```
python main.py source --target_dir target
```

With this you will flatten the source directory and put the flattened files in the target directory.