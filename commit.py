import git

repo = git.Repo('.')

uncommitted = repo.git.status('-s')

uncommitted = uncommitted.split('\n')

for i in uncommitted:
    x = i.split(' ')[1:]
    # print(x)
    x = ' '.join(x).strip()
    if x not in ('commit.py', ''):
        print("Adding: " + x.replace("\"", ""))
        repo.git.add(x.replace("\"", ""))
        print("Commiting: " + x.replace("\"", ""))
        repo.git.commit("-m", f"Committing {x}")
        print("Pushing: " + x.replace("\"", ""))
        repo.git.push()
