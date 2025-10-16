import pandas as pd
import numpy as np
import os

# Update these paths based on your actual structure
PROJECT_ROOT = "Downloads/STData/merged_data/processed_data"
EXTRACTED_DATA_DIR = os.path.join(PROJECT_ROOT, "extracted_data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "synchronized_data")

class DataSynchronizer:
    def __init__(self, data_directory=EXTRACTED_DATA_DIR, output_directory=OUTPUT_DIR):
        self.data_directory = data_directory
        self.output_directory = output_directory
        self.modalities = ['IVT', 'TIVA', 'EYE', 'GSR', 'EEG', 'PSY']
        self.data = {}
    
    def load_data(self):
        """Load all modality data files"""
        for modality in self.modalities:
            file_path = os.path.join(self.data_directory, f"{modality}_extracted.xlsx")
            try:
                self.data[modality] = pd.read_excel(file_path)
                print(f"✅ Loaded {modality} data: {len(self.data[modality])} rows")
            except Exception as e:
                print(f"❌ Error loading {modality}: {e}")
    
    # ... rest of your script methods ...

def main():
    print("Starting Multi-Modal Data Synchronization Pipeline...")
    print(f"Data directory: {EXTRACTED_DATA_DIR}")
    
    # Initialize synchronizer
    synchronizer = DataSynchronizer()
    
    # Load data
    synchronizer.load_data()
    
    # Synchronize all modalities
    synchronized_data = synchronizer.synchronize_all_modalities()
    
    # Export results
    synchronizer.export_synchronized_data(synchronized_data, synchronizer.output_directory)
    
    print("✅ Synchronization completed successfully!")
    
    return synchronized_data

if __name__ == "__main__":
    synchronized_data = main()