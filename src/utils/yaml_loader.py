import yaml
import os
import inspect
from pathlib import Path


__all__ = ["load_config", "load_instructions"]

def _get_project_root() -> Path:
    """Returns the root directory of the project."""
    # This assumes the file is in src/utils/    
    return Path(__file__).parent.parent.parent

def load_config(config_name: str):
    """
    Loads a YAML configuration file from the configs/ directory.
    
    Args:
        config_name: Name of the file (e.g., 'agent_config.yaml' 
                    or the full path 'configs/agent_config.yaml')
    """
    root = _get_project_root()
    
    # If user passed just the filename, prepend 'configs/'
    if not config_name.startswith("configs/"):
        config_path = root / "configs" / config_name
    else:
        config_path = root / config_name

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {config_name}: {exc}")
            return None

def load_instructions(instructions_name: str) -> str:
    """
    Loads text content from a file. If the input is a filename, it loads from the 
    directory where this function is called (not where it's defined).

    Args:
        instructions_name: The filename or path to load.

    Returns:
        str: The content of the file.
    
    Raises:
        FileNotFoundError: If the file is not found.
    """
    # Get the caller's stack frame to find where the function was called from
    try:
        frame = inspect.stack()[1]
        caller_file = frame.filename
        caller_dir = os.path.dirname(os.path.abspath(caller_file))
    except (IndexError, AttributeError):
        # Fallback if stack inspection fails (e.g. from REPL or unusual execution context)
        caller_dir = os.getcwd()

    # Resolve the path relative to the caller's directory
    file_path = os.path.join(caller_dir, instructions_name)

    # Check if file exists at resolved path. If not, check if instructions_name
    # was meant to be absolute or relative to CWD.
    if not os.path.exists(file_path):
        if os.path.exists(instructions_name):
            file_path = instructions_name
        else:
            # If neither exists, let open() fail with the resolved path or raise explicit error
            # But raise explicit error to be helpful about where we looked
            raise FileNotFoundError(f"Instructions file not found: {instructions_name} (searched in {caller_dir})")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
