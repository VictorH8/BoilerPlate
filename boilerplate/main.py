#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


class BoilerPlate:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=(
                "📦 Crie rapidamente a estrutura inicial de projetos em diversas linguagens.\n"
                "Gera pastas e arquivos padrão para começar a codar com boas práticas.\n"
                "Ideal para Python, Node.js, e outros stacks suportados via templates."
            ),
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self.parser.add_argument(
            "--list",
            action="store_true",
            help="Exibe uma lista dos templates e licenças disponíveis. Exemplos de templates: python, node. Exemplos de licenças: MIT, GPL.",
        )
        self.parser.add_argument(
            "--name", help="Nome do diretório/projeto a ser criado"
        )
        self.parser.add_argument(
            "--template",
            help="Define o template/base do projeto (ex: python, flask, node)",
        )
        self.parser.add_argument(
            "--license",
            help="Especifique a licença do seu projeto (ex: MIT, GPL, Apache). Se nenhuma licença for escolhida, a licença padrão será MIT.",
        )
        self.templates = ["python", "flask", "javascript", "node"]
        self.license_list = ["MIT", "GPL", "APACHE", "BSD", "CC", "MPL", "EPL", "LGPL"]
        self.file_contents = {
            "mit": "https://dpaste.org/9ddEc/raw",
            "gpl": "https://choosealicense.com/licenses/gpl-3.0.txt",
            "apache": "https://choosealicense.com/licenses/apache-2.0.txt",
            "bsd": "https://choosealicense.com/licenses/bsd-3-clause.txt",
            "cc": "https://creativecommons.org/licenses/by/4.0/legalcode.txt",
            "mpl": "https://choosealicense.com/licenses/mpl-2.0.txt",
            "epl": "https://www.eclipse.org/legal/epl-2.0/epl-2.0.txt",
            "lgpl": "https://www.gnu.org/licenses/lgpl-3.0.txt",
            "flask": "https://dpaste.org/eFpjt/raw",
            "html_js_template": "https://dpaste.org/Y66LF/raw",
            "css": "https://dpaste.org/FZ7ty/raw",
            "html": "https://dpaste.org/jta0w/raw",
            "gitignore": "https://dpaste.org/AbXEi/raw",
            "gitignore_python": "https://www.toptal.com/developers/gitignore/api/python",
            "gitignore_node": "https://www.toptal.com/developers/gitignore/api/node",
            "node_package_json": "https://dpaste.org/R4HNP/raw"
        }

    def get_content(self, source):
        source = source.lower()
        if source not in self.file_contents:
            print(f"⚠️ Licença '{source}' não encontrada. Usando MIT como fallback.")
            source = "mit"

        data = self.file_contents[source]
        result = subprocess.run(["curl", data], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Erro ao executar curl: {result.stderr}")
            return "Licença não disponível no momento."

        return result.stdout

    def run(self):
        args = self.parser.parse_args()

        try:
            if args.list:
                self.list_templates()
            else:
                self.validate_args(args)
                self.create_project(args)
        except ValueError as ve:
            print(f"❌ Erro: {ve}")
            sys.exit(1)
        except FileExistsError:
            print(
                f"⚠️ O diretório '{args.name}' já existe. Escolha outro nome ou remova o diretório."
            )
            sys.exit(1)
        except Exception as e:
            print("❌ Ocorreu um erro inesperado.")
            print(f"Detalhes: {e}")
            sys.exit(1)

    def validate_args(self, args):
        if not args.name or not args.template:
            raise ValueError(
                "Os argumentos --name e --template são obrigatórios se --list não for usado."
            )
        if args.template not in self.templates:
            raise ValueError(
                f"Template '{args.template}' não é suportado. Use --list para ver opções válidas."
            )

    def list_templates(self):
        print("🗂️  Templates disponíveis:")
        for t in self.templates:
            print(f" - {t}")

        print(f"\n📜 Licenças disponíveis:")
        for l in self.license_list:
            print(f" - {l}")

    def create_project(self, args):
        project_path = Path(args.name).resolve()
        project_path.mkdir(exist_ok=False)
        print(f"📁 Criando projeto em: {project_path}")

        if args.license:
            license = args.license.lower()
        else:
            license = "mit"

        if args.template == "python":
            self.create_python_template(project_path, license)

        if args.template == "javascript":
            self.create_javascript_template(project_path, license)

        if args.template == "flask":
            self.create_flask_template(project_path, license)

        if args.template == "node":
            self.create_node_template(project_path, license)

    def create_python_template(self, path: Path, license="MIT"):
        try:
            print("🐍 Criando ambiente virtual em .venv...")
            subprocess.run(["python3", "-m", "venv", str(path / ".venv")], check=True)

            print("📁 Criando estrutura de diretórios...")
            (path / "src").mkdir(exist_ok=True)
            (path / "tests").mkdir(exist_ok=True)

            print("📄 Gerando arquivos iniciais...")
            (path / "README.md").write_text(
                "# Projeto Python Gerado Pelfalei errado o BoilerPlate\n"
            )
            (path / "src" / "__init__.py").touch()
            (path / "LICENSE").write_text(self.get_content(license))
            (path / ".gitignore").write_text("__pycache__/\n*.pyc\n.env\n.venv/\n")

            print("✅ Template Python criado com sucesso!")
        except subprocess.CalledProcessError:
            print(
                "❌ Falha ao criar o ambiente virtual. Verifique se o Python está instalado corretamente."
            )
        except Exception as e:
            print(f"❌ Erro ao criar template Python: {e}")

    def create_javascript_template(self, path: Path, license="MIT"):
        try:
            print("📁 Criando estrutura de diretórios...")
            (path / "assets").mkdir(exist_ok=True)

            print("📄 Gerando arquivos iniciais...")
            (path / "index.html").write_text(self.get_content("html_js_template"))
            (path / "style.css").write_text(self.get_content("css"))
            (path / "script.js").touch()
            (path / "README.md").touch()
            (path / "LICENSE").write_text(self.get_content(license))
        except Exception as e:
            print(f"❌ Erro ao criar template JavaScript: {e}")

    def create_flask_template(self, path: Path, license="MIT"):
        try:
            print("🐍 Criando ambiente virtual em .venv...")
            subprocess.run(["python3", "-m", "venv", str(path / ".venv")], check=True)

            print("📁 Criando estrutura de diretórios...")
            (path / "app").mkdir(exist_ok=True)
            (path / "app" / "static").mkdir(exist_ok=True)
            (path / "app" / "static" / "css").mkdir(exist_ok=True)
            (path / "app" / "static" / "images").mkdir(exist_ok=True)
            (path / "app" / "static" / "js").mkdir(exist_ok=True)
            (path / "app" / "templates").mkdir(exist_ok=True)

            print("📄 Gerando arquivos iniciais...")
            (path / "app" / "__init__.py").touch()
            (path / "app" / "main.py").write_text(self.get_content("flask"))
            (path / "app" / "static" / "js" / "script.js").touch()
            (path / "app" / "static" / "css" / "style.css").write_text(self.get_content("css"))
            (path / "app" / "templates" / "index.html").write_text(self.get_content("html"))
            (path / "README.md").touch()
            (path / "LICENSE").write_text(self.get_content(license))
            (path / ".gitignore").write_text(self.get_content("gitignore_python"))

            print("✅ Template Flask criado com sucesso!")
        except subprocess.CalledProcessError:
            print(
                "❌ Falha ao criar o ambiente virtual. Verifique se o Python está instalado corretamente."
            )
        except Exception as e:
            print(f"❌ Erro ao criar template Flask: {e}")


    def create_node_template(self, path: Path, license="MIT"):
        try:
            print("📁 Criando estrutura de diretórios...")
            (path / "src").mkdir(exist_ok=True)
            (path / "src" / "config").mkdir(exist_ok=True)
            (path / "src" / "controllers").mkdir(exist_ok=True)
            (path / "src" / "middleware").mkdir(exist_ok=True)
            (path / "src" / "models").mkdir(exist_ok=True)
            (path / "src" / "routes").mkdir(exist_ok=True)
            (path / "src" / "services").mkdir(exist_ok=True)
            (path / "src" / "utils").mkdir(exist_ok=True)
            (path / "src" / "validations").mkdir(exist_ok=True)
            (path / "src" / "tests").mkdir(exist_ok=True)

            print("📄 Gerando arquivos iniciais...")
            (path / "src" / "app.js").touch()
            (path / "src" / "server.js").touch()
            (path / ".env").touch()
            (path / ".gitignore").write_text(self.get_content("gitignore_node"))
            (path / "package.json").write_text(self.get_content("node_package_json"))
            (path / "LICENSE").write_text(self.get_content(license))
            (path / "README.md").touch()

            print("✅ Template Node.js criado com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao criar template Node: {e}")


if __name__ == "__main__":
    BoilerPlate().run()
