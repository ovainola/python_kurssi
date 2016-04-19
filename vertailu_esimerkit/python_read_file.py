# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("data.csv", "r") as data_file:
        lines = data_file.readlines()

    price_floats = []
    for each in lines[1:]
        only_start_price = each.split(";")[1]
        replaced_commas = only_start_price.replace(",", ".")
        price_floats.append(float(replaced_commas))
    plt.plot(price_floats)
    plt.show()
