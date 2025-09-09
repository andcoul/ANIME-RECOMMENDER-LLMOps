import pandas as pd

class DataLoader:
    def __init__(self, file_path: str, processed_data: str):
        self.file_path = file_path
        self.processed_data = processed_data   

    def load_data(self) -> pd.DataFrame:
        """Load data from a CSV file into a pandas DataFrame."""
        try:
            df = pd.read_csv(self.file_path, encoding='utf-8', on_bad_lines='skip').dropna()

            required_cols = {'Name' , 'Genres','sypnopsis'}
            missing = required_cols - set(df.columns)
            if missing:
                raise ValueError("Missing column  in CSV File")
            
            df['combined_info'] = ("Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"])
            df[['combined_info']].to_csv(self.processed_data, index=False, encoding='utf-8')

            return self.processed_data
        
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The provided CSV file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: There was a parsing error while reading the CSV file.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise