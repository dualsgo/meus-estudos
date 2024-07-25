import git

# Abre o repositório
repo = git.Repo('caminho/para/seu/repositorio')

# Obtém o histórico de commits
commits = list(repo.iter_commits('main', max_count=5))

# Gera um resumo das alterações
for commit in commits:
    print(f"Commit: {commit.hexsha}")
    print(f"Autor: {commit.author.name}")
    print(f"Data: {commit.committed_datetime}")
    print(f"Mensagem: {commit.message}")
    print("Alterações:")
    for diff in commit.diff('HEAD~1'):
        print(diff)
