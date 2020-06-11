
cat = """
    Semana 1	La permanencia de los cachorros junto a su madre es inminente durante los primeros tres días, ya que esa primera leche llamada calostro les proporcionará los anticuerpos necesarios, quienes actuarán como defensa frente la agresión de sustancias extrañas.
    Estos anticuerpos permanecerán en los cachorros hasta la sexta semana de vida.
    Semana 2	Primera dosis de antiparasitario. Se sugiere repetir el tratamiento cada 3 ó 4 meses, no obstante los análisis de materia fecal para recuento de huevos es lo recomendado antes de cualquier tratamiento.
    Semana 6	En esta semana se debe inicar plan vacunal, se recomienda la aplicación de la vacuna Triple Viral (Calicivirosis felina, Panleucopenia felina y Rinotraqueitis) y la vacuna contra la Leucemia Felina.
    Semana 10	Segunda dosis de las vacunas Triple Viral (Calicivirosis felina, Panleucopenia felina y Rinotraqueitis) y la vacuna contra la Leucemia Felina. Primera dosis de la vacuna Antirrábica.
    Una vez al año	Refuerzo de todas las vacunas.
    """
dog = """
    1° Semana	Es importantísima la estadía del cachorro con su madre ya que los primeros tres días recibirán el calostro que les proporcionará importante cantidad de anticuerpos para poder reaccionar ante sustancias extrañas.
Estos anticuerpos permanecerán en los cachorros, alrededor de la sexta semana de vida donde comienzan a declinar y es aquí donde se los debe vacunar por primera vez.
2° Semana	Se realiza la primera desparasitación de los cachorros, la misma debe ser en gotas y se realiza de acuerdo al peso de los mismos.
Laboratorios Over cuenta con OVERSOLE PA, un antihelmíntico de administración oral, que nos asegura en esta etapa de la vida de los cachorros la acción directa contra Ancylostomas y Áscaris
3° Semana	Se comienza a suplementar a los cachorros con papillas, en el mercado hay muy buenas formulaciones que ayudan a que este paso sea lo más natural posible para evitar accidentes dentro de la cría.
Esto es muy importante en crías numerosas, ya que obviamente existe diversidad en el tamaño como también en el comportamiento de los cachorros.
4° Semana	Se realiza la segunda desparasitación de los cachorros, esta es contra coccidios.
Son parásitos microscópicos, básicamente células simples que infectan el intestino, esto acarrea diarrea sanguinolenta con importante pérdida de líquidos, lo cual puede provocar la muerte en animales muy jóvenes.
6° Semana	Como citamos anteriormente este es el momento donde la protección de los anticuerpos maternos comienza a descender, es por esto que se aplica la primer vacuna (45 días de vida).
Es aquí donde el animal comienza a tener inmunidad activa, esta se da porque el animal comienza a fabricar sus propios anticuerpos ya sea por la vacuna o por contacto con el virus.
8° Semana	En este momento se coloca la segunda vacuna, ya que han desaparecido totalmente los anticuerpos maternos, y actúa reforzando los anticuerpos generados por la primera.
Hay que tener en cuenta que a esta edad los cachorros son retirados del criadero e ingresan a su nuevo hogar, esto trae acarreado un cuadro de estrés, que es normal, pero que afecta su inmunidad.
También se realiza una nueva desparasitación contra ancylostomas y áscaris, que son los parásitos más comunes en los cachorros de esta edad.
12° o 13° Semana	La tercera vacuna del cachorro en líneas generales se la coloca a las 12 semanas, pero esto depende del profesional actuante, ya que también se la puede colocar a las 13 ó 14 semanas
    """

default_vaccination_plan = { 'gato' : cat , 'perro' : dog}


class VaccinationPlanService(object):

    @staticmethod
    def create_initial_vaccination_plan(animal):

        description = 'Todavia no incluimos plan vacunatorio para tu mascota'
        if animal is not None or animal.race.lower() in default_vaccination_plan:
            description = default_vaccination_plan[animal.race]
        from rest_api.models.vaccination_plan import VaccinationPlan

        VaccinationPlan.objects.create(
            animal=animal,
            description=description
        )
