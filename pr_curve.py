# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:35:19 2021

@author: TylerFeldman
"""

import matplotlib.pyplot as plt

def pr_curve(precision_file, recall_file):
    """ Creates and saves a pr curve from the precision and recall files output 
    from the yolov3 training process

    Parameters
    ----------
    precision_file : string
        Path to .txt file containing precision values (e.g. 'precision.txt')
    recall_file : string
        Path to .txt file containing recall values (e.g. 'recall.txt')
        
    """
    
    with open(precision_file, 'r') as f:
        lines = f.read().split('\n')[:-1]
        precision = [float(line.strip('[]')) for line in lines]
    
    with open(recall_file, 'r') as f:
        lines = f.read().split('\n')[:-1]
        recall = [float(line.strip('[]')) for line in lines]
        
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.plot(recall, precision)
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_xlim(0, 1.01)
    ax.set_ylim(0, 1.01)
    fig.tight_layout()
    fig.savefig('PR_curve.png', dpi=300)
    plt.show()
    
    
def pr_curve_comparison(*args):
    """ Creates and saves a graph that contains any number of pr curves

    Parameters
    ----------
    *args : Any number of lists in format ['precision_file.txt', 'recall_file.txt', 'label']
    
        First item in each list is the path to the .txt file containing the precision values.
        Second item in each list is the path to .txt file containing recall values.
        Third item in each list is the label for that particular pr curve, and will go in the legend.

        For a graph with two pr curves, *args would be something like
        ['precision_1.txt', 'recall_1.txt', 'label_1'], ['precision_2.txt', 'recall_2.txt', 'label_2']

    """

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))    

    for arg in args:    
        with open(arg[0], 'r') as f:
            lines = f.read().split('\n')[:-1]
            precision = [float(line.strip('[]')) for line in lines]
        
        with open(arg[1], 'r') as f:
            lines = f.read().split('\n')[:-1]
            recall = [float(line.strip('[]')) for line in lines]
            
        ax.plot(recall, precision, label=arg[2])    
                    
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_xlim(0, 1.01)
    ax.set_ylim(0, 1.01)
    ax.legend(loc='best')
    fig.tight_layout()
    fig.savefig('PR_curve.png', dpi=300)
    plt.show()
    

def metrics(precision_file, recall_file):
    """ Finds max f1, max precision, and max recall using precision and recall .txt files

    Parameters
    ----------
    precision_file : string
        Path to .txt file containing precision values (e.g. 'precision.txt')
    recall_file : string
        Path to .txt file containing recall values (e.g. 'recall.txt')
        
    """

    max_p = 0
    max_r = 0
    max_f1 = 0

    precision_f = open(precision_file, 'r')
    recall_f = open(recall_file, 'r')

    lines = precision_f.read().split('\n')[:-1]
    precision = [float(line.strip('[]')) for line in lines]

    lines = recall_f.read().split('\n')[:-1]
    recall = [float(line.strip('[]')) for line in lines]

    for i in range(len(precision)):
        max_p = max(max_p, precision[i])
        max_r = max(max_r, recall[i])
        max_f1 = max(max_f1, (2*precision[i]*recall[i]) / (precision[i]+recall[i]))

    print(f'For {precision_file} and {recall_file},\nMax Precision: {max_p} \nMax Recall: {max_r} \nMax F1: {max_f1}')


if __name__ == '__main__':
    #pr_curve('precision.txt', 'recall.txt')
    metrics('precision.txt', 'recall.txt')
    metrics('precision(1).txt', 'recall(1).txt')
    pr_curve_comparison(['precision.txt', 'recall.txt', 'Baseline Dataset'], ['precision(1).txt', 'recall(1).txt', 'Adding Synthetic'])