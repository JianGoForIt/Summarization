#conda env create -f environment.yml
#conda activate prefix-tuning

pushd transformer
pip install -e .
popd

pip install datasets
pip install pytorch-lightning==0.8.5
pip install gitpython
pip install rouge-score==0.0.4
pip install sacrebleu==1.4.14

pushd ../
git clone https://github.com/NVIDIA/apex
pushd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
popd
popd

pushd transformers/examples/seq2seq
mkdir -p ./xsum/raw_text
python generate_xsum_files.py
popd
