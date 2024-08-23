# Hacker's Digital Diary

## Overview

Hacker's Digital Diary is a simple Python application built with Tkinter, designed to allow users to maintain a digital diary. The application supports creating, saving, viewing, and editing diary entries.

## Features

- **Add New Entries**: Write and save new diary entries with timestamps.
- **View and Edit Entries**: View existing entries and edit them if needed.
- **Persistent Storage**: Diary entries are stored in a text file, ensuring that data persists between sessions.

## Requirements

- Python 3.x
- Tkinter (comes bundled with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/digital-diary.git
    ```

2. Navigate to the project directory:

    ```bash
    cd digital-diary
    ```

3. Run the application:

    ```bash
    python digital_diary.py
    ```

## Usage

- **Add Entry**: Type your entry into the text box and click "SAVE ENTRY" to save it.
- **View/Edit Entries**: Click "VIEW/EDIT ENTRIES" to open a window displaying all saved entries. You can select an entry to edit it.

## Code Overview

- **DigitalDiaryApp**: Main class handling the application logic and GUI.
  - `__init__(self, root)`: Initializes the application and sets up the GUI.
  - `create_widgets(self)`: Creates and arranges the widgets on the main window.
  - `load_entries(self)`: Loads diary entries from the file.
  - `save_entry(self)`: Saves a new entry to the file.
  - `view_entries(self)`: Displays a window with all entries.
  - `show_entries_window(self)`: Creates a window for viewing and editing entries.
  - `edit_entry(self, listbox)`: Edits a selected entry.
  - `save_all_entries(self)`: Saves all entries back to the file.

## Contributing

Feel free to open issues or submit pull requests to improve the application. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

---

Happy journaling!
