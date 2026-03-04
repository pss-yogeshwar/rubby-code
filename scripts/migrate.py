# import os
# import requests
# import logging
# from pathlib import Path

# print("=== FOXPRO → CONSOLE C# (GROQ) ===")

# # ================================
# # LOGGING
# # ================================
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(levelname)s | %(message)s"
# )
# log = logging.getLogger("foxpro-groq")

# # ================================
# # CONFIG
# # ================================
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise RuntimeError("GROQ_API_KEY not set")

# MODEL = "llama-3.1-8b-instant"
# API_URL = "https://api.groq.com/openai/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {GROQ_API_KEY}",
#     "Content-Type": "application/json"
# }

# FOXPRO_DIR = Path(".")
# OUT_DIR = Path("dotnet_out")
# OUT_DIR.mkdir(exist_ok=True)

# EXTENSIONS = [".prg"]

# # ================================
# # CLEAN FOXPRO
# # ================================
# def clean_text(s):
#     return "".join(c for c in s if c == "\n" or (32 <= ord(c) <= 126))

# # ================================
# # GROQ CALL
# # ================================
# def groq_call(prompt):
#     payload = {
#         "model": MODEL,
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0,
#         "max_tokens": 2048
#     }

#     r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
#     r.raise_for_status()
#     return r.json()["choices"][0]["message"]["content"]

# # ================================
# # CONVERT FOXPRO → CONSOLE C#
# # ================================
# def convert_foxpro(code):
#     prompt = f"""
# You are converting Visual FoxPro code into C# CONSOLE APPLICATION code.

# TARGET PLATFORM:
# - .NET Console
# - Linux compatible
# - OnlineGDB compatible

# ABSOLUTE RULES (MANDATORY):
# - Output ONLY console-based C#
# - Use Console.ReadLine() and Console.WriteLine()
# - DO NOT use System.Windows.Forms
# - DO NOT use Microsoft.VisualBasic
# - DO NOT use MessageBox
# - DO NOT use InputBox
# - DO NOT invent GUI logic

# MAPPING RULES:
# - INPUT var      → Console.ReadLine()
# - ? output       → Console.WriteLine()
# - FoxPro numeric → double
# - DO CASE        → if / else if / else
# - IF / ELSE      → if / else

# GENERAL:
# - Preserve logic exactly
# - Line-by-line conversion
# - No refactoring
# - No markdown
# - No explanations
# - Output ONLY valid C# code

# FOXPRO CODE:
# {code}
# """
#     return groq_call(prompt)

# # ================================
# # MAIN
# # ================================
# files = []
# for ext in EXTENSIONS:
#     files.extend(FOXPRO_DIR.rglob(f"*{ext}"))

# log.info("FoxPro files found: %d", len(files))

# for f in files:
#     log.info("Converting %s", f.name)

#     fox = clean_text(f.read_text(errors="ignore"))
#     cs = convert_foxpro(fox)

#     out_file = OUT_DIR / (f.stem + ".cs")
#     out_file.write_text(cs, encoding="utf-8")

#     log.info("Saved → %s", out_file)

# print("=== CONVERSION COMPLETE ===")




#working code this foxpro to csharp and 
#this is the rubby to csharp converter, it is not complete but it is a start
























# import os
# import requests
# import logging
# from pathlib import Path

# print("=== RUBY → CONSOLE C# (GROQ) ===")

# # ================================
# # LOGGING
# # ================================
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(levelname)s | %(message)s"
# )
# log = logging.getLogger("ruby-groq")

# # ================================
# # CONFIG
# # ================================
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise RuntimeError("GROQ_API_KEY not set")

# MODEL = "llama-3.1-8b-instant"
# API_URL = "https://api.groq.com/openai/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {GROQ_API_KEY}",
#     "Content-Type": "application/json"
# }

# SOURCE_DIR = Path(".")
# OUT_DIR = Path("dotnet_out")
# OUT_DIR.mkdir(exist_ok=True)

# EXTENSIONS = [".rb"]

# # ================================
# # CLEAN TEXT
# # ================================
# def clean_text(s):
#     return "".join(c for c in s if c == "\n" or (32 <= ord(c) <= 126))

# # ================================
# # REMOVE MARKDOWN ```
# # ================================
# def clean_csharp_output(text):
#     text = text.replace("```csharp", "")
#     text = text.replace("```cs", "")
#     text = text.replace("```", "")
#     return text.strip()

# # ================================
# # GROQ CALL
# # ================================
# def groq_call(prompt):
#     payload = {
#         "model": MODEL,
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0,
#         "max_tokens": 2048
#     }

#     r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
#     r.raise_for_status()
#     return r.json()["choices"][0]["message"]["content"]

# # ================================
# # ✅ RUBY → SAFE CONSOLE C#
# # ================================
# def convert_ruby(code):
#     prompt = f"""
# You are converting Ruby code into STRICTLY VALID C# CONSOLE APPLICATION code.

# VERY IMPORTANT RULES (MUST FOLLOW):
# - ALWAYS use double for numeric variables.
# - NEVER use float.
# - Use Convert.ToDouble(Console.ReadLine()) for numeric input.
# - Output MUST compile without errors.
# - Do NOT include ``` markdown.
# - Do NOT include explanations.
# - Output ONLY C# code.

# TARGET:
# - .NET Console
# - Linux compatible
# - OnlineGDB compatible

# MAPPING RULES:
# - puts → Console.WriteLine()
# - print → Console.Write()
# - gets → Console.ReadLine()
# - to_i → Convert.ToInt32()
# - to_f → Convert.ToDouble()
# - case → switch
# - elsif → else if

# GENERAL:
# - Preserve logic
# - Strong typing required
# - Add using System;
# - Wrap code inside class Program with static void Main()

# RUBY CODE:
# {code}
# """
#     return groq_call(prompt)

# # ================================
# # MAIN
# # ================================
# files = []
# for ext in EXTENSIONS:
#     files.extend(SOURCE_DIR.rglob(f"*{ext}"))

# log.info("Ruby files found: %d", len(files))

# for f in files:
#     log.info("Converting %s", f.name)

#     ruby_code = clean_text(f.read_text(errors="ignore"))

#     # 🔥 SAFE conversion
#     cs = clean_csharp_output(convert_ruby(ruby_code))

#     out_file = OUT_DIR / (f.stem + ".cs")
#     out_file.write_text(cs, encoding="utf-8")

#     log.info("Saved → %s", out_file)

# print("=== CONVERSION COMPLETE ===")



















import os
import requests
import logging
import subprocess
import json
from pathlib import Path

print("=== GITNEXUS INIT + RUBY → C# (GROQ) ===")

# ================================
# LOGGING
# ================================
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("gitnexus-groq")

# ================================
# ENV CONFIG
# ================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SOURCE_REPO_URL = os.getenv("SOURCE_REPO_URL")
SOURCE_REPO_PAT = os.getenv("SOURCE_REPO_PAT")
MIGRATION_ID = os.getenv("MIGRATION_ID")
BACKEND_URL = os.getenv("BACKEND_URL")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set")

if not SOURCE_REPO_URL or not SOURCE_REPO_PAT:
    raise RuntimeError("Repository details missing")

MODEL = "llama-3.1-8b-instant"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# ================================
# 🔥 GITNEXUS INIT
# ================================
WORKSPACE = Path("workspace")
OUT_DIR = Path("dotnet_out")

WORKSPACE.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)

log.info("Cloning source repository...")

repo_url = SOURCE_REPO_URL.replace(
    "https://",
    f"https://{SOURCE_REPO_PAT}@"
)

subprocess.run(
    ["git", "clone", repo_url, str(WORKSPACE)],
    check=True
)

log.info("Repository cloned")

# -------------------------
# Language detection
# -------------------------
extensions = {}
for f in WORKSPACE.rglob("*.*"):
    ext = f.suffix.lower()
    extensions[ext] = extensions.get(ext, 0) + 1

if not extensions:
    raise RuntimeError("No files found in repo")

detected_language = max(extensions, key=extensions.get)

metadata = {
    "migration_id": MIGRATION_ID,
    "detected_language": detected_language,
    "file_count": sum(extensions.values()),
    "extensions": extensions
}

(Path("gitnexus.json")).write_text(
    json.dumps(metadata, indent=2)
)

log.info("GitNexus metadata generated")

# Optional status update
if BACKEND_URL:
    try:
        requests.post(
            f"{BACKEND_URL}/api/pipeline/update",
            json={
                "migration_id": MIGRATION_ID,
                "stage": "gitnexus_init",
                "status": "completed"
            },
            timeout=5
        )
    except Exception:
        pass

# ================================
# CLEAN FUNCTIONS
# ================================
def clean_text(s):
    return "".join(c for c in s if c == "\n" or (32 <= ord(c) <= 126))

def clean_csharp_output(text):
    return text.replace("```csharp", "").replace("```cs", "").replace("```", "").strip()

# ================================
# GROQ CALL
# ================================
def groq_call(prompt):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 2048
    }

    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

# ================================
# CONVERSION
# ================================
def convert_ruby(code):
    prompt = f"""
You are converting Ruby code into STRICTLY VALID C# CONSOLE APPLICATION code.

RULES:
- ALWAYS use double
- NEVER use float
- Use Convert.ToDouble(Console.ReadLine())
- Add using System;
- Wrap in class Program with static void Main()
- NO markdown
- NO explanation
- ONLY C# CODE

RUBY CODE:
{code}
"""
    return groq_call(prompt)

# ================================
# FILE PROCESSING
# ================================
ruby_files = list(WORKSPACE.rglob("*.rb"))

log.info("Ruby files found: %d", len(ruby_files))

for f in ruby_files:
    log.info("Converting %s", f.name)

    ruby_code = clean_text(f.read_text(errors="ignore"))
    cs = clean_csharp_output(convert_ruby(ruby_code))

    out_file = OUT_DIR / (f.stem + ".cs")
    out_file.write_text(cs, encoding="utf-8")

    log.info("Saved → %s", out_file)

print("=== GITNEXUS MIGRATION COMPLETE ===")