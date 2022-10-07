from scipy.stats import mannwhitneyu
import numpy as np

def compare_dist(data1, data2):
    # this function will compare two distributions using mann whitneya and returns if true if the distributions can be
    # considered similar

    # data3 = np.concatenate([x['downlink_results']['raw_data_dict']['snr'] for x in data1])
    # data4 = np.concatenate([x['downlink_results']['raw_data_dict']['snr'] for x in data2])

    data1 = np.concatenate([x['downlink_results']['raw_data_dict']['cap'] for x in data1])
    data2 = np.concatenate([x['downlink_results']['raw_data_dict']['cap'] for x in data2])
    stat, p = mannwhitneyu(data1, data2)

    # print('previous batch cap mean: ', str(data1.mean()), ' ---------   current batch cap mean: ', str(data2.mean()))
    # print('previous batch cap std: ', str(data1.std()), ' ---------   current batch cap std: ', str(data2.std()))
    # print('statistic = %.3f, p = %.3f' % (stat, p))


    # print('')
    # print('previous batch snr mean: ', str(data3.mean()), ' ---------   current batch snr mean: ', str(data4.mean()))
    # print('previous batch snr std: ', str(data3.std()), ' ---------   current batch snr std: ', str(data4.std()))
    # stat, p = mannwhitneyu(data3, data4)
    # print('statistic = %.3f, p = %.3f' % (stat, p))

    print('statistic = %.3f, p = %.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution\n')
        print('data1 [mean, std]: [' + str(data1.mean()) + ', ' + str(data1.std()) + ']' +
              'data2 [mean, std]: [' + str(data2.mean()) + ', ' + str(data2.std()) + ']')
        return True
    else:
        print('Probably different distributions')
        print('data1 [mean, std]: [' + str(data1.mean()) + ', ' + str(data1.std()) + ']' +
              'data2 [mean, std]: [' + str(data2.mean()) + ', ' + str(data2.std()) + ']')
        return False
