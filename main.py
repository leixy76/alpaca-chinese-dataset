import json
import math
from os import listdir
from os.path import isfile, join


merged_file_path = './alpaca-chinese-52k.json'
split_file_dir = './data'
split_file_path_template = './data/alpaca_chinese_part_{0}.json'
chunk_size = 1000


def split():
    # NOTE do not call this function unless you edit the merged file only and want to update the split file.
    with open(merged_file_path, 'r', encoding='utf-8') as rf:
        samples = json.load(rf)
        print(f'total samples {len(samples)}')
        chunk_num = math.ceil(len(samples) / chunk_size)
        for i in range(0, chunk_num):
            sample_chunk = samples[i * chunk_size: (i + 1) * chunk_size]
            print(len(sample_chunk))
            with open(split_file_path_template.format(i), 'w', encoding='utf-8') as wf:
                wf.write(json.dumps(sample_chunk, ensure_ascii=False, indent=4))


def merge():
    split_files = [join(split_file_dir, file_name) for file_name in listdir(split_file_dir)]
    samples = []
    for split_file in split_files:
        if not split_file.endswith('.json'):
            continue
        with open(split_file, 'r', encoding='utf-8') as rf:
            items = json.load(rf)
            samples.extend(items)
    print(len(samples))
    with open(merged_file_path, 'w', encoding='utf-8') as wf:
        wf.write(json.dumps(samples, ensure_ascii=False, indent=4))


def merge_data_v3():
    merged_file_path_v3 = './alpaca-chinese-52k-v3.json'
    split_file_dir_v3 = './data_v3'

    split_files = [join(split_file_dir_v3, file_name) for file_name in listdir(split_file_dir_v3)]
    samples = []
    for split_file in split_files:
        if not split_file.endswith('.json'):
            continue
        with open(split_file, 'r', encoding='utf-8') as rf:
            items = json.load(rf)
            samples.extend(items)
    print(len(samples))
    with open(merged_file_path_v3, 'w', encoding='utf-8') as wf:
        wf.write(json.dumps(samples, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # merge()  # merge the split file to alpaca-chinese-52k.json
    merge_data_v3()
