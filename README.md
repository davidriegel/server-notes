# server-notes

A minimal CLI tool to quickly save notes and thoughts directly from the terminal. Notes are stored locally in a `notes.json` file.

## Usage

```bash
python3 notes.py <command> [title] [note]
```

|Command                |Description            |
|-----------------------|-----------------------|
|`add <title> <note>`   |Create a new note      |
|`show`                 |List all notes         |
|`show <title>`         |Show a specific note   |
|`update <title> <note>`|Update an existing note|
|`remove <title>`       |Delete a note          |
|`help`                 |Show help menu         |

## Examples

```bash
python3 notes.py add "nginx" "Check config at /etc/nginx/nginx.conf"
python3 notes.py show
python3 notes.py show "nginx"
python3 notes.py update "nginx" "Updated config path to /etc/nginx/sites-enabled"
python3 notes.py remove "nginx"
```

## Shell Alias

To use `note` as a shorthand from anywhere, add this to your `~/.zshrc` (or `~/.bashrc`):

```bash
alias note="python3 /path/to/server-notes/notes.py"
```

Reload your shell:

```bash
source ~/.zshrc
```

Now you can use it like:

```bash
note add "deploy" "Remember to restart the service after deploy"
note show
```
