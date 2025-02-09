from setuptools import setup, find_packages

setup(
    name="cleanup",  # Nome do seu antivírus
    version="0.1",  # Versão do seu antivírus
    packages=find_packages(),  # Vai encontrar automaticamente os pacotes no projeto
    install_requires=[  # Dependências do seu antivírus
        'requests',  # Aqui você coloca as dependências, como requests
        'watchdog',  # Se você estiver usando o watchdog
    ],
    entry_points={  # Define o comando para rodar o antivírus
        'console_scripts': [
            'clan-up = clan_up.monitoramento:main',  # Defina a função principal para rodar o antivírus
        ],
    },
    author="Bernardo",  # Substitua pelo seu nome
    author_email="bernardodoagro9@gmail.com",  # Substitua pelo seu e-mail
    description="Antivírus criado por você!",  # Uma descrição breve
    long_description=open('README.md').read(),  # Lê o arquivo README.md para descrever mais detalhes
    long_description_content_type='text/markdown',  # Tipo de conteúdo do README
    url="https://seu-site.com",  # Coloque um link para o seu projeto (se tiver)
)