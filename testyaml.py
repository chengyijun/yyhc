import yaml


def main():
    with open('./config.yaml', 'r') as f:
        data = f.read()
    config_data = yaml.load(data, Loader=yaml.FullLoader)
    print(config_data)


if __name__ == '__main__':
    main()
