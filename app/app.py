import random
import time

from dy_dyjsb.dyjsb import dyjsb_init, dyjsb_task_open_daily_box, dyjsb_keep_account
from hg.hg import hg_init, hg_task_open_daily_box


def main():
    while True:
        dyjsb_init()

        dyjsb_keep_account()
        time.sleep(1.9)
        dyjsb_task_open_daily_box()

        hg_init()
        for i in range(4):
            hg_task_open_daily_box()
            time.sleep(random.uniform(1.05, 1.2) * 60 * 1.5)


if __name__ == "__main__":
    main()
