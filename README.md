# IntArtificial_ImageGeneration

# **Investigacion Preliminar**

## **Dall-E**

**¿Qué es?**

“DALL-E es un modelo de inteligencia artificial desarrollado por OpenAI, la misma organización detrás de GPT-3.5, que tiene la capacidad de generar imágenes a partir de descripciones textuales.” (Emilio Romero, 2023)


**¿Cómo funciona?** 

Según Emilio Romero, DALL-E utiliza una técnica de aprendizaje profundo conocida como Red Generativa Antagónica (GAN) que son sistemas de IA que constan de dos partes principales: un generador y un discriminador. El generador toma una descripción textual y la convierte en una imagen utilizando una red neuronal profunda que aprende a mapear las palabras de la descripción en una representación visual. Además de eso, esta red neuronal utiliza una técnica llamada codificación por atención, que le permite prestar atención a partes específicas de la descripción para generar detalles visuales más exactos y precisos.
Por otro lado, el discriminador tiene la tarea de evaluar si las imágenes generadas por el generador son reales o falsas. A medida que el generador mejora, el discriminador se vuelve más exigente y preciso en la detección de imágenes generadas artificialmente.


**Aplicaciones**

Entre sus principales aplicaciones se encuentran el arte y diseño como guía o inspiración para algunos artistas o diseñadores. Además de la publicidad y el marketing ya que puede generar imágenes llamativas y atractivas para productos y servicios. Como complemento, se utiliza también en el ámbito de la investigación científica para visualizar conceptos abstractos. También se utiliza para la generación de contenido en medios digitales creando portadas llamativas para los sitios web, redes sociales y más.




## **Vertex AI**

**¿Qué es?**

Es una plataforma de aprendizaje automático administrada por Google Cloud. Unifica todas las herramientas y servicios de Google Cloud relacionados con la inteligencia artificial y el aprendizaje automático. Cumple con el objetivo de facilitar la creación, implementación y mantenimiento de modelos de IA personalizados.

**¿Cómo funciona?**

Vertex AI combina flujos de trabajo de ingeniería de datos, ciencia de datos e ingeniería de aprendizaje automático. La plataforma incluye las herramientas AutoML y AI Platform en una interfaz de API unificada, una biblioteca cliente y una interfaz de usuario. AutoML se encarga de entrenar modelos en conjuntos de datos de imagen, video, texto, etc., sin necesidad de que el usuario escriba un código específico. Por otro lado, AI Platform ayuda a ejecutar un código de entrenamiento personalizado. Vertex AI permite la unión de ambas herramientas y sus funciones, así como elegir la opción de entrenamiento para guardar modelos, implementarlos e incluso solicitar predicciones. 

Cabe mencionar que Imagen on Vertex AI [servicio Generative AI] genera costos cuando se usa y que ciertas funcionalidades de IA generativa de imágenes están disponibles en distintas etapas de lanzamiento; por ejemplo, la generación de imágenes, edición de imágenes, ajustes del modelo y entrenamiento tienen una disponibilidad general restringida por lo que tienes que unirte al programa de testers de Google Cloud y esperar ser aceptado en la waitlist.

**Aplicaciones**

Vertex AI ha sido utilizado para diversas aplicaciones, por ejemplo, Enterprise Search y Conversations en Vertex AI permite a las organizaciones crear aplicaciones de búsqueda y chat utilizando sus datos en pocos minutos. Vertex AI Conversation permite usar lenguaje natural para definir qué respuestas se desea que tenga el chatbot.

Además los clientes de esta plataforma tienen acceso a cientos de modelos base, incluyendo versiones de código abierto. En casos particulares se ofrecen modelos específicos para las industrias de ciberseguridad y empresas de ciencias biológicas y sanitarias como el modelo Med-PaLM 2 [chatbot a lo Bard o ChatGPT pero para fines médicos] en la reconocida Mayo Clinic en Rochester, Minnesota.

En cuanto a Imagen on Vertex AI [servicio Generative AI], la empresa ModiFace [pertenece a L'Oréal, empresa líder en el mercado de los cosméticos] utiliza esta plataforma para estar a la vanguardia en términos de IA en la industria de la belleza.  


## **Midjourney**

**¿Qué es?**

Midjourney es un programa y servicio de inteligencia artificial generativa. Midjourney genera imágenes a partir de descripciones en lenguaje natural (prompts). Está alojado por el laboratorio de investigación independiente Midjourney, Inc., con sede en San Francisco.

**¿Cómo funciona?**

Midjourney se utiliza a través de la plataforma Discord, aunque existe una API que se puede utilizar con Python. Existe una lista de comandos que va desde crear imágenes hasta aumentar su calidad o juntar imágenes.

**Aplicaciones**

Su más notoria aplicación ese la de aumentar la calidad de imágenes. A diferencia de Dall-e o Stable Diffusion, Midjourney no es muy bueno al interpretar un prompt, pero es mejor al momento de reimaginar una imagen.


## **Stable Diffusion**

**¿Qué es?**

Un motor de generación de imágenes creado por la universidad LMU Munich en colaboración con la startup Runway. Permite la generación texto-imagen, imagen-imagen e inpainting (restauración o rellenado de partes de la imagen). Es gratuito (con acceso a herramientas básicas, para mayor personalización existen planes de pago), de código abierto, y no incluye restricciones (a excepción de las éticas y legales) para la generación de imágenes, además su uso y distribución tanto personal como comercial está permitido bajo la licencia Creative ML OpenRAIL-M.

**¿Cómo funciona?**

Utiliza una variante del modelo de difusión llamada modelo de difusión latente (LDM), entrado para eliminar ruido gaussiano de las imágenes de entrenamiento, mediante añadir este ruido a las imágenes durante el entrenamiento de manera controlada para que el modelo aprenda a eliminarlo y mejorar la calidad de las imágenes. Stable Diffusion sigue un proceso de tres partes: un codificador variacional (VAE) que comprime la imagen a un espacio latente, la aplicación de ruido gaussiano iterativo a la representación latente, y un bloque U-Net que elimina el ruido de la representación, por último un decodificador VAE genera la imagen final. 

Es accesible a través de una REST API que ofrece las herramientas anteriormente mencionadas, la capacidad de especificar la cantidad de imágenes a generar, configurar su alto y ancho, además soporta formatos PNG y JPG.

**Aplicaciones**
Algunas apps y/o sitios web que usan Stable Diffusion son:
My Story Bot: Utilizado para generar libros de cuentos para niños de manera automática.
Art Design: Da sugerencias de contenido atractivo y creativo para SEO.
Iconik AI: Genera iconos profesionales que cumplen con las pautas de diseño de iOS, Android y sitios web.
Senti NFT: Crea imágenes y las convierte en tokens no fungibles (NFT).



## **DeepAI Image Generator**

**¿Qué es?**

Es una herramienta de generación de imágenes a partir de texto. El software es de código abierto y para poder utilizarlo solo se debe de crear una cuenta en la plataforma. Tiene distintas librerías disponibles que permiten obtener distintos acabados. Aunque algunos de los servicios y librerías relacionadas con la generación básica de imágenes se pueden utilizar de forma gratuita, servicios más especializados, dentro de los cuales se encuentra el uso del API, tiene un costo.

DeepAI API permite a desarrolladores tener a su alcance funciones como búsqueda semántica, traducción, parafraseo, generación de imágenes, colorización, identificación de objetos, etc... por lo cual es bastante útil para el uso personalizado que genere valor a una cierta actividad.


**¿Cómo funciona?**
Es un modelo de lenguaje basado en transformadores, que es un tipo de arquitectura de red neuronal que fue introducida en un artículo de investigación por Vaswani y otros en 2017. El modelo Transformer está compuesto por un codificador y un decodificador, cada uno de ellos formado por una pila de capas similares. El codificador procesa secuencias de entrada, como frases en lenguaje natural, y genera una codificación para cada token en la secuencia. Luego, el decodificador utiliza estas codificaciones para generar una secuencia de tokens de salida, que pueden ser palabras o frases correspondientes a la secuencia de entrada.

**Aplicaciones**
Una de las principales innovaciones del Transformer es el mecanismo de autoatención. Este mecanismo permite al modelo ponderar la importancia de diferentes tokens en la secuencia de entrada al generar la secuencia de salida. Específicamente, en cada capa del codificador o decodificador, el modelo calcula una matriz de atención que refleja la similitud entre cada par de tokens en la secuencia de entrada o salida. Luego, esta matriz de atención se aplica a las codificaciones y decodificaciones para producir una suma ponderada que captura las partes más importantes de la secuencia de entrada o salida.

El Transformer también utiliza conexiones residuales y normalización de capa para ayudar a superar problemas con gradientes que desaparecen en redes más profundas. Estos mecanismos aseguran que los gradientes puedan fluir suavemente a través de la red durante el entrenamiento, incluso cuando se utilizan muchas capas. En general, el modelo de lenguaje basado en Transformer es una herramienta poderosa para el procesamiento de lenguaje natural. Su capacidad para capturar las relaciones entre palabras y frases, y para generar respuestas contextualmente informadas, lo ha convertido en un enfoque popular para una amplia gama de aplicaciones de inteligencia artificial, incluyendo chatbots, traducción automática y generación de texto.

# **Referencias**

Romero, E. (2023). Qué es DALL-E y cómo usar esta inteligencia artificial para crear imágenes. Recuperado de: https://www.inesem.es/revistadigital/diseno-y-artes-graficas/que-es-dall-e-y-como-usar-esta-inteligencia-artificial-para-crear-imagenes/

Geekflare. (2023). Google Cloud Vertex AI: Esto es lo que necesita saber. Recuperado el 9 Octubre 2023, desde https://geekflare.com/es/google-clouds-vertex-ai/

Google Cloud. (2023). Vertex AI | Google Cloud. Recuperado el 9 Octubre 2023, desde https://cloud.google.com/vertex-ai

AI Chat. (n.d.). DeepAI. Retrieved October 10, 2023, from https://deepai.org/chat

Stable diffusion and dreambooth API - generate and finetune dreambooth stable diffusion using API. (n.d.). Stable Diffusion And Dreambooth API - Generate and Finetune Dreambooth Stable Diffusion Using API. Retrieved October 10, 2023, from https://stablediffusionapi.com/

(N.d.). Stablediffusionweb.com. Retrieved October 10, 2023, from https://stablediffusionweb.com/

