import sys

data = sys.argv[1:]
old_version = data[0]
commit_message = " ".join(data[1:])

def bump_version(old_version: str, commit_message: str) -> str:
    """
    Bupms versions acording to commit message. 
    If the message contains one of keywords the function updates the version acordingly.
    If commit message conteins multiple keyword arguments it bumps the version for the highest change.
    
    Args:
        old_version (str): Version to bump.
        commit_message (str): Contains the message from commit to check for keywords.
            Keywords exaples:
            - "BRAKING CHANGE" for major update
            - "minor" for minor updates
            - "patch" for patch update

    Returns:
        str: The return is a string describing the new version.
    """
    version_list = old_version.split(".")
    
    if "BREAKING CHANGE" in commit_message:
        integer_to_change = int(version_list[0]) + 1
        version_list[0] = str(integer_to_change)
        version_list[1] = "0"
        version_list[2] = "0"
    elif "minor" in commit_message:
        integer_to_change = int(version_list[1]) + 1
        version_list[1] = str(integer_to_change)
        version_list[2] = "0"
    elif "patch" in commit_message:
        integer_to_change = int(version_list[2]) + 1
        version_list[2] = str(integer_to_change)
    
    return ".".join(version_list)

new_version = bump_version(old_version, commit_message)

sys.stdout.write(new_version)
