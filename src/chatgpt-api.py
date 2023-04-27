```
NAME
       chatgpt-api.py

VERSION
        1.0
AUTHOR
	Hely Salgado 

DESCRIPTION

	interfaz CLI para chatgpt

	El programa es una interfaz para interaccionar con chatpgt
	usando el modelo gpt-3.5-turbo

	Hay dos opciones:
	new:  crear una nueva conversaci�n con el chat
	exit: para salirse de la interfaz

CATEGORY
	chatbots

USAGE
	python chatgpt-api.py

ARGUMENTS

        none

SEE ALSO
 	tomado de : https://gist.github.com/mouredev/58abfbcef017efaf3852e8821564c011

```

### from https://gist.github.com/mouredev/58abfbcef017efaf3852e8821564c011

##### librerias
import openai  # pip install openai
import config # local
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""


def main():

    openai.api_key = config.api_key

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Dando Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente que sabe todo sobre Mario Bros"}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        # una respuesta
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold red]> [/bold red] [red]{response_content}[/red]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)
