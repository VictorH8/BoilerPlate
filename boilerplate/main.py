#!/usr/bin/env python3

import argparse
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
            help="Lista os templates prontos disponíveis (ex: python, node, flask)",
        )
        self.parser.add_argument(
            "--name",
            required=True,
            help="Nome do diretório/projeto a ser criado"
        )
        self.parser.add_argument(
            "--template",
            required=True,
            help="Define o template/base do projeto (ex: python, flask, node)",
        )

    def run(self):
        args = self.parser.parse_args()
        self.create_project(args)

    def create_project(self, args):
        project_path = Path(args.name)
        print(f"📁 Criando projeto em: {project_path.resolve()}")
        project_path.mkdir(exist_ok=True)

        if args.template == "python":
            print("python")


if __name__ == "__main__":
    BoilerPlate().run()
