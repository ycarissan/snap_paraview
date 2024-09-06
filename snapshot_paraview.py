from paraview.simple import *
import numpy
import json

# Charger le fichier VTK
vtk_file = "PHB7H.vtk"  # Remplace par ton fichier VTK
reader = LegacyVTKReader(FileNames=[vtk_file])

# Appliquer la représentation par défaut
renderView = GetActiveViewOrCreate('RenderView')
display = Show(reader, renderView)
renderView.ResetCamera()

# Charger les préférences du fichier JSON
preferences_file = "preset_ims.json"  # Remplace par ton fichier JSON

with open(preferences_file, 'r') as f:
    preferences = json.load(f)

# Appliquer les préférences du fichier JSON (Exemple d'application de couleurs)
# Tu peux adapter cette partie selon ce que ton fichier JSON contient
if 'colors' in preferences:
    ColorBy(display, ('POINTS', preferences['colors']['field']))

# Mettre à jour la vue
#renderView.Update()

# Fonction pour sauvegarder un snapshot
def take_snapshot(filename):
    SaveScreenshot(filename, renderView)

angles=[0, 10, 20, 30, 40, 50, 60, 70, 80]
for i, angle in enumerate(angles):
    transform = Transform(Input=reader)
    Hide(reader, renderView)

    transform.Transform.Rotate = [0.0, angle, 0.0]  # Rotation autour de l'axe Y (axe vertical)
    display = Show(transform, renderView)
    renderView.Update()
    take_snapshot(f"snapshot_{i+1}.png")
    Delete(transform)
