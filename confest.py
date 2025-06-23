import sys
from pathlib import Path


project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))