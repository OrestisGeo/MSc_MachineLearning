import nbformat
from pathlib import Path

def clean_notebook(path: Path):
    print(f"➜ Ελέγχω: {path}")
    nb = nbformat.read(path, as_version=4)
    changed = False

    # metadata σε επίπεδο notebook
    md = getattr(nb, "metadata", None)

    if md is not None and "widgets" in md:
        print(f"   ⚠ Βρέθηκε metadata.widgets στο {path.name} → το σβήνω")
        del md["widgets"]
        changed = True
    else:
        print(f"   ✓ Δεν υπάρχει metadata.widgets στο {path.name}")

    if changed:
        nbformat.write(nb, path)
        print(f"   💾 Αποθηκεύτηκε καθαρισμένο: {path}")
    else:
        print(f"   (Καμία αλλαγή στο {path.name})")

def main():
    root = Path(__file__).resolve().parent
    print(f"Τρέχω από φάκελο: {root}")
    found_any = False

    # Βρες ΟΛΑ τα .ipynb κάτω από τον φάκελο του script
    for path in root.rglob("*.ipynb"):
        found_any = True
        clean_notebook(path)

    if not found_any:
        print("⚠ Δεν βρέθηκαν καθόλου .ipynb αρχεία κάτω από αυτόν τον φάκελο!")

if __name__ == "__main__":
    main()