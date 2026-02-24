import os
import subprocess
import sys

# ====== CONFIG ======
PARENT_FOLDER = r"C:\\Users\\Daniel\\Desktop\\Aos-Modpack\\core modlist\\Catagories"
RUSTIQUE_EXE = os.path.join(os.getcwd(), "rustique.exe")
# ====================

def main():
    if not os.path.isfile(RUSTIQUE_EXE):
        print(f"Error: rustique.exe not found at {RUSTIQUE_EXE}")
        sys.exit(1)

    if not os.path.isdir(PARENT_FOLDER):
        print(f"Error: Parent folder not found: {PARENT_FOLDER}")
        sys.exit(1)

    # Loop through all items in parent folder
    for item in os.listdir(PARENT_FOLDER):
        subfolder_path = os.path.join(PARENT_FOLDER, item)

        # Only process directories
        if os.path.isdir(subfolder_path):
            print(f"Running rustique on: {subfolder_path}")

            try:
                subprocess.run(
                    [RUSTIQUE_EXE, "-m", subfolder_path, "list"],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error processing {subfolder_path}: {e}")

    print("Done.")

if __name__ == "__main__":
    main()