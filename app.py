import streamlit as st


#----------------------------
# CONFIGURACION DE LA PAGINA
#----------------------------

st.set_page_config(
    page_title= "proyecto artemis 2",
    page_icon="🌕",
    layout= "wide"

)



#----------------------
# ENCABEZADO Y PORTADA
#----------------------

st.title('El Programa Artemis II: Análisis Exhaustivo de la Primera Misión Tripulada al Entorno Lunar del Siglo XXI 🌕' )
st.subheader("Ventana de Misión: 1 de abril de 2026 – 10 de abril de 2026.")

# navegacion por pesñas

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Contexto Histórico, Propósito y Evolución del Programa Artemis", 
     "Perfil Detallado y Trayectoria de la Tripulación",
     "Logros Técnicos e Hitos Históricos Sin Precedentes",
     "Arquitectura y deseño del sistema de transporte espacial",
     "Conclusiones y Repercusiones para el Futuro de la Exploración Espacial"]
)
#----------------------------------------------------------------------
# EMPEZAMOS ESCRIBIENDO EL CODIGO DE LA PRIMERA SECCION ES DECIR: TAB 1
#----------------------------------------------------------------------
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.header("INTRODUCCION")
        st.write(
            "La misión Artemisa 2 (Artemis II) marca un punto de inflexión estratégico en la historia de la exploración espacial moderna,"
            "representando el regreso de seres humanos a las proximidades de la Luna por primera vez desde el término del programa Apolo en 1972. Como el primer ensayo tripulado del programa Artemis de la NASA, "
            "la misión de aproximadamente 10 días tiene como propósito evaluar la capacidad operativa integrada del cohete de elevación superpesada Space Launch System (SLS) y la nave espacial Orion bajo condiciones reales con astronautas a bordo."
        )
#justamente debajo de la introduccion agregamos un separador y un subtitulo para el panorama general de artemis recordando precisamete que st.divider() es un separador y st.subheader() es un subtitulo y se deben de poner en la misma sangria de tab1 y fuera de la sangria de col1, col2, col3 para que se vea bien en la pagina
    
    st.divider()
    col1, col2, col3 = st.columns([1, 2, 1]) 
    
    
    with col2:
     st.subheader("PANORAMA GENERAL DE ARTEMIS:")
     st.write(
        "La misión Artemis II representa un hito pivotal en la estrategia de exploración espacial contemporánea, al constituir la primera prueba de vuelo tripulada del programa Artemis de la " \
        "Administración Nacional de Aeronáutica y del Espacio (NASA). Tras la validación no tripulada de los sistemas integrados durante la misión Artemis I, este vuelo de prueba con cuatro astronautas a bordo marca el retorno directo de la humanidad a las proximidades " \
        "cislunares después de más de medio siglo. La misión tiene un doble propósito estratégico: validar la capacidad operativa del sistema de soporte vital en el entorno de radiación del espacio profundo y demostrar las maniobras de encuentro, pilotaje manual y navegación requeridas para misiones complejas de descenso en la superficie lunar "
        "(Artemis III) y la posterior exploración tripulada del planeta Marte."
      )
     st.write(
       "El perfil de vuelo de Artemis II comprende un cronograma operativo de aproximadamente diez días (específicamente 9 días, 1 hora y 32 minutos), con una ventana de lanzamiento " \
       "programada a partir del 1 de abril de 2026 y un amarizaje estimado para el 10 de abril de 2026. A diferencia de las misiones Apolo " \
       "tradicionales, que insertaban la nave directamente en una órbita de captura lunar, Artemis II utiliza una trayectoria de retorno libre en " \
       "forma de ocho que aprovecha la gravedad combinada de la Tierra y de la Luna para garantizar un reingreso seguro sin necesidad de " \
       "encendidos de propulsión críticos durante la fase de regreso. Este diseño operativo minimiza el riesgo sistémico mientras expone a la " \
       "tripulación y a los subsistemas del vehículo a las rigurosas condiciones del espacio profundo."
      )
     st.write(
       "La trayectoria se estructura dinámicamente desde el despegue propulsado por el cohete Space Launch System (SLS) hasta la inserción en " \
       "una Órbita Terrestre Alta (HEO). En esta fase inicial de verificación orbital, el vehículo efectúa una trayectoria elíptica de " \
       "44,525 por 115 millas estatutas antes de recibir el impulso decisivo mediante el encendido de Inyección Translunar (TLI). Dicho " \
       "encendido proyecta a la nave en un viaje de ida de cuatro días hacia el satélite natural. Tras completar un sobrevuelo lunar cercano a " \
       "una altitud de entre 4,000 y 6,000 millas náuticas sobre la superficie, la gravedad lunar curva naturalmente el rumbo de regreso de " \
       "Orion hacia la Tierra, concluyendo con un reingreso atmosférico a alta velocidad y un amarizaje controlado en el Océano Pacífico."
      )
     st.write(
       "La relevancia de esta misión radica en el paso progresivo de la infraestructura espacial desde la órbita terrestre baja (LEO) " \
       "hacia el entorno cislunar. A través de este informe, se analizan exhaustivamente la trayectoria de la tripulación, los logros " \
       "históricos alcanzados, la arquitectura técnica del lanzador SLS y la nave Orion, los complejos desafíos de ingeniería asociados a" \
       "l escudo térmico y los sistemas de soporte vital, así como la carga útil científica de vanguardia que acompaña este vuelo espacial."
      )
    col_imagen, col_video = st.columns(2)
    with col_imagen:
         st.image(
            "artemis2.jpeg",
            caption="Artemis II: la primera misión tripulada del programa Artemis, marcando un hito en la exploración lunar moderna.",
            width=560,
         )
    with col_video:
         st.video(
            "https://www.youtube.com/watch?v=d4QGZl18p2w",
            width="stretch",
         )

#-----------------------------------------------------------------------
# EMPLEZAMOS ESCRIBIENDO EL CODIGO DE LA SEGUNDA SECCION ES DECIR: TAB 2
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------
# RECORDAR LAS SIGUIENTES VARIABLES: 
# st.info("...") → caja azul, ícono ℹ️ — para datos o notas generales
# st.success("...") → caja verde, ícono ✅ — para algo positivo o completado
# st.warning("...") → caja amarilla, ícono ⚠️ — para advertencias
# st.error("...") → caja roja, ícono ❌ — para errores o algo negativo
#--------------------------------------------------------------------------

with tab2:
    if st.session_state.get("astronauta_elegido") is None:
        # st.session_state.get("astronauta_elegido") se diferencia de
        # st.session_state["astronauta_elegido"] = "Reid Wiseman" ya que en el segundo
        # ahí guardas el nombre de Reid, no lo estás consultando; el primero es para
        # consultar si hay un astronauta elegido o no, y el segundo para guardar el nombre.
        st.info(
            "En esta sección, se presenta un análisis exhaustivo del perfil de la tripulación de Artemis II, "
            "incluyendo sus antecedentes profesionales, experiencia en vuelos espaciales y contribuciones individuales al éxito de la misión.👨‍🚀🌌"
        )
        st.warning(
            "nota: recuerda que la tripulación de Artemis II está compuesta por cuatro astronautas, "
            "cada uno con un conjunto único de habilidades y experiencias que son cruciales para la misión.🪐"
        )
        st.divider()
        st.header("Perfil de la Tripulación")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("*Astronauta 1*: Reid Wiseman😎")
            st.image(
                "ws.jpg",
                caption="Reid Wiseman, comandante de Artemis II, con experiencia en misiones de la Estación Espacial Internacional, ISS.",
                width=280,
            )

            if st.button("Haz clic para saber mas de reid wiseman", key="reid_wiseman"):
             st.session_state["astronauta_elegido"] = "Reid Wiseman"
             st.rerun()
        with col2:
            st.subheader("*Astronauta 2*: Christina Koch🌟")
            st.image(
                "christina.webp",
                caption="Christina Koch, especialista de misión de Artemis II, conocida por su récord de caminatas espaciales.",
                width=280,
            )
            if st.button("Haz clic para saber mas de christina koch", key="christina_koch"):
             st.session_state["astronauta_elegido"] = "Christina KocH"
             st.rerun()
        with col3:
            st.subheader("*Astronauta 3*: Jeremy Hansen🚀")
            st.image(
                "hansen.webp",
                caption="Jeremy Hansen, piloto de Artemis II, con experiencia en vuelos espaciales y entrenamiento en la ESA.",
                width=280,
            )
            if st.button("Haz clic para saber mas de jeremy hansen", key="jeremy_hansen"):
             st.session_state["astronauta_elegido"] = "Jeremy Hansen"
             st.rerun()
        with col4:
            st.subheader("*Astronauta 4*: Victor Glover🛰️")
            st.image(
                "victor.webp",
                caption="Victor Glover, especialista de misión de Artemis II, con experiencia en vuelos espaciales y operaciones de la ISS.",
                width=280,
            )
            if st.button("Haz clic para saber mas de victor glover", key="victor_glover"):
             st.session_state["astronauta_elegido"] = "Victor Glover"
             st.rerun()
       
 #---------------------------------------------------------------------------------------------------------------------
 # INICIAMOS EL PERFIL DETALLADO DE REID WISEMAN EN CASO DE QUE EL USUARIO HAYA HECHO CLIC EN EL BOTON DE REID WISEMAN
 #----------------------------------------------------------------------------------------------------------------------
    else:
        if st.button ("<-Volver a la lista de astronautas", key= "volver"):
            st.session_state["astronauta_elegido"] = None # Borra la selección actual asignando un valor nulo al registro de la sesión devolviendo al usuario al if anterior
            st.rerun()
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------
 # para cear el boton de continuar al siguiente astronauta primero debemos asignarle un posicion a cada uno con respecto al orden en como los estamos escribiendo
 # es decir, si nuestro primer astronauta es reid entonces resivira la posicion 0 
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------
        astronautas = [
           "Reid Wiseman", #posicion 0
           "Christina KocH", #posicion 1
           "Jeremy Hansen", #posicion 2
           "Victor Glover" #posicion 3
        ]
 #---------------------------------------------------------------------------------------
 # luego le asignamos un nombre de variable a la carpeta session_state ["astronauta_elegido"]
 #---------------------------------------------------------------------------------------
        astronauta_actual= st.session_state[ 
           "astronauta_elegido"
        ]
 #-------------------------------------------------------------------------------------------------------------------------------------------------
 # Luego le decimos a streamlit que entre a la memoria y evalue dicha carpeta, es decir, en la carpeta del o de la astronauta que fue elegida, 
 # (la cual por cierto es la que guarda el nombre del astronauta elegido) y esto lo hacemos primero poniendole un nombre (indice_actual)
 # y luego poniendo el nombre de la variable que queremos que evalue con la palabra .index
 #---------------------------------------------------------------------------------------------------------------------------------------------------
        indice_actual= astronautas.index(
           astronauta_actual
        )
        siguiente_indice = (indice_actual + 1) % len(astronautas)
    
 # Para finalizar invocamos el boton 

        if st.button ("siguiente astronauta", key= "siguiente"):
           st.session_state["astronauta_elegido"] = astronautas [siguiente_indice]
           st.rerun()

        st.write(f"Mostrando detalle de: {st.session_state['astronauta_elegido']}")
        if st.session_state["astronauta_elegido"] == "Reid Wiseman":
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.header("Perfil Detallado de Reid Wiseman")

                st.image(
                    "wiseman_chief_astronaut_0.webp",
                    width=300,
                )

            st.divider()
            st.subheader("Reid Wiseman: Comandante de Artemis II (NASA)")
            st.write(
                "Gregory Reid Wiseman nació el 11 de noviembre de 1975 en Baltimore, Maryland. Tras graduarse de la Dulaney High School en 1993, obtuvo una Licenciatura en Ciencias (Bachelor of Science) en Ingeniería de Computadores y Sistemas en el Rensselaer Polytechnic Institute en 1997. " \
                "Posteriormente, en 2006, completó una Maestría en Ciencias en Ingeniería de Sistemas en la Universidad Johns Hopkins"
            )
            st.write(
                "Wiseman inició su carrera militar tras ser comisionado a través del Cuerpo de Entrenamiento de Oficiales de la Reserva Naval (NROTC) en 1997. Designado como aviador naval en 1999, completó la transición al caza F-14 Tomcat en el Escuadrón de Caza 101. Asignado al Escuadrón de Caza 31, " \
                "ejecutó dos despliegues operativos en Oriente Medio en apoyo a las Operaciones Southern Watch, Enduring Freedom e Iraqi Freedom. En 2003 fue seleccionado para ingresar a la Escuela de Pilotos de Prueba Navales de los Estados Unidos (clase 125), graduándose en junio de 2004. Como piloto de pruebas en el Escuadrón de Prueba y Evaluación Aérea 23 (VX-23), " \
                "participó en programas de desarrollo del F-35 Lightning II, separación de armas en F-18 y pruebas de idoneidad en portaaviones con el T-45 Goshawk."
            )
            st.write(
                "Seleccionado por la NASA en junio de 2009 como integrante del Grupo 20 de astronautas, Wiseman concluyó su instrucción básica en 2011. Su primer vuelo espacial tuvo lugar entre mayo y noviembre de 2014, sirviendo como Ingeniero de Vuelo a bordo de la Estación Espacial Internacional (EEI) durante la Expedición 40/41. Acumuló 165 días en el espacio y " \
                "ejecutó dos caminatas espaciales (EVA) con un total de 12 horas y 47 minutos. Entre diciembre de 2020 y noviembre de 2022 ocupó el cargo de Jefe de la Oficina de Astronautas de la NASA (Chief of the Astronaut Office), posición que dejó para reincorporarse a " \
                "la rotación activa de vuelo y asumir el mando de Artemis II. Entre sus galardones destacan la Legion of Merit, " \
                "la Defense Superior Service Medal y la Air Medal con V de combate."
            )
            st.success(
                "La ciudad natal de Reid es Baltimore, Maryland. Su difunta esposa, Carroll, dedicó su vida a ayudar a otros como enfermera registrada en la unidad de cuidados intensivos para recién nacidos. Le sobreviven sus dos hijos. " \
                "A pesar de una larga lista de elogios profesionales, Reid considera su tiempo como padre soltero como su mayor desafío y la fase más gratificante de su vida. Cuando se enfrenta a un desafío en su vida personal o profesional, Reid a menudo busca orientación en libros de expertos en el tema y mantiene una mentalidad de crecimiento hacia el aprendizaje y las soluciones colaborativas. Su padre, Bill, reside en Hunt Valley, Maryland. ✨✨✨"
            )
            st.success(
                "*OBTUVO PREMIOS COMO:*Legión al Mérito, Medalla de Servicio Superior de Defensa, Medalla Aérea con Combate V (cinco premios), Medalla de Reconocimiento de la Armada y el Cuerpo de Marines con Combate V (cuatro premios), Medalla de Logros de la Armada y el Cuerpo de Marines, varios otros premios de campaña y servicio.🎖️🎖️🎖️"
            )
        elif st.session_state["astronauta_elegido"] == "Christina KocH":
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.header("Perfil Detallado de Christina Koch")
                st.image(
                    "koch.webp",
                    width=300,
                )
            st.divider()
            st.subheader("Christina Koch: Especialista de Misión (NASA)")
            st.write (
               "Christina Koch es una exploradora e ingeniera que se convirtió en astronauta en 2013. Se desempeñó como especialista de misión de la misión Artemis II de la NASA en 2026. " \
               "Su experiencia previa en vuelos espaciales fue vivir y trabajar en la Estación Espacial Internacional durante casi todo 2019 en las Expediciones 59, 60 y 61.  Para esta misión, voló en el cohete ruso Soyuz y se entrenó extensamente en Rusia.  " \
               "Christina pasó un total de 328 días consecutivos en el espacio y participó en las primeras caminatas espaciales exclusivamente femeninas. " \
                "Después de este vuelo espacial y antes de ser asignada a Artemis II, se desempeñó como Jefa de Rama de Tripulación Asignada en la Oficina de Astronautas e hizo una rotación como Asistente de Integración Técnica para el Director del Centro en el Centro Espacial Johnson de la NASA. Antes de convertirse en astronauta,La experiencia de Christina abarcó tanto el desarrollo de instrumentos para misiones científicas espaciales como la ingeniería de campo científica remota en la Antártida y el Ártico. Sus pasatiempos incluyen el surf, la escalada en roca y hielo, la programación, el servicio comunitario, los triatlones, el yoga, el mochilerismo, la carpintería, la fotografía y los viajes."
            )
            st.write(
               "Christina Hammock Koch [pronunciación: “Cook”] fue seleccionada como astronauta de la NASA en 2013. Se desempeñó como ingeniera de vuelo en la Estación Espacial Internacional (ISS)" \
               " para las Expediciones 59, 60 y 61. Koch estableció un récord para el vuelo espacial más largo realizado por una mujer con un total de 328 días en el espacio y participó en la " \
               "primera caminata espacial exclusivamente femenina. Se desempeñó como Especialista de Misión I de la misión Artemis II de la NASA. La tripulación se lanzó en el cohete Space Launch" \
               " System de la NASA a las 6:35 p.m. EDT 1 de abril de 2026 desde la plataforma de lanzamiento 39B en el Centro Espacial Kennedy de la agencia en Florida. Con 8,8 millones de libras " \
               "de empuje en el despegue, el cohete construido en Estados Unidos impulsó a la tripulación dentro de la nave espacial Orión al espacio, llevándola a la órbita con una precisión " \
               "milimétrica. Los astronautas de la NASA Reid Wiseman, Victor Glover y Christina Koch,y el astronauta de la CSA (Agencia Espacial Canadiense) Jeremy Hansen amerizó a las 20:07 " \
               "horas. EDT 10 de abril de 2026 frente a la costa de San Diego, completando un viaje de casi 10 días que los llevó a 252,756 millas desde su hogar en su distancia más lejana de la " \
               "Tierra."
            )
        elif st.session_state["astronauta_elegido"] == "Jeremy Hansen":
           col1, col2,col3 = st.columns([1, 2, 1])
           with col2:
                st.header("Perfil Detallado de Jeremy Hansen")
                st.image(
                    "canadian.jpg",
                    width=250,
                )
           st.divider()
           st.subheader("jeremy hansen:Especialista de mision (CSA)")
           st.write (
           "Jeremy Roger Hansen (London, ON; 27 de enero de 1976) es un astronauta canadiense de la CSA (Agencia Espacial Canadiense). " \
           "Se unió al cuerpo de astronautas de CSA en 2009 tras un proceso de selección del que también resultó selecto David Saint-Jacques. " \
           "Antes de su entrenamiento como tal, Hansen tenía el rango de capitán en la Real Fuerza Aérea Canadiense, pilotando aviones de combate CF‑18 en " \
           "la base militar de CFB Cold Lake (provincia de Alberta, en Canadá), y años después obtuvo el rango de coronel."
        )
           st.write(
           "El 1 de abril de 2026, Hansen despegó como miembro de la tripulación de la misión Artemis II, cuyo objetivo era realizar un sobrevuelo lunar. " \
           "Es el primer astronauta canadiense en viajar más allá de la órbita terrestre baja y acercarse a la Luna."
        )
           st.markdown ("#### Vida personal y educación")
           st.write (
           "Hansen nació en London, Ontario y creció en una granja cercana a Ailsa Craig, Ontario, hasta que se mudó a Ingersoll durante su adolescencia. " \
           "El coronel está casado y tiene tres hijos. A los 12 años comenzó su experiencia como aviador al unirse al programa Air Cadet y obtuvo licencias " \
           "de planeador y piloto privado a través de este programa a la edad de 17 años.[1]" \
           "" \
        )

           st.write(
           "En 1999, Hansen se graduó con honores de ciencias del espacio en el Royal Military College de Kingston, Ontario. " \
           "Obtuvo un título de maestría en física por la misma institución en 2000."
        )
           st.write(
           "Hansen posee una licenciatura en ciencias espaciales y una maestría en física con especialización en el seguimiento de " \
           "satélites mediante sistemas ópticos de amplio campo. Seleccionado como astronauta de la CSA en 2009, Hansen fue el primer " \
           "canadiense asignado para liderar una clase de candidatos a astronauta de la NASA en 2017. Además, ha participado en las misiones " \
           "análogas CAVES de la ESA (exploración subterránea en Cerdeña) y NEEMO 19 (operaciones bajo el océano en el hábitat Aquarius). " \
           "Sus responsabilidades en la misión incluyen las operaciones de soporte vital de la cápsula, la verificación de la integración del Módulo de " \
           "Servicio Europeo (ESM) y las observaciones astronómicas y lunares desde la ventana de la nave espacial."
        )
        elif st.session_state ["astronauta_elegido"]== "Victor Glover":
           col1, col2, col3= st.columns([1,2,1])
           with col2:
              st.header("perfil detallado de victor glover")
              st.image(
                 "victor.webp",
                  width=280 ,
              )  
           st.divider()  
           st.write(
           "El Capitán Victor J. Glover, Jr. se desempeña como piloto de la misión. Graduado en ingeniería general y " \
           "con maestrías en ingeniería de vuelo, sistemas operativos y arte y ciencia militar operacional, Glover es un experimentado " \
           "piloto de pruebas de la Marina de los Estados Unidos con más de 3,000 horas de vuelo en más de 40 aeronaves diferentes. " \
           "Seleccionado en la generación de astronautas de 2013, Glover voló como piloto de la misión SpaceX Crew-1 (Expedición 64/65) a la EEI, " \
           "donde acumuló 168 días en el espacio y completó cuatro caminatas espaciales. En Artemis II, Glover tiene a su cargo el control " \
           "directo de los subsistemas de propulsión, la navegación, la energía de la nave Orion, y la ejecución de las operaciones de pilotaje " \
           "manual de proximidad y encuentro espacial (RPOD) con la etapa superior del cohete en órbita terrestre alta."
              )
           st.write(
                  "### Estudios universitarios y formación académica"
              )
           st.write(
              "Victor Glover obtuvo la Licenciatura en Ingeniería General (B.S. in General Engineering) por la Universidad Politécnica Estatal de California (Cal Poly, San Luis Obispo) en 1999. Fue el primer miembro de su familia en obtener un título universitario. " \
              "Posteriormente completó un Máster en Ingeniería de Pruebas de Vuelo en la Escuela de Pilotos de Pruebas de la Fuerza Aérea de Estados Unidos (Air University, Base Edwards) en 2007, un Máster en Ingeniería de Sistemas en la Escuela Naval de Posgrados en 2009 y un Máster en Arte y Ciencia Operacional Militar en Air University en 2010. " \
              "También obtuvo certificados en Estudios Legislativos por la Universidad de Georgetown y en Sistemas Espaciales por la Naval Postgraduate School."
           )
           st.write(
              "### Experiencias personales y lecciones de vida"
           )
           st.write(
              "Durante su segundo año en Cal Poly, Glover reprobó una materia de ingeniería. Un profesor le advirtió que el talento sin esfuerzo no sería suficiente para alcanzar sus objetivos. Glover asumió la responsabilidad, cambió sus hábitos de estudio y convirtió el rigor en una norma de trabajo. " \
              "Hijo de un oficial de policía y una contadora, también recibió una importante influencia familiar: su abuelo sirvió en la Fuerza Aérea durante la época de la Guerra de Corea, aunque no pudo volar debido a las barreras raciales. Inicialmente quería enlistarse como Navy SEAL, pero su padre lo orientó hacia la aviación naval y la carrera de astronauta."
           )
           st.write(
              "Desde joven destacó como atleta: fue Atleta del Año en 1994 por sus logros en fútbol americano y salto con garrocha, y durante la universidad compitió simultáneamente en lucha olímpica (wrestling) y fútbol americano."
           )
           st.write(
              "### Experiencia operativa y combate"
           )
           st.write(
              "Glover acumuló más de 3.000 horas de vuelo en más de 40 aeronaves y participó en misiones de combate en Irak a bordo del portaaviones USS John F. Kennedy. Antes de ser seleccionado por la NASA en 2013, trabajó en el Capitolio como asesor de política espacial en el Senado de Estados Unidos."
           )
           st.write(
              "### Vida familiar y vínculo desde la órbita"
           )
           st.write(
              "Está casado desde hace más de 20 años con Dionna Odom, a quien conoció en la universidad, y es padre de cuatro hijas. Durante sus 168 días en la Estación Espacial Internacional mantuvo la cercanía con su familia organizando partidas semanales de mímica en gravedad cero por videoconferencia."
              )
with tab3:
   col1, col2, col3 = st.columns ([1,2,1])
   with col2:
      st.header(
         "Hitos Históricos sin Precedentes y Logros Técnicos🏆"
      )
   st.divider()  
   col1, col2, col3 = st.columns ([1,2.5,1])
   with col2:
      st.subheader(
      "1. El récord absoluto de distancia humana (Superando al Apolo 13):" 
   )
      st.write(
      "**Métrica:** Orion alcanza una distancia máxima de 406,771 km (252,756 millas) con respecto a la Tierra."
   )
      st.write(
      "**Análisis:** Rompe el récord histórico establecido en abril de 1970 por el Apolo 13 (400,171 km). La nave se adentra 6,600 km "
      "(4,101 millas) más allá de la cara oculta de la Luna. A esa distancia, el tiempo de latencia en las comunicaciones de radiofrecuencia (RF) roza los 1.3 segundos por vía."
   )
      st.subheader(
      "2. Transformación de la Demografía Cislunar:"
   )
      st.write(
      "Rompe la exclusividad de los 12 hombres estadounidenses que caminaron sobre la Luna entre 1969 y 1972. " \
      "Incorpora por primera vez a una mujer (Christina Koch), un hombre afrodescendiente (Victor Glover) y un ciudadano " \
      "canadiense (Jeremy Hansen) en una trayectoria cislunar de espacio profundo."
   )
      st.subheader(
      "3. Primera Integración Operativa **Fly-by-Wire** en Espacio Profundo:"
   )
      st.write(
      "A diferencia de los interruptores discretos y computadoras de guía analógicas del Apolo, " \
      "Artemis II opera con control de vuelo digital fly-by-wire, pantallas táctiles de cristal líquido integradas y " \
      "comandos de subsistemas distribuidos en red mediante buses de datos ARINC 664.  "
   )
      st.header(
      "Análisis Profundo de las Maniobras Clave"
   )
      st.subheader(
      "1. Demostración RPOD en Órbita Terrestre Alta (HEO)"
   )
      st.write(
      "Tras el encendido de elevación de apogeo por parte de la etapa ICPS, Orion se separa de la misma a una altitud elíptica de casi " \
      "70,000 km. En ese instante, Victor Glover toma el mando manual mediante los joysticks de control de actitud y traslación. " \
      "Con la etapa gastada flotando como blanco, Glover maniobra la cápsula a distancias cortas para probar la respuesta dinámica de los " \
      "propulsores RCS, la calibración de las cámaras ópticas y los sensores de proximidad. Es la prueba definitiva de que la masa de la " \
      "nave responde con precisión a la fuerza vectorial aplicada por el piloto antes de enviarla a la Luna."
   )
      st.subheader(
      "2. Sistema de Comunicaciones Ópticas O2O (Orion Artemis II Optical Communications System)"
   )
      st.write(
      "Desarrollado por el Laboratorio Lincoln del MIT y la NASA, el O2O utiliza un terminal óptico con espejos direccionables " \
      "para apuntar con precisión quirúrgica un haz láser infrarrojo desde la nave en movimiento hacia estaciones terrenas en " \
      "California y Nuevo México. Transmitir a 260 Mbps a más de 400,000 km de distancia equivale a llevar una conexión de fibra óptica al " \
      "espacio profundo, marcando el estándar para la futura red de telecomunicaciones en Marte.  "     
   )
      st.subheader(
      "3. Modificación del Perfil de Entrada y Manejo del Escudo Avcoat"
   )
      st.write(
      "Durante el reingreso a 40,000 km/h (11 km/s), la energía cinética del vehículo se transforma en un frente de onda de choque " \
      "térmico de 2,760 °C. Para resolver la pérdida imprevista de bloques de material carbonizado (char loss) sufrida en Artemis I, " \
      "la computadora de vuelo de Artemis II ejecuta una técnica de entrada ajustada: varía el ángulo de ataque **(gamma)** mediante el " \
      "desplazamiento de su centro de gravedad con los propulsores del Módulo de Tripulación. Esto aplana la curva de acumulación de " \
      "presión de gas interno por pirólisis en la matriz de Avcoat, evitando que el material ablativo colapse y se desprenda en pedazos."
   )
   st.divider()
   col1, col2, col3 = st.columns ([1,2,1])
   with col2:
      st.header(
         "Carga Útil Científica e Investigaciones Biomédicas en Espacio Profundo🔬⚗️"
      )  
   st.divider()
   col1, col2, col3 = st.columns ([1,3,1])
   with col2:
      st.info(
         "**Al traspasar la protección del campo magnético terrestre (la magnetosfera) y atravesar los cinturones de " \
         "radiación de Van Allen, los astronautas de Artemis II quedan expuestos a los rayos cósmicos galácticos (GCR) y a los eventos de " \
         "partículas solares (SPE). Por esta razón, la nave funciona como un laboratorio de investigación científica aplicada.**"
      )
      st.subheader(
         "1. Experimento AVATAR (A Virtual Astronaut Tissue Analog Response)🔬"
      )
      st.write(
         "Desarrollado mediante la colaboración entre la NASA, los Institutos Nacionales de Salud (NIH), BARDA, Space Tango, " \
         "Emulate y el Centro de Investigación de Salud Naval (NHRC), el experimento AVATAR emplea dispositivos de tecnología " \
         "microfluídica conocidos como **órganos en un chip (organ-on-a-chip).**"
      )
      st.write(
         "Los chips, del tamaño aproximado de una unidad de memoria USB, contienen microcanales transparentes habitados por células " \
         "madre vivas de médula ósea humana. La médula ósea es un tejido altamente radiosensible responsable de la hematopoyesis "
         "(generación de glóbulos rojos, blancos y plaquetas). Durante el vuelo, los chips permiten medir de forma directa el nivel " \
         "de ruptura del ADN de la médula ósea provocado por las partículas ionizantes del espacio profundo sin poner en peligro la " \
         "integridad física inmediata de los tripulantes. Asimismo, evalúan la neocitolisis, un proceso fisiológico desencadenado en " \
         "microgravedad donde el cuerpo humano destruye de forma selectiva sus propios glóbulos rojos recién sintetizados al percibir " \
         "un falso exceso de fluido sanguíneo en el torso superior. La instrumentación automatizada de AVATAR evalúa los mecanismos " \
         "celulares subyacentes a esta respuesta para guiar la formulación de terapias farmacológicas proyectadas para las misiones a Marte."
      )
      st.subheader(
         "2. ARCHeR y Estudio de Biomarcadores Inmunológicos🧬"
      )
      st.write(
         "La combinación de confinamiento, alteración de ritmos circadianos, microgravedad y radiación provoca una supresión del sistema " \
         "inmunitario de los astronautas. Mediante la investigación ARCHeR (Artemis Research for Crew Health and Readiness), " \
         "la tripulación utiliza dispositivos biométricos de pulsera para registrar de manera continua la calidad del sueño, " \
         "la actividad motora y las fluctuaciones fisiológicas de estrés. Complementariamente, los análisis de muestras de sangre y " \
         "saliva recolectadas durante la misión evalúan la supresión inmunológica y la reactivación de virus latentes en el sistema nervioso "
         "(como el virus de la varicela-zóster o el virus de Epstein-Barr). Además, cuatro sensores de radiación instalados en la cabina trazan " \
         "un mapa de las dosis de exposición acumuladas en el interior de Orion."
      )
      st.subheader(
         "3. Cargas Útiles Secundarias: CubeSats en Órbita Terrestre Alta"
      )
      st.markdown(
         """
         - 🚀 **ATENEA (CONAE, Argentina):** Evalúa la eficacia de nuevos materiales de blindaje contra la radiación, captura datos del espectro de radiación en las inmediaciones terrestres y valida enlaces de comunicación a larga distancia.
         - ☢️ **K-Rad Cube (KASA, Corea del Sur):** Utiliza un dosímetro de radiación fabricado con un material equivalente al tejido humano para cuantificar las dosis equivalentes absorbidas al atravesar los cinturones de Van Allen.
         - 🌌 **Space Weather CubeSat (Agencia Espacial Saudí):** Monitoriza la radiación ambiental, los rayos X solares, las partículas energéticas y las fluctuaciones del campo magnético espacial.
         - 🧪 **TACHELES (DLR, Alemania):** Analiza los efectos directos de la radiación ionizante del espacio profundo sobre componentes electrónicos comerciales de última generación para el desarrollo de vehículos lunares.
         """
      )
with tab4:
   col1, col2, col3 = st.columns([1,4,1])
   with col2:
      st.header(
         "Desafíos de Ingeniería Críticos y Resoluciones Tecnológicas 🔧⚙️"
      )
   st.divider()
   col1, col2, col3 = st.columns([1,2,1])
   with col2:
      st.info(
         "ℹ️ El programa Artemis II debió resolver complejos dilemas térmicos y mecánicos detectados durante la telemetría post-vuelo de " \
         "Artemis I antes de autorizar la integración de tripulantes humanos."
      ) 
      st.subheader(
        "1. El Escudo Térmico de Orion y la Anomalía de Pérdida de Material Incandescente (Avcoat)🔥" 
      )
      st.write(
         "El escudo térmico de la nave Orion, con un diámetro de 16.5 pies (5.0 metros), constituye la estructura de protección ablativa " \
         "más grande jamás desarrollada para misiones espaciales tripuladas. El material ablativo primario es Avcoat, una resina epoxi " \
         "novolaca formulada con microglobos de vidrio dentro de una estructura en panal de abejas de fibra de vidrio. Este sistema está " \
         "diseñado para erosionarse intencionalmente y disipar los casi 5,000 °F (2,760 °C) generados durante el reingreso a velocidades " \
         "lunares de aproximadamente 25,000 mph (40,000 km/h)."
      )
      st.write(
         "Tras el amarizaje de la cápsula Artemis I en diciembre de 2022, las inspecciones forenses revelaron más de 100 ubicaciones donde el " \
         "material ablativo carbonizado (char) se desprendió en fragmentos o pedazos sólidos en lugar de sublimarse de forma gradual. " \
         "La investigación posterior, liderada por la NASA y el Centro de Análisis Avanzado del Laboratorio Nacional Lawrence Berkeley (ALS), " \
         "determinó la causa raíz del fenómeno. Durante la etapa de descenso aerodinámico y las variaciones de aceleración en la atmósfera " \
         "terrestre, la elevación de temperatura penetró profundamente en las capas vírgenes del Avcoat. La pirólisis de la resina generó gases " \
         "internos que no encontraron una vía de permeabilidad adecuada para ventilarse hacia el exterior. Esta falta de permeabilidad provocó " \
         "un aumento continuo de la presión de poro interna hasta superar la resistencia mecánica de la capa carbonizada, ocasionando que " \
         "pequeños bloques de Avcoat se fracturaran y se desprendieran de forma irregular. Adicionalmente, informes del Inspector General de la " \
         "NASA (OIG) advirtieron sobre la erosión y fundición localizada en torno a tres de los cuatro pernos de separación del Módulo de " \
         "Servicio, lo que generó preocupación sobre la posible ingestión de gases calientes en la estructura posterior del vehículo."
      )
      st.write(
         "Dado que el escudo térmico de la cápsula de Artemis II ya se encontraba totalmente ensamblado al momento de identificarse la " \
         "anomalía, la NASA ejecutó un programa intensivo de más de 100 pruebas en las instalaciones de chorro de arco (arc jet) del Centro de " \
         "Investigación Ames. Los datos demostraron que la cápsula retuvo un margen de Avcoat no consumido suficiente para mantener la " \
         "temperatura interna del habitáculo en niveles seguros para los astronautas. La solución operacional adoptada para Artemis II consiste " \
         "en modificar la trayectoria de reingreso en la atmósfera (entry profile), ajustando el ángulo de ataque aerodinámico para aminorar la " \
         "acumulación de gas en el interior del material ablativo sin comprometer la seguridad. Para las misiones subsiguientes, " \
         "como Artemis III, la NASA rediseñó el proceso de manufactura, sustituyendo el rellenado individual de 300,000 celdas por bloques de " \
         "Avcoat pre-mecanizados (menos de 200 bloques) adheridos con porosidad y permeabilidad controladas para permitir la liberación " \
         "continua de vapor y gas sin fracturas estructurales."
      )
      st.subheader(
         "2. Sistema de Control Ambiental y Soporte Vital (ECLSS)༄.°"
      )
      st.write(
         "A diferencia de la Estación Espacial Internacional, que depende de reabastecimientos periódicos desde la Tierra, la nave " \
         "Orion en Artemis II opera un sistema ECLSS cerrado optimizado para el volumen y las restricciones de masa de una misión de " \
         "espacio profundo."
      )
      st.write(
         "El control de dióxido de carbono ($CO_2$) y la humedad de la cabina utiliza la tecnología Carbon Dioxide and Moisture Removal Amine Swingbed (CAMRAS). El sistema consta de lechos dobles rellenos de un absorbente " \
         "químico basado en aminas sólidas. Mientras un lecho filtra activamente el aire de la cabina reteniendo el $CO_2$ y la humedad, el " \
         "segundo lecho se expone automáticamente al vacío del espacio exterior mediante una válvula de alternancia (swingbed). La baja presión del " \
         "vacío desorbe y expulsa el $CO_2$ y el vapor de agua hacia el espacio, regenerando el material sin consumir botes sustituibles de " \
         "hidróxido de litio (LiOH), lo que optimiza el peso de la nave."
      )
      st.write(
         "Asimismo, el ESM suministra nitrógeno y oxígeno para mantener la presión de cabina en 14.7 psi. " \
         "El sistema de suministro de agua potable distribuye 240 kg de agua almacenada para hidratación y preparación de " \
         "alimentos mediante calentadores dedicados, mientras que las excretas biológicas se gestionan mediante un inodoro espacial " \
         "compacto optimizado para condiciones de microgravedad y aceleración."
      )
   st.divider()   
   col1, col2, col3 = st.columns ([1,2,1])   
   with col2:
      st.header(
         "Perfil de Vuelo y Mecánica Orbital de la Misión🚀➕➖ "
      )
   st.divider()
   col1, col2, col3 = st.columns([1,3,1])
   with col2:
    st.warning(
      "La secuencia operativa de Artemis II se divide en fases de ejecución bien definidas que balancean la prueba de " \
      "subsistemas cerca de la Tierra con el riesgo de ingresar al espacio profundo."
   )   
    st.write(
       "**La Fase 1** comienza con el despegue desde la Rampa 39B del Centro Espacial Kennedy impulsado por el SLS. Tras el desprendimiento de " \
       "los aceleradores sólidos y de la etapa central, la etapa ICPS coloca a la nave Orion en una órbita terrestre inicial. Posteriormente, " \
       "la ICPS ejecuta un primer encendido propulsivo para insertar al vehículo en una Órbita Terrestre Alta (HEO) elíptica de 44,525 por " \
       "115 millas estatutas (aproximadamente 71,650 x 185 km) con un período orbital de 24 horas. Durante este primer día en órbita, los " \
       "astronautas verifican el funcionamiento del sistema ECLSS, la salud de las baterías y los despliegues mecánicos. En esta fase, el " \
       "piloto Victor Glover toma el control manual de los propulsores del RCS para ejecutar maniobras de aproximación y pilotaje de precisión "
       "(RPOD) tomando como objetivo la etapa gastada de la ICPS, validando los sensores ópticos, de cámaras y LiDAR que se emplearán en " \
       "futuras misiones de acoplamiento."
    )
    st.write(
       "**La Fase 2** se inicia una vez confirmada la estabilidad de los subsistemas. La ICPS ejecuta el encendido de Inyección Translunar (TLI) de 18 minutos, " \
       "acelerando el vehículo para abandonar la órbita terrestre. Tras completar esta maniobra, la ICPS se desacopla de la nave y " \
       "ejecuta su propio encendido de desecho para reingresar de forma segura en la atmósfera terrestre sobre el Océano Pacífico. Orion " \
       "inicia entonces una trayectoria de retorno libre saliente que dura aproximadamente cuatro días. Durante este trayecto, los astronautas " \
       "prueban las comunicaciones en espacio profundo a través de la Red del Espacio Profundo (DSN) de la NASA y monitorean los niveles de " \
       "radiación del entorno."
    )
    st.write(
       "**La Fase 3** abarca el sobrevuelo lunar y el pasaje sobre la cara oculta del satélite. Orion no realiza un encendido de captura " \
       "para entrar en órbita lunar, sino que aprovecha la masa de la Luna para efectuar un sobrevuelo a una altitud de entre 4,000 y 6,000 " \
       "millas estatutas (alrededor de 6,400 a 9,600 km) sobre la superficie. La atracción gravitatoria altera la trayectoria de la nave en " \
       "una figura en ocho, impulsándola de regreso hacia la Tierra de manera natural. En este tramo, la tripulación viaja hasta 4,600 millas " \
       "más allá de la cara oculta lunar, registrando datos e imágenes del entorno cislunar."
    )
    st.write(
       "**La Fase 4** comprende la separación del Módulo de Servicio Europeo, la reorientación del Módulo de Tripulación y el reingreso atmosférico." \
       "La cápsula penetra la interfaz atmosférica (Entry Interface) a 400,000 pies de altitud (122 km) a una velocidad de 25,000 mph "
       "(40,000 km/h). La fricción extrema genera una capa de plasma supercalentado a 5,000 °F que interrumpe temporalmente las comunicaciones " \
       "por radio. A 25,000 pies de altitud, dos paracaídas de frenado (drogue) frenan la nave hasta las 307 mph, y a 9,500 pies se despliegan " \
       "tres paracaídas principales de 116 pies de diámetro que reducen la velocidad de caída a 17 mph para un amarizaje suave en el Océano " \
       "Pacífico, donde la tripulación es recuperada por equipos de la Marina de los EE. UU. y de la NASA."
    )
   st.divider()
   col_imagen, col_img = st.columns(2) 
   with col_imagen:
      st.image(
         "navegacion.webp",
         caption="trayecto de la mision completa de artemis 2",
         width= "stretch"
         )
   with col_img:
      st.image(
         "planos.webp",
         caption= "planos de las partes visibles del cohete de artemis 2 (los planos mas tecnicos y formales no se hacen publicos por motivos de seguridad)",
         width= 600
      )  
with tab5:
   col1, col2, col3 = st.columns ([1,0.7,1]) 
   with col2:
      st.header(
         "CONCLUSIONES🎆🎇"
      )
   st.divider()
   col1, col2, col3 = st.columns([1,2,1])
   with col2:
      st.write(
         "Artemis II no es un eco de la era Apolo ni un simple vuelo de demostración; es la prueba de fuego que valida la infraestructura con la que la humanidad asegurará su presencia " \
         "permanente en el espacio profundo. Pasar de la teoría a la ejecución real bajo las fuerzas brutales de 8.8 millones de libras de empuje del cohete SLS, " \
         "operar por primera vez un sistema de soporte vital regenerativo en el entorno cislunar y resolver anomalías complejas de ingeniería como " \
         "la microfísica del escudo ablativo Avcoat no son logros menores: representan la frontera entre la supervivencia y el fallo catastrófico. " \
         "Esta misión transforma la mecánica orbital y la trayectoria de retorno libre en un protocolo operativo estricto, demostrando que la nave Orion no " \
         "solo es capaz de resistir el vacío hostil, sino de dominarlo."
      )
      st.write(
         "Al mismo tiempo, este vuelo redefine la escala humana y científica de la exploración interplanetaria. Al romper el récord histórico de distancia con una tripulación que refleja por " \
         "primera vez la diversidad de nuestra especie y llevar a bordo experimentos microfluídicos de vanguardia como AVATAR, Artemis II convierte cada kilómetro recorrido en telemetría " \
         "biológica indispensable. Atravesar los cinturones de radiación de Van Allen y mapear la respuesta celular ante la radiación cósmica galáctica demuestra que los límites biológicos de la " \
         "aviación espacial no son barreras infranqueables, sino variables de ingeniería que se pueden medir, modelar y vencer."
      )
      st.write(
         "En última instancia, Artemis II establece el estándar definitivo de excelencia para las misiones del futuro: un entorno donde el margen de error es cero, " \
         "la improvisación está prohibida y el talento no sirve si no está respaldado por un rigor absoluto. Este sobrevuelo de diez días alrededor de la Luna no representa un cierre, " \
         "sino el verdadero punto de partida: la consolidación de un corredor cislunar permanente que utilizará la Luna no como un destino final, sino como la rampa de despegue hacia la " \
         "conquista de Marte."
      )
with st.sidebar:
   st.title(
      "ARTEMIS"
   )
   st.write(
      "En que puedo ayudarlo comandante🫡"
   )
   respuestas = {
    ("hola", "buenas", "hey", "que tal"):
        "¡Hola! Soy el asistente de Artemis II 🚀. Pregúntame sobre la tripulación, el cohete, las fechas o los objetivos de la misión, o lo que se te pegue la gana",

    ("que es artemis", "que es la mision", "de que trata"):
        "Artemis II fue el primer vuelo tripulado del Programa Artemis de la NASA, llevando a 4 astronautas en un sobrevuelo alrededor de la Luna, sin aterrizar, como prueba antes de una futura misión de alunizaje (Artemis III).",

    ("cuando", "fecha", "lanzamiento", "despego", "despegó"):
        "Artemis II despegó el 1 de abril de 2026 desde la Plataforma de Lanzamiento 39B del Centro Espacial Kennedy, en Florida, EEUU",

    ("cuanto duro", "duracion", "dias", "cuanto tiempo"):
        "La misión duró aproximadamente 10 días en total, desde el despegue hasta el regreso a la Tierra.",


    ("tripulacion", "astronautas", "quienes son", "quienes viajaron"):
        "La tripulación estuvo compuesta por 4 personas: el comandante Reid Wiseman, el piloto Victor Glover, la especialista de misión Christina Koch (los tres de la NASA), y el especialista de misión Jeremy Hansen, de la Agencia Espacial Canadiense (CSA).",

    ("reid", "wiseman", "comandante"):
        "Reid Wiseman fue el comandante de Artemis II. Es astronauta de la NASA desde 2009, con experiencia previa en la Estación Espacial Internacional.",

    ("victor", "glover", "piloto"):
        "Victor Glover fue el piloto de Artemis II, y con esta misión se convirtió en la primera persona afroamericana en viajar más allá de la órbita baja terrestre, rumbo a la Luna.",

    ("christina", "koch"):
        "Christina Koch fue especialista de misión en Artemis II. Ya tenía el récord del vuelo espacial individual más largo hecho por una mujer, gracias a su tiempo en la Estación Espacial Internacional.",

    ("jeremy", "hansen", "canada", "canadiense"):
        "Jeremy Hansen fue especialista de misión en Artemis II, y el primer astronauta no estadounidense en viajar hacia la Luna. Pertenece a la Agencia Espacial Canadiense (CSA).",

    ("cohete", "sls", "space launch system"):
        "El cohete usado fue el SLS (Space Launch System), el cohete más potente construido por la NASA hasta la fecha, diseñado específicamente para las misiones Artemis.",

    ("orion", "capsula", "nave"):
        "Orion es la cápsula donde viajó la tripulación. Fue lanzada por el cohete SLS, y es la que regresó a los astronautas de forma segura a la Tierra tras el sobrevuelo lunar.",

    ("objetivo", "proposito", "para que sirvio", "por que"):
        "El objetivo principal fue probar, con astronautas a bordo, los sistemas de soporte vital, los controles de la nave Orion y el escudo térmico durante el reingreso a la atmósfera — todo antes de intentar un alunizaje en Artemis III.",

    ("distancia", "que tan lejos", "kilometros"):
        "La tripulación viajó unos 965.600 km en total, pasando más allá de la cara oculta de la Luna — la distancia más grande que un ser humano ha recorrido desde la Tierra.",

    ("apollo", "ultima vez", "cuando fue la ultima"):
        "La última vez que astronautas viajaron tan lejos de la Tierra fue con el programa Apollo, que terminó en 1972 con la misión Apollo 17.",

    ("riesgo", "peligro", "radiacion", "comunicacion"):
        "La tripulación estuvo expuesta a niveles más altos de radiación de lo normal, y en ciertos tramos del viaje perdieron temporalmente la comunicación con el control de misión, debido a la distancia.",

    ("artemis 3", "artemis iii", "siguiente mision", "alunizaje"):
        "Artemis III es la siguiente misión planeada, y busca ser la primera en llevar astronautas a caminar sobre la superficie lunar desde 1972.",

    ("diferencia con artemis 1", "artemis i"):
        "Artemis I (2022) fue una misión de prueba sin tripulación. Artemis II fue la primera con astronautas reales a bordo, aunque sin aterrizar en la Luna.",

    ("gracias",):
        "¡De nada! Si tienes otra pregunta sobre la misión, aquí estoy.",

    ("adios", "chao", "hasta luego"):
        "¡Hasta luego! Gracias por explorar la misión Artemis II conmigo. 🌕",
   
    ("que es artemis", "que es la mision", "de que trata"):
        "Artemis II fue el primer vuelo tripulado del Programa Artemis de la NASA, llevando a 4 astronautas en un sobrevuelo alrededor de la Luna, sin aterrizar, como prueba antes de una futura misión de alunizaje (Artemis III).",

    ("cuando", "fecha", "lanzamiento", "despego", "despegó"):
        "Artemis II despegó el 1 de abril de 2026 desde la Plataforma de Lanzamiento 39B del Centro Espacial Kennedy, en Florida.",

    ("cuanto duro", "duracion", "dias", "cuanto tiempo"):
        "La misión duró aproximadamente 10 días en total, desde el despegue hasta el regreso a la Tierra.",

    ("tripulacion", "astronautas", "quienes son", "quienes viajaron"):
        "La tripulación estuvo compuesta por 4 personas: el comandante Reid Wiseman, el piloto Victor Glover, la especialista de misión Christina Koch (los tres de la NASA), y el especialista de misión Jeremy Hansen, de la Agencia Espacial Canadiense (CSA).",

    ("reid", "wiseman", "comandante"):
        "Reid Wiseman fue el comandante de Artemis II. Es astronauta de la NASA desde 2009, con experiencia previa en la Estación Espacial Internacional.",

    ("victor", "glover", "piloto"):
        "Victor Glover fue el piloto de Artemis II, y con esta misión se convirtió en la primera persona afroamericana en viajar más allá de la órbita baja terrestre, rumbo a la Luna.",

    ("christina", "koch"):
        "Christina Koch fue especialista de misión en Artemis II. Ya tenía el récord del vuelo espacial individual más largo hecho por una mujer, gracias a su tiempo en la Estación Espacial Internacional.",

    ("jeremy", "hansen", "canada", "canadiense"):
        "Jeremy Hansen fue especialista de misión en Artemis II, y el primer astronauta no estadounidense en viajar hacia la Luna. Pertenece a la Agencia Espacial Canadiense (CSA).",

    ("cohete", "sls", "space launch system"):
        "El cohete usado fue el SLS (Space Launch System), el cohete más potente construido por la NASA hasta la fecha, diseñado específicamente para las misiones Artemis.",

    ("orion", "capsula", "nave"):
        "Orion es la cápsula donde viajó la tripulación. Fue lanzada por el cohete SLS, y es la que regresó a los astronautas de forma segura a la Tierra tras el sobrevuelo lunar.",

    ("objetivo", "proposito", "para que sirvio", "por que"):
        "El objetivo principal fue probar, con astronautas a bordo, los sistemas de soporte vital, los controles de la nave Orion y el escudo térmico durante el reingreso a la atmósfera — todo antes de intentar un alunizaje en Artemis III.",

    ("distancia", "que tan lejos", "kilometros"):
        "La tripulación viajó unos 965.600 km en total, pasando más allá de la cara oculta de la Luna — la distancia más grande que un ser humano ha recorrido desde la Tierra.",

    ("apollo", "ultima vez", "cuando fue la ultima"):
        "La última vez que astronautas viajaron tan lejos de la Tierra fue con el programa Apollo, que terminó en 1972 con la misión Apollo 17.",

    ("riesgo", "peligro", "radiacion", "comunicacion"):
        "La tripulación estuvo expuesta a niveles más altos de radiación de lo normal, y en ciertos tramos del viaje perdieron temporalmente la comunicación con el control de misión, debido a la distancia.",

    ("artemis 3", "artemis iii", "siguiente mision", "alunizaje"):
        "Artemis III es la siguiente misión planeada, y busca ser la primera en llevar astronautas a caminar sobre la superficie lunar desde 1972.",
 
    ("diferencia con artemis 1", "artemis i"):
        "Artemis I (2022) fue una misión de prueba sin tripulación. Artemis II fue la primera con astronautas reales a bordo, aunque sin aterrizar en la Luna.",

    ("gracias",):
        "¡De nada! Si tienes otra pregunta sobre la misión, aquí estoy.",

    ("adios", "chao", "hasta luego"):
        "¡Hasta luego! Gracias por explorar la misión Artemis II conmigo. 🌕",
}
   respuesta_default=(
      "lo siento aun soy un poco tonto 🤪 y no tengo informacion sobre esto tadavia, intenta preguntar de otra forma te sugiero algo como: ¿quienes fueron los astronautas de la mision artemis 2?"
)
def generar_respuesta(pregunta_usuario: str)->str:
   pregunta_lower = pregunta_usuario.lower()
   mejor_puntage = 0
   mejor_respuesta = respuesta_default # le establecemos un parametro inicial que practicamente dice: hasta el momento la mejor respuesta es la ya viene de fabrica, si el bucle encuentra un amejor respuesta entonces se le aumenta 1 y python imprimira la mejor respuesta

   #------------------------------------------------------------------------------------------------------------------------------------------------
   # La palabra "def" sirve precisamente para crear un anueva funcion, en este caso creamos la funcion generar_respustas
   # y dentro del parentesis ubicams el parametro, es decir, el dato de entrada de la funcion el str dentro del parenntesis indica
   # o le dice a la funcion: resiviras un dato de entrada en texto, esto sirve prcisamente para que python no confunda texto con numeros
   # y pueda ejecutar la funcion sin ningun error. lo que se ubica fuera del parentisis de la forma: ->str:, sireve precisanteme para decirle 
   # a python: como dato de salida de la funcion muestra texto.
   #
   # .lower sirve precisamente para convertir tod el texto a minusculos y pues para que python no se confunda, por ejemplo:
   # si el usuario pone: Hola Como Estas como dato de entrada en la funcion python lo interpretara todo en minusculas 
   #------------------------------------------------------------------------------------------------------------------------------------------------

   for palabras_clave, respuesta in respuestas.items():
      puntage = 0
      for palabra in palabras_clave:  #analizamos cada palabra en la tupla de palabras
         if palabra in pregunta_lower:  # preguntasmo si la palabra analizadase encuentra en lo que el usuario pidio o escribio 
          puntage +=1 # si coincide el condicional devuenve verdadero y aumenta un punto 
      if puntage > mejor_puntage:
         mejor_puntage = puntage
         mejor_respuesta = respuesta
   return mejor_respuesta # paramos justamente cuando se alcanza la mejor respuesta
 
# la palabra "for" en python sirve para crear bucles o ciclos que repiten un bloque de codigo un numero determinadop de veces


#el primer bucle (for) busca la dupla en el diccionario y el segundo bucle (el for dentro del for) evalua cada palabra dentro de la dupla en busca de concistencias tomando en cuenta la frase del usuario


# Guardar historial de mensajes entre interacciones
with st.sidebar:
    
    # Inicialización del historial de comunicaciones
    if "historial" not in st.session_state:
        st.session_state.historial = []
        
    # Renderizado de mensajes previos en el panel lateral
    for mensaje in st.session_state.historial:
        with st.chat_message(mensaje["rol"]):
            st.write(mensaje["contenido"])
            
    # Despliegue del input del usuario en el panel lateral
    pregunta = st.chat_input("Escribe tu pregunta aquí o hare una revolucion")
    
    # Procesamiento si el usuario envía un mensaje
    if pregunta:
        # Registrar y mostrar la pregunta del usuario
        st.session_state.historial.append({"rol": "user", "contenido": pregunta})
        with st.chat_message("user"):
            st.write(pregunta)
            
        # Generar y mostrar la respuesta del sistema
        respuesta = generar_respuesta(pregunta)
        st.session_state.historial.append({"rol": "assistant", "contenido": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)
          



    #------------------------
    # ME DEBEN 50K CARE MONDA 
    #-----------------------