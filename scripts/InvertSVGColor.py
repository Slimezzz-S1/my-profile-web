import os
from pathlib import Path

ROOTDIR : Path | str = Path(__file__).parent.parent
ASSETS : Path | str = ROOTDIR / 'src' / 'assets'
ICONFOLDERS : Path | str = ASSETS / 'icons'
INVERTEDICONFOLDERS : Path | str = ICONFOLDERS / 'inverted'
ICONS : list[Path | str] = [icon for icon in os.listdir(ICONFOLDERS) if os.path.isfile(ICONFOLDERS / icon) and icon.endswith('svg')]

def checkFolders() -> bool:
    if not os.path.exists(ICONFOLDERS):
        raise FileNotFoundError(f"'{str(ASSETS / 'icons')}' doesn't exist")
    
    return True

def main() -> None:
    if not os.path.exists(INVERTEDICONFOLDERS):
        os.makedirs(INVERTEDICONFOLDERS)

    for icon in ICONS:
        with open(ICONFOLDERS / icon, 'r') as originalIcon:
            with open(INVERTEDICONFOLDERS / icon, 'w') as newIcon:
                newIcon.write(str(originalIcon.read()).replace('currentColor', '#ffffff'))

    return None

if __name__ == '__main__':
    main()