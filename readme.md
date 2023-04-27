
# chatgpt-api

`chatgpt-api` es una interfaz CLI (Command Line Interface) en python para interactuar con el chatbot chat-gpt. El programa usa el modelo `gpt-3.5-turbo` ver los [modelos disponibles](https://platform.openai.com/docs/models/overview).


## Instalación

El programa se ejecuta en línea de comando de la siguiente forma

```unix
python chatgpt-api.py
```

Requiere las siguientes librerias de python 

- `openai` : necesaria para usar el API de chatgpt
- `config`: es una libreria local que contiene la llave de acceso al servidor del chatgpt 
- `typer`: libreria para interfaces CLI
- `rich`: usada para escribir texto enriquecido ( color y estilo)


Será necesario que instales las librerias antes de correr el programa. Aquí las instrucciones para instalar las librerias con el comando pip

```unix
pip install openai
pip install "typer[all]"
pip install rich
````

## Ejemplos

`chat-gpt` puede ser usado en 3 roles distintos, visita la [página de ayuda](https://platform.openai.com/docs/introduction/overview), y las [guías](https://help.openai.com/en/articles/7042661-chatgpt-api-transition-guide) para entender mejor el uso de ésta herramienta.

Diseñar tu mensaje es esencialmente cómo "programa" el modelo, generalmente proporcionando algunas instrucciones o algunos ejemplos. Se puede usar para prácticamente cualquier tarea, incluida la generación de contenido o código, resumen, expansión, conversación, escritura creativa, transferencia de estilo y más.

Para usar el programa te recomendamos los sig. páginas de ayuda para algunos conceptos que debes entender.

- ***prompt***:  El prompt (o contexto inicial) es una parte importante de la entrada de texto que se le proporciona a un modelo de lenguaje como ChatGPT. Es el texto que se usa para iniciar la conversación y proporciona contexto al modelo para generar una respuesta valiosa y coherente. El prompt puede ser una sola oración o un párrafo completo, y puede incluir información sobre el tema de la conversación, el tono deseado y el propósito de la interacción( ver [prompt aprende a utilizarlo](https://www.bilib.es/actualidad/blog/noticia/articulo/el-prompt-de-chatgpt-aprende-a-utilizarlo-para-obtener-los-mejores-resultados/) o [10 “prompts” básicos](https://elandroidefeliz.com/chatgpt-prompts-basicos-para-principiantes/)

Te mostramos el sig. ejemplo

```
python3 chatgpt-api.py
💬 ChatGPT API en Python
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Comando ┃ Descripción                  ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit    │ Salir de la aplicación       │
│ new     │ Crear una nueva conversación │
└─────────┴──────────────────────────────┘

¿Sobre qué quieres hablar? : eres un experto chef especializado en comida mexicana

>  ¡Hola! Soy un asistente virtual y puedo ayudarte con todo lo relacionado con la comida mexicana. ¿Qué te gustaría
saber o qué platillo en específico te gustaría aprender a cocinar?

¿Sobre qué quieres hablar? : dime la receta del mole poblano
>  ¡Por supuesto! Aquí te dejo la receta para preparar el delicioso mole poblano:

Ingredientes:
- 2 a 3 libras de pollo
- 5 chiles mulatos
- 5 chiles pasilla secos
- 5 chiles anchos
- 3 jitomates medianos
- 1/2 cebolla grande
- 3 dientes de ajo
- 1/4 taza de aceite vegetal
...
```

## Páginas relacionadas

- El código de este script viene de [mouredev github](https://gist.github.com/mouredev/58abfbcef017efaf3852e8821564c011)




