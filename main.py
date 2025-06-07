from fastapi import FastAPI, Form, UploadFile
import uuid, os, subprocess, shutil

app = FastAPI()

@app.post("/run")
async def run_code(
    lang: str = Form(...),
    code: UploadFile = Form(...),
    stdin: UploadFile = Form(None)
):
    uid = str(uuid.uuid4())
    root = f"/tmp/voidrun/{uid}"
    os.makedirs(root, exist_ok=True)

    code_path = os.path.join(root, code.filename)
    stdin_path = os.path.join(root, "stdin.txt")

    with open(code_path, "wb") as f:
        shutil.copyfileobj(code.file, f)

    if stdin:
        with open(stdin_path, "wb") as f:
            shutil.copyfileobj(stdin.file, f)
    else:
        open(stdin_path, "w").close()

    # Determine runner command
    if lang == "python":
        cmd = f"firejail --quiet --net=none --private={root} timeout 5 python3 {code.filename}"
    elif lang == "c":
        cmd = f"gcc {code.filename} -o a.out && firejail --quiet --net=none --private={root} timeout 5 ./a.out"
    elif lang in ["js", "ts"]:
        runner = "ts-node" if code.filename.endswith(".ts") else "node"
        cmd = f"firejail --quiet --net=none --private={root} timeout 5 {runner} {code.filename}"
    else:
        return {"error": "Unsupported language"}

    result = subprocess.run(
        ["bash", "-c", cmd],
        cwd=root,
        stdin=open(stdin_path, "r"),
        capture_output=True,
        text=True,
        timeout=10
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "exit_code": result.returncode
    }
