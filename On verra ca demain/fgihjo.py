import os
import json
import cv2  # OpenCV pour obtenir la durée des vidéos locales

# Dossier contenant les vidéos
dossier_videos = "vidéos"  # Remplacez par le chemin complet si nécessaire

# Liste pour stocker les informations des vidéos
videos = []

# Fonction pour obtenir la durée d'une vidéo
def obtenir_duree(chemin_video):
    try:
        video = cv2.VideoCapture(chemin_video)
        if video.isOpened():
            frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = video.get(cv2.CAP_PROP_FPS)
            if fps > 0:
                duree = frames / fps
                minutes = int(duree // 60)
                secondes = int(duree % 60)
                return f"{minutes:02}:{secondes:02}"
        return "00:00"
    except Exception as e:
        return "00:00"

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier_videos):
    chemin_complet = os.path.join(dossier_videos, fichier)
    if fichier.endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv')):  # Extensions vidéo courantes
        titre_sans_extension = os.path.splitext(fichier)[0]  # Nom sans l'extension
        duree = obtenir_duree(chemin_complet)  # Durée de la vidéo
        videos.append({
            "titre": titre_sans_extension,
            "chemin": chemin_complet,
            "type": "local",  # Toujours local pour les vidéos dans ce dossier
            "duree": duree
        })

# Ajout d'un exemple de vidéo en iframe
videos.append({
    "titre": "Vidéo en ligne",
    "chemin": "https://www.pornhub.com/embed/ph629ca11f10c52",
    "type": "iframe",
    "duree": "N/A"  # Durée non applicable pour une iframe
})

# Sauvegarde dans un fichier JSON
fichier_json = "videos.json"
with open(fichier_json, "w", encoding="utf-8") as json_file:
    json.dump(videos, json_file, indent=4, ensure_ascii=False)

print(f"Les informations des vidéos ont été enregistrées dans {fichier_json}.")
