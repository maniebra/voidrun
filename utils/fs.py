import os
import shutil
import uuid

def create_sandbox_dir(base: str = "/tmp/voidrun") -> str:
    """
    Creates a unique temp directory inside base path.
    Returns the absolute path to the sandbox dir.
    """
    sandbox_id = str(uuid.uuid4())
    path = os.path.join(base, sandbox_id)
    os.makedirs(path, exist_ok=True)
    return path

def save_file(dest_path: str, file_obj) -> None:
    """
    Saves a FastAPI UploadFile to the given path.
    """
    with open(dest_path, "wb") as f:
        f.write(file_obj.file.read())

def ensure_empty_stdin(path: str) -> None:
    """
    Creates an empty stdin.txt file if no stdin provided.
    """
    with open(path, "w") as f:
        pass

def cleanup_dir(path: str) -> None:
    """
    Deletes the entire directory tree at the given path.
    """
    if os.path.exists(path):
        shutil.rmtree(path)
