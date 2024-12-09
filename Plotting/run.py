import subprocess


base_path = 'Plotting'
scripts = []

parts = [
    "Graph_All",
    "Graph_Together",
    "Graph",
    "Years"
]
options = [
    "Wordcount",
    "Sentimental",
]
for o in options:
    for p in parts:
        scripts.append(f"{base_path}/{o}/{p}.py")

for script in scripts:
    print(script)
    subprocess.run(['.venv/Scripts/python.exe', script])
