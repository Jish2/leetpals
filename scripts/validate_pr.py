import sys

n = len(sys.argv)

github_username = sys.argv[1]
changed_files = sys.argv[2:]

print(github_username, changed_files)
