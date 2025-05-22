import os
from typing import List
import json

async def load_batch_results(batch_file: str) -> List:
    """Load previously processed batch results from a file."""
    batch_results = []
    with open(batch_file, 'r') as f:
        for line in f:
            if line.strip() != "FAILED":
                result = line
            else:
                result = "FAILED"
            batch_results.append(result)
    return batch_results

async def save_batch_results(batch_file, batch_results):
    with open(batch_file, 'w') as f:
        for result in batch_results:
            # Handle explicit "FAILED" string
            if result == "FAILED":
                f.write("FAILED\n")
                continue
                
            # Handle None or empty results
            if result is None or len(result) == 0:
                f.write("FAILED\n")
                continue
                
            # Handle case where first element might be None
            if result[0] is None:
                f.write("FAILED\n")
                continue
                
            try:
                # Try to write the JSON, but catch any potential errors
                f.write(result[0].json() + '\n')
            except (AttributeError, TypeError, ValueError) as e:
                print(f"Error processing result: {str(e)}")
                f.write("FAILED\n")


def setup_intermediate_dir(file_name: str) -> str:
    """Create and return the intermediate directory path."""
    intermediate_dir = f"intermediate_steps/{file_name}"
    if not os.path.exists(intermediate_dir):
        os.makedirs(intermediate_dir)
    return intermediate_dir

def create_batch_file(dir,i):
            return f"{dir}/batch_{i}.json"


async def load_pre_proccessed_batch(batch_file,batch_size,i):
                print(f"Loading pre-processed batch {i//batch_size + 1}")
                return await load_batch_results(batch_file)