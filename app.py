import myhelp.filework as mf
import myhelp.interface as mi
from os import listdir

repo = mf.load("repo.json", 2)
newrepo = f"r{len(repo)+1}"
config = mf.load("config.toml", 1)

if len(repo) > 0:
    for i in range(len(repo)):
        mi.system(f"rm -rf {config['Git']['tempFolder']}/{repo[i]}")
    mf.jsDump("repo.json", [])

mi.update()
mi.aprint("GitArch")
link = input("\nType link: ")
repo.append(newrepo)
mf.jsDump("repo.json", repo)

mi.system(f"git clone {link} {config['Git']['tempFolder']}/{newrepo}")
repoFold = listdir(f"{config['Git']['tempFolder']}/{newrepo}")

for i in range(len(repoFold)):
    print(repoFold[i])