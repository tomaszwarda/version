import sys

data = sys.argv[1:]
ver = data[0]
bump_txt = data[1]

def bump(bump_txt: str, version: str) -> str:
    version_list = version.split(".")
    if "patch" in bump_txt:
        v = int(version_list[2]) + 1
        version_list[2] = str(v)
    elif "minor" in bump_txt:
        v = int(version_list[1]) + 1
        version_list[1] = str(v)
        version_list[2] = "0"
    elif "major" in bump_txt:
        v = int(version_list[0]) + 1
        version_list[0] = str(v)
        version_list[1] = "0"
        version_list[2] = "0"
    
    return ".".join(version_list)

new = bump(bump_txt, ver)

sys.stdout.write(new)
