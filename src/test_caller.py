import sys
import os
# Add parent dir to path so we can import src.utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.yaml_loader import load_instructions

try:
    content = load_instructions("dummy.txt")
    print(f"SUCCESS: {content}")
except Exception as e:
    print(f"FAILURE: {e}")
