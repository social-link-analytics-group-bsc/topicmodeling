# TopicModeling of Foundations

pip3 install -r requirements.txt

1. Collect links and fetch data

python3 get_links.py

python3 get_rcentral_data.py

python3 get_ccatalana_data.py

python3 build_rcentral_ccatalana_csv.py

2. Build Spanish dataframe

python3 build_spanish_dataframe.py && python3 export_spanish_dataframe.py

3. Export training data

python3 preprocessing.py

4. Run hLDA

python3 HLDA.py
