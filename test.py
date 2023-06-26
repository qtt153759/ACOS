import findfile,json
from glob import glob

def read_json(data_path, data_type="train"):
    data = []
    dirs  = glob(data_path)

    print(dirs)
    for dir in dirs:
        files = findfile.find_files(dir, [data_type, ".jsonl"], exclude_key=[".txt"])
        for f in files:
            print(f)
            with open(f, "r", encoding="utf8") as fin:
                for line in fin:
                    data.append(json.loads(line))
    return data

read_json("dataset", "train")