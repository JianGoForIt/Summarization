from datasets import load_dataset

output_dir='./xsum/raw_text/'

dataset = load_dataset('xsum', cache_dir='./xsum')

def write_file(dataset, output_dir, file_name):
    with open(output_dir + "/" + file_name + '.source', 'w') as f:
        for x in dataset:
            f.write(x['document'].replace('\n', ' ') + '\n')

    with open(output_dir + '/' + file_name + '.target', 'w') as f:
        for x in dataset:
            f.write(x['summary'].replace('\n', ' ') + '\n')



if __name__ == "__main__":
    write_file(dataset['test'], output_dir, 'test')
    write_file(dataset['validation'], output_dir, 'validation')
    write_file(dataset['train'], output_dir, 'train')
