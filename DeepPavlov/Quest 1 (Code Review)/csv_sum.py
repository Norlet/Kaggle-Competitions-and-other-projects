import pandas as pd

df = pd.read_csv("data.csv", sep=",", header=None)
print(df.values.sum()==10)

#добавим проверку на валидность данных

def check_sum(datapath, target_sum):
    df = pd.read_csv(datapath, sep=",", header=None)
    try:
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='raise')
    except Exception:
        print('Dataframe contain not numeric type of data')
        exit()
    return df.values.sum() == target_sum


if __name__ == "__main__":
    config = read_yaml('config.yaml')
    assert os.path.exists(config['DATAPATH']), "Файл не найден"
    print(check_sum(config['DATAPATH'], config['TARGET_SUM']))
