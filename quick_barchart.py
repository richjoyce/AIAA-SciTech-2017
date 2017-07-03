# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
sns.set_context('poster')

width = 0.25
padding = (1-width*2)/2
figsize=(12,6)
print(padding)

def barchart(data, errs, ytitle, legend=True, ymax=None):
    fig, ax = plt.subplots(figsize=figsize)
    rects1 = ax.bar([padding, 1+width+padding], [data[0], data[3]], width, yerr=[errs[0], errs[3]], color=sns.color_palette()[4], error_kw=dict(ecolor='k'))
    rects2 = ax.bar([padding+width, 1+padding], [data[1], data[2]], width, yerr=[errs[1], errs[2]], color=sns.color_palette()[0], error_kw=dict(ecolor='k'))

    if legend:
        ax.legend((rects1[0], rects2[0]), ('No Haptics', 'Passive Haptics'))

    ax.set_xticks([padding+(width/2.), 0.5, padding+width+(width/2), 1+padding+(width/2.), 1.5, 1+padding+width+(width/2)])
    ax.set_xticklabels(('NH', 'No Haptics First', 'PH', 'PH', 'Passive Haptics First', 'NH'))
    for t, y in zip(ax.get_xticklabels(), [0, -0.05, 0, 0, -0.05, 0]):
        t.set_y(y)

    for off in [0, 1]:
        ax.text(off + padding+(width/2.), 1, "First\nCondition:", horizontalalignment='center', fontsize=14)
        ax.text(off + padding+width+(width/2.), 1, "Second\nCondition:", horizontalalignment='center', fontsize=14)

    if ymax is not None:
        ax.set_ylim(0,ymax)
    ax.set_xlim(0,2)

    ax.set_ylabel(ytitle)
    ax.set_xlabel("Condition Order")
    ax.xaxis.grid(False)
    plt.tight_layout()

def linechart(data, errs, ytitle, legend=True, ylim=None):
    fig, ax = plt.subplots(figsize=figsize)
    nh = sns.color_palette()[4]
    ph = sns.color_palette()[0]
    jiggle = 0.03
    j = jiggle
    lines1 = plt.plot([1-j,2-j], data[:2], color='k', alpha=0.3) #cccccc') #sns.color_palette()[1])
    lines2 = plt.plot([1+j,2+j], data[2:], color='k', alpha=0.3) #cccccc') #sns.color_palette()[2])
    errs1 = plt.errorbar([1-j, 2+j], (data[0], data[3]), yerr=(errs[0], errs[3]), marker='s', ms=16, mfc=nh, ecolor=nh, linestyle='None')
    errs2 = plt.errorbar([1+j, 2-j], (data[2], data[1]), yerr=(errs[1], errs[2]), marker='o', ms=16, mfc=ph, ecolor=ph, linestyle='None')

    if legend:
        ax.legend((errs1[0], errs2[0]), ('No Haptics', 'Passive Haptics'))

    ax.set_xticks([1, 2])
    ax.set_xticklabels(('First Condition', 'Second Condition'))

    if ylim is not None:
        ax.set_ylim(ylim)
    ax.set_xlim(0.75,2.25)

    ax.set_ylabel(ytitle)
    #ax.set_xlabel("Condition Order")
    ax.xaxis.grid(False)
    plt.tight_layout()

def barchart3(data, errs, ytitle, legend=True, ymax=None):
    fig, ax = plt.subplots(figsize=figsize)
    rects1 = ax.bar([0.5, 1.5, 2.5], [data[0], data[1], data[2]], .4, yerr=[errs[0], errs[1], errs[2]], color=sns.color_palette()[4], error_kw=dict(ecolor='k'))
    rects2 = ax.bar([0.1, 1.1, 2.1], [data[3], data[4], data[5]], .4, yerr=[errs[3], errs[4], errs[5]], color=sns.color_palette()[0], error_kw=dict(ecolor='k'))

    if legend:
        ax.legend((rects1[0], rects2[0]), ('No Haptics', 'Passive Haptics'))

    ax.set_xticks([0.3, 0.5, 0.7, 1.3, 1.5, 1.7, 2.3, 2.5, 2.7])
    ax.set_xticklabels(('PH', 'Distance 20cm', 'NH', 'PH', 'Distance 30cm', 'NH', 'PH', 'Distance 40cm', 'NH'))
    for t, y in zip(ax.get_xticklabels(), [0, -0.05, 0, 0, -0.05, 0, 0, -0.05, 0]):
        t.set_y(y)

    if ymax is not None:
        ax.set_ylim(0,ymax)

    ax.set_ylabel(ytitle)
    ax.xaxis.grid(False)

barchart([72.9, 73.8, 70.4, 63.9], [3.1, 3.2, 2.3, 2.0], 'Presence Score', ymax=90)
plt.savefig('figures/presence_bar.png')
plt.close('all')

linechart([72.9, 73.8, 70.4, 63.9], [3.1, 3.2, 2.3, 2.0], 'Presence Score')
plt.savefig('figures/presence_line.png')
plt.close('all')

barchart([15.0, 15.2, 11.7, 14.5], [0.9, 1.0, 1.1, 0.9], 'Arm Fatigue', ymax=20)
plt.savefig('figures/fatigue_bar.png')
plt.close('all')

linechart([15.0, 15.2, 11.7, 14.5], [0.9, 1.0, 1.1, 0.9], 'Arm Fatigue', ylim=(6,20))
plt.savefig('figures/fatigue_line.png')
plt.close('all')

barchart([15.1, 11.9, 10.9, 13.2], [1.0, 1.3, 0.7, 0.9], 'Time (minutes)', ymax=20)
plt.savefig('figures/time_bar.png')
plt.close('all')

linechart([15.1, 11.9, 10.9, 13.2], [1.0, 1.3, 0.7, 0.9], 'Time (minutes)')
plt.savefig('figures/time_line.png')
plt.close('all')

corrd = [533, 707, 1253, 364, 500, 804]
corre = [20, 21, 40, 15, 19, 35]
barchart3(corrd, corre, 'Corrective Phase Time (msec)', ymax=1600)
plt.savefig('figures/corrective_time.png')
plt.close('all')
