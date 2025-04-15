#!/usr/bin/env python3

import argparse
from pathlib import Path
import subprocess
import sys


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
            help="Lista os templates prontos disponíveis (ex: python, node, flask)",
        )
        self.parser.add_argument(
            "--name", help="Nome do diretório/projeto a ser criado"
        )
        self.parser.add_argument(
            "--template",
            help="Define o template/base do projeto (ex: python, flask, node)",
        )

        self.templates = ["python", "flask", "javascript" ]
        self.file_contents = {
            "flask": "https://dpaste.org/eFpjt/raw",
            "mit_license": "https://dpaste.org/9ddEc/raw"
        }


    def get_content(self, source):
        if source not in self.file_contents:
            return False
    
        data = self.file_contents[source]
        result = subprocess.run(["curl", data], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Erro ao executar curl: {result.stderr}")
            return False
        
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
        print("📚 Templates disponíveis:")
        for t in self.templates:
            print(f" - {t}")


    def create_project(self, args):
        project_path = Path(args.name).resolve()
        project_path.mkdir(exist_ok=False)
        print(f"📁 Criando projeto em: {project_path}")

        if args.template == "python":
            self.create_python_template(project_path)

        if args.template == "javascript":
            self.create_javascript_template(project_path)

        if args.template == "flask":
            self.create_flask_template(project_path)

        print("✅ Projeto criado com sucesso!")


    def create_python_template(self, path: Path):
        try:
            print("🐍 Criando ambiente virtual em .venv...")
            subprocess.run(["python3", "-m", "venv", str(path / ".venv")], check=True)

            print("📁 Criando estrutura de diretórios...")
            (path / "src").mkdir(exist_ok=True)
            (path / "tests").mkdir(exist_ok=True)

            print("📄 Gerando arquivos iniciais...")
            (path / "README.md").write_text(
                "# Projeto Python Gerado Pelo BoilerPlate\n"
            )
            (path / "src" / "__init__.py").touch()
            (path / ".gitignore").write_text("__pycache__/\n*.pyc\n.env\n.venv/\n")

            print("✅ Template Python criado com sucesso!")
        except subprocess.CalledProcessError:
            print(
                "❌ Falha ao criar o ambiente virtual. Verifique se o Python está instalado corretamente."
            )
        except Exception as e:
            print(f"❌ Erro ao criar template Python: {e}")


    def create_javascript_template(self, path: Path):
        try:
            print("📁 Criando estrutura de diretórios...")
            (path / "app").mkdir(exist_ok=True)
            (path / "static").mkdir(exist_ok=True)
            (path / "templates").mkdir(exist_ok=True)
    

            print("📄 Gerando arquivos iniciais...")
            (path / "index.html").touch()
            (path / "style.css").touch()
            (path / "script.js").touch()
            (path / "README.md").touch()
        except Exception as e:
            print(f"❌ Erro ao criar template JavaScript: {e}")

    def create_flask_template(self, path: Path):
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
            (path / "app" / "main.py").write_text(self.get_content("cavalo"))
            (path / "app" / "static" / "js" / "script.js").touch()
            (path / "app" / "static" / "css" / "style.css").touch()
            (path / "app" / "templates" / "index.html").touch()
            (path / "README.md").touch()
            (path / "LICENSE").write_text(self.get_content("mit_license"))
            (path / ".gitignore").write_text("__pycache__/\n*.pyc\n.env\n.venv/\n")


            print("✅ Template Flask criado com sucesso!")
        except subprocess.CalledProcessError:
            print(
                "❌ Falha ao criar o ambiente virtual. Verifique se o Python está instalado corretamente."
            )
        except Exception as e:
            print(f"❌ Erro ao criar template Flask: {e}")


if __name__ == "__main__":
    BoilerPlate().run()
