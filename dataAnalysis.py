from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def drawMap(filename):
    df = pd.read_csv(filename)
    x = df['Step']
    y = df['Value'].values
    plt.plot(range(y.shape[0]), y)
    plt.show()

def main():
    dirname = './train_table/vgg16/'
    accuary = dirname + 'run-.-tag-epoch_accuracy.csv'
    loss = dirname + 'run-.-tag-epoch_loss.csv'
    val_loss = dirname + 'run-.-tag-epoch_val_loss.csv'
    val_accuary = dirname + 'run-.-tag-epoch_val_accuracy.csv'
    
    data_acc = drawMap(val_loss)
    
    


if __name__ == '__main__':
    main()