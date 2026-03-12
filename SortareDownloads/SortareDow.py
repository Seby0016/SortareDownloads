import shutil
from pathlib import Path

cale_downloads = Path.home() / "Downloads"

categorii = {
    "Imagini": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Arhive": [".zip", ".rar", ".7z", ".tar"],
    "Documente": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Cod": [".py", ".cpp", ".c", ".java", ".html", ".css"]
}

folder_altele = "Altele"


def afla_folderul(extensie):
    for nume_folder, lista_extensii in categorii.items():
        if extensie in lista_extensii:
            return nume_folder
    return folder_altele


def nume_nou_daca_exista(cale_fisier):
    if not cale_fisier.exists():
        return cale_fisier

    nume = cale_fisier.stem
    extensie = cale_fisier.suffix
    folder = cale_fisier.parent
    nr = 1

    while True:
        fisier_nou = folder / f"{nume}_{nr}{extensie}"
        if not fisier_nou.exists():
            return fisier_nou
        nr += 1


def sorteaza_downloads(cale):
    for fisier in cale.iterdir():
   
        if fisier.is_dir():
            continue

        extensie = fisier.suffix.lower()
        folder_bun = afla_folderul(extensie)

        cale_folder_nou = cale / folder_bun
        cale_folder_nou.mkdir(exist_ok=True)

        cale_finala = cale_folder_nou / fisier.name
        cale_finala = nume_nou_daca_exista(cale_finala)

        try:
            shutil.move(str(fisier), str(cale_finala))
            print(f"Am mutat {fisier.name} in folderul {folder_bun}")
        except:
            print(f"N-a mers la fisierul {fisier.name}")


if __name__ == "__main__":
    print("Incep Sortarea")
    sorteaza_downloads(cale_downloads)
    print("The enddd")