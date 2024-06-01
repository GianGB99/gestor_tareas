class Tarea:
def __init__(self, titulo, descripcion):
self.titulo = titulo
self.descripcion = descripcion
self.completada = False
class GestorTareas:
pass

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def ver_tareas(self):
        return self.tareas

def setUp(self):
    self.gestor = GestorTareas()
    self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
    self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")
def test_ver_tareas(self):
    tareas = self.gestor.ver_tareas()
    self.assertEqual(len(tareas), 2)
    self.assertEqual(tareas[0].titulo, "Tarea 1")
    self.assertEqual(tareas[0].descripcion, "Descripción de la tarea 1")
    self.assertEqual(tareas[1].titulo, "Tarea 2")
    self.assertEqual(tareas[1].descripcion, "Descripción de la tarea 2")


def test_ver_tareas_sin_titulo(self):
    with self.assertRaises(ValueError):
        self.gestor.agregar_tarea("", "Descripción")
