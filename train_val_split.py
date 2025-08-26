import os
from pathlib import Path

# Definisikan path dan pemetaan kelas
source_data_path = Path('/content/custom_data')
combined_labels_path = Path('/content/all_species_data/labels')

# PENTING: Pastikan urutan nama folder sesuai dengan urutan 'names' di data.yaml nanti
# Anda bisa mengubah urutan ini jika perlu
class_mapping = {
    'Sea Bass_YOLO with Images': 0,
    'Striped Red Mullet_YOLO with Images': 1,
    'Trout_YOLO with Images': 2
}

print("Starting label index update...")
remapped_count = 0

# Loop melalui setiap folder spesies asli
for species_folder_name, new_class_id in class_mapping.items():
    original_labels_path = source_data_path / species_folder_name / 'labels'

    if not original_labels_path.exists():
        print(f"Warning: Label folder for {species_folder_name} not found.")
        continue

    # Loop melalui setiap file label asli di dalam folder spesies
    for original_label_file in original_labels_path.glob('*.txt'):
        # Tentukan path file yang sesuai di folder gabungan
        target_label_file = combined_labels_path / original_label_file.name
        
        if target_label_file.exists():
            updated_lines = []
            with open(target_label_file, 'r') as f:
                lines = f.readlines()
            
            # Baca setiap baris, ganti indeks kelas, dan simpan
            for line in lines:
                parts = line.strip().split()
                # Ganti class ID lama (misal: 0) dengan yang baru
                parts[0] = str(new_class_id)
                updated_lines.append(" ".join(parts))
            
            # Tulis kembali file dengan indeks kelas yang sudah benar
            with open(target_label_file, 'w') as f:
                f.write("\n".join(updated_lines))
            remapped_count += 1

print(f"Update complete. Total files remapped: {remapped_count}")