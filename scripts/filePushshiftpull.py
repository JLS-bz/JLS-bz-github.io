from tqdm import tqdm
import urllib.request
import os
dates = ['2019-11', '2019-12', '2020-01', ..., '2022-04']

for i, date in enumerate(dates):
    file_url = f'https://files.pushshift.io/reddit/submissions/RS_{date}.zst'
    file_name = f'Datasets/RS_{date}.zst'

    if not os.path.exists(file_name):
        with tqdm(unit='MB', unit_scale=True, unit_divisor=1024, miniters=1,
                  desc=f'{i+1}/{len(dates)}: {file_name}', leave=True) as t:
            def reporthook(blocknum, blocksize, totalsize):
                readsofar = blocknum * blocksize
                if totalsize > 0:
                    percent = readsofar * 1e2 / totalsize
                    s = "\r%5.1f%% %*d / %d" % (
                        percent, len(str(totalsize)), readsofar/1000000, totalsize/1000000)
                    t.set_description(s)
            urllib.request.urlretrieve(file_url, file_name, reporthook=reporthook)
    else:
        print(f"{file_name} already exists.")
